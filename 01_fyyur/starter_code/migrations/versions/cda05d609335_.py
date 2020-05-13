"""empty message

Revision ID: cda05d609335
Revises: 5b890403e46f
Create Date: 2020-05-10 01:47:57.326608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cda05d609335'
down_revision = '5b890403e46f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artistgeners', sa.Column('name', sa.String(), nullable=False))
    op.add_column('venuegeners', sa.Column('name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venuegeners', 'name')
    op.drop_column('artistgeners', 'name')
    # ### end Alembic commands ###
