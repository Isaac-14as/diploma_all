import datetime
from pydantic import BaseModel


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
    value_device: list[ValueDeviceGet]



class ExtremeValueBase(BaseModel):
    min_full_power: float
    max_full_power: float
    min_active_power: float
    max_active_power: float
    min_reactive_power: float
    max_reactive_power: float
    min_voltage: float
    max_voltage: float
    min_amperage:float
    max_amperage:float
    min_power_factor: float
    max_power_factor: float

class ExtremeValueCreate(ExtremeValueBase):
    device_id: int

class ExtremeValueGet(ExtremeValueBase):
    add_at: datetime.datetime


class ManagementLogInfo(BaseModel):
    info: str
    action: str
    user_id: int
    device_id: int