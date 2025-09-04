"""
Data collectors package for gathering data from various APIs.
"""

from .weather_collector import WeatherCollector

# TODO: Add other collectors as they are created
# from .news_collector import NewsCollector
# from .transportation_collector import TransportationCollector
# from .geographic_collector import GeographicCollector

__all__ = [
    'WeatherCollector',
    # 'NewsCollector', 
    # 'TransportationCollector',
    # 'GeographicCollector'
]
