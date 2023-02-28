"""phone column

Revision ID: 6cff786b8fb1
Revises: f82c935c2543
Create Date: 2023-02-28 18:21:18.321934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cff786b8fb1'
down_revision = 'f82c935c2543'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('T_USUARIOS', sa.Column('USU_PHONE', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('T_USUARIOS', 'USU_PHONE')
    # ### end Alembic commands ###
