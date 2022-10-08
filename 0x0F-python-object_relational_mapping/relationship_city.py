#!/usr/bin/python3
"""Definition of City class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String, ForeignKey)

Base = declarative_base()


class City(Base):
    """Class City"""

    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
