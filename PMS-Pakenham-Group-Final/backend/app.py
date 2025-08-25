
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the PMS API"

@app.route('/register')
def register():
    return jsonify({"message": "Registration endpoint"})

@app.route('/book')
def book_appointment():
    return jsonify({"message": "Appointment booking endpoint"})

if __name__ == '__main__':
    app.run(debug=True)
