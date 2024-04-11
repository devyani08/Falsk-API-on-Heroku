
from flask import Flask, send_file


app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to The Student Exam Score Tracker API!'

@app.route('/data')
def get_data():
    try:
        # print("Attempting to send file...")
        return send_file('csvjson.json', mimetype='application/json')
    except FileNotFoundError:
        return "Error: JSON data file not found", 404
if __name__ == '__main__':
    app.run(debug=True)
