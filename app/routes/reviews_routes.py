from flask import Blueprint
from ..controllers import reviews_controllers


review_bp = Blueprint('reviews',__name__)

review_bp.route('/review', methods=['GET', 'POST'])(reviews_controllers.review)
review_bp.route('/review_display', methods=['GET'])(reviews_controllers.review_display)