import uuid
from abc import abstractmethod


class IIDService:
    @staticmethod
    @abstractmethod
    def get_id() -> uuid.UUID:
        ...


class IDService(IIDService):
    @staticmethod
    def get_id() -> uuid.UUID:
        return str(uuid.uuid4())
