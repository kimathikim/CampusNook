#!/usr/bin/python3
"""Cities Module"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_m import Base_m, Base
from models.state import State
class City(Base_m, Base):
    """This class defines the structure of the cities table"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey(State.id), nullable=False)
    properties = relationship('Properties', backref='city', cascade='all, delete-orphan')
    def __init__(self, *args, **kwargs):
        """Init method for the City class"""
        super().__init__(*args, **kwargs)
        self.name = kwargs['name']
        self.state_id = kwargs['state_id']
