import tensorflow as tf
import numpy as np

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape=(100,), activation="relu"),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

def predict_phishing(url):
    encoded_url = np.zeros((1, 100))
    encoded_url[0] = np.array([ord(c) for c in url])
    prediction = model.predict(encoded_url)
    return prediction[0][0]

def warn_of_phishing(url):
    phishing_likelihood = predict_phishing(url)
    if phishing_likelihood > 0.5:
        print("[WARNING] Phishing attempt detected: " + url)
    else:
        print("[INFO] Safe URL: " + url)

warn_of_phishing("http://www.google.com")
warn_of_phishing("http://phishing-site.com")
