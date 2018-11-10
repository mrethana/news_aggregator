# from __init__ import db
# from newspackage import db
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship

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
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates = 'content')
    # sub_categories = relationship('Category',secondary='content_categories')


class Provider(Base):
    __tablename__ = 'providers'
    id = Column(Integer, primary_key = True)
    expertise = Column(String(100))
    api_id = Column(String(100))
    content = relationship('Content', back_populates = 'provider')
    expertise_id = Column(Integer, ForeignKey('expertise.id'))
    expertise = relationship('Expertise', back_populates = 'provider')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    content = relationship('Content', back_populates = 'category')
    # actors = relationship('Actor',secondary='actor_roles') to be sub categories

# class ContentCategories(Base):
#      __tablename__ = 'content_categories'
#     content_id = Column(Integer, ForeignKey('content.id'), primary_key = True)
#     category_id = Column(Integer, ForeignKey('categories.id'), primary_key = True)

class Expertise(Base):
    __tablename__ = 'expertise'
    id = Column(Integer, primary_key = True)
    type = Column(String(100))
    provider = relationship('Provider', back_populates = 'expertise')

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
