from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from create import User, Item, Bid


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

bidder1 = User(username='bob', password='just4now')
bidder2 = User(username='rich', password='P@ssw0rd')
bidder3 = User(username='josh', password='testtest')
session.add_all([bidder1, bidder2, bidder3])
session.commit()

auction_item = Item(
    name='baseball',
    description='just a baseball',
    owner_id=bidder1.id
)
session.add_all([auction_item])
session.commit()

bid1 = Bid(price='12.00', bidder_id=bidder1.id, item_id=auction_item.id)
bid2 = Bid(price='15.00', bidder_id=bidder2.id, item_id=auction_item.id)
bid3 = Bid(price='20.00', bidder_id=bidder3.id, item_id=auction_item.id)
bid4 = Bid(price='25.00', bidder_id=bidder1.id, item_id=auction_item.id)
session.add_all([bid1, bid2, bid3, bid4])
session.commit()
