"""create table users

Revision ID: 0b4a7bcf2233
Revises: 4d3de7a365c9
Create Date: 2023-02-28 17:34:08.111638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b4a7bcf2233'
down_revision = '4d3de7a365c9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('T_USUARIOS',
        sa.Column('USU_ID', sa.Integer(), nullable=False),
        sa.Column('USU_EMAIL', sa.String(100), nullable=False),
        sa.Column('USU_PASSWORD', sa.String(), nullable=False),
        sa.Column('USU_CREATED_AT', sa.DATETIME, server_default=sa.text('GETDATE()'), nullable=False),
        sa.PrimaryKeyConstraint('USU_ID'),
        sa.UniqueConstraint('USU_EMAIL')
    )
    pass


def downgrade() -> None:
    op.drop_table('T_USUARIOS')
    pass
