from db.models.likes import Like
from utils.repository import SQLAlchemyRepository


class LikesRepository(SQLAlchemyRepository):
    model = Like
