#!/usr/bin/python3
"""Definition of the State class with relationship to City"""

from relationship_city import Base, City

from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import relationship


class State(Base):
    """Class State"""

    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states',
                          cascade='all, delete-orphan')
