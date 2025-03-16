from sqlmodel import SQLModel, Field, Column
from typing import Optional

from sqlalchemy import UUID, Index, String, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.mysql import TINYINT

from datetime import datetime
import uuid


class User(SQLModel, table=True):
    __table_args__ = (
        Index('User_unique', 'UserName', unique=True),        
        Index('User_unique_2', 'NormalizedUserName', unique=True),
        Index('User_unique_3', 'Email', unique=True),
        Index('User_unique_4', 'NormalizedEmail', unique=True)
    )

    UserId: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, sa_column=Column('UserId', UUID, primary_key=True))
    UserName: str = Field(sa_column=mapped_column('UserName', String(12), nullable=False))
    NormalizedUserName: str = Field(sa_column=mapped_column('NormalizedUserName', String(12), nullable=False))
    Email: str = Field(sa_column=mapped_column('Email', String(1000), nullable=False))
    NormalizedEmail: str = Field(sa_column=mapped_column('NormalizedEmail', String(1000), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    FirstName: Optional[str] = Field(default=None, sa_column=mapped_column('FirstName', String(50)))
    LastName: Optional[str] = Field(default=None, sa_column=mapped_column('LastName', String(50)))
    PasswordHash: Optional[str] = Field(default=None, sa_column=mapped_column('PasswordHash', String(2000)))
    UserImage: Optional[str] = Field(default=None, sa_column=mapped_column('UserImage', String(3000)))
    CreatedBy: Optional[uuid.UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[uuid.UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))
