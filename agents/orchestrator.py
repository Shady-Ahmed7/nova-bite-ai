
from agents.rag_agent import rag_answer
from agents.ops_agent import handle_ops

class Orchestrator:

    def __init__(self):
        self.memory = []

    def route(self, query):
        q = query.lower()

        # RAG: restaurant knowledge queries
        rag_keywords = [
            "menu", "vegan", "hours", "opening", "allergen",
            "ingredients", "dish", "food", "restaurant", "catering"
        ]

        # OPS: tools / actions
        ops_keywords = [
            "book", "reserve", "table", "availability",
            "special", "loyalty", "points"
        ]

        if any(word in q for word in rag_keywords):
            return "rag"

        if any(word in q for word in ops_keywords):
            return "ops"

        return "rag"  # fallback to RAG instead of blocking user

    def handle(self, query):
        # store memory (last 5 turns only)
        self.memory.append(query)
        self.memory = self.memory[-5:]

        route = self.route(query)

        if route == "rag":
            return rag_answer(query)

        elif route == "ops":
            return handle_ops(query)

        return "I couldn't understand your request. Please ask about menu, booking, or restaurant services."
