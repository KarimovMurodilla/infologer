from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.manager import get_user_manager
from db.models.users import User
from schemas.users import UserSchema, UserSchemaAdd


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


router_jwt = fastapi_users.get_auth_router(auth_backend)
router_jwt.prefix = "/auth/jwt"
router_jwt.tags = ["auth"]

router_auth = fastapi_users.get_register_router(UserSchema, UserSchemaAdd)
router_auth.prefix= "/auth"
router_auth.tags = ["auth"]


current_user = fastapi_users.current_user()
