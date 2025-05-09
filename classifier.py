import tensorflow as tf
import pickle
from keras.layers import TFSMLayer

model = TFSMLayer("models/formintel_model", call_endpoint="serve")

with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("models/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

def predict_form_type(text):
    X = vectorizer.transform([text]).toarray()
    preds = model(X)
    label_index = tf.argmax(preds, axis=1).numpy()[0]
    return label_encoder.inverse_transform([label_index])[0]
