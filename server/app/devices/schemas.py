import datetime
from pydantic import BaseModel

from app.users.schemas import SUserBase


class DeviceBase(BaseModel):
    name: str
    type: str
    is_active: bool 
    status: str

class ValueDeviceBase(BaseModel):
    full_power: float
    active_power: float
    reactive_power: float
    voltage: float
    amperage: float
    power_factor: float

class ValueDeviceCreate(ValueDeviceBase):
    device_id: int
    
class ValueDeviceGet(ValueDeviceBase):
    date_of_collection: datetime.datetime

class DeviceBaseGet(DeviceBase):
    id: int
    # value_device: list[ValueDeviceGet]


class AccidentLog(BaseModel):
    info: str
    date_of_origin: datetime.datetime

class AccidentLogGet(BaseModel):
    id: int
    info: str
    date_of_origin: datetime.datetime
    device: DeviceBaseGet


class ManagementLogInfo(BaseModel):
    info: str
    action: str
    user_id: int
    device_id: int


class ManagementLogInfoGet(ManagementLogInfo):
    id: int
    users: SUserBase
    device: DeviceBase
    date_of_origin: datetime.datetime


class ValueFullPower(BaseModel):
    full_power: float
    date_of_collection: datetime.datetime

    
# class ExtremeValueBase(BaseModel):
#     min_full_power: float
#     max_full_power: float
#     min_active_power: float
#     max_active_power: float
#     min_reactive_power: float
#     max_reactive_power: float
#     min_voltage: float
#     max_voltage: float
#     min_amperage:float
#     max_amperage:float
#     min_power_factor: float
#     max_power_factor: float

# class ExtremeValueCreate(ExtremeValueBase):
#     device_id: int

# class ExtremeValueGet(ExtremeValueBase):
#     add_at: datetime.datetime