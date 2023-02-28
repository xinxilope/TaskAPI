"""add FK T_POSTS table

Revision ID: 1e84faf77d81
Revises: 0b4a7bcf2233
Create Date: 2023-02-28 17:56:51.946506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e84faf77d81'
down_revision = '0b4a7bcf2233'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('T_POSTS', sa.Column('POS_USU_ID', sa.Integer(), nullable=False))
    op.create_foreign_key('POSTS_USUARIOS_FK', source_table='T_POSTS', referent_table='T_USUARIOS', local_cols=['POS_USU_ID'], remote_cols=['USU_ID'])
    pass


def downgrade() -> None:
    op.drop_constraint('POSTS_USUARIOS_FK', table_name='T_POSTS')
    op.drop_column('T_POSTS', 'POS_USU_ID')
    pass
