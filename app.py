from flask import Flask, render_template, request
import pandas as pd
from src.preprocessing import preprocess_text
from src.tfidf_model import build_tfidf_model
from src.search_engine import rank_documents

app = Flask(__name__)

data = pd.read_csv("data/news_articles.csv")
data["clean_content"] = data["content"].apply(preprocess_text)
vectorizer, tfidf_matrix = build_tfidf_model(data["clean_content"])

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = ""
    if request.method == "POST":
        query = request.form["query"]
        clean_query = preprocess_text(query)
        query_vector = vectorizer.transform([clean_query])
        scores = rank_documents(query_vector, tfidf_matrix)
        data["score"] = scores
        top_results = data[data["score"] > 0].sort_values(
            by="score", ascending=False).head(5)
        for _, row in top_results.iterrows():
            results.append({
                "id": int(row["id"]),
                "title": row["title"],
                "score": round(float(row["score"]), 4),
                "preview": row["content"][:200] + "..."
            })
    return render_template("index.html", results=results, query=query)

@app.route("/article/<int:article_id>")
def article(article_id):
    row = data[data["id"] == article_id].iloc[0]
    return render_template("article.html",
                           title=row["title"],
                           content=row["content"])

if __name__ == "__main__":
    app.run(debug=True)
