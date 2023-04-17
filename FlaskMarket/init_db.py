from market import app, db
from market.model import User, Item 

if __name__=="__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()

    user1 = User(username="Long", email_address="long.dh2000@gmail.com", password_harsh="123456")
    item1 = Item(name="Iphone", description="desc1", barcode="121212121212", price=500)
    item2 = Item(name="Laptop", description="desc2", barcode="131313131313", price=500)
    
    with app.app_context():
        db.session.add(user1)
        db.session.add(item1)
        db.session.add(item2)
        db.session.commit()

        test = Item.query.filter_by(name="Iphone").first()
        test.owner = User.query.filter_by(username="Long").first().id
        db.session.add(test)
        db.session.commit()

        test2 = Item.query.filter_by(name="Iphone").first()
        print(test2.owned_user)

     