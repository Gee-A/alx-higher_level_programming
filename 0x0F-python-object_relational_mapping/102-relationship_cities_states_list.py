#!/usr/bin/python3
"""lists all City objects from the given database
"""

import sys
from relationship_state import (Base, State, City)

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city in session.query(City).order_by(City.id).all():
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

    session.close()
