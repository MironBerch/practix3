from abc import ABC, abstractmethod


class BasePgSchema(ABC):

    @abstractmethod
    def to_tuple():
        return NotImplemented

    @staticmethod
    @abstractmethod
    def db_tablename():
        return NotImplemented

    @staticmethod
    @abstractmethod
    def db_fieldnames():
        return NotImplemented


class BaseSQLiteSchema(ABC):

    @abstractmethod
    def to_pg():
        return NotImplemented
