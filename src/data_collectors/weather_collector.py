"""
Weather data collector for OpenWeatherMap and National Weather Service APIs.
"""
import requests
import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional
import logging

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from config.settings import Config

logger = logging.getLogger(__name__)

class WeatherCollector:
    """Collects weather data from multiple sources."""
    
    def __init__(self):
        self.config = Config()
        self.session = requests.Session()
    
    def get_current_weather(self, city: str = None, lat: float = None, lon: float = None) -> Dict:
        """
        Get current weather data from OpenWeatherMap.
        
        Args:
            city: City name (optional)
            lat: Latitude (optional)
            lon: Longitude (optional)
            
        Returns:
            Dictionary containing current weather data
        """
        try:
            if city:
                url = f"{self.config.OPENWEATHER_BASE_URL}/weather"
                params = {
                    'q': city,
                    'appid': self.config.OPENWEATHER_API_KEY,
                    'units': 'imperial'
                }
            elif lat and lon:
                url = f"{self.config.OPENWEATHER_BASE_URL}/weather"
                params = {
                    'lat': lat,
                    'lon': lon,
                    'appid': self.config.OPENWEATHER_API_KEY,
                    'units': 'imperial'
                }
            else:
                raise ValueError("Either city or lat/lon must be provided")
            
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            data['collected_at'] = datetime.now().isoformat()
            
            logger.info(f"Successfully collected weather data for {city or f'{lat},{lon}'}")
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error collecting weather data: {e}")
            return {}
        except Exception as e:
            logger.error(f"Unexpected error in weather collection: {e}")
            return {}
    
    def get_weather_forecast(self, city: str = None, lat: float = None, lon: float = None) -> Dict:
        """
        Get 5-day weather forecast from OpenWeatherMap.
        
        Args:
            city: City name (optional)
            lat: Latitude (optional)
            lon: Longitude (optional)
            
        Returns:
            Dictionary containing forecast data
        """
        try:
            if city:
                url = f"{self.config.OPENWEATHER_BASE_URL}/forecast"
                params = {
                    'q': city,
                    'appid': self.config.OPENWEATHER_API_KEY,
                    'units': 'imperial'
                }
            elif lat and lon:
                url = f"{self.config.OPENWEATHER_BASE_URL}/forecast"
                params = {
                    'lat': lat,
                    'lon': lon,
                    'appid': self.config.OPENWEATHER_API_KEY,
                    'units': 'imperial'
                }
            else:
                raise ValueError("Either city or lat/lon must be provided")
            
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            data['collected_at'] = datetime.now().isoformat()
            
            logger.info(f"Successfully collected forecast data for {city or f'{lat},{lon}'}")
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error collecting forecast data: {e}")
            return {}
        except Exception as e:
            logger.error(f"Unexpected error in forecast collection: {e}")
            return {}
