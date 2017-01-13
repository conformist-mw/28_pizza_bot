from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()


class Catalog(Base):
    __tablename__ = 'catalog'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    choices = relationship('Choice')


class Choice(Base):
    __tablename__ = 'choice'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('catalog.id'))
    title = Column(String)
    price = Column(Integer)


engine = create_engine('sqlite:///pizza.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

catalog = [
    {
        'title': 'Маргарита',
        'description': 'соус,сыр Моцарелла',
        'choices': [
            {
                'title': '30 см (450гр)',
                'price': 360,
            },
            {
                'title': '40 см (750гр)',
                'price': 460,
            }
        ],
    },
    {
        'title': 'Маргарита <Помидоро>',
        'description': 'соус,сыр Моцарелла,помидоры',
        'choices': [
            {
                'title': '30см (500гр)',
                'price': 400,
            },
            {
                'title': '40cм (850гр)',
                'price': 490,
            }
        ],
    },
    {
        'title': 'Грибная',
        'description': 'соус,сыр Моцарелла,шампиньоны',
        'choices': [
            {
                'title': '30см (500гр)',
                'price': 430,
            },
            {
                'title': '40см (870гр)',
                'price': 540,
            }
        ],
    },
    {
        'title': 'С ветчиной',
        'description': 'соус,сыр Моцарелла,ветчина',
        'choices': [
            {
                'title': '30см (500гр)',
                'price': 430,
            },
            {
                'title': '40см (870гр)',
                'price': 540,
            }
        ],
    },
    {
        'title': 'Ветчина с грибами',
        'description': 'соус,сыр Моцарелла,шампиньоны,ветчина',
        'choices': [
            {
                'title': '30см (580гр)',
                'price': 460,
            },
            {
                'title': '40см (930гр)',
                'price': 570,
            }
        ],
    },
    {
        'title': 'Салями',
        'description': 'соус,сыр Моцарелла,салями',
        'choices': [
            {
                'title': '30см (500гр)',
                'price': 450,
            },
            {
                'title': '40см (870гр)',
                'price': 560,
            }
        ],
    },
    {
        'title': 'Гавайская',
        'description': 'соус,сыр Моцарелла,ветчина,ананасы',
        'choices': [
            {
                'title': '30см (580гр)',
                'price': 470,
            },
            {
                'title': '40см (870гр)',
                'price': 580,
            }
        ],
    },
    {
        'title': 'Четыре сыра',
        'description': 'соус,сыр Моцарелла,сыр Гауда,сыр Эдам,сыр Дор-Блю',
        'choices': [
            {
                'title': '30см (600гр)',
                'price': 470,
            },
            {
                'title': '40см (870гр)',
                'price': 580,
            }
        ],
    },
    {
        'title': 'Пеперонни',
        'description': 'соус,сыр Моцарелла,пепперони,перец сладкий',
        'choices': [
            {
                'title': '30см (550гр)',
                'price': 470,
            },
            {
                'title': '40см (920гр)',
                'price': 600,
            }
        ],
    },
    {
        'title': 'С курицей',
        'description': 'соус,сыр Моцарелла,куриные грудки,помидоры,шампиньоны перец',
        'choices': [
            {
                'title': '30см (550гр)',
                'price': 500,
            },
            {
                'title': '40см (920гр)',
                'price': 610,
            }
        ],
    },
    {
        'title': 'Овощная',
        'description': 'соус,сырМоцарелла,перец,лук,шампиньоны,кукуруза,маслины',
        'choices': [
            {
                'title': '30см (600гр)',
                'price': 470,
            },
            {
                'title': '40см (920гр)',
                'price': 580,
            }
        ],
    },
    {
        'title': 'Четыре сезона',
        'description': 'соус,сыр Моцарелла,1/4 салями,1/4 мясная,1/4 ветчина грибы,1/4 четыре',
        'choices': [
            {
                'title': '30см (600гр)',
                'price': 500,
            },
            {
                'title': '40см (930гр)',
                'price': 620,
            }
        ],
    },
    {
        'title': 'Кальцоне',
        'description': 'соус, сыр Моцарелла, ветчина, грибы, чесночное масло, кунжут',
        'choices': [
            {
                'title': '30см (520гр)',
                'price': 440,
            },
            {
                'title': '40см (870гр)',
                'price': 530,
            }
        ],
    },
    {
        'title': 'С тунцом',
        'description': 'соус, сыр Моцарелла, тунец консервированный, помидоры, лук репчатый, маслины',
        'choices': [
            {
                'title': '30см (570гр)',
                'price': 470,
            },
            {
                'title': '40см (950гр)',
                'price': 570,
            }
        ],
    },
    {
        'title': 'С беконом',
        'description': 'соус,сыр,Моцарелла,бекон,помидоры,маслины',
        'choices': [
            {
                'title': '30см (570гр)',
                'price': 470,
            },
            {
                'title': '40см (950гр)',
                'price': 590,
            }
        ],
    },
]


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
