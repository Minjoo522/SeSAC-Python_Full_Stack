"""password_hash added

Revision ID: 5f4e0250a487
Revises: 1e3179ac779b
Create Date: 2023-08-01 10:51:15.416475

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from app import User
from werkzeug.security import generate_password_hash


# revision identifiers, used by Alembic.
revision = '5f4e0250a487'
down_revision = '1e3179ac779b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # 0. null이 가능하게 생성
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=120), nullable=True))

    # 데이터 마이그레이션을 수행
    # 1. DB에 접근
    # 2. 올드 컬럼(password) 컬럼에서 데이터를 가져온다
    # 3. 읽은 데이터를 내가 원하는 새로운 hash 포맷으로 변경한다

    # 1. DB 연결
    bind = op.get_bind()
    session = Session(bind=bind)

    # 2. 데이터 가져오기
    users = session.query(User).all()

    # 3. 데이터 변환 과정
    for user in users:
        # 패스워드 해시 처리 해야함
        user.password_hash = generate_password_hash(user.password)

    session.commit()
    session.close()

    with op.batch_alter_table('user', schema=None) as batch_op:
            batch_op.alter_column('password_hash', nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
