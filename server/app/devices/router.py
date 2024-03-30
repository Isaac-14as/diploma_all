from fastapi import APIRouter, Depends

from app.devices.dao import DevaseDAO, ValueDeviceDAO
from app.devices.schemas import *
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/device",
    tags=["Devices"],
)


@router.post('/create_device', dependencies=[Depends(get_current_user)])
async def create_device(device: DeviceBase):
    await DevaseDAO.add(**device.model_dump())
    return {'status': 200, 'detail': 'Устройство успешно добавлено.'}


@router.get('/get_all_devices', response_model=list[DeviceBaseGet], dependencies=[Depends(get_current_user)])
async def get_all_device():
    devices = await DevaseDAO.find_all()
    return devices


# вероятно, не нужно
@router.post('/create_value_device', dependencies=[Depends(get_current_user)])
async def create_device(value_device: ValueDeviceCreate):
    await ValueDeviceDAO.add(**value_device.model_dump())
    return {'status': 200, 'detail': 'Значение успешно добавлено.'}


@router.get('/get_all_value_device_by_id', response_model=list[ValueDeviceGet], dependencies=[Depends(get_current_user)])
async def get_all_value_device_by_id(device_id: int):
    res = await ValueDeviceDAO.find_all(device_id=device_id)
    return res

@router.get('/get_last_value_device_by_id', response_model=ValueDeviceGet, dependencies=[Depends(get_current_user)])
async def get_last_value_device_by_id(device_id: int):
    res = await ValueDeviceDAO.find_last_value(device_id)
    return res


@router.post('/add_extreme_value', dependencies=[Depends(get_current_user)])
async def add_extreme_value(value_extreme_value: ValueDeviceCreate):
    await ValueDeviceDAO.add(**value_extreme_value.model_dump())
    return {'status': 200, 'detail': 'Значение успешно добавлено.'}


# доделать
# @router.get('/get_last_extreme_value_by_id', response_model=, dependencies=[Depends(get_current_user)])
# async def get_extreme_value_by_id(device_id: int):
#     res = await ValueDeviceDAO.find_all(device_id=device_id)
#     return res
