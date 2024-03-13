from pydantic import BaseModel
from .models import StatusEnum


class Application(BaseModel):
    id: int
    status: StatusEnum

    class Meta:
        orm_mode = True

