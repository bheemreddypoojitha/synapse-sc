from crewai import Agent, Task, Crew, Process, LLM
from enterprise_tools import search_logistics_alerts, query_erp, execute_reroute
from dotenv import load_dotenv
import os

load_dotenv()

groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

def run_synapse_swarm():
    # --- 1. DEFINE AGENTS ---
    sentinel = Agent(
        role='Global Supply Chain Sentinel',
        goal='Monitor APIs for supply chain disruptions and output verified alerts.',
        backstory='You are an early-warning AI. You only use the tools provided to fetch real-world data.',
        tools=[search_logistics_alerts],
        verbose=True,
        allow_delegation=False,
        llm=groq_llm
    )

    quant = Agent(
        role='Financial Quant',
        goal='Calculate the financial impact of delays using the ERP system.',
        backstory='You cross-reference external alerts with internal ERP data to find financial exposure. You are highly analytical.',
        tools=[query_erp],
        verbose=True,
        allow_delegation=False,
        llm=groq_llm
    )

    orchestrator = Agent(
        role='Logistics Orchestrator',
        goal='Determine alternative routes and execute them if within budget.',
        backstory='You are the decisive commander. You execute orders using the execution tool, but strictly follow financial guardrails.',
        tools=[execute_reroute],
        verbose=True,
        allow_delegation=False,
        llm=groq_llm
    )

    # --- 2. DEFINE TASKS ---
    task1 = Task(
        description="Use the 'Search Global Logistics Alerts' tool to run a diagnostic scan for 'Asian Pacific Ports'. Identify any critical disruptions and note the specific location.",
        expected_output="A summary of the current critical disruption, specifically naming the port affected.",
        agent=sentinel
    )

    task2 = Task(
        description="Take the affected port location from the Sentinel's alert and use the 'Query ERP Inventory Database' tool to check our exposure. Calculate the total SLA penalty for a 3-day delay.",
        expected_output="A financial damage report detailing at-risk inventory value and total calculated penalties for 3 days.",
        agent=quant
    )

    task3 = Task(
        description="Review the Quant's report. We have two backup vendors available: 'AirFreight-Pro' ($12,000) and 'Rail-Express' ($4,500). Use the 'Execute Rerouting & Verify Guardrails' tool to book the fastest option that DOES NOT trigger a compliance error.",
        expected_output="The final API response from the execution tool and a clear summary of the action taken.",
        agent=orchestrator
    )

    # --- 3. ASSEMBLE CREW ---
    crew = Crew(
        agents=[sentinel, quant, orchestrator],
        tasks=[task1, task2, task3],
        process=Process.sequential # They run in order
    )

    # Kickoff returns the final output from Task 3
    result = crew.kickoff()
    return str(result)
