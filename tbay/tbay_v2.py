from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from create import User, Item, Bid


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

bidder1 = User(username='bob', password='just4now')
bidder2 = User(username='rich', password='testtest')
bidder3 = User(username='justin', password='P@ssw0rd')
session.add_all([bidder1, bidder2, bidder3])
session.commit()

auction_item = Item(
    name='baseball',
    description='just a baseball',
    owner_id=bidder1.id
)
session.add_all([auction_item])
session.commit()

bid1 = Bid(price='12.70', bidder_id=bidder1.id, item_id=auction_item.id)
bid2 = Bid(price='17.00', bidder_id=bidder2.id, item_id=auction_item.id)
bid3 = Bid(price='23.00', bidder_id=bidder3.id, item_id=auction_item.id)
bid4 = Bid(price='25.90', bidder_id=bidder1.id, item_id=auction_item.id)
session.add_all([bid1, bid2, bid3, bid4])
session.commit()
