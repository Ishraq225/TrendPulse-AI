# 📊 TrendPulse AI
### Social Media Trend Intelligence & Sentiment Analysis Platform

TrendPulse AI is a Python-based data analytics platform designed to explore social media discussions, analyze audience sentiment, identify popular topics, and visualize discussion patterns over time.

The project combines data collection, data preprocessing, sentiment analysis, and interactive visualization to transform raw social media text into meaningful insights.

> **Project Status:** Phase 2 Completed | Phase 3: Exploratory Data Analysis (Upcoming)

---

## 🎯 Project Objectives

- Collect and process publicly available social media datasets.
- Clean and standardize raw text data.
- Analyze positive, negative, and neutral sentiment.
- Identify frequently discussed topics.
- Explore platform-wise discussion patterns.
- Visualize sentiment and topic trends over time.
- Build an interactive analytics dashboard.

## ✨ Features

### 1. Data Collection
- Download public datasets using the Hugging Face Datasets library.
- Convert datasets into Pandas DataFrames.
- Preserve original downloaded data in CSV format.

### 2. Data Preprocessing
- Standardize column names.
- Handle missing text and platform values.
- Convert timestamps into datetime format.
- Remove invalid records and duplicate posts.
- Generate internal post identifiers.
- Save cleaned data separately from raw data.

### 3. Sentiment Analysis
- Analyze text using VADER Sentiment Analysis.
- Classify posts into:
  - 😊 Positive
  - 😞 Negative
  - 😐 Neutral

### 4. Interactive Dashboard
- Total post statistics.
- Sentiment distribution.
- Topic popularity.
- Sentiment trends over time.
- Platform-wise analysis.
- Interactive topic and platform filters.
- Downloadable analyzed dataset.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Streamlit | Interactive dashboard |
| Plotly | Data visualization |
| VADER | Sentiment analysis |
| Hugging Face Datasets | Dataset collection |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
TrendPulse-AI/
│
├── data/
│   ├── raw/
│   │   ├── sample_posts.csv
│   │   └── social_media_posts.csv
│   │
│   └── processed/
│       └── social_media_posts.csv
│
├── scripts/
│   └── collect_data.py
│
├── src/
│   └── data/
│       ├── __init__.py
│       └── prepare_data.py
│
├── notebooks/
│
├── dashboard/
│
├── reports/
│
├── tests/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📊 Dataset Information

The initial real-world data pipeline uses a publicly available Hugging Face dataset:

**Dataset:** [Hackathon Sentiment Analysis](https://huggingface.co/datasets/Tarakeshwaran/Hackathon_Sentiment_analysis)

### Current Dataset Statistics

| Metric | Value |
|---|---:|
| Original records | 732 |
| Processed records | 707 |
| Number of columns | 9 |
| Missing values in processed dataset | 0 |
| Platforms | 3 |

### Platform Distribution

| Platform | Records |
|---|---:|
| Instagram | 249 |
| Twitter | 235 |
| Facebook | 223 |

### Date Range

May 15, 2010 – October 22, 2023

**Note:** The dataset contains historical records and is used for analytical and educational purposes. It does not represent live social media activity.

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.12 recommended
- Git
- Visual Studio Code (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/Ishraq225/TrendPulse-AI.git

cd TrendPulse-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

### 4. Collect the Dataset

```bash
python scripts/collect_data.py
```

This downloads the dataset and saves the original records in:

```text
data/raw/social_media_posts.csv
```

### 5. Prepare the Dataset

```bash
python -m src.data.prepare_data
```

This cleans and standardizes the dataset and saves the output in:

```text
data/processed/social_media_posts.csv
```

### 6. Launch the Dashboard

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 🔍 Data Processing Workflow

```text
Public Hugging Face Dataset
           |
           v
     Data Collection
           |
           v
       Raw CSV File
           |
           v
    Data Preprocessing
           |
           v
   Cleaned Processed CSV
           |
           v
    Sentiment Analysis
           |
           v
   Interactive Dashboard
           |
           v
     Visual Insights
```

## 🗺️ Development Roadmap

| Phase | Description | Status |
|---|---|---|
| Phase 1 | Dashboard MVP and initial sentiment analysis | ✅ Completed |
| Phase 2 | Real-world dataset collection and preprocessing | ✅ Completed |
| Phase 3 | Exploratory Data Analysis (EDA) | 🔄 Upcoming |
| Phase 4 | Advanced NLP and sentiment analysis | ⏳ Planned |
| Phase 5 | Topic modeling and trend intelligence | ⏳ Planned |
| Phase 6 | Advanced dashboard and deployment | ⏳ Planned |

### Planned Improvements

- Advanced sentiment analysis using Transformer models.
- Topic extraction and topic modeling with BERTopic.
- Keyword frequency and hashtag analysis.
- Emerging topic detection.
- Time-based trend identification.
- Improved data quality and automated validation.
- Database integration using PostgreSQL.
- Cloud deployment.

## ⚠️ Limitations

- Current analysis uses a historical public dataset.
- VADER is a baseline sentiment analysis tool and may not understand sarcasm, context, or complex language.
- Hashtags are currently used as topic proxies where available.
- The application does not currently collect live social media posts.
- Identified patterns should not be interpreted as real-time public opinion.

## 👩‍💻 Author

**Ishraq Sajid**

BS Artificial Intelligence Student  
Bahria University, Karachi

- GitHub: [@Ishraq225](https://github.com/Ishraq225)
- LinkedIn: [Ishraq Sajid](https://www.linkedin.com/in/ishraq-sajid-44b372352/)

---

⭐ If you find this project interesting, consider giving the repository a star!

*Built as a hands-on Artificial Intelligence and Data Science portfolio project.*


<img width="1900" height="618" alt="image" src="https://github.com/user-attachments/assets/8be48db7-6daa-496d-8181-a16f8064520a" />
<img width="1407" height="607" alt="image" src="https://github.com/user-attachments/assets/ec351597-f742-4c90-8998-7afc989c7c2d" />
<img width="1392" height="617" alt="image" src="https://github.com/user-attachments/assets/20a96756-3d8f-4fd5-ba7f-cee89bacd354" />
<img width="1427" height="672" alt="image" src="https://github.com/user-attachments/assets/9d59160e-f1ed-46cc-ae5a-78060995ece3" />
<img width="1373" height="637" alt="image" src="https://github.com/user-attachments/assets/4076db48-a8cd-4fdb-82ca-cb07abe65a23" />
<img width="1387" height="631" alt="image" src="https://github.com/user-attachments/assets/0ee36a5c-6c2a-4ad3-8396-8ec3367639d6" />
