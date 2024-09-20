from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,  relationship
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()

#band model
class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    hometown = Column(String())

    #relationships
    concerts = relationship("Concert", back_populates="band")
    venue = association_proxy('reviews', 'venue', creator=lambda venue: Concert(venue=venue))

#venue model
class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    #relationships
    concerts = relationship("Concert", back_populates='venue')
    band = relationship('concerts', 'band', creator=lambda band: Concert(band=band))

#concert model
class Concert(Base):
    __tablename__ = 'concerts'    

    id = Column(Integer(), primary_key=True)
    date = Column(String())
    band_id = Column(Integer(), ForeignKey('bands.id'))#belongs to band
    venue_id = Column(Integer(), ForeignKey('venues.id'))#belongs to venue

    # relationship
    band =relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

engine = create_engine('sqlite:///band_concerts.db')    

Session = sessionmaker(bind=engine)
mysession = Session()