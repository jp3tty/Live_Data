# Live Data Collection Project

A comprehensive data collection and analysis project that gathers real-time data from multiple sources including weather, news, transportation, and geographic data.

## �� Project Overview

This project demonstrates skills in:
- Real-time data collection from multiple APIs
- Data processing and storage pipelines
- Interactive visualizations and dashboards
- Geographic data analysis
- News sentiment analysis
- Transportation pattern analysis

## 📊 Data Sources

### Weather Data
- **OpenWeatherMap API** - Global weather data, forecasts, and historical data
- **National Weather Service API** - Official U.S. weather data

### News Data
- **NewsAPI** - News headlines and articles from multiple sources
- **Guardian API** - High-quality journalism content

### Transportation Data
- **OpenSky Network** - Real-time air traffic control data and flight tracking
- **Transport for London (TfL) Open Data** - London transport system data

### Geographic Data
- **OpenStreetMap (OSM)** - Free, editable world maps
- **OpenCelliD** - Cell tower location data

## �� Quick Start

1. **Clone and Setup**
   ```bash
   cd Live_Data
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Run Data Collection**
   ```bash
   python scripts/collect_data.py
   ```

4. **Explore Data**
   ```bash
   jupyter notebook notebooks/
   ```

## 📁 Project Structure

```
Live_Data/
├── config/                 # Configuration settings
├── src/                    # Source code
│   ├── data_collectors/    # API data collection modules
│   ├── data_processors/    # Data processing and cleaning
│   ├── storage/           # Database and file storage
│   └── utils/             # Utility functions
├── notebooks/             # Jupyter notebooks for analysis
├── data/                  # Data storage
│   ├── raw/              # Raw API data
│   ├── processed/        # Cleaned data
│   └── outputs/          # Analysis outputs
├── visualizations/        # Charts, maps, and dashboards
├── tests/                # Unit tests
├── scripts/              # Main execution scripts
└── docs/                 # Documentation
```

## 🔧 Configuration

Edit `config/settings.py` to customize:
- API endpoints and parameters
- Data collection intervals
- Geographic coordinates
- Database settings

##  Features

- **Real-time Data Collection** - Automated data gathering from multiple sources
- **Data Processing Pipeline** - Clean, transform, and store data efficiently
- **Interactive Visualizations** - Dynamic charts and maps using Plotly and Folium
- **Sentiment Analysis** - News sentiment analysis using TextBlob
- **Geographic Analysis** - Location-based insights and mapping
- **Transportation Tracking** - Flight and transport pattern analysis

##  Testing

```bash
pytest tests/
```

## 📝 API Keys Required

- OpenWeatherMap API key
- NewsAPI key
- Guardian API key (optional)

##  Contributing

This is a portfolio project demonstrating data collection and analysis skills.

## 📄 License

MIT License

