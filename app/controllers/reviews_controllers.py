from flask import request, redirect, url_for, render_template
from ..models.reviews import Review
from bson.objectid import*


def review():
    if request.method == 'POST':
        # Get the review data from the request
        name = request.form.get('name')
        category= request.form.get('category')
        description = request.form.get('description')
        review_message = request.form.get('review_message')
        rating = int(request.form.get('rating'))

        # Prepare the review data as a dictionary
        review_data = {
            'name': name,
            'category': category,
            'description': description,
            'review_message': review_message,
            'rating': rating
        }

        # Save the review data to the MongoDB database
        Review.save_review(review_data)

        # Redirect to the review_display route after submission
        return redirect(url_for('rev.review_display'))

    # Render the review template on GET request
    return render_template('review.html')

def review_display():
    display = Review.get_reviews()
    return render_template('review.html', displays=display)