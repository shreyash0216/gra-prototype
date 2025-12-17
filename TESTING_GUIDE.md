# 🧪 GRA Prototype Testing Guide

## Quick Test Checklist

### ✅ System Status
- [x] Backend server running on http://localhost:8000
- [x] All API endpoints responding
- [x] Sample data loaded successfully
- [x] All 6 automated tests passed

## 🌐 Frontend Testing (Browser)

### 1. Open the Frontend
- Navigate to `frontend/index.html` in your browser
- You should see a modern interface with two main sections

### 2. Test Query Interface (Left Side)

#### Basic Query Test:
1. **Load Sample Data**: Click "Load Sample Data" button (bottom)
2. **Enter Query**: Type `"What is RAG and how does it work?"`
3. **Select Template**: Choose "Default"
4. **Submit**: Click "Submit Query"
5. **Expected**: You should get a response about RAG systems

#### Template Testing:
1. Try the same query with different templates:
   - **Analytical**: More structured, data-driven response
   - **Creative**: More innovative, brainstorming approach
   - **Technical**: Detailed implementation focus
   - **Summarization**: Concise, key points format

#### Context Testing:
1. Add context: `"I'm building an AI system for agriculture"`
2. Ask: `"How can I implement climate adaptation features?"`
3. **Expected**: Response should incorporate your context

### 3. Test Simulation Center (Right Side)

#### Basic Query Simulation:
1. **Select**: "Basic Query Test"
2. **Set Parameters**: 
   - Query Count: 5
   - Delay: 0.1 seconds
3. **Run**: Click "Run Simulation"
4. **Expected**: Performance metrics showing success rate, response times

#### Stress Test:
1. **Select**: "Stress Test"
2. **Set Parameters**:
   - Concurrent Users: 3
   - Queries per User: 10
3. **Run**: Click "Run Simulation"
4. **Expected**: Load testing results with failure rates, resource usage

#### Context Switching Test:
1. **Select**: "Context Switching"
2. **Set**: Context Switches: 5
3. **Run**: Click "Run Simulation"
4. **Expected**: Context switching performance and accuracy metrics

#### Knowledge Gap Analysis:
1. **Select**: "Knowledge Gap Analysis"
2. **Set Parameters**:
   - Query Count: 10
   - Knowledge Coverage: 0.7
3. **Run**: Click "Run Simulation"
4. **Expected**: Analysis of knowledge availability and confidence scores

## 🔧 API Testing (Command Line)

### Health Check
```bash
curl http://localhost:8000/
```
**Expected**: `{"message":"GRA Prototype API is running"}`

### Query Test
```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query":"What is simulation testing?","context":"I need to validate my system"}'
```

### Simulation Test
```bash
curl -X POST http://localhost:8000/simulate \
  -H "Content-Type: application/json" \
  -d '{"scenario_type":"basic_query","parameters":{"query_count":3,"delay":0.1}}'
```

### List Scenarios
```bash
curl http://localhost:8000/scenarios
```

## 🎯 Expected Results

### Query Responses Should Include:
- **Response**: Generated text based on your query and context
- **Context**: Retrieved relevant documents from the knowledge base
- **Proper formatting**: Clean, readable responses

### Simulation Results Should Show:
- **Performance Metrics**: Response times, success rates
- **Resource Usage**: Memory, CPU utilization (for stress tests)
- **Quality Metrics**: Accuracy scores, confidence levels
- **Detailed Breakdown**: Individual query results

## 🚨 Troubleshooting

### If Frontend Doesn't Load:
1. Check if `frontend/index.html` exists
2. Try opening directly in browser
3. Check browser console for errors

### If API Calls Fail:
1. Verify backend is running: `http://localhost:8000/`
2. Check for CORS errors in browser console
3. Ensure sample data is loaded

### If Simulations Don't Work:
1. Load sample data first
2. Check parameter values are valid
3. Try simpler scenarios first (basic_query)

## 🎉 Success Indicators

### ✅ Working System Shows:
- Fast response times (< 3 seconds)
- High success rates (> 95%)
- Relevant context retrieval
- Proper error handling
- Responsive UI interactions

### 📊 Performance Benchmarks:
- **Query Response**: < 2 seconds
- **Basic Simulation**: < 5 seconds
- **Stress Test**: Handles 50+ concurrent queries
- **Context Switching**: < 15% accuracy drop

## 🔄 Continuous Testing

### Regular Checks:
1. Run `python test_system.py` daily
2. Test new queries weekly
3. Monitor performance trends
4. Update sample data monthly

### Load Testing:
1. Gradually increase concurrent users
2. Test with larger datasets
3. Monitor memory usage
4. Check response time degradation

---

**🎯 Your system is ready for production testing!**

All automated tests passed, indicating your GRA prototype is functioning correctly and ready for real-world scenarios.