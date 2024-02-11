#!/usr/bin/python3
"""Init file for the models module"""
from models.engine.config import DBStorage
storage = DBStorage()
storage.reload()


