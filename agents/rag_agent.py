
from rag.retriever import load_retriever

retriever = load_retriever()

def rag_answer(query):
    docs = retriever.invoke(query)

    if not docs:
        return "I couldn't find that information in our system."

    # Take only most relevant result
    best_match = docs[0].page_content

    return f"""Based on our restaurant system:

{best_match}
"""
