#!/usr/bin/python3
'''Prop_images module.'''

from sqlalchemy import Column, String, ForeignKey, LargeBinary
from models.base_m import Base_m, Base


class Prop_images(Base_m, Base):
    """This class defines the structure of the prop_images table"""
    __tablename__ = 'prop_images'
    property_id = Column(String(128), ForeignKey('props.id'), nullable=False)
    image = Column(LargeBinary, nullable=False)
    
    def __init__(self, *args, **kwargs):
        """Init method for the Prop_images class"""
        super().__init__(*args, **kwargs)
        self.property_id = kwargs['property_id']
        self.image = kwargs['image']
