#!/usr/bin/python3
"""Landlord class for the database"""

from models.base_m import Base_m, Base
from sqlalchemy import Column, String
import sqlalchemy


class Landlord(Base_m, Base):
    """Landlord class for the database"""
    __tablename__ = 'landlords'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    zip_code = Column(String(128), nullable=False)
    def __init__(self, *args, **kwargs):
        """Init method for the Landlord class"""
        super().__init__(*args, **kwargs)

