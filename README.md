📊 CORD-19 Research Explorer

This project explores the CORD-19 dataset (COVID-19 Open Research Dataset) and provides both a Jupyter Notebook analysis and an interactive Streamlit app. The goal is to practice basic data analysis, visualization, and web app development.

🚀 Project Overview

The project is divided into the following parts:

Data Loading and Exploration

Load metadata_5000.csv (a subset of the full dataset)

Inspect dataset shape, structure, and missing values

Data Cleaning and Preparation

Handle missing values in key columns

Convert publication date into datetime and extract year

Add derived features (e.g., abstract word count)

Data Analysis and Visualization

Publications over time

Top journals publishing COVID-19 papers

Frequent words in paper titles

Word cloud of titles

Distribution of papers by source

Streamlit App

Interactive filters (year range)

Display charts dynamically

Word cloud generator

Show a sample of filtered papers

🛠️ Tools and Libraries

Python 3.7+

pandas
 – data manipulation

matplotlib
 & seaborn
 – visualization

wordcloud
 – word cloud generation

Streamlit
 – web application framework

Jupyter Notebook
 – interactive analysis

📂 Project Structure
Frameworks_Assignment/
│
├── metadata_5000.csv        # Sample dataset (subset of CORD-19 metadata)
├── notebook.ipynb           # Jupyter Notebook with step-by-step analysis
├── app.py                   # Streamlit app
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies

▶️ How to Run
1. Clone the Repository
git clone https://github.com/<your-username>/Frameworks_Assignment.git
cd Frameworks_Assignment

2. Install Dependencies
pip install -r requirements.txt


Or install manually:

pip install pandas matplotlib seaborn wordcloud streamlit

3. Run the Jupyter Notebook
jupyter notebook notebook.ipynb

4. Run the Streamlit App
streamlit run app.py

📊 Example Visualizations

Publications by Year

Top 10 Journals

Word Cloud of Titles

Source Distribution

(see figures in the notebook or Streamlit app output)

🧾 Findings (Sample Insights)

Publications surged significantly in 2020 due to COVID-19.

Journals such as The Lancet and BMJ are among the top publishers.

Common title words include COVID, SARS, health, impact, and patients.

The dataset has many missing values, requiring careful cleaning.

💡 Reflection

This project provided hands-on practice with:

Real-world dataset cleaning and preparation

Exploratory Data Analysis (EDA)

Creating visualizations to summarize trends

Building an interactive dashboard with Streamlit

Challenges:

Handling missing values in titles and dates

Ensuring the word cloud didn’t break when no titles were available

Managing dataset size (full CORD-19 is very large, so a subset was used)

📌 Next Steps

Expand the app with search functionality by keyword/author

Add time series analysis (monthly trends)

Use NLP techniques for deeper insights (topic modeling, sentiment)
