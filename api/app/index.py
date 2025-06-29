from flask import Flask, Response, jsonify
from flask_cors import CORS
from app.main import bp as main_bp
from .pdfextractor import convert_pdf_to_txt

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3001"}})  # Svelte dev server
app.register_blueprint(main_bp, url_prefix='/main')


@app.route('/')
def index():
    return jsonify({'message': 'Hey from flask!'})
