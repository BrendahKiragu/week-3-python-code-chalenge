from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()

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
    
    def concert_on(self, date):
        """queries and returns the first concert on a given date at a venue"""
        first_concert = mysession.query(Concert).filter_by(venue_id=self.id, date=date).first()
        return first_concert
    
    def most_frequent_band(self):
        """returns the band with most concerts at a venue on a given date"""
        return mysession.query(Band).join(Concert).filter(Concert.venue_id == self.id).group_by(Band.id).order_by(func.count(Concert.id).desc()).first()
 

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

    def play_in_venue(self, date, venue):
        """creates a new concert for the band in a given venue and date"""
        new_concert = Concert(date=date, band=self, venue=venue)
        mysession.add(new_concert)
        mysession.commit()
        return new_concert
    
    def all_introductions(self):
        """returns an list of a band's introductions"""
        all_introductions = []
        for concert in self.concerts: 
            all_introductions.append(concert.introduction())
        return all_introductions
    
    @classmethod
    def most_performances(cls):
        """returns the band that has played the most concerts"""
        return mysession.query(Band).join(Concert).group_by(Band.id).order_by(func.count(Concert.id).desc()).first()
  
    
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
    def get_band(self):
        """return the Band instance for this Concert"""
        return self.band
    
    def get_venue(self):
        """return the Venue instance for this Concert"""
        return self.venue
     
    def hometown_show(self):
        """returns true if the concert is in the band's hometown, false if it is not"""
        if self.band.hometown == self.venue.city:
            return True
        else:
            return False
        
    def introduction(self):
        """returns a string with the band's introduction for this concert"""    
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown} "

# Sets up the database engine and session
engine = create_engine('sqlite:///band_concerts.db')
Session = sessionmaker(bind=engine)
mysession = Session()


#uncomment below for example usage for VENUE model
# v1 = mysession.query(Venue).first()    
# print(f"{v1.title} has held {v1.venue_concerts()} concerts for these bands{v1.venue_bands()}")
# frequent_band = v1.most_frequent_band()
# print(frequent_band.name)


#uncomment below to run example usage for Band model   
# band1 = mysession.query(Band).first()    
# print(f"{band1.name} has had these concerts {band1.band_concerts()} at these venues{band1.band_venues()}") 

#Uncomment below for example usage for CONCERT model
# first_concert = mysession.query(Concert).first()
# print(f"The concert on {first_concert.date} was at {first_concert.venue.city}, {first_concert.band.hometown}")
