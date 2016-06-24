"""empty message

Revision ID: e26f43ffffb8
Revises: ffc3cf9856fb
Create Date: 2016-06-24 00:14:52.041919

"""

# revision identifiers, used by Alembic.
revision = 'e26f43ffffb8'
down_revision = 'ffc3cf9856fb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('avatar_url', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('leaves', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('losses', sa.Integer(), nullable=True),
    sa.Column('mastery_level', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('personal_status_message', sa.String(), nullable=True),
    sa.Column('total_achievements', sa.Integer(), nullable=True),
    sa.Column('total_worshipers', sa.Integer(), nullable=True),
    sa.Column('wins', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player')
    ### end Alembic commands ###