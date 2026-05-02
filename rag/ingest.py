
import json
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_documents(path="data/menu.json"):
    with open(path) as f:
        data = json.load(f)

    docs = []

    for item in data["menu"]:
        text = f"""
Name: {item['name']}
Type: {item['type']}
Vegan: {item['is_vegan']}
Allergens: {', '.join(item['allergens'])}
Description: {item['description']}
"""
        docs.append(text)

    hours = data["hours"]
    docs.append(f"Weekday hours: {hours['weekday']}")
    docs.append(f"Weekend hours: {hours['weekend']}")

    return docs

def create_vectorstore():
    docs = load_documents()

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.create_documents(docs)

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"
)
    
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("faiss_index")

if __name__ == "__main__":
    create_vectorstore()
