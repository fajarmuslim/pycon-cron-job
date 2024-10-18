from sqlalchemy import Column, String, Float
from db.models.base import Base


class Text(Base):
    id = Column(String, primary_key=True, index=True)
    text = Column(String,nullable=False)
