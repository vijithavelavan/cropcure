from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import json
import os
from .models import DetectionHistory
from .ml_model import detector
from .knowledge_base import get_disease_info
from googletrans import Translator

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username already exists'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'success': True, 'message': 'Registration successful'})
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'})
        return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    
    return render(request, 'login.html')

@login_required
def dashboard(request):
    history = DetectionHistory.objects.filter(user=request.user).order_by('-created_at')[:5]
    return render(request, 'dashboard.html', {'history': history})

@csrf_exempt
@login_required
def detect_disease(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        language = request.POST.get('language', 'en')
        
        # Save uploaded image
        file_path = default_storage.save(f'uploads/{image.name}', image)
        full_path = default_storage.path(file_path)
        
        try:
            # Predict disease
            predicted_disease, confidence = detector.predict(full_path)
            disease_info = get_disease_info(predicted_disease)
            
            # Translate if needed
            translator = Translator()
            if language != 'en':
                try:
                    disease_info['symptoms'] = translator.translate(disease_info['symptoms'], dest=language).text
                    disease_info['treatment'] = translator.translate(disease_info['treatment'], dest=language).text
                except:
                    pass
            
            # Save to history
            DetectionHistory.objects.create(
                user=request.user,
                image=file_path,
                predicted_disease=predicted_disease,
                confidence=confidence,
                symptoms=disease_info['symptoms'],
                treatment=disease_info['treatment']
            )
            
            return JsonResponse({
                'success': True,
                'disease': predicted_disease,
                'confidence': round(confidence * 100, 2),
                'symptoms': disease_info['symptoms'],
                'treatment': disease_info['treatment']
            })
            
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return render(request, 'detect.html')

@login_required
def history_view(request):
    history = DetectionHistory.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'history.html', {'history': history})

def logout_view(request):
    logout(request)
    return redirect('home')