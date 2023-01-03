from database import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Project(Base, TimestampMixin):
    __tablename__ = 'projects'

    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    title = Column(String(256), nullable=False)
