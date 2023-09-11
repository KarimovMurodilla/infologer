from schemas.comments import CommentsSchemaAdd
from utils.repository import AbstractRepository
from utils.unitofwork import IUnitOfWork


class CommentsService:
    async def add_comment(self, uow: IUnitOfWork, comment: CommentsSchemaAdd, user_id: int):
        comments_dict = comment.model_dump()
        comments_dict['user_id'] = user_id
        
        async with uow:
            comment_id = await uow.comments.add_one(comments_dict)
            await uow.commit()
            return comment_id

    async def get_comments(self, uow: IUnitOfWork, know_id: int):
        async with uow:
            comments = await uow.comments.find_all_by(know_id=know_id)
            return comments