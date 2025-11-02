from flask import Flask, render_template, request
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import torch

# Initialize Flask app
app = Flask(__name__)

# Load the model and tokenizer (assuming the model is saved in the "sentiment_model" folder)
model_path = r"C:\Users\Hp\Desktop\sentiment-analysis-app\sentiment_model"
model = DistilBertForSequenceClassification.from_pretrained(model_path)
tokenizer = DistilBertTokenizer.from_pretrained(model_path)

# Function to predict sentiment
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=64)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim=1).item()
    
    return predicted_class_id

# Mapping of class labels to sentiment
label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}

def predict_sentiment_label(text):
    predicted_class_id = predict_sentiment(text)
    return label_map.get(predicted_class_id, "Unknown")

# Route to render the form page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input text from the form
    user_input = request.form['text_input']
    
    # Get the predicted sentiment
    prediction = predict_sentiment_label(user_input)
    
    # Return the result to the frontend
    return render_template('index.html', prediction=prediction, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
