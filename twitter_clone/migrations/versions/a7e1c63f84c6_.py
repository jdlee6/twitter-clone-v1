"""empty message

Revision ID: a7e1c63f84c6
Revises: f69dda949e2b
Create Date: 2019-08-18 00:34:28.900547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7e1c63f84c6'
down_revision = 'f69dda949e2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('test', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'test')
    # ### end Alembic commands ###
