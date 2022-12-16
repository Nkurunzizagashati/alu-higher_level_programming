#!/usr/bin/python3
# a python file that contains the class definition
# of a State and an instance Base = declarative_base()
"""
    importing functions from 'sqlalchemy' module
"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)



class State(Base):
    """
        this class inherits from Base class
        it has class attribute id that represents a column of
        an auto-generated, unique integer, can’t be null and is a primary key
        and a class attribute name that represents a column of a string
        with maximum 128 characters and can’t be null
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
