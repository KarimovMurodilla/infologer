from db.models.knows import Know
from utils.repository import SQLAlchemyRepository


class KnowsRepository(SQLAlchemyRepository):
    model = Know
