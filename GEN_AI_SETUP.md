# 🤖 Gen AI Setup Guide

## Enable AI-Powered Analysis

GRA can use real Gen AI (OpenAI GPT or Anthropic Claude) for dynamic, intelligent responses instead of rule-based fallbacks.

---

## 🚀 Quick Setup

### Option 1: OpenAI (Recommended)

1. **Get API Key**
   - Go to https://platform.openai.com/api-keys
   - Sign up or login
   - Create new API key
   - Copy the key

2. **Configure Backend**
   ```bash
   cd gra-prototype/backend
   cp ../.env.example .env
   ```

3. **Add API Key to .env**
   ```bash
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

4. **Install Dependencies**
   ```bash
   pip install openai==1.3.0
   ```

5. **Restart Backend**
   ```bash
   python main.py
   ```

### Option 2: Anthropic Claude

1. **Get API Key**
   - Go to https://console.anthropic.com/
   - Sign up or login
   - Create API key
   - Copy the key

2. **Configure Backend**
   ```bash
   cd gra-prototype/backend
   cp ../.env.example .env
   ```

3. **Add API Key to .env**
   ```bash
   ANTHROPIC_API_KEY=your-anthropic-api-key-here
   ```

4. **Install Dependencies**
   ```bash
   pip install anthropic==0.7.0
   ```

5. **Restart Backend**
   ```bash
   python main.py
   ```

---

## 🧪 Testing Gen AI

### Test Climate Analysis

```bash
curl -X POST http://localhost:8001/analyze-climate \
  -H "Content-Type: application/json" \
  -d '{
    "farm_details": {
      "location": "Pune, Maharashtra",
      "farm_size": 5.0,
      "soil_type": "black",
      "water_source": "borewell",
      "current_crops": ["rice"],
      "budget": 100000,
      "experience_level": "intermediate"
    },
    "climate_concerns": ["drought"],
    "adaptation_goals": ["increase yield"]
  }'
```

Look for `"ai_powered": true` in the response!

### Test AI Chat

```bash
curl -X POST http://localhost:8001/ai-chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What crops are best for drought conditions?",
    "context": {"location": "Pune, Maharashtra"}
  }'
```

---

## 💰 Cost Considerations

### OpenAI Pricing (GPT-3.5-turbo)
- **Input**: $0.0015 per 1K tokens
- **Output**: $0.002 per 1K tokens
- **Average analysis**: ~$0.01-0.05 per request
- **Monthly estimate**: $10-50 for 1000 analyses

### Anthropic Pricing (Claude Haiku)
- **Input**: $0.00025 per 1K tokens
- **Output**: $0.00125 per 1K tokens
- **Average analysis**: ~$0.005-0.02 per request
- **Monthly estimate**: $5-20 for 1000 analyses

### Free Tier
- OpenAI: $5 free credit for new accounts
- Anthropic: Contact for trial credits

---

## 🔧 Configuration Options

### Environment Variables

```bash
# Required: Choose one
OPENAI_API_KEY=your_key_here
# OR
ANTHROPIC_API_KEY=your_key_here

# Optional: Database
DATABASE_URL=sqlite:///./climate_adaptation.db

# Optional: Server
PORT=8001
```

### Model Selection

Edit `backend/services/gen_ai_service.py`:

```python
# For OpenAI
self.model = "gpt-3.5-turbo"  # Fast & cheap
# OR
self.model = "gpt-4"  # More intelligent but expensive

# For Anthropic
self.model = "claude-3-haiku-20240307"  # Fast & cheap
# OR
self.model = "claude-3-sonnet-20240229"  # Balanced
# OR
self.model = "claude-3-opus-20240229"  # Most intelligent
```

---

## 🎯 What Gen AI Improves

### With Gen AI Enabled:
✅ **Dynamic Analysis** - Adapts to specific farm conditions
✅ **Contextual Recommendations** - Considers local factors
✅ **Natural Language** - More conversational responses
✅ **Up-to-date Knowledge** - Latest farming practices
✅ **Personalized Advice** - Tailored to farmer's experience
✅ **Complex Reasoning** - Better problem-solving

### Without Gen AI (Fallback):
📊 **Rule-based Analysis** - Predefined logic
📊 **Template Responses** - Fixed patterns
📊 **Static Knowledge** - Hardcoded data
📊 **General Advice** - Less personalized

---

## 🐛 Troubleshooting

### "No AI service available"
- Check if API key is set in .env
- Verify .env file is in backend/ directory
- Restart the backend server

### "API key invalid"
- Verify key is correct (no extra spaces)
- Check if key has proper permissions
- Ensure billing is set up (for OpenAI)

### "Rate limit exceeded"
- Wait a few minutes
- Upgrade to paid tier
- Implement request caching

### "Module not found: openai/anthropic"
```bash
pip install openai==1.3.0 anthropic==0.7.0
```

---

## 🚀 Deployment with Gen AI

### Vercel
Add environment variable in Vercel dashboard:
```
OPENAI_API_KEY=your_key_here
```

### Railway
Add environment variable in Railway dashboard:
```
OPENAI_API_KEY=your_key_here
```

### Heroku
```bash
heroku config:set OPENAI_API_KEY=your_key_here
```

---

## 📊 Monitoring Usage

### OpenAI Dashboard
- View usage: https://platform.openai.com/usage
- Set spending limits
- Monitor costs

### Anthropic Console
- View usage: https://console.anthropic.com/
- Track API calls
- Monitor costs

---

## 🔒 Security Best Practices

1. **Never commit API keys** to Git
2. **Use environment variables** for all keys
3. **Rotate keys regularly** (every 90 days)
4. **Set spending limits** to avoid surprises
5. **Monitor usage** for unusual activity
6. **Use separate keys** for dev/prod

---

## 💡 Tips for Best Results

1. **Be Specific** - Provide detailed farm information
2. **Use Context** - Include location and climate data
3. **Set Clear Goals** - Define what you want to achieve
4. **Iterate** - Refine based on AI responses
5. **Validate** - Cross-check AI recommendations with local experts

---

## 🎓 Learning Resources

### OpenAI
- Documentation: https://platform.openai.com/docs
- Best Practices: https://platform.openai.com/docs/guides/production-best-practices
- Community: https://community.openai.com/

### Anthropic
- Documentation: https://docs.anthropic.com/
- Prompt Engineering: https://docs.anthropic.com/claude/docs/prompt-engineering
- Support: https://support.anthropic.com/

---

**Your GRA system is now powered by cutting-edge Gen AI! 🤖✨**