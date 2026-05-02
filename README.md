# 🍽️ NovaBite Multi-Agent RAG System

## 📌 Overview
NovaBite Restaurants operates multiple branches and requires an AI assistant capable of handling both knowledge-based queries and operational tasks.

This project implements a **production-style multi-agent system** using:
- LangChain
- Retrieval-Augmented Generation (RAG)
- Tool-based execution (MCP-style simulation)
- Orchestrator + Sub-agents architecture
- Conversation memory

---

## 🧠 System Architecture

### 1. Orchestrator Agent
- Acts as the central controller
- Classifies user intent
- Routes queries to:
  - RAG Agent (knowledge)
  - Operations Agent (tools)
- Maintains short-term memory (last 5 interactions)
- Does NOT contain business logic

---

### 2. RAG Agent (Restaurant Knowledge)
Handles restaurant-related queries using internal data.

**Supported domains:**
- Menu descriptions  
- Opening hours  
- Allergen information  

### 🔍 RAG Pipeline
- **Data Source:** JSON menu + restaurant info  
- **Chunking Strategy:** Small semantic chunks (100–300 characters)  
- **Embedding Model:** sentence-transformers/paraphrase-MiniLM-L3-v2  
- **Vector Database:** FAISS  
- **Retrieval Strategy:** Top-K similarity search (k=2)  
- **Post-processing:** Query-aware filtering to avoid mixing answers  

---

### 3. Operations Agent (Tool-Based / MCP Style)
Simulates backend services.

**Implemented tools:**
- `check_table_availability(date, time, branch)`  
- `book_table(name, date, time, branch)`  
- `get_today_special(branch)`  
- `check_loyalty_points(user_id)`  

---

### 4. Memory Design
The system maintains a short-term conversational memory (last 5 interactions) within the orchestrator.  
This enables handling of follow-up queries and preserves conversational context.

---

## 🔄 System Flow

```
User Input
   ↓
Orchestrator Agent
   ↓
   ├───────────────┬───────────────┤
   ↓                               ↓
RAG Agent                   Operations Agent
   ↓                               ↓
Grounded Answer            Tool Execution
   ↓
Final Response
```

This flow shows how the orchestrator routes user requests to the appropriate agent and returns the final response.

---

## 🛡️ Hallucination Prevention
- Responses are strictly based on retrieved data  
- No generative LLM is used  
- If no data is found → safe fallback response  
- Query-aware filtering prevents irrelevant information mixing  

---

## 💡 Key Design Decisions

### Why FAISS?
- Fast local vector search  
- No external dependencies  
- Suitable for offline evaluation  

### Why MiniLM embeddings?
- Lightweight and fast  
- Good semantic similarity performance  
- No API cost  

### Why no LLM generation?
The system avoids generative LLM usage to ensure deterministic, safe, and fully grounded responses.  
This eliminates hallucinations and ensures outputs are traceable to the knowledge base.

---

## 🧪 Example Queries

### 🍽️ Knowledge (RAG)
- Do you have vegan pasta?  
- Is the chicken grilled or fried?  
- What are your weekend hours?  

### 🛠️ Operations (Tools)
- Book a table tomorrow at 8 PM in Maadi  
- What’s today’s special?  
- Check my loyalty points  

---

## ⚠️ Assumptions
- Data is static (no real database)  
- Tools simulate backend APIs  
- Memory is session-based only  

---

## 🚀 How to Run

### 1. Install dependencies
```
pip install langchain langchain-community faiss-cpu sentence-transformers
```

### 2. Build vector database
```
python rag/ingest.py
```

### 3. Run the system
```
python main.py
```

---

## 📊 Evaluation Readiness
The system can be evaluated based on:
- Retrieval accuracy  
- Response correctness  
- Tool execution reliability  
- Intent routing accuracy  

---

## 🎯 Key Features
✔ Multi-agent architecture  
✔ RAG-based knowledge retrieval  
✔ Tool-based execution  
✔ Memory-enabled interaction  
✔ No hallucination responses  
✔ Fully local (no API required)  

---

## 🏁 Conclusion
This project demonstrates a production-style AI assistant combining retrieval systems, tool orchestration, and agent-based design.

It is designed to be scalable, reliable, and safe for real-world use.