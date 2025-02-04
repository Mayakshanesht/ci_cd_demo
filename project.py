from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

@app.route('/')
def index():
    return '''
    <html>
        <head>
            <title>Simple Calculator</title>
        </head>
        <body>
            <h2>Enter Numbers</h2>
            <form action="/calculate" method="get">
                <label for="a">Number 1:</label>
                <input type="number" id="a" name="a" required>
                <br>
                <label for="b">Number 2:</label>
                <input type="number" id="b" name="b" required>
                <br>
                <label for="operation">Choose operation:</label>
                <select name="operation" id="operation">
                    <option value="add">Add</option>
                    <option value="multiply">Multiply</option>
                </select>
                <br><br>
                <button type="submit">Calculate</button>
            </form>
        </body>
    </html>
    '''

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        operation = request.args.get('operation')

        calc = Calculator(a, b)

        if operation == "add":
            result = calc.add()
        elif operation == "multiply":
            result = calc.multiply()
        else:
            return jsonify({"error": "Invalid operation. Use 'add' or 'multiply'"}), 400

        return f"<h2>Result: {result}</h2><br><a href='/'>Go Back</a>"

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
# from flask import Flask, request, render_template_string, jsonify
# from werkzeug.utils import secure_filename
# import torch
# from torchvision import models, transforms
# from PIL import Image
# import io
# import json

# app = Flask(__name__)

# # Initialize CV models
# model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
# model.eval()

# # Image preprocessing
# preprocess = transforms.Compose([
#     transforms.Resize(256),
#     transforms.CenterCrop(224),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
# ])

# # Load ImageNet labels
# with open('imagenet_class_index.json') as f:
#     labels = json.load(f)

# def analyze_image(img):
#     """Perform comprehensive image analysis"""
#     img_tensor = preprocess(img).unsqueeze(0)
    
#     with torch.no_grad():
#         outputs = model(img_tensor)
    
#     _, indices = torch.sort(outputs, descending=True)
#     return [(labels[str(idx.item())][1], torch.nn.functional.softmax(outputs, dim=1)[0][idx].item()) 
#             for idx in indices[0][:5]]

# @app.route('/')
# def index():
#     return render_template_string('''
#     <html>
#         <head>
#             <title>AI Vision Analyzer</title>
#             <style>
#                 body { max-width: 800px; margin: 20px auto; padding: 20px; }
#                 .result { margin-top: 20px; padding: 15px; border: 1px solid #ddd; }
#                 img { max-width: 500px; margin: 20px 0; }
#             </style>
#         </head>
#         <body>
#             <h1>🖼️ AI Vision Analyzer</h1>
#             <form action="/analyze" method="post" enctype="multipart/form-data">
#                 <input type="file" name="image" accept="image/*" required>
#                 <br><br>
#                 <button type="submit">Analyze Image</button>
#             </form>
            
#             {% if result %}
#                 <div class="result">
#                     <h2>Analysis Results</h2>
#                     {% if image %}
#                         <img src="data:image/png;base64,{{ image }}" alt="Uploaded Image">
#                     {% endif %}
#                     <h3>🔍 Top Predictions:</h3>
#                     <ol>
#                         {% for prediction in result.predictions %}
#                             <li>{{ prediction[0] }} ({{ "%.2f"|format(prediction[1]*100) }}%)</li>
#                         {% endfor %}
#                     </ol>
#                     <h3>📐 Image Metadata:</h3>
#                     <p>Format: {{ result.metadata.format }}<br>
#                     Size: {{ result.metadata.size }}<br>
#                     Mode: {{ result.metadata.mode }}</p>
#                 </div>
#             {% endif %}
#         </body>
#     </html>
#     ''')

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     try:
#         if 'image' not in request.files:
#             return render_template_string(index(), error="No image uploaded")
        
#         file = request.files['image']
#         if file.filename == '':
#             return render_template_string(index(), error="No selected file")
        
#         img = Image.open(io.BytesIO(file.read())).convert('RGB')
        
#         # Convert image to base64 for display
#         img_buffer = io.BytesIO()
#         img.save(img_buffer, format='PNG')
#         img_str = img_buffer.getvalue().hex()
        
#         # Perform analysis
#         predictions = analyze_image(img)
#         metadata = {
#             'format': img.format,
#             'size': img.size,
#             'mode': img.mode
#         }
        
#         return render_template_string(index(), 
#                                     result={'predictions': predictions, 'metadata': metadata},
#                                     image=img_str)

#     except Exception as e:
#         return render_template_string(index(), error=f"Error processing image: {str(e)}")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5002)