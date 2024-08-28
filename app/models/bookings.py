from .. import mongo

class book:
    def add_booking(booking):
        return mongo.db.bookings.insert_one(booking)
    
    def display_booking():
        return mongo.db.bookings.find()
    
    def booking():
        return mongo.db.bookings.find()
    
    
