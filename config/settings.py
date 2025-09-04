"""
Configuration settings for the Live Data project.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Main configuration class."""
    
    # API Keys
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
    NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')
    GUARDIAN_API_KEY = os.getenv('GUARDIAN_API_KEY')
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///data/live_data.db')
    
    # Data Collection Intervals (in seconds)
    WEATHER_UPDATE_INTERVAL = int(os.getenv('WEATHER_UPDATE_INTERVAL', 3600))
    NEWS_UPDATE_INTERVAL = int(os.getenv('NEWS_UPDATE_INTERVAL', 1800))
    TRANSPORT_UPDATE_INTERVAL = int(os.getenv('TRANSPORT_UPDATE_INTERVAL', 300))
    
    # Geographic Settings
    DEFAULT_LATITUDE = float(os.getenv('DEFAULT_LATITUDE', 40.7128))
    DEFAULT_LONGITUDE = float(os.getenv('DEFAULT_LONGITUDE', -74.0060))
    DEFAULT_CITY = os.getenv('DEFAULT_CITY', 'New York')
    
    # API Endpoints
    OPENWEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5"
    NEWSAPI_BASE_URL = "https://newsapi.org/v2"
    GUARDIAN_BASE_URL = "https://content.guardianapis.com"
    OPENSKY_BASE_URL = "https://opensky-network.org/api"
    
    # Data Storage Paths
    RAW_DATA_PATH = "data/raw"
    PROCESSED_DATA_PATH = "data/processed"
    OUTPUTS_PATH = "data/outputs"
