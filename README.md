# CropCure - Plant Disease Detection System

A web-based plant disease detection system using deep learning and machine learning algorithms.

## Features

- **AI-Powered Detection**: Uses MobileNetV2 with transfer learning
- **Multi-language Support**: Google Translate API integration
- **User Authentication**: Secure login/registration system
- **Detection History**: Track previous detections
- **Responsive Design**: Works on desktop and mobile devices

## Installation

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Database Setup**
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Create Superuser**
```bash
python manage.py createsuperuser
```

4. **Run Server**
```bash
python manage.py runserver
```

## Usage

1. Register a new account or login
2. Navigate to "Detect Disease"
3. Upload a leaf image
4. Select language preference
5. View results with symptoms and treatment recommendations

## Disease Classes

- Healthy
- Bacterial Blight
- Brown Spot
- Leaf Blast
- Tungro

## Technology Stack

- **Backend**: Django, TensorFlow, MobileNetV2
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite
- **ML**: Transfer Learning, CNN, Image Processing
- **Translation**: Google Translate API

## Project Structure

```
cropcure/
├── cropcure_project/          # Django project settings
├── detection/                 # Main app
├── templates/                 # HTML templates
├── static/                    # CSS, JS, images
├── media/                     # Uploaded images
└── requirements.txt           # Dependencies
```