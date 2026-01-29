# 🧠 ModelMind - Simple ML Debugger

AI-powered model debugging using Google Gemini.

## 📁 Project Structure

```
modelmind/
├── app.py                    # Streamlit UI
├── api.py                    # FastAPI server
├── requirements.txt          # Dependencies
├── .env.example              # Configuration template
│
├── ml_engine/
│   ├── model_parser.py       # Parse models (.h5, .pt, .pkl)
│   ├── training_analyzer.py  # Analyze training logs
│   ├── error_miner.py        # Detect issues
│   └── explainability.py     # Explain results
│
├── gemini_engine/
│   ├── prompts.py            # Gemini prompts
│   ├── reasoner.py           # Analyze with Gemini
│   ├── planner.py            # Plan experiments
│   └── reviewer.py           # Review analysis
│
├── report/
│   └── generate_report.py    # Generate reports
│
└── storage/
    ├── uploads/              # Uploaded models
    ├── outputs/              # Analysis outputs
    └── reports/              # Generated reports
```

## 🚀 Quick Start

### 1️⃣ Get Your Gemini API Key

- Visit: https://ai.google.dev/
- Click "Get API Key"
- Copy your key

### 2️⃣ Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add your API key:
# GEMINI_API_KEY=your_actual_key_here
```

### 3️⃣ Run

**Terminal 1 - Backend:**
```bash
python api.py
```

**Terminal 2 - Frontend:**
```bash
streamlit run app.py
```

Then visit: **http://localhost:8501**

## 🔑 Where to Put Your API Key

1. Open `.env` file
2. Find this line: `GEMINI_API_KEY=your-api-key-here`
3. Replace `your-api-key-here` with your actual Gemini API key
4. Save the file

Example:
```env
GEMINI_API_KEY=AIzaSyDxyz123abc456def789...
```

## ✨ Features

- ✅ Upload models (.h5, .pt, .pkl)
- ✅ Upload training logs (CSV, JSON, TXT)
- ✅ Automatic issue detection
- ✅ Gemini AI analysis
- ✅ Code improvements
- ✅ Experiment planning
- ✅ Generate reports
- ✅ Download results

## 📊 Workflow

1. **Upload** your model + logs
2. **Parse** model structure
3. **Detect** issues automatically
4. **Analyze** with Gemini AI
5. **Generate** improvements
6. **Plan** next experiments
7. **Export** report

## 🎯 What It Detects

- Too many layers (vanishing gradients)
- Loss divergence (bad learning)
- Overfitting patterns
- Data issues
- Architecture problems
- Hyperparameter issues

## 📝 Requirements

- Python 3.9+
- Google Gemini API key
- 2GB RAM
- Internet connection

## 🛠️ Technologies

- **Streamlit** - Web UI
- **FastAPI** - Backend API
- **Gemini** - AI Analysis
- **TensorFlow/PyTorch** - Model support
- **Pandas** - Data analysis

## 📚 File Descriptions

### ml_engine/
- **model_parser.py** - Reads TensorFlow, PyTorch, Pickle models
- **training_analyzer.py** - Analyzes training logs and metrics
- **error_miner.py** - Detects common ML issues
- **explainability.py** - Explains findings in simple terms

### gemini_engine/
- **prompts.py** - Templates for Gemini prompts
- **reasoner.py** - Analyzes models using Gemini
- **planner.py** - Plans next experiments
- **reviewer.py** - Reviews analysis quality

### report/
- **generate_report.py** - Creates formatted reports

## 🎉 That's It!

Your ModelMind is ready to debug ML models!

---

**Stop guessing. Start knowing. Let Gemini debug your models.** 🚀
