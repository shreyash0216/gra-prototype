# 🤖 Generative Resilience Agent (GRA)

**AI-Powered Climate Adaptation & Agricultural Intelligence Platform**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/shreyash0216/gra-prototype)

**Live Demo**: [Coming Soon - Deploy to get your URL]

---

## 🌟 What is GRA?

**Generative Resilience Agent (GRA)** is an advanced AI-powered platform that helps farmers adapt to climate change through:
- 🤖 **Gen AI Integration** - Powered by OpenAI GPT or Anthropic Claude for intelligent analysis
- 💬 **AI Chat Assistant** - Real-time conversational farming advice
- 🌡️ **Climate Risk Analysis** - AI-driven location-specific assessment
- 🌾 **Smart Crop Recommendations** - Gen AI-powered crop selection
- 📈 **Market Intelligence** - AI-analyzed price trends and strategies
- 🏛️ **Government Scheme Finder** - Automated subsidy matching
- 🗺️ **Visual Farm Planning** - SVG-based farm layout generation

### 🚀 Gen AI Powered
GRA uses real generative AI (GPT/Claude) for dynamic, intelligent responses. See [GEN_AI_SETUP.md](GEN_AI_SETUP.md) for configuration.

## Overview

This system helps farmers create comprehensive climate adaptation plans using AI analysis. It provides:

- **Climate Risk Analysis**: Identifies climate risks specific to your location
- **Crop Recommendations**: Suggests climate-resilient crops based on your farm conditions
- **Market Analysis**: Analyzes market potential for recommended crops
- **Government Schemes**: Finds relevant subsidies and support programs
- **Farm Layout Planning**: Generates visual farm layout diagrams
- **Nearby Farm Insights**: Learn from successful adaptation plans in your area

## Features

### 🌡️ Climate Analysis
- Location-specific climate risk assessment
- Adaptation strategy recommendations
- Urgency level calculation

### 🌾 Smart Crop Advisory
- AI-powered crop recommendations
- Soil and water compatibility analysis
- Seasonal planting calendar
- Yield and income projections

### 📈 Market Intelligence
- Real-time market price analysis
- Demand forecasting
- Export potential assessment
- Marketing strategy recommendations

### 🏛️ Government Scheme Finder
- Automated scheme matching
- Eligibility verification
- Application timeline planning
- Document requirement checklist

### 🗺️ Farm Layout Designer
- Visual farm layout generation
- Crop placement optimization
- Infrastructure planning
- Water source integration

## Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: Database ORM
- **SQLite**: Local database storage
- **AI Agents**: Climate analysis, crop advisory, market analysis, scheme finder

### Frontend
- **React**: Modern JavaScript UI library
- **Vanilla CSS**: Custom styling
- **SVG Graphics**: Farm layout visualization

### Database
- **SQLite**: Stores adaptation plans and farm data
- **JSON Knowledge Base**: Crop data, market info, government schemes

## Installation & Setup

### Prerequisites
- Python 3.8+
- Modern web browser

### Backend Setup
```bash
cd gra-prototype/backend
pip install -r ../requirements.txt
python main.py
```

### Frontend Access
Open `frontend/index.html` in your web browser or serve it locally:
```bash
cd gra-prototype/frontend
python -m http.server 3000
```

## Usage

1. **Fill Farm Details**: Enter your location, farm size, soil type, water source, and budget
2. **Specify Concerns**: List your climate concerns (drought, flooding, etc.)
3. **Set Goals**: Define your adaptation goals (increase yield, reduce water usage, etc.)
4. **Generate Plan**: Click "Generate Climate Adaptation Plan" to get AI analysis
5. **Review Results**: Examine crop recommendations, government schemes, and implementation timeline
6. **View Layout**: See the visual farm layout diagram
7. **Check Nearby Farms**: Learn from successful plans in your area

## API Endpoints

- `POST /analyze-climate`: Generate comprehensive adaptation plan
- `POST /nearby-farms`: Find adaptation plans from nearby farms
- `GET /plan/{plan_id}`: Retrieve specific adaptation plan
- `GET /crops`: Get crop database
- `GET /schemes`: Get government schemes database

## Sample Data

The system includes comprehensive sample data:
- **10 Crop varieties** with climate tolerance, market prices, and growing requirements
- **6 Government schemes** with eligibility criteria and subsidy amounts
- **Market data** with price trends and demand patterns

## Future Enhancements

- **LLM Integration**: Connect with Claude/GPT for advanced AI analysis
- **Weather API**: Real-time weather data integration
- **Mobile App**: React Native mobile application
- **IoT Integration**: Sensor data for precision agriculture
- **Blockchain**: Supply chain traceability
- **Machine Learning**: Predictive analytics for yield optimization

## Contributing

This is a prototype system. For production use:
1. Integrate with real LLM APIs (OpenAI, Anthropic)
2. Add proper authentication and user management
3. Implement geospatial databases for location queries
4. Add real-time weather and market data APIs
5. Enhance security and data validation

## License

MIT License - Feel free to use and modify for your projects.

---

**Built for farmers, by developers who care about sustainable agriculture and climate resilience.**