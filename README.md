# 🧠 FormIntel - AI-Powered Document Classification and Summarization

FormIntel is a full-stack document intelligence tool that uses OCR, NLP, and Machine Learning to:
- Extract text from uploaded document images,
- Classify the type of document (e.g., **Invoice**, **Receipt**, or **Timesheet**),
- Summarize long documents using T5 Transformers,
- Extract structured fields using simple pattern-based logic.

Built with **Flask**, **TensorFlow**, **TfidfVectorizer**, **Tesseract OCR**, and **HuggingFace Transformers**.

---

## 🚀 Features

- ✅ OCR image-to-text with Tesseract
- ✅ Document classification (ML model)
- ✅ Transformer-based text summarization
- ✅ REST API interface
- ✅ Fast JSON output (suitable for backend pipelines)
- ✅ Built-in data generator + stress test via `/predict`

---

## 🛠️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/cmdsnr/FormIntel.git
cd FormIntel
```
- Install Dependencies:
```
pip install -r requirements.txt
```
Then:
```
python train_model.py
```
Which will generate the keras file in the /model directory.
Finally run: `python app.py`
and use the `generate_and_post.py` file to try with a data sample I made. (The file will also send a post request with the json file)
You can also post an image file: `curl -X POST -F "file=@somefile.png" http://127.0.0.1:5000/process`
