# 🧪 Test Locally - Quick Guide

## ✅ Your Backend is Already Running!

Your backend is running on: **http://localhost:8001**

---

## 🚀 Option 1: Open Frontend File Directly

**Easiest way to test right now:**

1. Open File Explorer
2. Navigate to: `C:\Users\shreyash\OneDrive\Desktop\New folder\gra-prototype\frontend`
3. Double-click `index.html`
4. Your browser will open the file
5. ✅ Fill the form and test!

**Direct path**:
```
file:///C:/Users/shreyash/OneDrive/Desktop/New folder/gra-prototype/frontend/index.html
```

---

## 🚀 Option 2: Use Local Web Server

**Better for testing (avoids CORS issues):**

```bash
# Open PowerShell in frontend folder
cd "C:\Users\shreyash\OneDrive\Desktop\New folder\gra-prototype\frontend"

# Start simple web server
python -m http.server 3000
```

Then open in browser: **http://localhost:3000**

---

## 🧪 Test the System

### 1. Test Multi-Word Inputs

**Current Crops**:
- Type: `basmati rice, durum wheat, bt cotton`
- ✅ Should accept spaces and commas

**Climate Concerns**:
- Type: `severe drought, irregular rainfall, extreme heat waves`
- ✅ Should work perfectly

**Adaptation Goals**:
- Type: `maximize crop yield, minimize water consumption, improve soil health`
- ✅ Should accept all text

### 2. Fill Complete Form

```
Location: Pune, Maharashtra
Farm Size: 5
Soil Type: Black Cotton
Water Source: Borewell
Budget: 100000
Experience: Intermediate
Current Crops: rice, wheat, cotton
Climate Concerns: drought, irregular rainfall, heat waves
Adaptation Goals: increase yield, reduce water usage, improve soil health
```

### 3. Submit and Check Results

Click "Generate Climate Adaptation Plan"

**Expected**:
- ✅ Loading indicator shows
- ✅ Results appear in 2-3 seconds
- ✅ See crop recommendations
- ✅ See government schemes
- ✅ See cost analysis
- ℹ️ May see notice about Gen AI (normal without API key)

---

## 🤖 Add Gen AI (Optional)

Want AI-powered detailed analysis?

### Step 1: Get OpenAI API Key
1. Go to: https://platform.openai.com/api-keys
2. Sign up (get $5 free credit)
3. Create new key
4. Copy the key (starts with `sk-...`)

### Step 2: Add to Backend

```bash
# Navigate to backend folder
cd "C:\Users\shreyash\OneDrive\Desktop\New folder\gra-prototype\backend"

# Create .env file
echo OPENAI_API_KEY=sk-your-actual-key-here > .env
```

### Step 3: Restart Backend

1. Stop current backend (Ctrl+C in the terminal)
2. Start again:
   ```bash
   python main.py
   ```

### Step 4: Test Again

Fill form and submit. You should see:
- ✅ "✨ Results powered by Gen AI" in console
- ✅ More detailed analysis
- ✅ No "rule-based" notice

---

## 🌐 For Live Site (Vercel)

The live site (https://gra-prototype.vercel.app) won't work yet because:
- ❌ Backend not deployed
- ❌ Only frontend is on Vercel

**To fix**:
1. Deploy backend to Railway (see DEPLOY_BACKEND.md)
2. Connect Vercel to Railway URL
3. Then live site will work!

---

## 🐛 Troubleshooting

### "Failed to fetch" error
**Check**:
- Is backend running? Visit: http://localhost:8001
- Should see: `{"message": "Climate Adaptation System API"}`
- If not, restart backend: `cd backend && python main.py`

### Backend not starting
**Check**:
- Python installed? `python --version`
- Dependencies installed? `pip install -r requirements.txt`
- Port 8001 available? Try different port in main.py

### Form not submitting
**Check**:
- All required fields filled?
- Browser console for errors (F12)
- Network tab shows request to localhost:8001?

### Multi-word inputs not working
**Check**:
- Hard refresh browser (Ctrl+Shift+R)
- Clear cache
- Try incognito mode

---

## ✅ Quick Checklist

- [x] Backend running on localhost:8001
- [ ] Frontend opened (file or localhost:3000)
- [ ] Multi-word inputs tested
- [ ] Form filled completely
- [ ] Form submitted successfully
- [ ] Results displayed
- [ ] (Optional) Gen AI configured

---

## 📊 What You're Testing

### Without Gen AI:
- ✅ Multi-word input fields
- ✅ Form submission
- ✅ Rule-based analysis
- ✅ Crop recommendations
- ✅ Government schemes
- ✅ Cost calculations
- ✅ Farm layout SVG

### With Gen AI:
- ✅ All above features
- ✅ AI-powered detailed analysis
- ✅ Contextual recommendations
- ✅ Natural language responses
- ✅ Personalized advice

---

## 🎯 Summary

**Current Status**:
- ✅ Backend running locally (port 8001)
- ✅ Frontend ready to test
- ✅ Multi-word inputs fixed
- ✅ System functional

**Test Now**:
1. Open: `frontend/index.html` in browser
2. Fill form with multi-word inputs
3. Submit and see results!

**For Live Site**:
- Deploy backend to Railway
- See DEPLOY_BACKEND.md

---

**Your GRA is ready to test locally! 🌱🤖**

Backend: http://localhost:8001
Frontend: Open `frontend/index.html` in browser