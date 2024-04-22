"""Init

Revision ID: e49175d4331a
Revises: 
Create Date: 2024-04-11 20:12:37.033508

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e49175d4331a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    device_table = op.create_table(
        "device",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("role", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "extreme_value",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("min_full_power", sa.Float(), nullable=True),
        sa.Column("max_full_power", sa.Float(), nullable=True),
        sa.Column("min_active_power", sa.Float(), nullable=True),
        sa.Column("max_active_power", sa.Float(), nullable=True),
        sa.Column("min_reactive_power", sa.Float(), nullable=True),
        sa.Column("max_reactive_power", sa.Float(), nullable=True),
        sa.Column("min_voltage", sa.Float(), nullable=True),
        sa.Column("max_voltage", sa.Float(), nullable=True),
        sa.Column("min_amperage", sa.Float(), nullable=True),
        sa.Column("max_amperage", sa.Float(), nullable=True),
        sa.Column("min_power_factor", sa.Float(), nullable=True),
        sa.Column("max_power_factor", sa.Float(), nullable=True),
        sa.Column(
            "add_at",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.Column("device_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["device_id"], ["device.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "management_log",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("info", sa.String(), nullable=False),
        sa.Column("action", sa.String(), nullable=False),
        sa.Column(
            "data_of_origin",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("device_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["device_id"], ["device.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "value_device",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_power", sa.Float(), nullable=True),
        sa.Column("active_power", sa.Float(), nullable=True),
        sa.Column("reactive_power", sa.Float(), nullable=True),
        sa.Column("voltage", sa.Float(), nullable=True),
        sa.Column("amperage", sa.Float(), nullable=True),
        sa.Column("power_factor", sa.Float(), nullable=True),
        sa.Column(
            "date_of_collection",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.Column("device_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["device_id"], ["device.id"], ondelete="set null"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    data_device = [
        {'name': 'Трансформатор 1', 'type': 'трансформатор', 'is_active': True, 'status': 'исправен'},
        {'name': 'Трансформатор 2', 'type': 'трансформатор', 'is_active': True, 'status': 'исправен'},
        {'name': 'Трансформатор 3', 'type': 'трансформатор', 'is_active': True, 'status': 'исправен'},
        {'name': 'Трансформатор 4', 'type': 'трансформатор', 'is_active': True, 'status': 'исправен'},

        {'name': 'Разъединитель 1_1', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 1_2', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 1_3', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 1_4', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},

        {'name': 'Разъединитель 2_1', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 2_2', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 2_3', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 2_4', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 2_5', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 2_6', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 2_7', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 2_8', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},

        {'name': 'Разъединитель 3_1', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_2', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_3', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_4', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_5', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_6', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_7', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_8', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_9', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_10', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_11', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_12', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_13', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_14', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_15', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 3_16', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},

        {'name': 'Разъединитель 4_1', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 4_2', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 4_3', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 4_4', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 4_5', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
        {'name': 'Разъединитель 4_6', 'type': 'разъединитель', 'is_active': True, 'status': 'исправен'},
    ]
    # вставка данных в таблицу
    op.bulk_insert(device_table, data_device)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("value_device")
    op.drop_table("management_log")
    op.drop_table("extreme_value")
    op.drop_table("users")
    op.drop_table("device")
    # ### end Alembic commands ###
