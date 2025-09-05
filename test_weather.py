#!/usr/bin/env python3
"""
Simple test script for the weather collector.
"""
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data_collectors import WeatherCollector

def test_weather_collector():
    """Test the weather collector functionality."""
    print("Testing Weather Collector...")
    
    # Initialize collector
    collector = WeatherCollector()
    
    # Test with Portland, Oregon coordinates
    print("Collecting weather data for Portland, Oregon...")
    weather_data = collector.get_current_weather(lat=45.5152, lon=-122.6784)
    
    if weather_data:
        print("✅ Weather data collected successfully!")
        print(f"Temperature: {weather_data.get('main', {}).get('temp', 'N/A')}°C")
        print(f"Description: {weather_data.get('weather', [{}])[0].get('description', 'N/A')}")
        print(f"Collected at: {weather_data.get('collected_at', 'N/A')}")
    else:
        print("❌ Failed to collect weather data")
        print("Make sure you have set your OPENWEATHER_API_KEY in a .env file")

if __name__ == "__main__":
    test_weather_collector()