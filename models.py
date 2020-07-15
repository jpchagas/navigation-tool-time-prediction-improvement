from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Events(Base):
    __tablename__='events'

    id = Column(Integer,primary_key=True)
    begin = Column(DateTime,nullable=False)
    end = Column(DateTime)
    description = Column(String(200),nullable=False)
    attend = Column(Integer, nullable=False)
    establishments_id = Column(Integer,ForeignKey("establishments.id"),nullable=False)


    def __init__(self,begin=None, end=None, description=None,attend=None,establishments_id=None):
        self.begin=begin
        self.end=end
        self.description=description
        self.attend=attend
        self.establishments_id=establishments_id

    def __repr__(self):
        pass

class Establishments(Base):
    __tablename__='establishments'

    id = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False)
    address_id = Column(Integer,ForeignKey("adresses.id"),nullable=False)



    def __init__(self,name=None,address_id=None):
        self.name=name
        self.address_id=address_id

    def __repr__(self):
        pass

class Users(Base):
    __tablename__='users'

    id = Column(Integer,primary_key=True)
    fullname = Column(String(50),nullable=False)
    username = Column(String(50),nullable=False)
    email = Column(String(50),nullable=False)


    def __init__(self,fullname=None,username=None,email=None):
        self.fullname=fullname
        self.username=username
        self.email=email

    def __repr__(self):
        pass

class Adresses(Base):
    __tablename__='adresses'

    id = Column(Integer,primary_key=True)
    #cep = Column(Integer,nullable=False)
    cidade = Column(String(50),nullable=False)
    bairro = Column(String(50),nullable=False)
    estado = Column(String(50),nullable=False)
    logradouro = Column(String(50),nullable=False)
    numero = Column(String(50),nullable=False)

    def __init__(self,cidade=None,bairro=None,estado=None,logradouro=None,numero=None):
        #self.cep=cep
        self.cidade=cidade
        self.bairro=bairro
        self.estado=estado
        self.logradouro=logradouro
        self.numero=numero

    def __repr__(self):
        pass

class EventsList(Base):
    __tablename__='evenslist'
    
    user_id = Column(Integer,ForeignKey("users.id"),primary_key=True)
    event_id = Column(Integer,ForeignKey("events.id"),primary_key=True)

    def __init__(self):
        pass

    def __repr__(self):
        pass

#class Directions(Base):
#    __tablename__ = 'directions'

#    def __init__(self):
#        pass

#    def __repr__(self):
#        pass
    

