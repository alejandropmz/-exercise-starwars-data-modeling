import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fav_planets = relationship('Fav_planets', backref='user', lazy=True)
    fav_characters = relationship('Fav_characters', backref='user', lazy=True)
    fav_films = relationship('Fav_films', backref='user', lazy=True)
    fav_vehicles = relationship('Fav_vehicles', backref='user', lazy=True)
    fav_species = relationship('Fav_species', backref='user', lazy=True)
    fav_starships = relationship('Fav_starships', backref='user', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(300))
    fav_planets = relationship('Fav_planets', backref='user', lazy=True)

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    producer = Column(String(250), nullable=False)
    title = Column(String(300))
    episodie_id = Column(Integer)
    director = Column(String(300))
    release_date = Column(Integer)
    fav_films = relationship('Fav_films', backref='user', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(300))
    manufacturer = Column(String(300))
    cargo_capacity = Column(Integer)
    release_date = Column(String(300))
    fav_vehicles = relationship('Fav_vehicles', backref='user', lazy=True)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    height = Column(String(250), nullable=False)
    hair_color = Column(String(300))
    skin_color = Column(Integer)
    eye_color = Column(String(300))
    gender = Column(String(300))
    fav_people = relationship('Fav_people', backref='user', lazy=True)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    starship_class = Column(String(300))
    manufacturer = Column(String(300))
    lenght = Column(String(300))
    cargo_capacity = Column(Integer)
    fav_starships = relationship('Fav_starships', backref='user', lazy=True)

class Species(Base):
    __tablename__ = 'Species'
    id = Column(Integer, primary_key=True)
    clasification = Column(String(250), nullable=False)
    hair_color = Column(String(300))
    skin_color = Column(Integer)
    skin_color = Column(String(300))
    language = Column(String(300))
    Sav_species = relationship('Sav_species', backref='user', lazy=True)

class Fav_planets(Base):
    __tablename__ = 'fav_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    planets_id = Column(Integer,ForeignKey('planets.id'))

class Fav_Films(Base):
    __tablename__ = 'fav_films'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    films_id = Column(Integer,ForeignKey('films.id'))

class Fav_Vehicles(Base):
    __tablename__ = 'fav_vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    vehicles_id = Column(Integer,ForeignKey('vehicles.id'))

class Fav_People(Base):
    __tablename__ = 'fav_people'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    people_id = Column(Integer,ForeignKey('people.id'))

class Fav_Starships(Base):
    __tablename__ = 'fav_starships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    starships_id = Column(Integer,ForeignKey('starships.id'))

class Fav_Species(Base):
    __tablename__ = 'fav_species'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    species_id = Column(Integer,ForeignKey('species.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
