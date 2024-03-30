import datetime
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

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

    value_device: Mapped[list["ExtremeValue"]] = relationship(
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