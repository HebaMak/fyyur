"""empty message

Revision ID: 4369374542c7
Revises: 781e5fdd019b
Create Date: 2024-02-14 15:33:40.169493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4369374542c7'
down_revision = '781e5fdd019b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test1', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('test2', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('test3', sa.String(length=120), nullable=True))
        batch_op.drop_column('test')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('test3')
        batch_op.drop_column('test2')
        batch_op.drop_column('test1')

    # ### end Alembic commands ###