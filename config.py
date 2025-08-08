"""
Configuration for AutonomaX-Commander independent release
"""
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'autonomax-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///autonomax_commander.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Add more config as needed
