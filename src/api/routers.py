from api.tasks import router as router_tasks
# from api.users import router as router_users
from api.auth import router_jwt, router_auth


all_routers = [
    router_tasks,
    # router_users,
    router_jwt,
    router_auth
]
