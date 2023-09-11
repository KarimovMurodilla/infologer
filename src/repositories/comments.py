from db.models.comments import Comment
from utils.repository import SQLAlchemyRepository


class CommentsRepository(SQLAlchemyRepository):
    model = Comment
