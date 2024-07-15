from ..import mongo

class book:
    def add_booking(booking):
        return mongo.db.bookings.insert_one(booking)
    
    def display_booking():
        return mongo.db.bookings.find()
    
    def get_confirmation():
        return mongo.db.bookings.find()