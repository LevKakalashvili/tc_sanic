"""inittal

Revision ID: 924411266506
Revises: 
Create Date: 2022-11-11 14:38:35.614091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '924411266506'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('good',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('good')
    # ### end Alembic commands ###