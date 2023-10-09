from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    username = Column(String(32), unique=True, index=True, comment="用户名")
    password = Column(String(256), comment="哈希密码")
    email = Column(String(64), unique=True, comment="邮箱")
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime, onupdate=datetime.now, comment="更新时间")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    user_id = Column(Integer, index=True, comment='用户ID')
    content = Column(String(256), nullable=False, comment='内容')
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime, onupdate=datetime.now, comment="更新时间")
