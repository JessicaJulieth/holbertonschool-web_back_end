#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Saves the user
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **filters: Any) -> User:
        """
        Returns the first row
        """
        if not User.__dict__.get(*filters):
            raise InvalidRequestError
        query = self._session.query(User).filter_by(**filters)
        if not query.first():
            raise NoResultFound
        return query.first()

    def update_user(self, user_id: int, **kwargs)-> None:
        """Locate Users 
        """
         _id = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(_id, key):
                raise ValueError
            setattr(_id, key, value)
        self._session.commit()
