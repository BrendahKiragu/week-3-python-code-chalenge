from models import mysession, Band, Concert, Venue

def create_band():
    """Adds a new band to bands table"""
    name= input("Enter band name > ")
    hometown = input("Enter home town > ")
  
    try:
        band = Band(name=name, hometown=hometown)
        mysession.add(band)
        mysession.commit()
        print(f"{band.name} from {band.hometown} created successfully.")
    except Exception as exc:
      print("Error creating band", exc)  
# create_band()  

def delete_band():
    """Deletes a band from bands table"""
    band = input("Enter band name to delete > ")
    try:
        band_to_del = mysession.query(Band).filter_by(name=band).first()
        if not band_to_del:
            print(f"{band} not found") 
            return      

        mysession.delete(band_to_del)  
        mysession.commit()
        print(f"{band} deleted successfully!")
    except Exception as exc:
        mysession.rollback()
        print(f"Error deleting {band}", exc)   
# delete_band()  

def create_concert():
    """Adds a new concert to concerts table"""
    date = input("Enter YYYY/mm/dd of the concert > ")
    band_id = input ("Enter band id > ")  
    venue_id = input("Enter venue id > ")     
    try:
        new_concert = Concert(date=date, band_id=band_id, venue_id=venue_id)
        if not new_concert:
            print("Invalid details. Try again")
            return
        
        mysession.add(new_concert)
        mysession.commit()
    except Exception as exc:
        print(f"Error creating concert, {exc}")        
create_concert() 

def delete_concert():
    """Deletes a concert from concerts table"""
    concert = input('Enter concert date to delete > ')
    try:
        concert_to_del =mysession.query(Concert).filter_by(date=concert).first()       
        if not concert_to_del:
            print(f"Band's {concert} concert not found")
            return
        
        mysession.delete(concert_to_del)
        mysession.commit()
        print(F"Band's {concert} concert deleted successfully")
    except Exception as exc:
        mysession.rollback()
        print("Error deleting concert", exc)    
# delete_concert()   

def create_venue():
    """Adds a new venue to venues table"""
    name= input("Enter venue title > ")
    city = input("Enter venue city > ")
  
    try:
        venue = Venue(title=name, city=city)
        mysession.add(venue)
        mysession.commit()
        print(f"'{venue.title}' set at {venue.city} city created successfully.")
    except Exception as exc:
      print("Error creating venue", exc)  
# create_venue()   

def delete_venue():
    """Deletes a venue from bands table"""
    venue = input("Enter venue title to delete > ")
    try:
        venue_to_del = mysession.query(Venue).filter_by(title=venue).first()
        if not venue_to_del:
            print(f"{venue} not found") 
            return      

        mysession.delete(venue_to_del)  
        mysession.commit()
        print(f"{venue} deleted successfully!")
    except Exception as exc:
        mysession.rollback()
        print(f"Error deleting {venue}", exc)   
# delete_venue() 
