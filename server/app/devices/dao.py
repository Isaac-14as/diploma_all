from datetime import datetime
from app.dao.base import BaseDAO
from app.devices.models import AccidentLog, Device, ValueDevice, ManagementLog
from app.database import async_session_maker


from sqlalchemy import and_, func, select 
class DevaceDAO(BaseDAO):
    model = Device


class ValueDeviceDAO(BaseDAO):
    model = ValueDevice

    @classmethod
    async def find_last_value(cls, device_id: int):
        async with async_session_maker() as session:
            max_date_of_collection = select(func.max(cls.model.date_of_collection)).filter_by(device_id=device_id)
            query = select(cls.model).filter_by(date_of_collection=max_date_of_collection)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_by_date_time(cls, device_id: int, date: datetime.date, time_from: datetime.time, time_to: datetime.time):
        datetime_from = datetime.combine(date, time_from)
        datetime_to = datetime.combine(date, time_to)
        async with async_session_maker() as session:
            query = select(cls.model).where(
                and_(
                    cls.model.device_id == device_id,
                    cls.model.date_of_collection > datetime_from,
                    cls.model.date_of_collection < datetime_to
                )
            ).order_by(cls.model.date_of_collection)
            result = await session.execute(query)
            return result.scalars().all()
        

class ManagementLogDAO(BaseDAO):
    model = ManagementLog

    @classmethod
    async def find_by_date_time(cls, date: datetime.date, time_from: datetime.time, time_to: datetime.time):
        datetime_from = datetime.combine(date, time_from)
        datetime_to = datetime.combine(date, time_to)
        async with async_session_maker() as session:
            query = select(cls.model).where(
                and_(
                    cls.model.date_of_origin > datetime_from,
                    cls.model.date_of_origin < datetime_to
                )
            ).order_by(cls.model.date_of_origin)
            result = await session.execute(query)
            return result.scalars().all()




class AccidentLogDAO(BaseDAO):
    model = AccidentLog

    @classmethod
    async def find_by_date_time(cls, date: datetime.date, time_from: datetime.time, time_to: datetime.time):
        datetime_from = datetime.combine(date, time_from)
        datetime_to = datetime.combine(date, time_to)
        async with async_session_maker() as session:
            query = select(cls.model).where(
                and_(
                    cls.model.date_of_origin > datetime_from,
                    cls.model.date_of_origin < datetime_to
                )
            ).order_by(cls.model.date_of_origin)
            result = await session.execute(query)
            return result.scalars().all()

