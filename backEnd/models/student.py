#!/usr/bin/python3
"""Student class for the database"""
from models.base_m import Base_m, Base
import sqlalchemy
from sqlalchemy import Column, String

class Student(Base_m, Base):
    """Student class for the database"""
    __tablename__ = 'students'
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
        """Init method for the Student class"""
        super().__init__(*args, **kwargs)


