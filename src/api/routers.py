from api.auth import (
    router_jwt, router_auth, 
    router_google_oauth, router_password,
    router_users
)

from api.tasks import router as router_tasks
from api.knows import router as router_knows
from api.comments import router as router_comments
from api.likes import router as router_likes
from api.users import router as router_user
from api.feedback import router as router_feedback


all_routers = [
    router_jwt,
    router_auth,
    router_google_oauth,
    router_password,
    router_users,
    
    router_user,

    router_tasks,
    router_knows,
    router_comments,
    router_likes,
    router_feedback
]
