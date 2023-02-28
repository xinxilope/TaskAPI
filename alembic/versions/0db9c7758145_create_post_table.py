"""create post table

Revision ID: 0db9c7758145
Revises: 
Create Date: 2023-02-28 17:04:27.286185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0db9c7758145'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('T_POSTS',
        sa.Column('POS_ID', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('POS_TITLE', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('T_POSTS')
    pass
