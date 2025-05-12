from flask import render_template, request, jsonify, send_file
from app import app
import os
import io
import base64
from PIL import Image
import openai

# Configure your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        prompt = request.json.get('prompt')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        # Call DALL-E API
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="b64_json"
        )
        
        # Get the base64 image data
        image_data = response['data'][0]['b64_json']
        
        # Convert to bytes
        image_bytes = base64.b64decode(image_data)
        
        # Create a file-like object in memory
        image_file = io.BytesIO(image_bytes)
        
        # Generate a filename
        filename = f"generated_image_{hash(prompt)}.png"
        
        return jsonify({
            'image': image_data,
            'filename': filename
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download-image', methods=['POST'])
def download_image():
    try:
        data = request.json
        image_data = data.get('image')
        filename = data.get('filename')
        
        if not image_data or not filename:
            return jsonify({'error': 'Image data and filename are required'}), 400
        
        # Convert base64 to bytes
        image_bytes = base64.b64decode(image_data)
        
        # Create a file-like object in memory
        image_file = io.BytesIO(image_bytes)
        
        return send_file(
            image_file,
            mimetype='image/png',
            as_attachment=True,
            download_name=filename
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
