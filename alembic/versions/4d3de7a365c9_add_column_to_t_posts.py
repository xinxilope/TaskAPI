"""add column to T_POSTS

Revision ID: 4d3de7a365c9
Revises: 0db9c7758145
Create Date: 2023-02-28 17:21:42.619669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d3de7a365c9'
down_revision = '0db9c7758145'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('T_POSTS',
        sa.Column('POS_DESCRIPTION', sa.String()))
    pass


def downgrade() -> None:
    op.drop_column('T_POSTS', 'POS_DESCRIPTION')
    pass
