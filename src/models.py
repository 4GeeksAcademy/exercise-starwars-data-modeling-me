import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=True)
    lastname = Column(String(250), nullable=True)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    description = Column(String(250), nullable=True)
    climate = Column(String(250), nullable=True)
    population = Column(String(250), nullable=True)
    orbital_period = Column(String(250), nullable=True)
    rotation_period = Column(String(250), nullable=True)
    diameter = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table Characters.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    gender = Column(String(250), nullable=True)
    hair_color = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    birth_year = Column(String(250), nullable=True)
    rotation_period = Column(String(250), nullable=True)
    height = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)   

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table Favorites.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False, unique=True)
    planets_id = Column(Integer, ForeignKey("planets.id"), nullable=False, unique=True)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
