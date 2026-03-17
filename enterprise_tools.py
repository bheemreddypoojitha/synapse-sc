from crewai.tools import tool
import json

@tool("Search Global Logistics Alerts")
def search_logistics_alerts(query: str) -> str:
    """Useful to search for real-time weather, strikes, or port closures. Input should be a region."""
    # Mocking a real-time global logistics API
    mock_data = {
        "status": "CRITICAL ALERT",
        "location": "Port of Shenzhen, China",
        "event": "Category 4 Typhoon 'Mangkhut'",
        "impact": "All port operations halted for 72 hours minimum."
    }
    return json.dumps(mock_data)

@tool("Query ERP Inventory Database")
def query_erp(location: str) -> str:
    """Queries the enterprise SAP/ERP system to find delayed inventory at a specific port. Input is the port name."""
    if "Shenzhen" in location:
        return json.dumps({
            "delayed_shipments": 14,
            "inventory_value_usd": 2500000,
            "sla_penalty_per_day": 5000,
            "critical_components": ["Microchips", "Lithium Batteries"]
        })
    return json.dumps({"status": "No critical inventory found at this location."})

@tool("Execute Rerouting & Verify Guardrails")
def execute_reroute(vendor_name: str, cost: int) -> str:
    """Executes a logistics rerouting order. Fails if cost exceeds the $10,000 compliance guardrail. Inputs: vendor_name, cost."""
    # HARD CODED COMPLIANCE GUARDRAIL
    MAX_AUTONOMOUS_SPEND = 10000 
    
    if cost > MAX_AUTONOMOUS_SPEND:
        return f"ERROR: COMPLIANCE BREACH. Cost ${cost} exceeds autonomous limit of ${MAX_AUTONOMOUS_SPEND}. Reroute rejected. Human approval required."
    
    return f"SUCCESS: Order placed with {vendor_name} for ${cost}. Route updated in ERP system. Guardrail check passed."