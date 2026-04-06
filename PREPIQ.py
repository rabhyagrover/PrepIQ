#!/import time

# --- PRE-DEFINED DATA ---
# We use dictionaries to organize our questions by category
QUESTIONS = {
    "1": {
        "domain": "Technical",
        "list": [
            "What is the difference between a List and a Tuple?",
            "Can you explain what 'Inheritance' means in OOP?",
            "What is a 'Primary Key' in a database?",
            "How do you handle errors in your code?",
            "What is the time complexity of binary search?",
            "Can you explain the concept of 'Recursion' with an example?",
            "What are the advantages of using a framework like Django or Flask?",
            "How do you optimize a slow-running query in SQL?",
            "What is the difference between 'GET' and 'POST' HTTP methods?",
            "Explain exactly what happens, at the OS and hardware level, when a Python script reads a 10GB file on a machine with only 4GB of RAM. How does the Virtual Memory Manager, the Page Table, and the CPU cache interact in this scenario?"


        ]
    },
    "2": {
        "domain": "HR / Behavioral",
        "list": [
            "Tell me about a time you worked in a team.",
            "What are your greatest strengths and weaknesses?",
            "Why should we hire you for this role?",
            "How do you handle tight deadlines?",
            "Describe a challenging situation you faced and how you dealt with it.",
            "Where do you see yourself in 5 years?",
            "What motivates you to perform well in your job?",
            "How do you handle feedback and criticism?"

        ]
    }
}

def run_interview():
    print("--- Welcome to PrepIQ: Placement Readiness Tool ---")
    print("1. Technical Round")
    print("2. HR Round")
    
    choice = input("\nSelect your round (1 or 2): ")
    
    if choice not in QUESTIONS:
        print("Invalid choice. Restarting...")
        return

    selected_round = QUESTIONS[choice]
    print(f"\nStarting {selected_round['domain']} Interview...")
    print("------------------------------------------")

    user_answers = []
    
    # Loop through the questions one by one
    for i, q in enumerate(selected_round['list']):
        print(f"\nQuestion {i+1}: {q}")
        answer = input("Your Answer: ")
        user_answers.append(answer)
        print("Saving response...")
        time.sleep(1) # Adds a realistic "processing" feel

    generate_report(user_answers)

def generate_report(answers):
    """
    Analyzes the answers for professional keywords.
    """
    print("\n--- Generating Your PrepIQ Performance Report ---")
    time.sleep(2)
    
    # Keywords that a student should ideally use
    keywords = ["team", "logic", "efficient", "manage", "practice", "learned", "goal", "challenge", "solution", "improve", "feedback", "collaborate", "adapt", "resilient", "innovate", "leadership", "communication", "problem-solving", "time management", "critical thinking", "technical", "project", "deadline", "result", "success", "failure", "growth", "opportunity", "motivation", "passion", "dedication", "initiative", "responsibility", "accountability", "creativity", "analytical", "strategic", "vision", "execution", "performance", "quality", "impact", "value", "customer", "stakeholder", "teamwork", "collaboration", "adaptability", "resilience", "innovation", "leadership", "communication", "problem-solving", "time management", "critical thinking", "technical expertise", "project management", "deadline-driven", "result-oriented", "success-driven", "failure-tolerant", "growth mindset", "opportunity-seeking", "motivated", "passionate", "dedicated", "initiative-taking", "responsible", "accountable", "creative", "analytical", "strategic thinker", "visionary", "execution-focused", "performance-driven", "quality-conscious", "impactful", "value-driven", "customer-focused", "stakeholder-oriented", "teamwork-oriented", "collaboration-focused", "adaptability-skilled", "resilience-trained", "innovation-minded", "leadership-capable", "communication-skilled", "problem-solving-oriented", "time management proficient", "critical thinking adept", "technical expertise strong", "project management experienced", "deadline-driven efficient", "result-oriented achiever", "success-driven performer", "failure-tolerant learner", "growth mindset advocate", "opportunity-seeking proactive", "motivated self-starter", "passionate about learning", "dedicated to excellence", "initiative-taking go-getter", "responsible and reliable", "accountable for results", "creative problem solver", "analytical thinker", "strategic planner", "visionary leader", "execution-focused doer", "performance-driven achiever", "quality-conscious worker", "impactful contributor", "value-driven professional", "customer-focused service", "stakeholder-oriented approach", "teamwork-oriented collaborator", "collaboration-focused team player", "adaptability-skilled individual", "resilience-trained professional", "innovation-minded thinker", "leadership-capable individual", "communication-skilled communicator", "problem-solving-oriented mindset", "time management proficient organizer", "critical thinking adept analyst", "technical expertise strong coder", "project management experienced leader", "deadline-driven efficient worker", "result-oriented achiever performer", "success-driven performer achiever", "failure-tolerant learner resilient", "growth mindset advocate learner", "opportunity-seeking proactive individual", "motivated self-starter go-getter", "passionate about learning and growth", "dedicated to excellence and improvement", "initiative-taking go-getter proactive", "responsible and reliable team member", "accountable for results and outcomes", "creative problem solver innovative thinker", "analytical thinker strategic planner", "visionary leader execution-focused doer", "performance-driven achiever quality-conscious worker", "impactful contributor value-driven professional", "customer-focused service stakeholder-oriented approach", "teamwork-oriented collaborator collaboration-focused team player", "adaptability-skilled individual resilience-trained professional", "innovation-minded thinker leadership-capable individual", "communication-skilled communicator problem-solving-oriented mindset", "time management proficient organizer critical thinking adept analyst", "technical expertise strong coder project management experienced leader", "deadline-driven efficient worker result-oriented achiever performer", "success-driven performer achiever failure-tolerant learner resilient", "growth mindset advocate learner opportunity-seeking proactive individual", "motivated self-starter go-getter passionate about learning and growth", "dedicated to excellence and improvement initiative-taking go-getter proactive", "responsible and reliable team member accountable for results and outcomes", "creative problem solver", "innovative thinker", "analytical thinker", "strategic planner", "visionary leader", "execution-focused doer", "performance-driven achiever", "quality-conscious worker", "impactful contributor", "value-driven professional", "customer-focused service", "stakeholder-oriented approach", "teamwork-oriented collaborator", "collaboration-focused team player", "adaptability-skilled individual", "resilience-trained professional", "innovation-minded thinker", "leadership-capable individual", "communication-skilled"]
    
    for word in keywords:
        if word in full_transcript:
            score += 15
            found_words.append(word)

    # Final Output
    print(f"Readiness Score: {min(score, 100)}/100")
    print(f"Professional Keywords Detected: {', '.join(found_words) if found_words else 'None'}")
    
    if score >= 60:
        print("Result: You are ready for the actual placement round!")
    else:
        print("Result: Keep practicing! Focus on using more industry-specific terms.")

if __name__ == "__main__":
    run_interview()
