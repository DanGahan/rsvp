from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import url_quote
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Configure the PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/rsvp_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the model
class rsvps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    plus_one = db.Column(db.String(10), nullable=False)
    plus_one_name = db.Column(db.String(100))
    song_suggestion = db.Column(db.String(200))

@app.route('/rsvp', methods=['POST'])
def create_rsvp():
    data = request.json

     # Log received data
    logging.debug("Received data: %s", data)

    # Validate input
    if not all(key in data for key in ['name', 'plus_one', 'song_suggestion']):
        return jsonify({'error': 'Missing required fields'}), 400

    name = data['name']
    plus_one = data['plus_one']
    plus_one_name = data.get('plus_one_name', '')
    song_suggestion = data['song_suggestion']

    # Create a new RSVP entry
    rsvp = rsvps(name=name, plus_one=plus_one, plus_one_name=plus_one_name, song_suggestion=song_suggestion)
    db.session.add(rsvp)
    db.session.commit()

    return jsonify({'message': 'RSVP created successfully'}), 201

if __name__ == '__main__':
    
    db.create_all()  # Create the database tables
    app.run(debug=True, host='0.0.0.0')