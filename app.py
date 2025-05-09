from flask import Flask, request, jsonify
from ocr_engine import extract_text
from classifier import predict_form_type
from summarizer import summarize_text
from extractor import extract_fields

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_document():
    file = request.files['file']
    image_path = f"./uploads/{file.filename}"
    file.save(image_path)

    text = extract_text(image_path)
    doc_type = predict_form_type(text)
    summary = summarize_text(text)
    fields = extract_fields(text)

    return jsonify({
        "document_type": doc_type,
        "summary": summary,
        "extracted_fields": fields
    })

@app.route('/predict', methods=['POST'])
def predict_text():
    data = request.get_json()
    text = data.get('text', '').strip()
    if not text:
        return jsonify({"error": "No text provided"}), 400
    prediction = predict_form_type(text)
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)
