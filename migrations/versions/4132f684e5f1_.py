"""empty message

Revision ID: 4132f684e5f1
Revises: fd3b97c8cc9a
Create Date: 2016-08-05 22:38:18.946000

"""

# revision identifiers, used by Alembic.
revision = '4132f684e5f1'
down_revision = 'fd3b97c8cc9a'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('discount_codes', sa.Column('tickets_number', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('discount_codes', 'tickets_number')
    ### end Alembic commands ###
