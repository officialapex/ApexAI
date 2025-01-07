import os

class Config:
    """Base configuration class."""
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///apex_ai.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
