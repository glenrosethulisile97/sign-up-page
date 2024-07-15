from flask import request, redirect, url_for, render_template
from ..models.bookings import book

def add_booking():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        color = request.form.get("color")
        offices = request.form.get("offices")
        size = request.form.get("size")

        booking = {"name": name, "email": email, "color": color, "offices": offices, "size": size}
        book.add_booking(booking)
        return redirect(url_for("booking.confirmation"))
    
    return render_template("AddOffice.html")


def Confirmation():
     if request.method == 'GET':
          booking = []

          for i in book.get_confirmation():
            booking.append(i)


     return render_template("confirmation.html" , booking=booking ) 


def getBooking():
    booking = []
    if request.method == 'GET':
        for i in book.display_booking ():
            booking.append(i)

    return render_template("booking.html", booking=booking)

