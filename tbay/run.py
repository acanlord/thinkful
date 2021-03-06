from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from create import Item, Bid

def get_max_bid(item_id):
	bids = session.query(Bid).filter(Bid.item_id == item_id).all()
	highest_bid = bids[0].price
	for i in bids[1:]: 
		if i.price > highest_bid:	
			highest_bid = i.price
	return highest_bid 

print(get_max_bid(1))
#return highes
