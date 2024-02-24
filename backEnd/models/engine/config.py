#!/usr/bin/python3
"""Config file for the database. Will contain DBstorage class"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.landlord import Landlord
from models.property import Properties
from models.student import Student
from models.state import State
from models.cities import City
from models.base_m import Base
from models.prop_images import Prop_images
classes = {"Student": Student, "Landlord": Landlord, "Properties": Properties, "Prop_images": Prop_images
           , "State": State, "City": City}


class DBStorage:
    """Database storage class"""
    __engine = None
    __session = None
    def __init__(self):
        """Institate the DBStorage object"""
        CN_MYSQL_USER = getenv('CN_MYSQL_USER')
        CN_MYSQL_PWD = getenv('CN_MYSQL_PWD')
        CN_MYSQL_HOST = getenv('CN_MYSQL_HOST')
        CN_MYSQL_DB = getenv('CN_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                  .format(CN_MYSQL_USER, CN_MYSQL_PWD,
                                          CN_MYSQL_HOST, CN_MYSQL_DB),
                                  pool_pre_ping=True)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Retrieves an object w/class name and id
        """
        result = None
        try:
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                if obj.id == id:
                    result = obj
        except BaseException:
            pass
        return result

    def count(self, cls=None):
        """
        Counts number of objects in DBstorage
        """
        cls_counter = 0

        if cls is not None:
            objs = self.__session.query(classes[cls]).all()
            cls_counter = len(objs)
        else:
            for cls in classes:
                objs = self.__session.query(classes[cls]).all()
                cls_counter += len(objs)
        return cls_counter

    # delete all objects in the database
    def delete(self, obj=None):
        """
        Deletes an object from the database
        """
        if obj is not None:
            self.__session.delete(obj)

