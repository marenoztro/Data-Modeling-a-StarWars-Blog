import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favoritos = relationship('Favoritos', backref='usuario', lazy=True)


class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    year_Birth = Column(String(250))
    description = Column(String(250))
    favoritos = relationship('Favoritos', backref='personajes', lazy=True)



class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    description = Column(String(250))
    favoritos = relationship('Favoritos', backref='planetas', lazy=True)



class Favoritos (Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personajes_id = Column(Integer, ForeignKey('personajes.id'), nullable=False)
    planetas_id = Column(Integer, ForeignKey('planetas.id'), nullable=False)





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')