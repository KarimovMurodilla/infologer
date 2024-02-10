from db.models.feedback import Feedback
from utils.repository import SQLAlchemyRepository


class FeedbackRepository(SQLAlchemyRepository):
    model = Feedback
