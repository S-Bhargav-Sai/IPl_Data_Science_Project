# 🏏 CricPulse — AI Powered T20 Prediction & Strategy Engine

CricPulse is an end-to-end data science + machine learning + deployment project that predicts:
- Pre-match winner prediction
- Live ball-by-ball win probability
- Player role clustering (Aggressor, Anchor, Finisher etc.)
- Venue & matchup insights for strategy

This project demonstrates the **complete data science lifecycle**:
> Raw data → ETL → Analytics → ML → API → Dashboard → Deployment

---

## 🚀 Key Features

### ✅ Data Engineering (ETL + Data Warehousing)
- Collected ball-by-ball match data from **Cricsheet**
- Scraped player stats from **ESPNcricinfo** using BeautifulSoup
- Cleaned, merged, standardized and structured datasets
- Stored processed data into SQLite/PostgreSQL

### ✅ Exploratory Data Analysis (EDA)
- Venue scoring patterns (powerplay vs death overs)
- Batter vs bowler matchup strengths
- Player role identification using clustering (K-Means + PCA)

### ✅ Machine Learning Models
| Model | Type | Purpose |
|--------|------|----------|
| Winner Prediction Model | Supervised (XGBoost/LightGBM) | Predict match winner before start |
| Live Win Probability Model | Supervised | Updates probability after every ball |
| Player Archetype Model | Unsupervised (K-Means) | Aggressor / Anchor / Finisher roles |

### ✅ Deployment
- Backend API using **FastAPI**
- Streamlit dashboard UI
- REST endpoints: `/predict_winner`, `/live_win_probability`
- Version control & reproducibility with Git + Docker

---

## 📂 Folder Structure

CricPulse/
│
├── data/ # Cleaned datasets
├── data_viz/ # Visualization exports
├── db/
│ ├── schema.sql # Database schema
│ └── ipl_stats.db # SQLite DB (generated)
│
├── deployment/
│ ├── api.py # FastAPI backend
│ ├── dashboard.py # Streamlit application
│ └── schemas.py # Request/Response models
│
├── models/ # ML models (joblib/pkl files)
│
├── notebooks/ # Jupyter notebooks (EDA + ML)
│
├── scripts/
│ ├── build_db.py # ETL → DB builder
│ └── schema.sql # Table structure
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 🛠️ How to Run

### 1️⃣ Clone the repository
```sh
git clone <repo-url>
cd CricPulse
2️⃣ Install dependencies

pip install -r requirements.txt
3️⃣ Build database

python scripts/build_db.py
4️⃣ Open Jupyter notebooks for analysis

jupyter notebook
5️⃣ Launch the dashboard

streamlit run deployment/dashboard.py
📊 Deliverables
✅ Clean datasets
✅ SQLite database
✅ Machine learning models
✅ Streamlit dashboard + FastAPI backend

🔧 Tech Stack
Area	Tools Used
Data Cleaning	Python (Pandas, NumPy)
Database	SQLite / PostgreSQL
ML Models	Scikit-learn, XGBoost, LightGBM
Visualization	Tableau / Plotly / Streamlit
Deployment	FastAPI + Streamlit
Version Control	Git & GitHub

📬 Contact
Bhargav Sai Sanapala
GitHub: https://github.com/S-Bhargav-Sai
LinkedIn: https://www.linkedin.com/in/s-bhargav-sai-6073b6293/

yaml
Copy code

---

### ✅ After saving the cleaned README.md

Run these commands:

```sh
git add README.md
git add requirements.txt   # (if conflict existed)
git commit -m "Resolved merge conflicts and finalized README.md"
git push origin main