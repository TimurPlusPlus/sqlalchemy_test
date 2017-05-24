from sqlalchemy import create_engine
from sqlalchemy import Sequence

engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = 'users'

    id       = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name     = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)


ed_user = User(name='Ed', fullname='Ed Kek', password='228228')
print(ed_user.name)
print(ed_user.id)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)

our_user = session.query(User).filter_by(name='Ed').first()
print(our_user)

session.add_all([
     User(name='wendy', fullname='Wendy Williams', password='foobar'),
     User(name='mary', fullname='Mary Contrary', password='xxg527'),
     User(name='fred', fullname='Fred Flinstone', password='blah')])

ed_user.password = '2282291!!!'
print(our_user)

print(session.dirty)
print(session.new)
session.commit()

print(ed_user.id)
users = session.query(User).all()
print(users)
