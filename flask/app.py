from datetime import datetime
from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__,
    static_folder='./frontend/dist/nuxt',
    template_folder='./frontend/dist')

cors = CORS(app, resources={"/api/*": {"origins": "*"}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')

@app.route('/api/v1.0/message')
def message():
    data = {
        "message": "Nuevo mensaje desde un servidor Flask = " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)