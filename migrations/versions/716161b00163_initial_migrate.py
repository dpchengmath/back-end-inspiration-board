"""initial migrate

Revision ID: 716161b00163
Revises: 
Create Date: 2024-12-20 11:56:09.208176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '716161b00163'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('board_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('owner', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('board_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('board')
    # ### end Alembic commands ###
