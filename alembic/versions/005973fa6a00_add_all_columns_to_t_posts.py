"""add all columns to T_POSTS

Revision ID: 005973fa6a00
Revises: 1e84faf77d81
Create Date: 2023-02-28 18:05:32.113371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '005973fa6a00'
down_revision = '1e84faf77d81'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('T_POSTS', sa.Column('POS_PUBLISHED', sa.Boolean(), nullable=False, server_default='TRUE')),
    op.add_column('T_POSTS', sa.Column('POS_CREATED_AT', sa.DATETIME(), nullable=False, server_default=sa.text('GETDATE()')))
    pass


def downgrade() -> None:
    op.drop_column('T_POSTS', 'POS_PUBLISHED'),
    op.drop_column('T_POSTS', 'POS_CREATED_AT')
    pass
