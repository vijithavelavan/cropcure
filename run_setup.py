#!/usr/bin/env python
import os
import sys
import subprocess

def run_command(command):
    """Run a command and print the output"""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")
    return result.returncode == 0

def setup_project():
    """Setup the CropCure project"""
    print("Setting up CropCure project...")
    
    # Create media directory
    os.makedirs('media/uploads', exist_ok=True)
    print("Created media directories")
    
    # Run migrations
    if run_command('python manage.py makemigrations'):
        run_command('python manage.py migrate')
    
    # Collect static files
    run_command('python manage.py collectstatic --noinput')
    
    print("\nSetup complete!")
    print("To run the server: python manage.py runserver")
    print("To create admin user: python manage.py createsuperuser")

if __name__ == '__main__':
    setup_project()