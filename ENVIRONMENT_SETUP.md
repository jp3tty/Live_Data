# Environment Setup Guide

## Required API Keys

To use this project, you'll need to obtain API keys from the following services:

### 1. OpenWeatherMap API
- **Website**: https://openweathermap.org/api
- **Free Tier**: 1,000 calls/day
- **Environment Variable**: `OPENWEATHER_API_KEY`

### 2. NewsAPI
- **Website**: https://newsapi.org/
- **Free Tier**: 1,000 requests/day
- **Environment Variable**: `NEWSAPI_KEY`

### 3. Guardian API (Optional)
- **Website**: https://open-platform.theguardian.com/
- **Free Tier**: 5,000 requests/day
- **Environment Variable**: `GUARDIAN_API_KEY`

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# API Keys
OPENWEATHER_API_KEY=your_openweather_api_key_here
NEWSAPI_KEY=your_newsapi_key_here
GUARDIAN_API_KEY=your_guardian_api_key_here

# Database Configuration
DATABASE_URL=sqlite:///data/live_data.db

# Data Collection Settings
WEATHER_UPDATE_INTERVAL=3600  # seconds (1 hour)
NEWS_UPDATE_INTERVAL=1800     # seconds (30 minutes)
TRANSPORT_UPDATE_INTERVAL=300 # seconds (5 minutes)

# Geographic Settings
DEFAULT_LATITUDE=40.7128
DEFAULT_LONGITUDE=-74.0060
DEFAULT_CITY=New York
```

## Setup Instructions

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create .env file:**
   ```bash
   # Copy the environment variables above into a new .env file
   touch .env  # On Windows: type nul > .env
   ```

4. **Add your API keys to the .env file**

5. **Test the setup:**
   ```bash
   python test_weather.py
   ```

## Testing

Run the test script to verify everything is working:
```bash
python test_weather.py
```

This will test the weather collector with the default coordinates (New York).