import requests
import time
import json
import statistics

# --- CONFIGURATION ---
API_URL = "http://127.0.0.1:8000/start_plan"

# --- GOLDEN TEST SET ---
# We test the agent against these 5 diverse scenarios
TEST_DATASET = [
    {"destination": "Paris", "days": 3, "travelers": 2, "experience": "Luxury"},
    {"destination": "Tokyo", "days": 5, "travelers": 1, "experience": "Budget"},
    {"destination": "New York", "days": 2, "travelers": 4, "experience": "Adventure"},
    {"destination": "Dubai", "days": 4, "travelers": 2, "experience": "Luxury"},
    {"destination": "London", "days": 3, "travelers": 1, "experience": "Standard"}
]

def run_evaluation():
    print("📋 STARTING AGENT EVALUATION PIPELINE...\n")
    print(f"{'DESTINATION':<15} | {'STATUS':<10} | {'LATENCY (s)':<12} | {'SCORE':<10}")
    print("-" * 60)

    results = []
    latencies = []
    total_score = 0

    for test_case in TEST_DATASET:
        start_time = time.time()
        
        try:
            # 1. Call the Agent API
            response = requests.post(API_URL, json=test_case)
            latency = round(time.time() - start_time, 2)
            latencies.append(latency)
            
            data = response.json()
            
            # 2. EVALUATION LOGIC (The Grading Rubric)
            score = 0
            checks = []
            
            # Metric A: JSON Structure Validity (Critical)
            if "trip_details" in data and "itinerary" in data:
                score += 40
                checks.append("✅ Schema")
            else:
                checks.append("❌ Schema")

            # Metric B: Constraint Satisfaction (Did it listen?)
            # Check Destination
            if test_case["destination"].lower() in data["trip_details"]["destination"].lower():
                score += 30
                checks.append("✅ Dest")
            else:
                checks.append("❌ Dest")

            # Check Days
            if len(data["itinerary"]) == test_case["days"]:
                score += 30
                checks.append("✅ Days")
            else:
                checks.append("❌ Days")

            # Final Verdict for this test case
            status = "PASS" if score == 100 else "FAIL"
            total_score += score
            
            print(f"{test_case['destination']:<15} | {status:<10} | {latency:<12} | {score}/100")
            
            results.append({
                "case": test_case,
                "latency": latency,
                "score": score,
                "checks": checks
            })

        except Exception as e:
            print(f"{test_case['destination']:<15} | ERROR      | 0.00         | 0/100")
            print(f"  Error details: {e}")

    # --- FINAL REPORT GENERATION ---
    avg_latency = statistics.mean(latencies) if latencies else 0
    avg_score = total_score / len(TEST_DATASET) if TEST_DATASET else 0

    print("\n" + "="*60)
    print("📊 FINAL EVALUATION REPORT (METRICS)")
    print("="*60)
    print(f"1. Total Test Cases:      {len(TEST_DATASET)}")
    print(f"2. Average Success Rate:  {avg_score}%")
    print(f"3. Average Latency:       {avg_latency:.2f} seconds")
    print(f"4. Model Used:            Llama-3.3-70b-versatile")
    print("="*60)
    
    # Save to file for the project submission
    with open("evaluation_report.txt", "w") as f:
        f.write(f"Agent Evaluation Report\nAverage Score: {avg_score}%\nAvg Latency: {avg_latency}s")
    print("\n✅ Report saved to 'evaluation_report.txt'")

if __name__ == "__main__":
    # Ensure the main server is running before executing this
    try:
        requests.get("http://127.0.0.1:8000/")
        run_evaluation()
    except:
        print("❌ ERROR: The Agent Server is not running.")
        print("Please run 'python main.py' in a separate terminal first.")