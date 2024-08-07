"""initial migration

Revision ID: 9a693728aa76
Revises:
Create Date: 2024-08-07 22:29:30.890006

"""
from alembic import op
import sqlalchemy as sa
import pgvector


# revision identifiers, used by Alembic.
revision = '9a693728aa76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'faqs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('subtitle', sa.String(), nullable=True),
        sa.Column('body', sa.Text(), nullable=False),
        sa.Column('language', sa.String(), nullable=True),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('keywords', sa.String(), nullable=True),
        sa.Column('embedding', pgvector.sqlalchemy.vector.VECTOR(),
                  nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_faqs_id'), 'faqs', ['id'], unique=False)
    op.create_index(op.f('ix_faqs_title'), 'faqs', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_faqs_title'), table_name='faqs')
    op.drop_index(op.f('ix_faqs_id'), table_name='faqs')
    op.drop_table('faqs')
    # ### end Alembic commands ###
