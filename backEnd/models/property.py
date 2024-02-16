#!/usr/bin/python3
"""Properties module."""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_m import Base_m, Base
from models.landlord import Landlord
from models.cities import City

class Properties(Base_m, Base):
    """This class defines the structure of the properties table"""
    __tablename__ = 'props'
    landlord_id = Column(String(128), ForeignKey(Landlord.id), nullable=False)
    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    city_id = Column(String(128), ForeignKey(City.id), nullable=False)
    zip_code = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    price = Column(String(128), nullable=False)
    prop_images = relationship('Prop_images', backref='property', cascade='all, delete')
    
    def __init__(self, *args, **kwargs):
        """Init method for the Landlord class"""
        super().__init__(*args, **kwargs)

