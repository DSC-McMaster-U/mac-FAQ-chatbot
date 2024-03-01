from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def extract_top_n_keywords(doc, N):
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
    
    # Fit and transform the document
    # Note: fit_transform expects an iterable, so we pass [doc]
    tfidf_matrix = vectorizer.fit_transform([doc])
    
    # Get feature names to use as keywords
    feature_names = vectorizer.get_feature_names_out()
    
    # Extract dense scores for better manipulation
    dense = tfidf_matrix.todense()
    
    # Create a dictionary for the document's word scores
    doc_dict = {}
    for col in range(len(feature_names)):
        doc_dict[feature_names[col]] = dense[0, col]
    
    # Sort keywords by score
    sorted_keywords = sorted(doc_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Select top N keywords for the document, extracting only the word
    top_keywords = [word for word, score in sorted_keywords[:N]]
    
    return top_keywords


# # Sample document
# doc = "Python is a high-level, general-purpose programming language that emphasizes code readability with its notable use of significant whitespace."

# # Extract top 5 keywords from the document
# top_keywords = extract_top_n_keywords(doc, 10)

# # Print the results
# print(f"Top keywords: {top_keywords}")


if __name__ == "__main__":
    input_file = 'DB/data/faqs_dataset.jsonl'
    output_file = 'DB/data/faq_keywords_dataset.jsonl'

    # extract keywords and add new column
    df = pd.read_json(input_file, lines=True)

    df['top_keywords'] = (df['question'] + ' ' + df['answer']).apply(lambda text: extract_top_n_keywords(text,10))

    df.to_json(output_file, orient='records', lines='True')