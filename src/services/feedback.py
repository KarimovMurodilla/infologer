from schemas.feedback import FeedbackSchemaAdd
from utils.repository import AbstractRepository
from utils.unitofwork import IUnitOfWork

from .knows import KnowsService

from utils.misc.chatgpt import ChatGPT

class FeedbackService:
    async def add_feedback(self, uow: IUnitOfWork, feedback: FeedbackSchemaAdd):
        async with uow:
            feedback_id = await uow.feedback.add_one(feedback)
            await uow.commit()
            return feedback_id

    async def get_feedback(self, uow: IUnitOfWork, know_id: str):
        async with uow:
            feedback = await uow.feedback.find_one(know_id=know_id)
            return feedback
        
    async def generate_feedback(self, uow, know_id):
        chat_gpt = ChatGPT()

        know = await KnowsService().get_know(uow, know_id)
        content = f"{know.title}. {know.description}"
        response = chat_gpt.generate_feedback(content)

        feedback = FeedbackSchemaAdd(description=response, know_id=know_id)
        await self.add_feedback(uow, feedback.model_dump())

        return feedback