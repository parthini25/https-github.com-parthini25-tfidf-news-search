import pandas as pd
from src.preprocessing import preprocess_text
from src.tfidf_model import build_tfidf_model
from src.search_engine import rank_documents

def main():
    print("=== TF-IDF Ranked News Article Search Engine ===")

    # Load dataset
    data = pd.read_csv("data/news_articles.csv")

    # Preprocess all article content
    data["clean_content"] = data["content"].apply(preprocess_text)

    # Build TF-IDF model
    vectorizer, tfidf_matrix = build_tfidf_model(data["clean_content"])
    print("Index built successfully. Ready to search.\n")

    while True:
        query = input("Enter search query (or type exit to quit): ")
        if query.lower() == "exit":
            print("Exiting. Goodbye!")
            break

        clean_query = preprocess_text(query)
        query_vector = vectorizer.transform([clean_query])
        scores = rank_documents(query_vector, tfidf_matrix)
        data["score"] = scores

        results = data[data["score"] > 0].sort_values(by="score", ascending=False)

        if results.empty:
            print("No matching articles found.\n")
        else:
            print("\nTop Results:")
            print("-" * 50)
            for i, (_, row) in enumerate(results.head(5).iterrows(), 1):
                print(f"{i}. Title : {row['title']}")
                print(f"   Score : {row['score']:.4f}")
                print(f"   Preview: {row['content'][:80]}...")
                print()

if __name__ == "__main__":
    main()
