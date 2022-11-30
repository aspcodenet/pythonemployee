"""Added shoesize

Revision ID: 0f8a8793c415
Revises: 9c3ad5e08dd5
Create Date: 2022-11-30 10:32:40.399574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f8a8793c415'
down_revision = '9c3ad5e08dd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('shoesize', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.drop_column('shoesize')

    # ### end Alembic commands ###
