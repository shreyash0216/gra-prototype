# 🚀 Deploy Backend to Railway - Step by Step

## Why You Need This

Your Vercel deployment (https://gra-prototype.vercel.app) only hosts the **frontend**. 
The backend needs to be deployed separately to Railway.

---

## 🚂 Deploy to Railway (5 minutes)

### Step 1: Go to Railway
Open: https://railway.app

### Step 2: Sign Up/Login
- Click "Login"
- Choose "Login with GitHub"
- Authorize Railway

### Step 3: Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your repository: `shreyash0216/gra-prototype`
4. Click "Deploy Now"

### Step 4: Configure Build
Railway will auto-detect Python and use the `Procfile`:
```
web: cd backend && python main.py
```

### Step 5: Add Environment Variables (Optional - For Gen AI)

If you want AI-powered analysis:

1. In Railway dashboard, click on your project
2. Go to "Variables" tab
3. Click "New Variable"
4. Add:
   ```
   OPENAI_API_KEY=sk-your-openai-key-here
   ```
5. Click "Add"

**Get OpenAI Key**: https://platform.openai.com/api-keys

### Step 6: Get Your Backend URL

After deployment (2-3 minutes):
1. Go to "Settings" tab
2. Find "Domains" section
3. Click "Generate Domain"
4. Copy the URL (e.g., `https://your-app.railway.app`)

---

## 🔗 Connect Frontend to Backend

### Update Vercel Environment Variable

1. Go to Vercel dashboard: https://vercel.com/dashboard
2. Select your project: `gra-prototype`
3. Go to "Settings" → "Environment Variables"
4. Add new variable:
   ```
   Name: REACT_APP_API_BASE
   Value: https://your-railway-url.railway.app
   ```
5. Click "Save"
6. Go to "Deployments" tab
7. Click "..." on latest deployment
8. Click "Redeploy"

---

## ✅ Test Your Deployment

### Test Backend
Visit: `https://your-railway-url.railway.app`

Should see:
```json
{
  "message": "Climate Adaptation System API",
  "version": "1.0.0"
}
```

### Test Frontend
Visit: `https://gra-prototype.vercel.app`

1. Fill the form
2. Submit
3. Should work without "Failed to fetch" error!

---

## 🐛 Troubleshooting

### Railway deployment failed
- Check logs in Railway dashboard
- Verify `Procfile` exists
- Check `requirements.txt` is complete

### Backend URL not working
- Wait 2-3 minutes for deployment
- Check Railway logs for errors
- Verify domain is generated

### Frontend still shows error
- Verify environment variable in Vercel
- Redeploy Vercel after adding variable
- Check browser console for actual URL being called

---

## 💰 Cost

### Railway Free Tier
- $5 free credit per month
- Enough for ~500 hours of runtime
- Perfect for testing and small projects

### If you exceed free tier
- Pay-as-you-go: ~$0.000463 per minute
- ~$20/month for 24/7 uptime

---

## 🎯 Quick Alternative: Test Locally

Don't want to deploy backend yet? Test locally:

### Option A: Open Local File
```
file:///C:/Users/shreyash/OneDrive/Desktop/New folder/gra-prototype/frontend/index.html
```

### Option B: Local Server
```bash
cd gra-prototype/frontend
python -m http.server 3000
```
Then open: http://localhost:3000

Backend is already running on: http://localhost:8001

---

## 📊 Summary

**Current Status**:
- ✅ Frontend deployed to Vercel
- ✅ Backend running locally
- ❌ Backend not deployed (causing "Failed to fetch")

**Solution**:
1. Deploy backend to Railway (5 minutes)
2. Connect Vercel to Railway URL
3. Everything works!

**Or**:
- Test locally (works now!)

---

**Choose your path and your GRA will be fully functional! 🌱🤖**