# Band Concerts 

This project is a Python-based application that uses SQLAlchemy ORM to model a database of bands, venues, and concerts. It allows for tracking concerts, bands' performances at different venues, and several aggregate and relationship methods to extract meaningful information.

# Table of Contents
1. [Features](#features)
2. [Key Methods](#key-methods)
3. [Installation](#installation)
4. [Usage](#usage)

## Features

- **Band Model**: Represents bands, tracks their hometown, and the venues they have performed at.
- **Venue Model**: Represents concert venues, tracks concerts held at the venue and the bands that performed there.
- **Concert Model**: Represents a specific concert with a date, band, and venue.
  
### Key Methods:

#### Concert:
- **`hometown_show()`**: Returns `True` if the concert is in the band's hometown, otherwise `False`.
- **`introduction()`**: Returns an introduction string for the concert in the form: `"Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"`.

#### Band:
- **`play_in_venue(venue, date)`**: Creates a new concert for the band in the given venue on the given date.
- **`all_introductions()`**: Returns a list of introduction strings for all the concerts the band has performed.
- **`most_performances()`**: (Class Method) Returns the band that has played the most concerts.

#### Venue:
- **`concert_on(date)`**: Returns the first concert on the given date at the venue.
- **`most_frequent_band()`**: Returns the band with the most concerts at the venue.

## Installation
### Prerequisites
Make sure you have the following installed:
  - Python 3.x
  - SQLite3 

## Installation Instructions
1. Clone the Repository
  ```bash
      git clone [https://github.com/your-repo/band-concerts-database.git](https://github.com/BrendahKiragu/week-3-python-code-chalenge)
      cd band-concerts-database  

2. Create a virtual environment and install this project's dependencies. Then navigate to a subshell:
    ```bash
       pipenv install
       pipenv shell
    
3. Create and set up the SQLite database:
    - The database file `band_concerts.db` will automatically be created when you run pipenv install.

4. Install SQLAlchemy:
    ```bash
       pip install sqlalchemy

## Usage
1. Interacting with the database
   - You can query bands, venues, and concerts using the defined models and methods, for example, to query the most frequent band at a venue, add this in the models.py file:
   ```bash
       venue = mysession.query(Venue).first()
       print(venue.most_frequent_band().name)
   - Then run the Script on the terminal:
        `python models.py`
 
    - You can also add to the database using the predefined methods in the `seed.py file`. 
        - To do so, uncomment the function calls in the `seed.py` then on the terminal run 'python seed.py`
