# Deployment Guide - Climate Adaptation System

## 🚀 Recommended Deployment Strategy

### Frontend (Vercel) + Backend (Railway)

This approach gives you the best performance and reliability:

#### Step 1: Deploy Frontend to Vercel

1. **Go to Vercel**
   - Visit: https://vercel.com
   - Sign up/Login with GitHub

2. **Import Project**
   - Click "New Project"
   - Select your `gra-prototype` repository
   - Click "Import"

3. **Configure Deployment**
   - Framework Preset: **Other**
   - Root Directory: **Leave empty**
   - Build Command: **Leave empty**
   - Output Directory: **frontend**

4. **Deploy Frontend**
   - Click "Deploy"
   - Get your frontend URL (e.g., `https://your-app.vercel.app`)

#### Step 2: Deploy Backend to Railway

1. **Go to Railway**
   - Visit: https://railway.app
   - Sign up/Login with GitHub

2. **Deploy Backend**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `gra-prototype` repository
   - Railway will auto-detect Python and deploy

3. **Get Backend URL**
   - After deployment, get your backend URL (e.g., `https://your-backend.railway.app`)

#### Step 3: Connect Frontend to Backend

1. **Update Frontend Configuration**
   - Go to your Vercel project settings
   - Add environment variable: `REACT_APP_API_BASE=https://your-backend.railway.app`
   - Redeploy frontend

## 🌐 Alternative: All-in-One Deployment

### Method 2: Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy from project directory
cd gra-prototype
vercel

# Follow the prompts
```

## 🌐 Alternative Deployment Options

### Railway (Backend + Database)

1. Go to https://railway.app
2. Connect GitHub repository
3. Deploy backend as a service
4. Add environment variables if needed

### Netlify (Frontend Only)

1. Go to https://netlify.com
2. Drag and drop the `frontend` folder
3. Update API_BASE to point to your backend URL

### Heroku (Full Stack)

```bash
# Install Heroku CLI
# Create Procfile
echo "web: cd backend && python main.py" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

## 🔧 Environment Configuration

### Required Environment Variables

```bash
# Optional - defaults work for basic deployment
DATABASE_URL=sqlite:///./climate_adaptation.db
PORT=8000
```

### For Production

```bash
# Use PostgreSQL for production
DATABASE_URL=postgresql://user:password@host:port/database

# Add API keys for real LLM integration
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
```

## 📱 Testing Deployment

After deployment, test these endpoints:

1. **Frontend**: `https://your-app.vercel.app`
2. **API Health**: `https://your-app.vercel.app/api/`
3. **Crops Data**: `https://your-app.vercel.app/api/crops`
4. **Schemes Data**: `https://your-app.vercel.app/api/schemes`

## 🐛 Troubleshooting

### Common Issues

1. **Build Fails**
   - Check Python version (use 3.9+ for Vercel)
   - Verify requirements.txt has all dependencies

2. **API Not Working**
   - Check CORS settings in backend/main.py
   - Verify API routes in vercel.json

3. **Database Issues**
   - SQLite works for demo, use PostgreSQL for production
   - Check file permissions for SQLite

### Debug Commands

```bash
# Test locally
cd backend && python main.py
# Open frontend/index.html in browser

# Check logs
vercel logs your-deployment-url
```

## 🎯 Production Checklist

- [ ] Environment variables configured
- [ ] Database migrated (if using PostgreSQL)
- [ ] CORS settings updated for production domain
- [ ] API rate limiting implemented
- [ ] Error monitoring setup (Sentry, etc.)
- [ ] SSL certificate configured
- [ ] Custom domain setup (optional)

## 📊 Performance Optimization

1. **Frontend**
   - Enable gzip compression
   - Optimize images and assets
   - Use CDN for static files

2. **Backend**
   - Add Redis for caching
   - Implement database connection pooling
   - Add API rate limiting

3. **Database**
   - Add database indexes
   - Optimize queries
   - Regular backups

---

**Your Climate Adaptation System is now live and helping farmers worldwide! 🌱**