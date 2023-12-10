from flask import Flask, request, render_template, jsonify
from keras.models import load_model
import numpy as np
#import pre pro 1
from keras.preprocessing import image

#import pre pro 2 w pillow
from PIL import Image
from tensorflow.keras.preprocessing import image as tf_image

#import date 1
from datetime import datetime

app = Flask(__name__)

model = load_model('modelmodul6.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict2', methods=['POST'])
def predictv2():
    if request.method == 'POST':
        # Post
        file = request.files['file']

        # pre pro
        img = Image.open(file).convert('RGB').resize((150, 150))
        img_array = tf_image.img_to_array(img) / 255.0  # normalize dataset jeruk
        img_array = np.expand_dims(img_array, axis=0)  # conv jeruk ke array

        # predict
        prediction = model.predict(img_array)

        #Return dengan json
        return jsonify({'prediction': prediction.tolist()})


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # post
        file = request.files['file']

        # pre pro v3
        img = Image.open(file).convert('RGB').resize((150, 150))
        img_array = tf_image.img_to_array(img) / 255.0 # normalize dataset jeruk
        img_array = np.expand_dims(img_array, axis=0) # conv jeruk ke array

        # predict
        prediction = model.predict(img_array)
        predicted_label = str(np.argmax(prediction))

        labels = ['paper', 'rock', 'scissors']
        actual_label = labels[int(predicted_label)]

        # pil 1 return json / pil 2 value dom js (soon)
        return jsonify({
            'prediction': prediction.tolist(),
            'predicted_label': predicted_label,
            'actual_label': actual_label
        })


if __name__ == '__main__':
    app.run(debug=True)
