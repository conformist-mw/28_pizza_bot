from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

base_class = declarative_base()


class Catalog(base_class):
    __tablename__ = 'catalog'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    choices = relationship('Choice')

    def __str__(self):
        return '{} {}'.format(self.title, self.description)


class Choice(base_class):
    __tablename__ = 'choice'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('catalog.id'))
    catalog = relationship('Catalog')
    title = Column(String)
    price = Column(Integer)

    def __str__(self):
        return '{} - {} руб.'.format(self.title, self.price)
