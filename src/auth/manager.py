from typing import Optional

from fastapi import Depends, Request, Response, HTTPException
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions

from auth.user_db import User, get_user_db

from config import SECRET
from utils.misc.generators.code_generator import Generator
from utils.misc.redis_instance import redis_cache


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def create(
        self,
        user_create,
        safe: bool = False,
        request: Optional[Request] = None,
    ):
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        g = Generator()
        username = user_dict.get("first_name").lower() + '_' + str(g.generate_code())
        
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        user_dict["username"] = username

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user

    async def oauth_callback(
        self,
        oauth_name: str,
        access_token: str,
        account_id: str,
        account_email: str,
        expires_at: Optional[int] = None,
        refresh_token: Optional[str] = None,
        request: Optional[Request] = None,
        *,
        associate_by_email: bool = False,
        is_verified_by_default: bool = False,
    ):
        oauth_account_dict = {
            "oauth_name": oauth_name,
            "access_token": access_token,
            "account_id": account_id,
            "account_email": account_email,
            "expires_at": expires_at,
            "refresh_token": refresh_token,
        }

        try:
            user = await self.get_by_oauth_account(oauth_name, account_id)
        except exceptions.UserNotExists:
            try:
                # Associate account
                user = await self.get_by_email(account_email)
                if not associate_by_email:
                    raise exceptions.UserAlreadyExists()
                user = await self.user_db.add_oauth_account(user, oauth_account_dict)
            except exceptions.UserNotExists:
                # Create account
                password = self.password_helper.generate()
                first_name = redis_cache.get(f"{account_email}_first_name").decode()
                last_name = redis_cache.get(f"{account_email}_last_name").decode()

                g = Generator()
                username = first_name.lower() + '_' + str(g.generate_code())

                user_dict = {
                    "email": account_email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "username": username,
                    "hashed_password": self.password_helper.hash(password),
                    "is_verified": is_verified_by_default,
                }
                user = await self.user_db.create(user_dict)
                user = await self.user_db.add_oauth_account(user, oauth_account_dict)
                await self.on_after_register(user, request)
        else:
            # Update oauth
            for existing_oauth_account in user.oauth_accounts:
                if (
                    existing_oauth_account.account_id == account_id
                    and existing_oauth_account.oauth_name == oauth_name
                ):
                    user = await self.user_db.update_oauth_account(
                        user, existing_oauth_account, oauth_account_dict
                    )

        return user
    

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
