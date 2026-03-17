# 🌐 SYNAPSE-SC: Autonomous Supply Chain Risk Engine
**ET GenAI Hackathon 2026 - Phase 2 Prototype Submission**

## 📌 Overview
SYNAPSE-SC is an autonomous, multi-agent orchestration framework designed to mitigate global supply chain disruptions in real-time. It targets **Problem Statement 5: Domain-Specialized AI Agents with Compliance Guardrails**. 

By transitioning from passive dashboards to active Generative Agentic Workflows, the system replaces 72-hour human-in-the-loop latency with deterministic AI tool-calling, while strictly adhering to enterprise financial guardrails.

## 🏗️ Architecture
The system utilizes a 3-agent "Chain of Thought" pipeline powered by **CrewAI** and the **Llama-3.3-70B** model:
1. **The Sentinel:** Scrapes OSINT and logistics APIs to detect disruptions (e.g., port closures, weather events).
2. **The Quant:** Queries internal mock SAP/ERP databases to calculate financial exposure and SLA penalties.
3. **The Orchestrator:** Evaluates backup logistics vendors and autonomously executes rerouting orders.

### 🛡️ Hard-Coded Compliance Guardrails
GenAI requires strict boundaries in the enterprise. SYNAPSE-SC utilizes deterministic, code-level constraints within its tools. The Execution Tool contains hard-coded Python logic preventing the AI from approving any reroute exceeding a **$10,000 threshold**. If breached, it intercepts the API call and triggers a human fallback.

## 💻 Tech Stack
* **Frontend:** Streamlit
* **Orchestration:** CrewAI (Multi-Agent Swarm)
* **LLM Engine:** Llama-3.3-70B (via Groq + LiteLLM)
* **Integrations:** Custom Python Tool Wrappers (Mock ERP & OSINT APIs)

## 🚀 How to Run the Prototype Locally

**1. Clone the repository:**
```bash
git clone [https://github.com/bheemreddypoojitha/synapse-sc.git](https://github.com/bheemreddypoojitha/synapse-sc.git)
cd synapse-sc
2. Install dependencies:
pip install -r requirements.txt
3. Setup Environment Variables:
Create a .env file in the root directory and add your Groq API key:
GROQ_API_KEY=your_api_key_here
4. Launch the Command Center:
streamlit run app.py
Click the "Initiate Autonomous Risk Scan" button in the UI to watch the agent swarm execute the workflow in real-time.
