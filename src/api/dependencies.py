from typing import Annotated

from fastapi import Depends

from utils.unitofwork import IUnitOfWork, UnitOfWork
from api.users import current_user, User


UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
CurrentUser = Annotated[User, Depends(current_user)]