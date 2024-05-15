from fastapi import APIRouter, Depends, Path

from app.devices.dao import AccidentLogDAO, DevaceDAO, ManagementLogDAO, ValueDeviceDAO
from app.devices.schemas import *
from app.users.dependencies import get_current_user

from datetime import datetime

router = APIRouter(
    prefix="/device",
    tags=["Devices"],
)


@router.post('/create_device', dependencies=[Depends(get_current_user)])
async def create_device(device: DeviceBase):
    await DevaceDAO.add(**device.model_dump())
    return {'status': 200, 'detail': 'Устройство успешно добавлено.'}


@router.get('/get_all_devices', response_model=list[DeviceBaseGet], dependencies=[Depends(get_current_user)])
async def get_all_device():
    devices = await DevaceDAO.find_all()
    return devices

@router.get('/get_device_by_id/{id}', response_model=DeviceBaseGet, dependencies=[Depends(get_current_user)])
async def get_all_device(id: int):
    device = await DevaceDAO.find_one_or_none(id=id)
    return device


# вероятно, не нужно
@router.post('/create_value_device', dependencies=[Depends(get_current_user)])
async def create_device(value_device: ValueDeviceCreate):
    await ValueDeviceDAO.add(**value_device.model_dump())
    return {'status': 200, 'detail': 'Значение успешно добавлено.'}


@router.get('/get_all_value_device_by_id/{device_id}', response_model=list[ValueDeviceGet], dependencies=[Depends(get_current_user)])
async def get_all_value_device_by_id(device_id: int):
    res = await ValueDeviceDAO.find_all(device_id=device_id)
    return res

@router.get('/get_last_value_device_by_id/{device_id}', response_model=ValueDeviceGet, dependencies=[Depends(get_current_user)])
async def get_last_value_device_by_id(device_id: int):
    res = await ValueDeviceDAO.find_last_value(device_id)
    return res


@router.post('/add_extreme_value', dependencies=[Depends(get_current_user)])
async def add_extreme_value(value_extreme_value: ValueDeviceCreate):
    await ValueDeviceDAO.add(**value_extreme_value.model_dump())
    return {'status': 200, 'detail': 'Значение успешно добавлено.'}

@router.get('/get_full_power/{device_id}/{date}/{time_from}/{time_to}', response_model=list[ValueFullPower], dependencies=[Depends(get_current_user)])
async def get_full_power(device_id: int, date: str, time_from: str, time_to: str):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    time_from = datetime.strptime(time_from, "%H:%M:%S").time()
    time_to = datetime.strptime(time_to, "%H:%M:%S").time()
    res = await ValueDeviceDAO.find_by_date_time(device_id, date, time_from, time_to)
    return res

@router.get('/get_value_by_date_time/{device_id}/{date}/{time_from}/{time_to}', response_model=list[ValueDeviceGet], dependencies=[Depends(get_current_user)])
async def get_value_by_date_time(device_id: int, date: str, time_from: str, time_to: str):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    time_from = datetime.strptime(time_from, "%H:%M:%S").time()
    time_to = datetime.strptime(time_to, "%H:%M:%S").time()
    res = await ValueDeviceDAO.find_by_date_time(device_id, date, time_from, time_to)
    return res

@router.patch('/device_switch_off/{device_id}', dependencies=[Depends(get_current_user)])
async def device_switch_off(device_id: int):
    device = await DevaceDAO.find_by_id(device_id)
    device = {
        'name': device.name,
        'type': device.type,
        'is_active': False,
        'status': device.status
        }
    await DevaceDAO.change_by_id(device_id, **device)
    return {'status': 200, 'detail': 'Устройство выключено.'}

@router.patch('/device_turn_on/{device_id}', dependencies=[Depends(get_current_user)])
async def device_turn_on(device_id: int):
    device = await DevaceDAO.find_by_id(device_id)
    device = {
        'name': device.name,
        'type': device.type,
        'is_active': True,
        'status': device.status
        }
    await DevaceDAO.change_by_id(device_id, **device)
    return {'status': 200, 'detail': 'Устройство включено.'}


@router.post('/add_management_log', dependencies=[Depends(get_current_user)])
async def add_management_log(management_log_info: ManagementLogInfo):
    await ManagementLogDAO.add(**management_log_info.model_dump())
    return {'status': 200, 'detail': 'Запиь успешно добавлена.'}


@router.get('/get_all_management_log', response_model=list[ManagementLogInfoGet], dependencies=[Depends(get_current_user)])
async def get_all_management_log():
    management_log = await ManagementLogDAO.find_all()
    return management_log

@router.get('/get_management_log_date_time/{date}/{time_from}/{time_to}', response_model=list[ManagementLogInfoGet], dependencies=[Depends(get_current_user)])
async def get_management_log_date_time(date: str, time_from: str, time_to: str):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    time_from = datetime.strptime(time_from, "%H:%M:%S").time()
    time_to = datetime.strptime(time_to, "%H:%M:%S").time()
    res = await ManagementLogDAO.find_by_date_time(date, time_from, time_to)
    return res


@router.get('/get_accident_log', response_model=list[AccidentLogGet], dependencies=[Depends(get_current_user)])
async def get_accident_log():
    accident_log = await AccidentLogDAO.find_all()
    return accident_log

@router.get('/get_accident_log_date_time/{date}/{time_from}/{time_to}', response_model=list[AccidentLogGet], dependencies=[Depends(get_current_user)])
async def get_accident_log_date_time(date: str, time_from: str, time_to: str):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    time_from = datetime.strptime(time_from, "%H:%M:%S").time()
    time_to = datetime.strptime(time_to, "%H:%M:%S").time()
    res = await AccidentLogDAO.find_by_date_time(date, time_from, time_to)
    return res


# доделать
# @router.get('/get_last_extreme_value_by_id', response_model=, dependencies=[Depends(get_current_user)])
# async def get_extreme_value_by_id(device_id: int):
#     res = await ValueDeviceDAO.find_all(device_id=device_id)
#     return res
