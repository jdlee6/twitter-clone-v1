"""empty message

Revision ID: 0013c6a96e6b
Revises: a99034a802e3
Create Date: 2019-08-18 21:23:05.274350

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0013c6a96e6b'
down_revision = 'a99034a802e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=True),
                    sa.Column('username', sa.String(length=30), nullable=True),
                    sa.Column('email', sa.String(length=120), nullable=True),
                    sa.Column('image', sa.String(length=100), nullable=True),
                    sa.Column('password', sa.String(length=50), nullable=True),
                    sa.Column('join_date', sa.DateTime(), nullable=True),
                    sa.Column('test', sa.String(length=50), nullable=True),
                    sa.PrimaryKeyConstraint('id'))
    op.create_table('tweet', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('text', sa.String(length=140), nullable=True),
                    sa.Column('date_created', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['user_id'],
                        ['user.id'],
                    ), sa.PrimaryKeyConstraint('id'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweet')
    op.drop_table('user')
    # ### end Alembic commands ###
