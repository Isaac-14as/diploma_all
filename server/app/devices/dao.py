from app.dao.base import BaseDAO
from app.devices.models import Device, ValueDevice, ManagementLog
from app.database import async_session_maker


from sqlalchemy import func, select 
class DevaceDAO(BaseDAO):
    model = Device


class ValueDeviceDAO(BaseDAO):
    model = ValueDevice

    @classmethod
    async def find_last_value(cls, device_id: int):
        async with async_session_maker() as session:
            max_date_of_collection = select(func.max(ValueDevice.date_of_collection)).filter_by(device_id=device_id)
            query = select(ValueDevice).filter_by(date_of_collection=max_date_of_collection)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        

class ManagementLogDAO(BaseDAO):
    model = ManagementLog
