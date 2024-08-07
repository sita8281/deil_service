"""empty message

Revision ID: 7e20a09b58d8
Revises: dccc91cd0583
Create Date: 2024-03-04 13:31:48.731452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e20a09b58d8'
down_revision = 'dccc91cd0583'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config_storage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('date', sa.String(length=20), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('forward_gateway_params',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_ip', sa.String(length=20), nullable=True),
    sa.Column('external_port', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('forward_gateway_params')
    op.drop_table('config_storage')
    # ### end Alembic commands ###
