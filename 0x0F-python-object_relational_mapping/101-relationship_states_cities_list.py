#!/usr/bin/python3
"""lists all state objects, and corresponding city objects, contained in the
   given database.
"""

import sys
from relationship_state import (Base, City, State)

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State)\
                    .outerjoin(City)\
                    .order_by(State.id, City.id)\
                    .all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('    {}: {}'.format(city.id, city.name))

    session.close()
