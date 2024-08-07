"""empty message

Revision ID: 8967a37279d9
Revises: 5cfaf8ce45d7
Create Date: 2024-07-31 02:38:35.695084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8967a37279d9'
down_revision = '5cfaf8ce45d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('connect_statements', sa.Column('for_whom_color', sa.String(length=40), nullable=True))
    op.add_column('connect_statements', sa.Column('folder_id', sa.Integer(), nullable=True))
    op.alter_column('connect_statements', 'for_whom',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=100),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('connect_statements', 'for_whom',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=30),
               existing_nullable=True)
    op.drop_column('connect_statements', 'folder_id')
    op.drop_column('connect_statements', 'for_whom_color')
    # ### end Alembic commands ###
