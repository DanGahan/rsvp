from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from urllib.parse import quote as url_quote
import logging
import os

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Configure the PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the model
class rsvps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    attending = db.Column(db.String(10), nullable=False)
    vegetarian = db.Column(db.String(10), nullable=True)
    wine = db.Column(db.String(10), nullable=True)
    plus_one = db.Column(db.String(10), nullable=True)
    plus_one_name = db.Column(db.String(100), nullable=True)
    plus_one_vegetarian = db.Column(db.String(10), nullable=True)
    plus_one_wine = db.Column(db.String(10), nullable=True)
    song_suggestion = db.Column(db.String(200), nullable=True)
    

@app.route('/rsvp', methods=['POST'])
def create_rsvp():
    data = request.json

     # Log received data
    logging.debug("Received data: %s", data)

    # Validate input
    if not all(key in data for key in ['name', 'plus_one', 'song_suggestion']):
        return jsonify({'error': 'Missing required fields'}), 400

    name = data['name']
    attending = data['attending']
    vegetarian = data['vegetarian']
    wine = data['wine']
    plus_one = data['plus_one']
    plus_one_name = data.get('plus_one_name', '')
    plus_one_vegetarian = data.get('plus_one_vegetarian', False)
    plus_one_wine = data.get('plus_one_wine', False)
    song_suggestion = data['song_suggestion']
    

    # Create a new RSVP entry
    rsvp = rsvps(name=name, attending=attending, vegetarian=vegetarian, wine=wine, plus_one=plus_one, plus_one_name=plus_one_name, plus_one_vegetarian=plus_one_vegetarian, plus_one_wine=plus_one_wine, song_suggestion=song_suggestion)
    db.session.add(rsvp) 
    db.session.commit()

    return jsonify({'message': 'RSVP created successfully'}), 201

@app.route('/rsvps', methods=['GET'])
def get_all_rsvps():
    all_rsvps = rsvps.query.all()
    rsvps_list = [{'id': rsvp.id, 'name': rsvp.name, 'attending': rsvp.attending, 'vegetarian': rsvp.vegetarian, 'wine':rsvp.wine, 'plus_one': rsvp.plus_one, 'plus_one_name': rsvp.plus_one_name, 'plus_one_vegetarian': rsvp.plus_one_vegetarian, 'plus_one_wine': rsvp.plus_one_wine, 'song_suggestion': rsvp.song_suggestion} for rsvp in all_rsvps]
    return jsonify(rsvps_list)

  # Define the model
class evening_rsvps(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(100), nullable=False)
      attending = db.Column(db.String(10), nullable=False)
      vegetarian = db.Column(db.String(10), nullable=False)
      plus_one = db.Column(db.String(10), nullable=True)
      plus_one_name = db.Column(db.String(100), nullable=True)
      plus_one_vegetarian = db.Column(db.String(10), nullable=False)

@app.route('/evening_rsvp', methods=['POST'])
def create_evening_rsvp():
      data = request.json

       # Log received data
      logging.debug("Received data: %s", data)

      # Validate input
      if not all(key in data for key in ['name', 'attending']):
          return jsonify({'error': 'Missing required fields'}), 400

      name = data['name']
      attending = data['attending']
      vegetarian = data['vegetarian']
      plus_one = data['plus_one']
      plus_one_name = data.get('plus_one_name', '')
      plus_one_vegetarian = data['plus_one_vegetarian']
      # Create a new RSVP entry
      evening_rsvp = evening_rsvps(name=name, attending=attending, vegetarian=vegetarian, plus_one=plus_one, plus_one_name=plus_one_name, plus_one_vegetarian=plus_one_vegetarian)
      db.session.add(evening_rsvp)
      db.session.commit()

      return jsonify({'message': 'Evening RSVP created successfully'}), 201

@app.route('/evening_rsvps', methods=['GET'])
def get_all_evening_rsvps():
      all_evening_rsvps = evening_rsvps.query.all()
      evening_rsvps_list = [{'id': evening_rsvp.id, 'name': evening_rsvp.name, 'attending': evening_rsvp.attending, 'vegetarian': evening_rsvp.vegetarian, 'plus_one': evening_rsvp.plus_one, 'plus_one_name': evening_rsvp.plus_one_name, 'plus_one_vegetarian': evening_rsvp.plus_one_vegetarian} for evening_rsvp in all_evening_rsvps]
      return jsonify(evening_rsvps_list)

@app.route('/rsvp_count', methods=['GET'])
def get_rsvp_count():
    # Explicitly declare the SQL query as text
    query = text("SELECT (SELECT count(attending) FROM rsvps WHERE attending = 'Yes') + (SELECT count(plus_one) FROM rsvps WHERE plus_one = 'Yes') AS total_count")
    count = db.session.execute(query).scalar()
    return jsonify({'count': count})

if __name__ == '__main__':
    
    app.run(host='0.0.0.0')
