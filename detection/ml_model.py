import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
import numpy as np
from PIL import Image
import os

class DiseaseDetector:
    def __init__(self):
        self.model = None
        self.class_names = ['Healthy', 'Bacterial_Blight', 'Brown_Spot', 'Leaf_Blast', 'Tungro']
        self.load_model()
    
    def create_model(self):
        base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
        base_model.trainable = False
        
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        predictions = Dense(len(self.class_names), activation='softmax')(x)
        
        model = Model(inputs=base_model.input, outputs=predictions)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model
    
    def load_model(self):
        try:
            self.model = tf.keras.models.load_model('detection/crop_disease_model.h5')
        except:
            self.model = self.create_model()
    
    def preprocess_image(self, image_path):
        image = Image.open(image_path).convert('RGB')
        image = image.resize((224, 224))
        image_array = np.array(image) / 255.0
        return np.expand_dims(image_array, axis=0)
    
    def predict(self, image_path):
        processed_image = self.preprocess_image(image_path)
        predictions = self.model.predict(processed_image)
        predicted_class_idx = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class_idx])
        predicted_class = self.class_names[predicted_class_idx]
        return predicted_class, confidence

detector = DiseaseDetector()