from datetime import datetime
import uuid
from decimal import Decimal

from sqlmodel import SQLModel, Field, Column, Relationship
from typing import Optional, List

from sqlalchemy import UUID, Index, String, DateTime, ForeignKeyConstraint, DECIMAL
from sqlalchemy import text
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.mysql import TINYINT


class Fertilizer(SQLModel, table=True):
    __table_args__ = (
        Index('Fertilizers_unique', 'CommonName', unique=True),
        Index('Fertilizers_unique_1', 'ChemicalName', unique=True)
    )

    FertilizerId: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, sa_column=Column('FertilizerId', UUID, primary_key=True))
    CommonName: str = Field(sa_column=mapped_column('CommonName', String(100), nullable=False))
    ChemicalName: str = Field(sa_column=mapped_column('ChemicalName', String(1000), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    CreatedBy: Optional[uuid.UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[uuid.UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))

    fertilizernutrient: List['Fertilizernutrient'] = Relationship(back_populates='fertilizer')
    # fertilizerapplication: List['Fertilizerapplication'] = Relationship(back_populates='fertilizer')



class Fertilizernutrient(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['FertilizerId'], ['fertilizer.FertilizerId'], name='fk_fertilizer_nutrient'),
        Index('fk_fertilizer_nutrient', 'FertilizerId')
    )

    FertilizerNutrientId: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, sa_column=Column('FertilizerNutrientId', UUID, primary_key=True))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    FertilizerId: Optional[uuid.UUID] = Field(default=None, sa_column=mapped_column('FertilizerId', UUID))
    NitrogenPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('NitrogenPercent', DECIMAL(18, 2)))
    PhosphorousPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('PhosphorousPercent', DECIMAL(18, 2)))
    PotassiumPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('PotassiumPercent', DECIMAL(18, 2)))
    SulphurPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('SulphurPercent', DECIMAL(18, 2), server_default=text('0.00')))
    OtherNutrients: Optional[str] = Field(default=None, sa_column=mapped_column('OtherNutrients', String(1000)))
    CreatedBy: Optional[uuid.UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[uuid.UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))

    fertilizer: Optional['Fertilizer'] = Relationship(back_populates='fertilizernutrient')


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
