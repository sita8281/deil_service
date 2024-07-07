"""empty message

Revision ID: 134df8d6691b
Revises: 7e20a09b58d8
Create Date: 2024-03-04 13:36:18.966373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '134df8d6691b'
down_revision = '7e20a09b58d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carbon_api_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('date', sa.String(length=20), nullable=True),
    sa.Column('data', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carbon_api_data')
    # ### end Alembic commands ###
