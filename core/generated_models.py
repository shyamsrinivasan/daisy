from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, ForeignKeyConstraint, Index, String, UUID, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm.base import Mapped
from sqlmodel import Field, Relationship, SQLModel

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

    location: List['Location'] = Relationship(back_populates='district')
    registeroffice: List['Registeroffice'] = Relationship(back_populates='district')


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

    fertilizernutrient: List['Fertilizernutrient'] = Relationship(back_populates='fertilizer')
    fertilizerapplication: List['Fertilizerapplication'] = Relationship(back_populates='fertilizer')


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


class Menu(SQLModel, table=True):
    __table_args__ = (
        Index('menu_unique_1', 'LinkPath', unique=True),
    )

    MenuId: Optional[UUID] = Field(default=None, sa_column=mapped_column('MenuId', UUID, primary_key=True))
    MenuOrder: int = Field(sa_column=mapped_column('MenuOrder', INTEGER(11), nullable=False))
    ModuleName: str = Field(sa_column=mapped_column('ModuleName', String(100), nullable=False))
    ModuleOrder: int = Field(sa_column=mapped_column('ModuleOrder', INTEGER(11), nullable=False))
    LinkName: str = Field(sa_column=mapped_column('LinkName', String(100), nullable=False))
    LinkPath: str = Field(sa_column=mapped_column('LinkPath', String(100), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    MenuName: Optional[str] = Field(default=None, sa_column=mapped_column('MenuName', String(50)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))

    roleaccess: List['Roleaccess'] = Relationship(back_populates='menu')


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

    roleaccess: List['Roleaccess'] = Relationship(back_populates='role')
    userrole: List['Userrole'] = Relationship(back_populates='role')


class State(SQLModel, table=True):
    StateId: Optional[UUID] = Field(default=None, sa_column=mapped_column('StateId', UUID, primary_key=True))
    Name: str = Field(sa_column=mapped_column('Name', String(100), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    Abbreviation: Optional[str] = Field(default=None, sa_column=mapped_column('Abbreviation', String(5)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    CreatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('CreatedDate', DateTime))

    location: List['Location'] = Relationship(back_populates='state')
    registeroffice: List['Registeroffice'] = Relationship(back_populates='state')


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
    UserType: Optional[str] = Field(default=None, sa_column=mapped_column('UserType', String(1), server_default=text("'U'"), comment='U: Regular user, S: Super user, O: Other user, D: Development user'))

    userrole: List['Userrole'] = Relationship(back_populates='user')


class Fertilizernutrient(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['FertilizerId'], ['fertilizer.FertilizerId'], name='fk_fertilizer_nutrient'),
        Index('fk_fertilizer_nutrient', 'FertilizerId')
    )

    FertilizerNutrientId: Optional[UUID] = Field(default=None, sa_column=mapped_column('FertilizerNutrientId', UUID, primary_key=True))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    FertilizerId: Optional[UUID] = Field(default=None, sa_column=mapped_column('FertilizerId', UUID))
    NitrogenPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('NitrogenPercent', DECIMAL(18, 2)))
    PhosphorousPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('PhosphorousPercent', DECIMAL(18, 2)))
    PotassiumPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('PotassiumPercent', DECIMAL(18, 2)))
    SulphurPercent: Optional[Decimal] = Field(default=None, sa_column=mapped_column('SulphurPercent', DECIMAL(18, 2), server_default=text('0.00')))
    OtherNutrients: Optional[str] = Field(default=None, sa_column=mapped_column('OtherNutrients', String(1000)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))

    fertilizer: Optional['Fertilizer'] = Relationship(back_populates='fertilizernutrient')


class Location(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['DistrictId'], ['district.DistrictId'], name='fk_district_location'),
        ForeignKeyConstraint(['StateId'], ['state.StateId'], name='fk_state_location'),
        Index('fk_district_location', 'DistrictId'),
        Index('fk_state_location', 'StateId')
    )

    LocationId: Optional[UUID] = Field(default=None, sa_column=mapped_column('LocationId', UUID, primary_key=True))
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

    district: Optional['District'] = Relationship(back_populates='location')
    state: Optional['State'] = Relationship(back_populates='location')
    land: List['Land'] = Relationship(back_populates='location')


class Registeroffice(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['DistrictId'], ['district.DistrictId'], name='fk_district_registeroffice'),
        ForeignKeyConstraint(['StateId'], ['state.StateId'], name='fk_state_registeroffice'),
        Index('fk_district_registeroffice', 'DistrictId'),
        Index('fk_state_registeroffice', 'StateId')
    )

    RegisterOfficeId: Optional[UUID] = Field(default=None, sa_column=mapped_column('RegisterOfficeId', UUID, primary_key=True))
    Name: Optional[str] = Field(default=None, sa_column=mapped_column('Name', String(100)))
    Location_: Optional[str] = Field(default=None, sa_column=mapped_column('Location', String(100)))
    City: Optional[str] = Field(default=None, sa_column=mapped_column('City', String(100)))
    DistrictId: Optional[UUID] = Field(default=None, sa_column=mapped_column('DistrictId', UUID))
    StateId: Optional[UUID] = Field(default=None, sa_column=mapped_column('StateId', UUID))
    IsActive: Optional[int] = Field(default=None, sa_column=mapped_column('IsActive', TINYINT(1)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    CreatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('CreatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))

    district: Optional['District'] = Relationship(back_populates='registeroffice')
    state: Optional['State'] = Relationship(back_populates='registeroffice')
    landsurvey: List['Landsurvey'] = Relationship(back_populates='registeroffice')


class Roleaccess(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['MenuId'], ['menu.MenuId'], name='fk_menu_roleaccess'),
        ForeignKeyConstraint(['RoleId'], ['role.RoleId'], name='fk_role_roleaccess'),
        Index('roleaccess_MenuId_IDX', 'MenuId'),
        Index('roleaccess_RoleId_IDX', 'RoleId')
    )

    RoleAccessId: Optional[UUID] = Field(default=None, sa_column=mapped_column('RoleAccessId', UUID, primary_key=True))
    RoleId: UUID = Field(sa_column=mapped_column('RoleId', UUID, nullable=False))
    MenuId: UUID = Field(sa_column=mapped_column('MenuId', UUID, nullable=False))
    IsAdd: int = Field(sa_column=mapped_column('IsAdd', TINYINT(1), nullable=False))
    IsView: int = Field(sa_column=mapped_column('IsView', TINYINT(1), nullable=False))
    IsEdit: int = Field(sa_column=mapped_column('IsEdit', TINYINT(1), nullable=False))
    IsDelete: int = Field(sa_column=mapped_column('IsDelete', TINYINT(1), nullable=False))
    IsAdmin: int = Field(sa_column=mapped_column('IsAdmin', TINYINT(1), nullable=False))
    IsApprover: int = Field(sa_column=mapped_column('IsApprover', TINYINT(1), nullable=False))
    IsExport: int = Field(sa_column=mapped_column('IsExport', TINYINT(1), nullable=False))
    IsImport: int = Field(sa_column=mapped_column('IsImport', TINYINT(1), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))

    menu: Optional['Menu'] = Relationship(back_populates='roleaccess')
    role: Optional['Role'] = Relationship(back_populates='roleaccess')


class Userrole(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['RoleId'], ['role.RoleId'], name='fk_role_userrole'),
        ForeignKeyConstraint(['UserId'], ['user.UserId'], name='fk_user_userrole'),
        Index('fk_role_userrole', 'RoleId'),
        Index('userrole_unique', 'UserId', unique=True)
    )

    UserRoleId: Optional[UUID] = Field(default=None, sa_column=mapped_column('UserRoleId', UUID, primary_key=True))
    UserId: UUID = Field(sa_column=mapped_column('UserId', UUID, nullable=False))
    RoleId: UUID = Field(sa_column=mapped_column('RoleId', UUID, nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))

    role: Optional['Role'] = Relationship(back_populates='userrole')
    user: Optional['User'] = Relationship(back_populates='userrole')


class Land(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['LocationId'], ['location.LocationId'], name='fk_location_land'),
        Index('fk_location_land', 'LocationId'),
        Index('land_landid_IDX', 'LandId')
    )

    LandId: Optional[UUID] = Field(default=None, sa_column=mapped_column('LandId', UUID, primary_key=True))
    LandName: Optional[str] = Field(default=None, sa_column=mapped_column('LandName', String(100)))
    LocationId: Optional[UUID] = Field(default=None, sa_column=mapped_column('LocationId', UUID))
    CreatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('CreatedDate', DateTime))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    IsActive: Optional[int] = Field(default=None, sa_column=mapped_column('IsActive', TINYINT(1)))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))

    location: Optional['Location'] = Relationship(back_populates='land')
    field: List['Field_'] = Relationship(back_populates='land')
    landsurvey: List['Landsurvey'] = Relationship(back_populates='land')


class Field_(SQLModel, table=True):
    __tablename__ = 'field'
    __table_args__ = (
        ForeignKeyConstraint(['LandId'], ['land.LandId'], name='fk_land_field'),
        Index('field_unique', 'FieldCode', unique=True),
        Index('fk_land_field', 'LandId')
    )

    FieldId: Optional[UUID] = Field(default=None, sa_column=mapped_column('FieldId', UUID, primary_key=True))
    FieldCode: str = Field(sa_column=mapped_column('FieldCode', String(10), nullable=False))
    FieldName: str = Field(sa_column=mapped_column('FieldName', String(2000), nullable=False))
    LandId: UUID = Field(sa_column=mapped_column('LandId', UUID, nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))
    Acres: Optional[Decimal] = Field(default=None, sa_column=mapped_column('Acres', DECIMAL(18, 2)))
    Cents: Optional[Decimal] = Field(default=None, sa_column=mapped_column('Cents', DECIMAL(18, 2)))
    CreatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('CreatedBy', UUID))
    UpdatedDate: Optional[datetime] = Field(default=None, sa_column=mapped_column('UpdatedDate', DateTime))
    UpdatedBy: Optional[UUID] = Field(default=None, sa_column=mapped_column('UpdatedBy', UUID))

    land: Optional['Land'] = Relationship(back_populates='field')
    fertilizerapplication: List['Fertilizerapplication'] = Relationship(back_populates='field')


class Landsurvey(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['LandId'], ['land.LandId'], name='fk_land_landsurvey'),
        ForeignKeyConstraint(['RegisterOfficeId'], ['registeroffice.RegisterOfficeId'], name='fk_registeroffice_landsurvey'),
        Index('fk_land_landsurvey', 'LandId'),
        Index('fk_registeroffice_landsurvey', 'RegisterOfficeId')
    )

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

    land: Optional['Land'] = Relationship(back_populates='landsurvey')
    registeroffice: Optional['Registeroffice'] = Relationship(back_populates='landsurvey')


class Fertilizerapplication(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['FertilizerId'], ['fertilizer.FertilizerId'], name='fk_fertilizer_fertlizerapplication'),
        ForeignKeyConstraint(['FieldId'], ['field.FieldId'], name='fk_field_fertlizerapplication'),
        Index('fk_fertilizer_fertlizerapplication', 'FertilizerId'),
        Index('fk_field_fertlizerapplication', 'FieldId')
    )

    FertilizerApplicationId: Optional[UUID] = Field(default=None, sa_column=mapped_column('FertilizerApplicationId', UUID, primary_key=True))
    FertilizerId: UUID = Field(sa_column=mapped_column('FertilizerId', UUID, nullable=False))
    FieldId: UUID = Field(sa_column=mapped_column('FieldId', UUID, nullable=False))
    AppliedOn: datetime = Field(sa_column=mapped_column('AppliedOn', DateTime, nullable=False))
    QuantityInKg: Decimal = Field(sa_column=mapped_column('QuantityInKg', DECIMAL(4, 2), nullable=False))
    QuantityInBags: Decimal = Field(sa_column=mapped_column('QuantityInBags', DECIMAL(4, 2), nullable=False))
    IsActive: int = Field(sa_column=mapped_column('IsActive', TINYINT(1), nullable=False, server_default=text('1')))
    CreatedBy: UUID = Field(sa_column=mapped_column('CreatedBy', UUID, nullable=False))
    CreatedDate: datetime = Field(sa_column=mapped_column('CreatedDate', DateTime, nullable=False))

    fertilizer: Optional['Fertilizer'] = Relationship(back_populates='fertilizerapplication')
    field: Optional['Field_'] = Relationship(back_populates='fertilizerapplication')

