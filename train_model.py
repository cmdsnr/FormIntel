import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import os

os.makedirs("models", exist_ok=True)

data = {
    'text': [
        "Invoice number 12345 due 2023-06-01 amount $400",
        "Receipt for payment of $200 made on 2023-04-15",
        "Employee timesheet for May hours worked 160",
        "Invoice #56789 total due $350 client ABC Ltd",
        "Receipt for subscription paid on April 10th",
        "Timesheet log for John Doe for March 20"
    ] * 200,
    'label': ["Invoice", "Receipt", "Timesheet", "Invoice", "Receipt", "Timesheet"] * 200
}
df = pd.DataFrame(data)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['label'])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text']).toarray()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential([
    Input(shape=(X.shape[1],)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(3, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

model.export("models/formintel_model")

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
with open("models/label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("Model, vectorizer, and encoder saved.")
