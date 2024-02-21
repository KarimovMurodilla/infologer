from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from utils.new_httpx_oauth.clients.google import GoogleOAuth2

from auth.auth import auth_backend
from auth.manager import get_user_manager
from db.models.users import User
from schemas.users import UserSchema, UserSchemaAdd, UserUpdate

from config import CLIENT_ID, CLIENT_SECRET, SECRET, FRONTEND_BASE_URL


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


google_oauth_client = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)


router_jwt = {
    'router': fastapi_users.get_auth_router(auth_backend),
    'prefix': "/auth/jwt",
    'tags': ["auth"]
}

router_auth = {
    'router': fastapi_users.get_register_router(UserSchema, UserSchemaAdd),
    'prefix': "/auth",
    'tags': ["auth"]
}

router_google_oauth = {
    'router': fastapi_users.get_oauth_router(
        google_oauth_client, 
        auth_backend, 
        SECRET,
        redirect_url=f"{FRONTEND_BASE_URL}/auth/google/callback"
    ),
    'prefix': "/auth/google",
    'tags': ["auth"],
}

router_password = {
    'router': fastapi_users.get_reset_password_router(),
    'prefix': "/auth",
    'tags': ["auth"],
}

router_users = {
    'router': fastapi_users.get_users_router(UserSchema, UserUpdate),
    'prefix': "/fastapi_users",
    'tags': ["fastapi_users"],
}


current_user = fastapi_users.current_user()
