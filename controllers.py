import requests
from models import Base, Adresses, Establishments,Events,EventsList,Users#,Directions
import sqlalchemy as sa
import random
import pandas as pd
import numpy as np
import datetime as dt



engine = sa.create_engine('mysql+mysqlconnector://dba:pegasos93@localhost:3306/nttpi')

Session = sa.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def extractUser():
    return requests.get('https://randomuser.me/api').json()['results'][0]
    

def extractAdresses():
    url = 'http://cep.la/RS/Porto-Alegre/'
    headers = {'Accept':'application/json'}
    getneighborhoodlist = requests.get(url+str(random.randint(1,5)),headers=headers).json()
    getaddresses = requests.get(url+getneighborhoodlist[random.randint(1,20)]['nome'],headers=headers).json()
    return getaddresses[random.randint(1,20)]


def extractDirections():
    return requests.get('http://open.mapquestapi.com/directions/v2/route?key=kkGeHlAl57IKFaffe28R2WBviZESqrNG&from=Clarendon Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA').json()



def setup():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    lo = pd.read_csv('locals.csv')
    for index,row in lo.iterrows():
        print()
        a = Adresses('Porto Alegre',row['Neighborhood'],'RS',row['Address'],row['Number'])
        session.add(a)
        session.commit()
        e = Establishments(row['Name'],a.id)
        session.add(e)
        session.commit()

def generateevent():    
    us = extractUser()
    print(us)
    u = Users(fullname=None,username=None,email=None)
    index = random.randint(1,51)
    s = session.query(Establishments).filter(Establishments.id == str(index))
    ev = Events(dt.datetime.now(), dt.datetime.now(), 'Evennt ' + str(random.randint(1,100000)),random.randint(1,1000),s[0].id)




generateevent()