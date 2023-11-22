import pandas as pd
import os
from collections import defaultdict

def tokenize_document(document):
    return document.split()

def build_inverted_index(documents):
    inverted_index = defaultdict(lambda: defaultdict(int))

    for doc_id, (doc_title, document) in enumerate(documents):  # Unpack the tuple
        tokens = tokenize_document(document)
        for token in set(tokens):
            inverted_index[token][doc_title] += tokens.count(token)

    return inverted_index

folder_path = "./Collection/docs"
files = os.listdir(folder_path)
documents = []

for file in files:
    file_path = os.path.join(folder_path, file)
    with open(file_path, 'r', encoding='utf8') as f:
        document = f.read()
        documents.append((file, document))  # Use a tuple with (title, content)

inverted_index = build_inverted_index(documents)

# Convert the inverted index to a DataFrame
data = {'Word': [], 'Document Info': []}

for word, info in inverted_index.items():
    document_info = [[doc_title, frequency] for doc_title, frequency in info.items()]
    if document_info:
        data['Word'].append(word)
        data['Document Info'].append(document_info)

inverted_index_df = pd.DataFrame(data)



# Display the resulting DataFrame
print(inverted_index_df)