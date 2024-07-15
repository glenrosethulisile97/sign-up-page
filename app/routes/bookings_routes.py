from flask import Blueprint
from ..controllers import bookings_controllers

booking_bp = Blueprint('booking', __name__)

booking_bp.route("/AddBooking", methods=["GET", "POST"])(bookings_controllers.add_booking)
booking_bp.route("/getBooking", methods=["POST", "GET"])(bookings_controllers.getBooking)
booking_bp.route("/confirmation", methods=["POST", "GET"])(bookings_controllers.Confirmation)

