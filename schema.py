#!/usr/bin/python

from sqlalchemy import create_engine, Column, String, Integer, UniqueConstraint
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Car(Base):
    __tablename__= 'car'
    __table_args__ = (
        UniqueConstraint('name'),
    )
    
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    make = Column(String(256))
    model = Column(String(256))
    year = Column(Integer)

engine = create_engine('mysql://mysql_user:mysql_password@127.0.0.1:3306/inventory')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

s = session()
try:
    s.add(Car(name="clifford",make="Tesla",model="3",year=2018))
    s.add(Car(name="oldy",make="Nissan",model="xterra",year=2007))
    s.add(Car(name="Green Machine",make="Toyota",model="prius",year=2014))
    s.add(Car(name="shamu",make="BMW",model="i8",year=2015))
    s.add(Car(name="jett",make="BMW",model="x5",year=2013))
except:
    s.rollback()

it = s.query(Car).all()
for i in it:
    print i.name, i.make, i.model
#end for
