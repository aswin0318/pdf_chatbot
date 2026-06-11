# 🤖 PDF Chatbot - Setup Guide

## ✅ Problem Solved!

The chatbot now uses **Groq API** instead of HuggingFace Endpoint, which:
- ✨ Has **NO SSL certificate issues**
- ⚡ Is **much faster** (300+ req/sec)
- 💰 Is **completely FREE**
- 🎯 Uses powerful models like **Mixtral-8x7b**

---

## 🚀 Quick Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Get Your API Keys

#### Groq API Key (Required - for the chatbot)
1. Go to: https://console.groq.com/keys
2. Sign up with Google or email (takes 1 minute)
3. Create an API key
4. Copy the key

#### HuggingFace API Key (Optional - for PDF support)
1. Go to: https://huggingface.co/settings/tokens
2. Sign up or log in
3. Create a new token (read access is fine)
4. Copy the token

### Step 3: Create `.env` file
In your project root (same folder as `main.py`), create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
HF_API_KEY=your_huggingface_api_key_here
```

### Step 4: Run the App
```bash
python main.py
```
or with uvicorn:
```bash
uvicorn main:app --reload
```

Visit: http://localhost:8000

---

## 🎨 What Changed

| Before | Now |
|--------|-----|
| HuggingFace Endpoint | **Groq API** ✅ |
| SSL Certificate Errors | **No SSL issues** ✅ |
| Slow inference | **Ultra-fast** ✅ |
| Limited free tier | **Fully FREE** ✅ |
| TinyLlama model | **Mixtral-8x7b** ✅ |

---

## 📝 Features

✅ Chat without PDF (general Q&A)
✅ Upload PDF for enhanced responses
✅ Clean, modern UI with animations
✅ Typing indicator
✅ Message history
✅ Error handling

---

## 🆘 Troubleshooting

### "GROQ_API_KEY not set"
→ Make sure you created `.env` file with your keys

### "Connection error"
→ Check your internet connection and API key validity

### "Rate limit"
→ Groq has very generous limits (free tier is sufficient)

---

## 📚 Model Info

**Mixtral-8x7b-32768** (Default)
- Excellent quality
- Fast responses
- Good for both chat and reasoning

Other available models:
- `llama-2-70b-chat`
- `gemma-7b-it`

---

Enjoy your chatbot! 🎉
