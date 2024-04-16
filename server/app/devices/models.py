import datetime
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.users.models import *

class Device(Base):
    __tablename__ = 'device'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    type: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    status: Mapped[str] = mapped_column(default='good')

    value_device: Mapped[list["ValueDevice"]] = relationship(
        back_populates="device",
        lazy="selectin"
    )

    extreme_value: Mapped[list["ExtremeValue"]] = relationship(
        back_populates="device",
        lazy="selectin"
    )

    management_log: Mapped[list["ManagementLog"]] = relationship(
        back_populates="device",
        lazy="selectin"
    )


class ValueDevice(Base):
    __tablename__ = 'value_device'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_power: Mapped[float | None]
    active_power: Mapped[float | None]
    reactive_power: Mapped[float | None]
    voltage: Mapped[float | None]
    amperage: Mapped[float | None]
    power_factor: Mapped[float | None]
    date_of_collection: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    device_id: Mapped[int] = mapped_column(ForeignKey("device.id", ondelete="set null"))

    device: Mapped["Device"] = relationship(
        back_populates='value_device'
    )
    

class ExtremeValue(Base):
    __tablename__ = 'extreme_value'

    id: Mapped[int] = mapped_column(primary_key=True)
    min_full_power: Mapped[float | None]
    max_full_power: Mapped[float | None]
    min_active_power: Mapped[float | None]
    max_active_power: Mapped[float | None]
    min_reactive_power: Mapped[float | None]
    max_reactive_power: Mapped[float | None]
    min_voltage: Mapped[float | None]
    max_voltage: Mapped[float | None]
    min_amperage: Mapped[float | None]
    max_amperage: Mapped[float | None]
    min_power_factor: Mapped[float | None]
    max_power_factor: Mapped[float | None]
    add_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    device_id: Mapped[int] = mapped_column(ForeignKey("device.id", ondelete="CASCADE"))

    device: Mapped["Device"] = relationship(
        back_populates='extreme_value'
    )

class ManagementLog(Base):
    __tablename__ = 'management_log'

    id: Mapped[int] = mapped_column(primary_key=True)
    info: Mapped[str]
    data_of_origin: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    device_id: Mapped[int] = mapped_column(ForeignKey("device.id", ondelete="SET NULL"))

    users: Mapped["Users"] = relationship(
        back_populates='management_log'
    )

    device: Mapped["Device"] = relationship(
        back_populates='management_log'
    )

