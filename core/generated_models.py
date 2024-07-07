from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Index, String, UUID, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm.base import Mapped
from sqlmodel import Field, SQLModel

class Cropgrowplan(SQLModel, table=True):
    __table_args__ = (
        Index('CurrentGrowPlan_CurrentGrowPlanId_IDX', 'CropGrowPlanId', unique=True),
    )

    CropGrowPlanId: Optional[UUID] = Field(default=None, sa_column=mapped_column('CropGrowPlanId', UUID, primary_key=True))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    CropVarietyId: Optional[UUID] = Field(default=None, sa_column=mapped_column('CropVarietyId', UUID))
    GerminationTime: Optional[int] = Field(default=None, sa_column=mapped_column('GerminationTime', INTEGER(11)))
    FirstFertilizationDays: Optional[int] = Field(default=None, sa_column=mapped_column('FirstFertilizationDays', INTEGER(11)))
    SecondFertilizationDays: Optional[int] = Field(default=None, sa_column=mapped_column('SecondFertilizationDays', INTEGER(11)))
    RepeatedFertilizationDays: Optional[int] = Field(default=None, sa_column=mapped_column('RepeatedFertilizationDays', INTEGER(11)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Croptype(SQLModel, table=True):
    __table_args__ = (
        Index('CropTypeCode_unique', 'Code', unique=True),
    )

    CropTypeId: Optional[UUID] = Field(default=None, sa_column=mapped_column('CropTypeId', UUID, primary_key=True))
    Name: str = Field(sa_column=mapped_column('Name', String(1000), nullable=False))
    Code: str = Field(sa_column=mapped_column('Code', String(10), nullable=False))
    CropClass: str = Field(sa_column=mapped_column('CropClass', CHAR(2), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Cropvariety(SQLModel, table=True):
    __table_args__ = (
        Index('CropName_unique', 'Name', unique=True),
        Index('CropVarietyCode_unique', 'Code', unique=True)
    )

    CropVarietyId: Optional[UUID] = Field(default=None, sa_column=mapped_column('CropVarietyId', UUID, primary_key=True))
    CropTypeId: UUID = Field(sa_column=mapped_column('CropTypeId', UUID, nullable=False))
    Name: str = Field(sa_column=mapped_column('Name', String(1000), nullable=False))
    Code: str = Field(sa_column=mapped_column('Code', String(100), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    FirstHarvestDays: int = Field(sa_column=mapped_column('FirstHarvestDays', INTEGER(11), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    GerminationDays: Optional[int] = Field(default=None, sa_column=mapped_column('GerminationDays', INTEGER(11)))
    LastHarvestDays: Optional[int] = Field(default=None, sa_column=mapped_column('LastHarvestDays', INTEGER(11)))
    RepeatedHarvestEvery: Optional[int] = Field(default=None, sa_column=mapped_column('RepeatedHarvestEvery', INTEGER(11)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Currentgrow(SQLModel, table=True):
    CurrentGrowId: Optional[UUID] = Field(default=None, sa_column=mapped_column('CurrentGrowId', UUID, primary_key=True))
    GrowingSeasonId: UUID = Field(sa_column=mapped_column('GrowingSeasonId', UUID, nullable=False))
    CropTypeId: UUID = Field(sa_column=mapped_column('CropTypeId', UUID, nullable=False))
    StartDate: date = Field(sa_column=mapped_column('StartDate', Date, nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    FieldId: Optional[UUID] = Field(default=None, sa_column=mapped_column('FieldId', UUID))
    CurrentGrowthStatusId: Optional[UUID] = Field(default=None, sa_column=mapped_column('CurrentGrowthStatusId', UUID))
    CropVarietyId: Optional[UUID] = Field(default=None, sa_column=mapped_column('CropVarietyId', UUID))
    EndDate: Optional[date] = Field(default=None, sa_column=mapped_column('EndDate', Date))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Currentgrowdetail(SQLModel, table=True):
    CurrentGrowDetailId: Optional[UUID] = Field(default=None, sa_column=mapped_column('CurrentGrowDetailId', UUID, primary_key=True))
    CurrentGrowId: UUID = Field(sa_column=mapped_column('CurrentGrowId', UUID, nullable=False))
    SowDate: date = Field(sa_column=mapped_column('SowDate', Date, nullable=False))
    ExpectedTransplantDate: date = Field(sa_column=mapped_column('ExpectedTransplantDate', Date, nullable=False))


class District(SQLModel, table=True):
    DistrictId: Optional[UUID] = Field(default=None, sa_column=mapped_column('DistrictId', UUID, primary_key=True))
    StateId: Optional[UUID] = Field(default=None, sa_column=mapped_column('StateId', UUID))
    Name: Optional[str] = Field(default=None, sa_column=mapped_column('Name', String(100)))
    IsActive: Optional[int] = Field(default=None, sa_column=mapped_column('IsActive', TINYINT(1)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    CreatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('CreatedDate', DateTime))


class Fertilizer(SQLModel, table=True):
    __table_args__ = (
        Index('Fertilizers_unique', 'CommonName', unique=True),
        Index('Fertilizers_unique_1', 'ChemicalName', unique=True)
    )

    FertilizerId: Optional[UUID] = Field(default=None, sa_column=mapped_column('FertilizerId', UUID, primary_key=True))
    CommonName: str = Field(sa_column=mapped_column('CommonName', String(100), nullable=False))
    ChemicalName: str = Field(sa_column=mapped_column('ChemicalName', String(1000), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Fertilizernutrient(SQLModel, table=True):
    FertilizerNutrientId: Optional[UUID] = Field(default=None, sa_column=mapped_column('FertilizerNutrientId', UUID, primary_key=True))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    FertilizerId: Optional[UUID] = Field(default=None, sa_column=mapped_column('FertilizerId', UUID))
    NitrogenPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('NitrogenPercent', DECIMAL(18, 2)))
    PhosphorousPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('PhosphorousPercent', DECIMAL(18, 2)))
    PotassiumPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('PotassiumPercent', DECIMAL(18, 2)))
    SulphurPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('SulphurPercent', DECIMAL(18, 2), server_default=text('0.00')))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Field_(SQLModel, table=True):
    __tablename__ = 'field'
    __table_args__ = (
        Index('field_unique', 'FieldCode', unique=True),
    )

    FieldId: Optional[UUID] = Field(default=None, sa_column=mapped_column('FieldId', UUID, primary_key=True))
    FieldCode: str = Field(sa_column=mapped_column('FieldCode', String(10), nullable=False))
    LandId: UUID = Field(sa_column=mapped_column('LandId', UUID, nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    Location: Optional[str] = Field(default=None, sa_column=mapped_column('Location', String(2000)))
    Acres: Optional[Decimal] = Field(default=None, sa_column=mapped_column('Acres', DECIMAL(18, 2)))
    Cents: Optional[Decimal] = Field(default=None, sa_column=mapped_column('Cents', DECIMAL(18, 2)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Globaldata(SQLModel, table=True):
    __table_args__ = (
        Index('GlobalData_unique', 'Code', unique=True),
    )

    GlobalDataId: Optional[UUID] = Field(default=None, sa_column=mapped_column('GlobalDataId', UUID, primary_key=True))
    Code: str = Field(sa_column=mapped_column('Code', String(10), nullable=False))
    Description: str = Field(sa_column=mapped_column('Description', String(1000), nullable=False))
    IsDefault: int = Field(sa_column=mapped_column('IsDefault', TINYINT(1), nullable=False))
    IsFinal: int = Field(sa_column=mapped_column('IsFinal', TINYINT(1), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    RefId: Optional[UUID] = Field(default=None, sa_column=mapped_column('RefId', UUID))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))


class Growingseason(SQLModel, table=True):
    __table_args__ = (
        Index('GrowingSeason_unique', 'Name', unique=True),
    )

    GrowingSeasonId: Optional[UUID] = Field(default=None, sa_column=mapped_column('GrowingSeasonId', UUID, primary_key=True))
    Name: str = Field(sa_column=mapped_column('Name', String(1000), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    StartMonth: Optional[int] = Field(default=None, sa_column=mapped_column('StartMonth', INTEGER(11)))
    EndMonth: Optional[int] = Field(default=None, sa_column=mapped_column('EndMonth', INTEGER(11)))
    Period: Optional[int] = Field(default=None, sa_column=mapped_column('Period', INTEGER(11)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Land(SQLModel, table=True):
    __table_args__ = (
        Index('land_landid_IDX', 'LandId'),
        Index('land_latitude_IDX', 'Latitude'),
        Index('land_logitude_IDX', 'Longitude'),
        Index('unique_lat', 'Latitude', unique=True),
        Index('unique_long', 'Longitude', unique=True)
    )

    LandId: Optional[UUID] = Field(default=None, sa_column=mapped_column('LandId', UUID, primary_key=True))
    Latitude: str = Field(sa_column=mapped_column('Latitude', String(100), nullable=False))
    Longitude: str = Field(sa_column=mapped_column('Longitude', String(100), nullable=False))
    LocationName: Optional[str] = Field(default=None, sa_column=mapped_column('LocationName', String(100)))
    DistrictId: Optional[UUID] = Field(default=None, sa_column=mapped_column('DistrictId', UUID))
    Taluk: Optional[str] = Field(default=None, sa_column=mapped_column('Taluk', String(100)))
    City: Optional[str] = Field(default=None, sa_column=mapped_column('City', String(100)))
    StateId: Optional[UUID] = Field(default=None, sa_column=mapped_column('StateId', UUID))
    CreatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('CreatedDate', DateTime))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    IsActive: Optional[int] = Field(default=None, sa_column=mapped_column('IsActive', TINYINT(1)))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Landdocument(SQLModel, table=True):
    LandDocumentId: Optional[UUID] = Field(default=None, sa_column=mapped_column('LandDocumentId', UUID, primary_key=True))
    DocumentNumber: str = Field(sa_column=mapped_column('DocumentNumber', String(50), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    LandSurveyId: Optional[UUID] = Field(default=None, sa_column=mapped_column('LandSurveyId', UUID))
    RegisteredOn: Optional[date] = Field(default=None, sa_column=mapped_column('RegisteredOn', Date))
    LandOwnerId: Optional[str] = Field(default=None, sa_column=mapped_column('LandOwnerId', String(100)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))


class Landsurvey(SQLModel, table=True):
    LandSurveyId: Optional[UUID] = Field(default=None, sa_column=mapped_column('LandSurveyId', UUID, primary_key=True))
    LandId: UUID = Field(sa_column=mapped_column('LandId', UUID, nullable=False))
    RegisterOfficeId: Optional[UUID] = Field(default=None, sa_column=mapped_column('RegisterOfficeId', UUID))
    SurveyNumber: Optional[int] = Field(default=None, sa_column=mapped_column('SurveyNumber', INTEGER(11)))
    SubSurveyNumber: Optional[int] = Field(default=None, sa_column=mapped_column('SubSurveyNumber', INTEGER(11)))
    Alphabet: Optional[str] = Field(default=None, sa_column=mapped_column('Alphabet', String(2)))
    IsActive: Optional[int] = Field(default=None, sa_column=mapped_column('IsActive', TINYINT(1)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    CreatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('CreatedDate', DateTime))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Registeroffice(SQLModel, table=True):
    RegisterOfficeId: Optional[UUID] = Field(default=None, sa_column=mapped_column('RegisterOfficeId', UUID, primary_key=True))
    Name: Optional[str] = Field(default=None, sa_column=mapped_column('Name', String(100)))
    Location: Optional[str] = Field(default=None, sa_column=mapped_column('Location', String(100)))
    City: Optional[str] = Field(default=None, sa_column=mapped_column('City', String(100)))
    StateId: Optional[UUID] = Field(default=None, sa_column=mapped_column('StateId', UUID))
    DistrictId: Optional[str] = Field(default=None, sa_column=mapped_column('DistrictId', String(100)))
    IsActive: Optional[int] = Field(default=None, sa_column=mapped_column('IsActive', TINYINT(1)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    CreatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('CreatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))


class Role(SQLModel, table=True):
    __table_args__ = (
        Index('Role_unique', 'RoleCode', unique=True),
        Index('Role_unique_1', 'RoleName', unique=True)
    )

    RoleId: Optional[UUID] = Field(default=None, sa_column=mapped_column('RoleId', UUID, primary_key=True))
    RoleCode: str = Field(sa_column=mapped_column('RoleCode', String(10), nullable=False))
    RoleName: str = Field(sa_column=mapped_column('RoleName', String(100), nullable=False))
    Description: str = Field(sa_column=mapped_column('Description', String(1000), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class State(SQLModel, table=True):
    StateId: Optional[UUID] = Field(default=None, sa_column=mapped_column('StateId', UUID, primary_key=True))
    Name: str = Field(sa_column=mapped_column('Name', String(100), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    Abbreviation: Optional[str] = Field(default=None, sa_column=mapped_column('Abbreviation', String(5)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    CreatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('CreatedDate', DateTime))


class User(SQLModel, table=True):
    __table_args__ = (
        Index('User_unique', 'UserName', unique=True),
        Index('User_unique_1', 'FirstName', unique=True),
        Index('User_unique_2', 'NormalizedUserName', unique=True),
        Index('User_unique_3', 'Email', unique=True),
        Index('User_unique_4', 'NormalizedEmail', unique=True)
    )

    UserId: Optional[UUID] = Field(default=None, sa_column=mapped_column('UserId', UUID, primary_key=True))
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
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))


class Userrole(SQLModel, table=True):
    __table_args__ = (
        Index('userrole_unique', 'UserId', unique=True),
    )

    UserRoleId: Optional[UUID] = Field(default=None, sa_column=mapped_column('UserRoleId', UUID, primary_key=True))
    UserId: UUID = Field(sa_column=mapped_column('UserId', UUID, nullable=False))
    RoleId: UUID = Field(sa_column=mapped_column('RoleId', UUID, nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))

