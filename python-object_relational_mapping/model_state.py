#!/usr/bin/python3
# a python file that contains the class definition
# of a State and an instance Base = declarative_base()
"""
    we will use sqlalchemy module in our codes
"""


from sqlalchemy import Column, String, MetaData, Integer
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
        this is State class it inherits from Base class
        and it can't be null
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
