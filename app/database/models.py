import uuid
from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Integer, ForeignKey, Column, String, TIMESTAMP, Boolean
from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class Operation(Base):
    __tablename__ = 'operation'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quantity = Column(String)
    figi = Column(String)
    instrument_type = Column(String, nullable=True)
    date = Column(TIMESTAMP, default=datetime.utcnow)
    type = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(SQLAlchemyBaseUserTableUUID, Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("role.id"), default=1)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    message = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}





