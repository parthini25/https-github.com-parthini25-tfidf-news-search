# TF-IDF Ranked News Article Search Engine

## Project Title
TF-IDF Ranked Search for News Articles

## Objective
To build a ranked news article search engine using TF-IDF weighting
and Cosine Similarity deployed as a Flask web application accessible
through a public URL.

## Tools and Technologies Used
- Python 3
- Flask (Web Framework)
- Scikit-learn (TF-IDF Vectorization and Cosine Similarity)
- Pandas (CSV Data Handling)
- NLTK (Stop Word Removal)
- Gunicorn (Production Server for Deployment)
- PyCharm (IDE)
- Git and GitHub (Version Control)
- Render (Cloud Deployment)

## Installation Steps

Step 1: Install Python
- Download Python 3 from https://www.python.org/downloads
- During installation tick "Add Python to PATH"
- Verify: open Command Prompt and type python --version

Step 2: Install PyCharm
- Download PyCharm from https://www.jetbrains.com/pycharm/
- Install with default settings

Step 3: Clone the Repository
- Open Command Prompt
- Run this command:
  git clone https://github.com/SREEKALA17/tfidf-news-search.git

Step 4: Open Project in PyCharm
- Open PyCharm
- Click Open
- Select the cloned tfidf-news-search folder
- Click OK

Step 5: Install Required Libraries
- Open Terminal tab at bottom of PyCharm
- Run this command:
  pip install -r requirements.txt
- Wait for all libraries to install successfully

## Instructions to Run the Application

Step 1: Open the project in PyCharm

Step 2: Open Terminal tab at the bottom of PyCharm

Step 3: Type this command and press Enter:
  python app.py

Step 4: You will see this message in terminal:
  * Running on http://127.0.0.1:5000

Step 5: Open any browser (Chrome, Edge)

Step 6: Type this in the address bar:
  http://127.0.0.1:5000

Step 7: The search engine home page will open

Step 8: Type a search query example:
  artificial intelligence healthcare

Step 9: Click the Search button

Step 10: Ranked news articles will appear with
  relevance scores and Read Full Article button

Step 11: Click Read Full Article to read the complete article

Step 12: Click Back to Search to return to results

To stop the application:
  Press CTRL+C in the PyCharm terminal

## Live URL (No Installation Required)
https://tfidf-news-search.onrender.com

## GitHub Repository
https://github.com/SREEKALA17/tfidf-news-search

## Project Structure
tfidf_news_search/
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── Procfile
├── .gitignore
├── data/
│   └── news_articles.csv
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── tfidf_model.py
│   └── search_engine.py
└── templates/
    ├── index.html
    └── article.html

## Deployment on Render

The application is deployed on Render cloud platform.

### Steps to Deploy on Render:

Step 1: Create a free account at https://render.com
        Click Sign Up → Continue with GitHub

Step 2: Click New + → Web Service

Step 3: Connect your GitHub repository
        Select tfidf-news-search → Click Connect

Step 4: Fill deployment settings:
        Name          → tfidf-news-search
        Region        → Singapore
        Branch        → main
        Runtime       → Python 3
        Build Command → pip install -r requirements.txt
        Start Command → gunicorn app:app

Step 5: Select Free plan → Click Deploy Web Service

Step 6: Wait 3-5 minutes for build to complete

Step 7: Your live URL will be:
        https://tfidf-news-search.onrender.com

### Note:
Render free plan sleeps after 15 minutes of inactivity.
First load may take 1-2 minutes to wake up.
Open the URL 5 minutes before demonstration.
