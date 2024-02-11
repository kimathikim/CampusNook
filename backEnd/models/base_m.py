#!/usr/bin/python3
"""Base model for all other classes"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from os import getenv
import uuid
import models
time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

class Base_m:
    """Base class for all other classes"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    def __init__(self, *args, **kwargs):
        """Init method for the base class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
            for key, value in kwargs.items():
                setattr(self, key, value)
    def __str__(self):
        """String representation of the base class"""
        return "{}.{}".format(self.__class__.__name__, self.id)
    def save(self):
        """Update the updated_at attribute and save to the database"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
    def to_dict(self):
        """Return a dictionary representation of the base class"""
        new_dict = self.__dict__.copy()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        new_dict['created_at'] = new_dict['created_at'].strftime(time)
        new_dict['updated_at'] = new_dict['updated_at'].strftime(time)
        return new_dict
    def delete(self):
        """Delete the current instance from the database"""
        models.storage.delete(self)
        models.storage.save()



