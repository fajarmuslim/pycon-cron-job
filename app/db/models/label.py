from sqlalchemy import Column, String, Float
from db.models.base import Base


class Label(Base):
    id = Column(String, primary_key=True, index=True)
    sentiment = Column(String,nullable=True)
    emotion = Column(String,nullable=True)
