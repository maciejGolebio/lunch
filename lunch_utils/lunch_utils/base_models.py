from pydantic import BaseModel


class IdModel(BaseModel):
    id: str
