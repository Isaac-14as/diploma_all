from sqlalchemy import Column, Integer, String, Boolean, Float, Date
from app.database import Base

class Device(Base):
    __tablename__ = 'device'
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    status = Column(String, nullable=False, default='good')


class ValueDevice(Base):
    __tablename__ = 'value_device'
    
    id = Column(Integer, primary_key=True, nullable=False)
    full_power = Column(Float, nullable=True)
    active_power = Column(Float, nullable=True)
    reactive_power = Column(Float, nullable=True)
    voltage = Column(Float, nullable=True)
    amperage = Column(Float, nullable=True)
    power_factor = Column(Float, nullable=True)
    date_of_collection = Column(Date, nullable=False)
    
