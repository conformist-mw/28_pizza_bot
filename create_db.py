from models import Base, Catalog, Choice, catalog
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import getenv
engine = create_engine(getenv('db_uri'))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
for item in catalog:
    new_item = Catalog()
    new_item.title = item['title']
    new_item.description = item['description']
    for choice in item['choices']:
        choices = Choice()
        choices.title = choice['title']
        choices.price = choice['price']
        new_item.choices.append(choices)
    session.add(new_item)
session.commit()
