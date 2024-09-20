from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
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
    venues = association_proxy('concerts', 'venue', creator=lambda venue: Concert(venue=venue))

    def band_concerts(self):
        """returns a collection of all the concerts that the Band has played"""
        return self.concerts
    
    def band_venues(self):
        """returns a collection of all the venues that the Band has performed at"""
        return self.venues

#venue model
class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    #relationships
    concerts = relationship("Concert", back_populates='venue')
    bands = association_proxy('concerts', 'band', creator=lambda band: Concert(band=band))

    def venue_concerts(self):
        """returns a collection of all the concerts for the Venue"""
        return self.concerts
    
    def venue_bands(self):
        """returns a collection of all the bands who performed at the Venue"""
        return self.bands
#concert model
class Concert(Base):
    __tablename__ = 'concerts'    

    id = Column(Integer(), primary_key=True)
    date = Column(String())
    band_id = Column(Integer(), ForeignKey('bands.id'))#belongs to band
    venue_id = Column(Integer(), ForeignKey('venues.id'))#belongs to venue

    #relationships
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    #methods
    def band(self):
        """return the Band instance for this Concert"""
        return self.band
    
    def venue(self):
        """return the Venue instance for this Concert"""
        return self.venue
     

# Sets up the database engine and session
engine = create_engine('sqlite:///band_concerts.db')
Session = sessionmaker(bind=engine)
mysession = Session()

# Creates test instances of Band and Venue
# band1 = Band(name="band3", hometown="Canada")
# band2 = Band(name="band4", hometown="USA")
# venue1 = Venue(title="venue3", city="Toronto")
# venue2 = Venue(title="venue4", city="Miami")

# # Add to session and commit
# mysession.add_all([band1, band2, venue1, venue2])
# mysession.commit()
