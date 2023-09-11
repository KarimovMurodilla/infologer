from api.users import router_jwt, router_auth

from api.tasks import router as router_tasks
from api.knows import router as router_knows
from api.comments import router as router_comments
from api.likes import router as router_likes


all_routers = [
    router_jwt,
    router_auth,

    router_tasks,
    router_knows,
    router_comments,
    router_likes
]
