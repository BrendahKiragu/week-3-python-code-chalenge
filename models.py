from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,  relationship

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    hometown = Column(String())

#venue model
class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

class Concert(Base):
    __tablename__ = 'concerts'    

    id = Column(Integer(), primary_key=True)
    date = Column(String())
    band_id = Column(Integer(), ForeignKey('bands.id'))#belongs to band
    venue_id = Column(Integer(), ForeignKey('venues.id'))#belongs to venue


engine = create_engine('sqlite:///band_concerts.db')    

Session = sessionmaker(bind=engine)
mysession = Session()