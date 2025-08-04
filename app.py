
from flask import Flask, request, render_template
import google.generativeai as genai
from PIL import Image

app = Flask(__name__)

genai.configure(api_key='AIzaSyBdUM521lV7jxNHxaimQDJ4imO97_SMyGc')  # Replace with your API key

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return "No file uploaded!"
        
        img = Image.open(file)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(["Describe this image:", img])
        description = response.text
        
        return render_template('result.html', description=description)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
