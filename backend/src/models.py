import database
from sqlalchemy import String, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'

    id = Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25))
    password: Mapped[int] = mapped_column()
    language: Mapped[str] = mapped_column(String(25), default='English')

class Post(Base):
    __tablename__ = 'post'

    url: Mapped[str] = mapped_column(Text, primary_key=True)
    owner: Mapped[int] = mapped_column(ForeignKey('user.id'))
    likeNum: Mapped[int] = mapped_column(default=0)
    description: Mapped[str] = mapped_column(Text)
    postTime: Mapped[str] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now
    )