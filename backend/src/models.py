from datetime import datetime
from sqlalchemy import String, DateTime, Text, ForeignKey, func, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

"""
Database tables are defined here.
"""

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25))
    password: Mapped[str] = mapped_column(String(255))
    language: Mapped[str] = mapped_column(String(25), default='en')

class Post(Base):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[int] = mapped_column(ForeignKey('user.id'))
    like_num: Mapped[int] = mapped_column(default=0)
    description: Mapped[str] = mapped_column(Text)
    post_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )

class PostImages(Base):
    __tablename__ = 'post_images'

    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    image_url: Mapped[str] = mapped_column(Text)

class PostTranslation(Base):
    __tablename__ = 'post_translation'
    __table_args__ = (UniqueConstraint('post_id', 'language'),)

    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))
    language: Mapped[str] = mapped_column(String(10))
    description: Mapped[str] = mapped_column(Text)