# 🏏 CricPulse — AI Powered T20 Prediction & Strategy Engine

CricPulse is an end-to-end data science + machine learning + deployment project that predicts:
- Pre-match winner prediction  
- Live ball-by-ball win probability  
- Player role clustering (Aggressor, Anchor, Finisher etc.)  
- Venue and matchup insights for decision-making  

This project demonstrates the **complete data science lifecycle**:
> Raw cricket data → ETL → Analytics → ML → API → Dashboard → Deployment

---

## 🚀 Key Features

### ✅ Data Engineering (ETL + Data Warehousing)
- Collected ball-by-ball match data from **Cricsheet**
- Scraped player stats from **ESPNcricinfo** using BeautifulSoup
- Created a unified dataset (merged, cleaned, structured)
- Stored processed data into a database (**SQLite/PostgreSQL**)

### ✅ Exploratory Data Analysis (EDA)
- Venue scoring patterns (average runs, death overs impact, etc.)
- Batter vs bowler matchup strengths (dot %, strike rate, six %)
- Player role identification using clustering (K-Means + PCA)

### ✅ Machine Learning Models
| Model | Type | Purpose |
|--------|------|----------|
| **Winner Prediction Model** | Supervised (XGBoost/LightGBM) | Predict match winner before start |
| **Live Win Probability Model** | Supervised ML | Updates probability after every ball |
| **Player Archetype Model** | Unsupervised (K-Means clustering) | Identifies player type (Anchor, Finisher, etc.) |

### ✅ Deployment
- Backend API built with **FastAPI**
- Web dashboard built using **Streamlit**
- Model served through REST endpoints (`/predict_winner`, `/live_win_probability`)
- Version control & containerization using Git + Docker

---

## 📂 Folder Structure
IPL/
│
├── data/
│ └── final_clean_data/ # Cleaned datasets used for analytics
│
├── data_viz/ # Visualization exports (Tableau screenshots / charts if needed)
│
├── db/
│ ├── schema.sql # Database schema (table definitions)
│ └── ipl.db (Generated) # SQLite DB (created after running script)
│
├── deployment/ # Streamlit/Flask app (optional deployment)
│
├── models/ # ML models (if applied, like prediction models)
│
├── notebooks/ # Jupyter notebooks for EDA & analysis
│
├── scripts/
│ ├── build_db.py # Python script to generate DB from CSVs
│ └── schema.sql # Database schema file
│
├── .gitignore # Ignoring unnecessary temporary files
│
├── IPL_Insights_Dashboard.twbx # Tableau dashboard packaged workbook
│
└── README.md # Documentation (you are reading it)



---

## 🚀 How to Run the Project

### **1. Clone the Repository**
```sh
git clone <repo-url>
cd IPL
2. Install Dependencies
Ensure Python 3.8+ is installed.

sh
Copy code
pip install -r requirements.txt

3. Build the Database
python scripts/build_db.py


This will:

Read cleaned CSVs from data/final_clean_data/

Create a SQLite database (ipl.db)

Load data into tables defined in schema.sql

4. Run Analysis

Open notebooks and explore insights:

notebooks/
    EDA.ipynb
    player_performance.ipynb

5. View Dashboard

Open IPL_Insights_Dashboard.twbx in Tableau Desktop:

Interactive insights for teams, players, venues, toss impact, etc.

📊 Insights Generated

Examples of insights found:

Best performing teams across seasons.

Impact of toss decisions on match outcomes.

Venue-wise win probability.

Most consistent players (runs, strike rate, wicket-taking trends).

🔧 Tools & Technologies Used
Area	Tools
Data Cleaning	Python (Pandas, NumPy)
Database	SQLite, SQL
Visualization	Tableau
Optional Deployment	Streamlit / Flask
Version Control	Git & GitHub
🏁 Final Deliverables

✔ Clean datasets
✔ SQLite database populated using Python
✔ Jupyter notebooks with detailed analysis
✔ Tableau dashboard with IPL insights

📬 Contact

If you find this useful or want collaboration, reach out anytime!
Github:https://github.com/S-Bhargav-Sai
LinkedIn:https://www.linkedin.com/in/s-bhargav-sai-6073b6293/
Bhargav Sai Sanapala

