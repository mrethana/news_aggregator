# from __init__ import db
# from newspackage import db
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

class Content(Base):
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    content_url = Column(String(600))
    image_url = Column(String(600))
    title = Column(String(600))
    published = Column(String(600))
    length = Column(Integer)
    medium_id = Column(Integer, ForeignKey('mediums.id'))
    medium = relationship('Medium', back_populates = 'content')
    provider_id = Column(Integer, ForeignKey('providers.id'))
    provider = relationship('Provider', back_populates = 'content')
    categories = relationship('Category',secondary='content_categories',back_populates = 'content_pieces')
    difficulty_id = Column(Integer, ForeignKey('difficulties.id'))
    difficulty = relationship('Difficulty', back_populates = 'content')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    content_pieces = relationship('Content',secondary='content_categories', back_populates = 'categories')

class ContentCategory(Base):
    __tablename__ = 'content_categories'
    id = Column(Integer, primary_key = True)
    value = Column(Integer)
    content_id = Column(Integer, ForeignKey('content.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    content = relationship(Content, backref=backref('content_categories', cascade='all, delete-orphan'))
    category = relationship(Category, backref=backref('content_categories', cascade='all, delete-orphan'))


class Provider(Base):
    __tablename__ = 'providers'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    api_id = Column(String(100))
    content = relationship('Content', back_populates = 'provider')
    formality_id = Column(Integer, ForeignKey('formality.id'))
    formality = relationship('Formality', back_populates = 'provider')


class Difficulty(Base):
    __tablename__ = 'difficulties'
    id = Column(Integer, primary_key = True)
    type = Column(String(100))
    content = relationship('Content', back_populates = 'difficulty')


class Formality(Base):
    __tablename__ = 'formality'
    id = Column(Integer, primary_key = True)
    type = Column(String(100))
    provider = relationship('Provider', back_populates = 'formality')

class Medium(Base):
    __tablename__ = 'mediums'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    content = relationship('Content', back_populates = 'medium')

# for dash

# class Content(db.Model):
#     __tablename__ = 'content'
#     id = db.Column(db.Integer, primary_key=True)
#     content_url = db.Column(db.String(600))
#     image_url = db.Column(db.String(600))
#     # description = db.Column(db.String(600))
#     title = db.Column(db.String(600))
#     published = db.Column(db.String(600))
#     medium_id = db.Column(db.Integer, db.ForeignKey('mediums.id'))
#     medium = db.relationship('Medium', back_populates = 'content')
#     provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'))
#     provider = db.relationship('Provider', back_populates = 'content')
#     search_param = db.Column(db.VARCHAR(100))
#
# class Provider(db.Model):
#     __tablename__ = 'providers'
#     id = db.Column(db.Integer, primary_key = True)
#     provider_name = db.Column(db.String(100))
#     newsapi_id = db.Column(db.String(100))
#     content = db.relationship('Content', back_populates = 'provider')
#
# # class Categories(db.Model)
#
# class Medium(db.Model):
#     __tablename__ = 'mediums'
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(100))
#     content = db.relationship('Content', back_populates = 'medium')
#
# db.create_all()
