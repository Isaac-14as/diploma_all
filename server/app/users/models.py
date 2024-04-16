import enum
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.devices.models import ManagementLog

# class Role(enum.Enum):
#     staff = "сотрудник"
#     admin = "администратор"


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]
    name: Mapped[str]
    role: Mapped[str]

    management_log: Mapped[list["ManagementLog"]]  = relationship(
        back_populates="users",
        lazy="selectin"
    )

