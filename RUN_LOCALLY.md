# 🚀 Run GRA Locally - Complete Guide

## ✅ Your System is NOW RUNNING!

**Backend**: http://localhost:8001 ✅ Running
**Frontend**: http://localhost:3000 ✅ Running

---

## 🌐 Open Your Application

### Click this link to test:
**http://localhost:3000**

Or copy-paste in your browser:
```
http://localhost:3000
```

---

## 🧪 Test the Application

### 1. Open the App
- Go to: http://localhost:3000
- You should see the GRA interface

### 2. Test Multi-Word Inputs

**Fill the form with these values**:

```
Location: Pune, Maharashtra
Farm Size: 5
Soil Type: Black Cotton
Water Source: Borewell
Budget: 100000
Experience Level: Intermediate

Current Crops (type exactly as shown):
rice, wheat, cotton, sugarcane

Climate Concerns (type exactly as shown):
drought, irregular rainfall, heat waves, water scarcity

Adaptation Goals (type exactly as shown):
increase yield, reduce water usage, improve soil health, climate resilience
```

### 3. Submit Form
- Click "🔍 Generate Climate Adaptation Plan"
- Wait 2-3 seconds
- ✅ You should see results!

### 4. Test AI Chat
- Click "🤖 AI Assistant" button (bottom right)
- Ask: "What crops are best for drought conditions?"
- Get response!

---

## 🛑 Stop the Servers

When you're done testing:

### Stop Frontend Server:
```powershell
# Press Ctrl+C in the terminal running frontend
# Or close the terminal window
```

### Stop Backend Server:
```powershell
# Press Ctrl+C in the terminal running backend
# Or close the terminal window
```

---

## 🔄 Restart Servers (If Needed)

### Start Backend:
```powershell
cd "C:\Users\shreyash\OneDrive\Desktop\New folder\gra-prototype\backend"
python main.py
```

### Start Frontend:
```powershell
cd "C:\Users\shreyash\OneDrive\Desktop\New folder\gra-prototype\frontend"
python -m http.server 3000
```

---

## 🤖 Add Gen AI (Optional)

Want AI-powered detailed analysis instead of rule-based?

### Step 1: Get OpenAI API Key
1. Go to: https://platform.openai.com/api-keys
2. Sign up (get $5 free credit)
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)

### Step 2: Add to Backend

```powershell
# Navigate to backend folder
cd "C:\Users\shreyash\OneDrive\Desktop\New folder\gra-prototype\backend"

# Create .env file with your API key
echo OPENAI_API_KEY=sk-your-actual-key-here > .env
```

### Step 3: Restart Backend

1. Stop backend (Ctrl+C)
2. Start again:
   ```powershell
   python main.py
   ```

### Step 4: Test
- Fill form and submit
- Check browser console (F12)
- Should see: "✨ Results powered by Gen AI"
- Get more detailed AI-powered analysis!

---

## 📊 What You're Running

### Backend (Port 8001)
- FastAPI server
- 4 AI agents (Climate, Crop, Market, Scheme)
- SQLite database
- RESTful API endpoints

### Frontend (Port 3000)
- React application
- Climate adaptation form
- AI chat assistant
- Results visualization
- Farm layout generator

---

## 🐛 Troubleshooting

### Frontend not loading?
**Check**:
- Is frontend server running? Look for "Serving HTTP on port 3000"
- Try: http://127.0.0.1:3000
- Try: http://localhost:3000

### Backend not responding?
**Check**:
- Is backend running? Visit: http://localhost:8001
- Should see: `{"message":"Climate Adaptation System API"}`
- If not, restart: `cd backend && python main.py`

### "Failed to fetch" error?
**Check**:
- Both servers running?
- Backend on port 8001?
- Frontend on port 3000?
- No firewall blocking?

### Multi-word inputs not working?
**Check**:
- Hard refresh browser (Ctrl+Shift+R)
- Clear browser cache
- Try incognito mode

### Port already in use?
**Backend (8001)**:
```powershell
# Find process using port 8001
netstat -ano | findstr :8001

# Kill process (replace PID with actual number)
taskkill /PID <PID> /F

# Or change port in backend/main.py
```

**Frontend (3000)**:
```powershell
# Use different port
python -m http.server 3001
# Then open: http://localhost:3001
```

---

## 📁 Project Structure

```
gra-prototype/
├── backend/
│   ├── main.py              ← Backend server (port 8001)
│   ├── agents/              ← AI agents
│   ├── database/            ← SQLite database
│   ├── services/            ← Gen AI service
│   └── data/                ← Knowledge base
├── frontend/
│   └── index.html           ← Frontend app (port 3000)
└── requirements.txt         ← Python dependencies
```

---

## 🎯 Quick Commands Reference

### Check if servers are running:
```powershell
# Check backend
Invoke-WebRequest -Uri http://localhost:8001 -UseBasicParsing

# Check frontend
Invoke-WebRequest -Uri http://localhost:3000 -UseBasicParsing
```

### Start backend:
```powershell
cd backend
python main.py
```

### Start frontend:
```powershell
cd frontend
python -m http.server 3000
```

### Install dependencies (if needed):
```powershell
pip install -r requirements.txt
```

### Test system:
```powershell
python test_system.py
```

---

## ✅ Success Checklist

- [x] Backend running on port 8001
- [x] Frontend running on port 3000
- [ ] Opened http://localhost:3000 in browser
- [ ] Tested multi-word inputs
- [ ] Filled complete form
- [ ] Submitted form successfully
- [ ] Saw results displayed
- [ ] Tested AI chat assistant
- [ ] (Optional) Added Gen AI API key

---

## 🌟 Features to Test

### 1. Multi-Word Input Fields ✏️
- Type: `basmati rice, durum wheat, bt cotton`
- Should accept spaces and commas

### 2. Climate Analysis 🌡️
- Get location-specific climate risks
- See adaptation strategies
- View urgency levels

### 3. Crop Recommendations 🌾
- AI-powered crop selection
- Yield projections
- Income estimates
- Seasonal calendar

### 4. Market Intelligence 📈
- Current prices
- Market trends
- Selling strategies

### 5. Government Schemes 🏛️
- Relevant subsidies
- Application process
- Document requirements
- Total potential savings

### 6. Farm Layout 🗺️
- Visual SVG diagram
- Crop placement
- Water source integration

### 7. AI Chat Assistant 🤖
- Real-time farming advice
- Contextual responses
- Detailed guidance

---

## 💡 Tips

1. **Keep both terminals open** while testing
2. **Check browser console** (F12) for debug info
3. **Use Ctrl+Shift+R** to hard refresh if changes don't appear
4. **Test without Gen AI first** to verify basic functionality
5. **Add Gen AI later** for enhanced analysis

---

## 🎉 You're All Set!

**Your GRA is running locally!**

- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:8001
- **Status**: ✅ Both servers running

**Next Steps**:
1. Open http://localhost:3000
2. Fill the form
3. Test multi-word inputs
4. Submit and see results!
5. Try the AI chat assistant

---

**Enjoy testing your Generative Resilience Agent! 🌱🤖**