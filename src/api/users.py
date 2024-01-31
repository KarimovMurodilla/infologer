from typing import Optional

from passlib.context import CryptContext
from fastapi import APIRouter, HTTPException

from api.tasks import UOWDep, CurrentUser
from services.users import UsersService
from utils.misc.celery_tasks.email_sender import send_verify_code_to_email, email_verification_is_successful
from utils.misc.generators.code_generator import Generator


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("")
async def get_users(
    uow: UOWDep,
    page: int
):
    users = await UsersService().get_users(uow, offset=page)
    return users


@router.get("/filter")
async def get_user_by_username(
    uow: UOWDep,
    username: str,
    page: int
):
    users = await UsersService().get_users_by_username(uow, username, offset=page)
    return users


@router.get("/check_email")
async def is_email_exists(
    uow: UOWDep,
    email: str
):
    user = await UsersService().get_user_by_email(uow, email)

    return {"detail": bool(user)}


@router.get("/check_username")
async def is_username_exists(
    uow: UOWDep,
    username: str
):
    user = await UsersService().get_user_by_username(uow, username)

    return {"detail": bool(user)}

@router.get("/get_by_username")
async def is_username_exists(
    uow: UOWDep,
    current_user: CurrentUser,
    username: str
):
    user = await UsersService().get_user_by_username(uow, username)

    return {"detail": user}

@router.post("/signup/verify")
async def verify_email(
    first_name: str,
    email: str
):
    g = Generator()
    code = g.generate_code()

    send_verify_code_to_email.delay(first_name, email, code)

    return {"message": "Verification code has been sent"}


@router.post("/signup/verify/check")
async def verify_email_code_check(
    email: str,
    code: int
):
    
    if email_verification_is_successful(email, code):
        return {"message": "Email verification successful"}
    
    else:
        raise HTTPException(status_code=401, detail="Invalid verification code")