#!/usr/bin/python3
"""Class definition of a State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String)

Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
