from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_m import Base_m, Base

class State(Base_m, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs['name']
