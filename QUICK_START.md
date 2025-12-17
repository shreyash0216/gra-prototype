# 🚀 Quick Start Guide - GRA with Gen AI

## Get Your System Running in 5 Minutes

### Step 1: Get an OpenAI API Key (2 minutes)

1. Go to https://platform.openai.com/api-keys
2. Sign up (free $5 credit for new users)
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)

### Step 2: Configure Backend (1 minute)

```bash
cd gra-prototype/backend

# Create .env file
echo "OPENAI_API_KEY=sk-your-actual-key-here" > .env
```

### Step 3: Install Dependencies (1 minute)

```bash
# Install Python packages
pip install -r ../requirements.txt
```

### Step 4: Start Backend (30 seconds)

```bash
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8001
🤖 Using Gen AI for analysis...
```

### Step 5: Open Frontend (30 seconds)

Open `frontend/index.html` in your browser

---

## 🧪 Test Gen AI

### Test 1: AI Chat
1. Click the "🤖 AI Assistant" button (bottom right)
2. Ask: "What crops are best for drought conditions?"
3. Get real AI response!

### Test 2: Full Analysis
1. Fill the form:
   - Location: `Pune, Maharashtra`
   - Farm Size: `5`
   - Soil: `Black Cotton`
   - Water: `Borewell`
   - Budget: `100000`
   - Crops: `rice, wheat`
   - Concerns: `drought, irregular rainfall`
   - Goals: `increase yield, reduce water usage`

2. Click "Generate Climate Adaptation Plan"
3. Wait 10-15 seconds
4. Get AI-powered recommendations!

---

## ✅ Verify Gen AI is Working

Check the backend console for:
```
🤖 Using Gen AI for analysis...
```

Check the browser console for:
```
✨ Results powered by Gen AI
```

If you see these, Gen AI is working! 🎉

---

## 💰 Cost Estimate

- **Per Analysis**: ~$0.02-0.05
- **Per Chat**: ~$0.001-0.005
- **100 Analyses**: ~$2-5
- **Free Credit**: $5 (100-250 analyses)

---

## 🐛 Troubleshooting

### "No AI service available"
```bash
# Check if .env file exists
cat backend/.env

# Should show:
OPENAI_API_KEY=sk-...
```

### "Invalid API key"
- Verify key is correct
- No extra spaces
- Starts with `sk-`

### "Rate limit exceeded"
- Wait 1 minute
- Check usage at https://platform.openai.com/usage

---

## 🎯 What You Get with Gen AI

### AI-Powered Analysis:
✅ Dynamic crop recommendations based on your specific conditions
✅ Contextual climate risk assessment
✅ Personalized adaptation strategies
✅ Natural language explanations
✅ Up-to-date farming practices

### Without Gen AI (Fallback):
📊 Rule-based recommendations
📊 Template responses
📊 Static knowledge base

---

## 🚀 Deploy with Gen AI

### Vercel
1. Deploy frontend to Vercel
2. Add environment variable:
   ```
   OPENAI_API_KEY=sk-your-key
   ```

### Railway (Backend)
1. Deploy backend to Railway
2. Add environment variable:
   ```
   OPENAI_API_KEY=sk-your-key
   ```

---

## 📚 Next Steps

1. ✅ Test locally with Gen AI
2. ✅ Deploy to production
3. ✅ Monitor usage and costs
4. ✅ Collect user feedback
5. ✅ Iterate and improve

---

**Your Gen AI-powered GRA is ready to help farmers! 🌱🤖**

For detailed setup, see [GEN_AI_SETUP.md](GEN_AI_SETUP.md)