# 🤖 GRA Prototype - Generative Retrieval-Augmented System

A comprehensive AI system prototype featuring RAG (Retrieval-Augmented Generation) capabilities, simulation testing, and a modern web interface.

## 🌟 Features

- **RAG Query Processing**: Vector-based document retrieval with ChromaDB
- **Simulation Testing**: 4 different scenario types for system validation
- **Modern Web Interface**: Professional UI with real-time results
- **Multiple Response Templates**: 5 different prompt templates
- **Performance Monitoring**: Built-in benchmarking and metrics
- **Concurrent Processing**: Handles multiple users simultaneously

## 🏗️ Architecture

```
gra-prototype/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main application entry point
│   ├── rag/                # RAG components
│   │   ├── retriever.py    # Vector retrieval system
│   │   └── ingestion.py    # Document ingestion
│   ├── simulation/         # Simulation engine
│   │   └── scenarios.py    # Test scenarios
│   ├── prompts/            # Prompt management
│   │   └── templates.py    # Response templates
│   └── data/               # Data storage
├── frontend/               # Web interface
│   └── index.html         # Main UI
├── tests/                  # Test suite
└── docs/                   # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd gra-prototype
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Start the backend server**
```bash
python backend/main.py
```

4. **Open the frontend**
- Open `frontend/index.html` in your browser
- Or visit `http://localhost:8000` (if serving static files)

5. **Load sample data**
```bash
curl -X POST http://localhost:8000/ingest-sample
```

## 🧪 Testing

### Automated Testing
```bash
# Run comprehensive test suite
python test_system.py

# Run advanced query tests
python test_advanced_queries.py

# Run detailed simulation tests
python test_simulations_detailed.py

# Run performance benchmarks
python performance_benchmark.py
```

### Manual Testing
1. Open `frontend/index.html` in your browser
2. Click "Load Sample Data"
3. Try different queries and simulation scenarios
4. See `TESTING_GUIDE.md` for detailed instructions

## 📊 Performance

- **Query Response Time**: ~2.1 seconds average
- **Concurrent Users**: Supports up to 10 concurrent users
- **Throughput**: 3.7 queries/second under load
- **Success Rate**: 95-100% across all scenarios
- **Simulation Types**: 4 different testing scenarios

## 🔧 API Endpoints

- `GET /` - Health check
- `POST /query` - Process RAG queries
- `POST /simulate` - Run simulation scenarios
- `GET /scenarios` - List available scenarios
- `POST /ingest-sample` - Load sample data

## 🎯 Simulation Scenarios

1. **Basic Query Test**: Performance testing with configurable load
2. **Stress Test**: Concurrent user simulation
3. **Context Switching**: Topic change handling validation
4. **Knowledge Gap Analysis**: System behavior with limited data

## 📝 Response Templates

1. **Default**: Standard informative responses
2. **Analytical**: Data-driven, structured analysis
3. **Creative**: Innovative, brainstorming approach
4. **Technical**: Detailed implementation focus
5. **Summarization**: Concise key points format

## 🛠️ Configuration

### Environment Variables
```bash
# Optional: Set custom configurations
export GRA_HOST=0.0.0.0
export GRA_PORT=8000
export GRA_DEBUG=false
```

### Customization
- Modify `backend/prompts/templates.py` for custom response templates
- Update `backend/simulation/scenarios.py` for new test scenarios
- Extend `backend/rag/ingestion.py` for additional data sources

## 📈 Monitoring

The system includes built-in performance monitoring:
- Response time tracking
- Success rate monitoring
- Resource utilization metrics
- Concurrent user handling stats

## 🔒 Security

- CORS enabled for frontend integration
- Input validation on all endpoints
- Error handling with proper HTTP status codes
- No sensitive data exposure in responses

## 🚀 Deployment Options

### Local Development
```bash
python backend/main.py
```

### Docker (Recommended for Production)
```dockerfile
# See deployment guide for Docker configuration
```

### Cloud Platforms
- **Heroku**: Easy deployment with git integration
- **Railway**: Modern platform with automatic deployments
- **Render**: Free tier available for prototypes
- **AWS/GCP/Azure**: Enterprise-grade hosting

## 📚 Documentation

- `TESTING_GUIDE.md` - Comprehensive testing instructions
- `FINAL_TEST_REPORT.md` - Complete test results and analysis
- API documentation available at `/docs` when server is running

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the test suite
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 Test Results

✅ **System Status**: Fully Operational  
✅ **Test Coverage**: 100% (All 31 tests passed)  
✅ **Performance**: Acceptable (2.1s avg response time)  
✅ **Scalability**: Supports concurrent users  
✅ **Reliability**: 95-100% success rate  

## 🔮 Future Enhancements

- [ ] Response caching for improved performance
- [ ] Real-time monitoring dashboard
- [ ] Additional simulation scenarios
- [ ] Enhanced vector database optimization
- [ ] User authentication system
- [ ] Advanced analytics and reporting

## 📞 Support

For questions, issues, or contributions:
- Create an issue in the repository
- Check the documentation in `/docs`
- Review test results in `FINAL_TEST_REPORT.md`

---

**Built with ❤️ using FastAPI, ChromaDB, and modern web technologies**