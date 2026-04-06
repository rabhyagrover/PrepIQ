import time
import sys

# --- CONTENT BANK ---
# Grouped to provide a structured interview experience
INTERVIEW_ROUNDS = {
    "1": {
        "title": "Technical Deep-Dive",
        "intro": "Focus on clarity, logic, and your ability to explain complex systems.",
        "questions": [
            "What is the difference between a List and a Tuple?",
            "Can you explain 'Inheritance' in OOP to a non-technical person?",
            "How do you handle errors or exceptions in your Python scripts?",
            "Explain exactly what happens at the OS/Hardware level when a script reads a 10GB file on 4GB of RAM.",
            "What is the time complexity of binary search, and why does it matter?",
            "Can you explain the concept of 'Recursion' with an example?",
            "What are the advantages of using a framework like Django or Flask?",
            "How do you optimize a slow-running query in SQL?",
            "What is the difference between 'GET' and 'POST' HTTP methods?"
        ]
    },
    "2": {
        "title": "HR and Behavioral Leadership",
        "intro": "We are looking for self-awareness, resilience, and your personal growth mindset.",
        "questions": [
            "Tell me about a time you worked in a team to solve a conflict.",
            "Why should we hire you over other candidates with similar skills?",
            "How do you handle feedback and criticism from a lead or peer?",
            "Describe a challenging situation you faced and the steps you took to deal with it.",
            "Where do you see your career path leading in the next 5 years?",
            "Can you share an example of a project where you took initiative and led the team to success?",
            "How do you stay motivated and productive when working on long-term projects?",
            "Describe a time when you had to adapt to a significant change at work. What was the outcome?"
        ]
    }
}

def typewriter_print(text, delay=0.03):
    """Simulates a natural conversational pace in the console."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def run_interview():
    typewriter_print("Welcome to PrepIQ: Your Personal Placement Readiness Coach.")
    print("-" * 60)
    
    # Adding a personalized touch by asking for their target role
    position = input("Before we begin, what position are you applying for? ").strip()
    
    print("\nAvailable Practice Modules:")
    print("1. Technical Round (Python, Systems, and Data)")
    print("2. HR Round (Leadership, Behavior, and Culture)")
    
    choice = input("\nWhich round would you like to focus on today? (1 or 2): ").strip()
    
    if choice not in INTERVIEW_ROUNDS:
        typewriter_print("I didn't quite catch that. Please restart the session to select a valid round.")
        return

    round_data = INTERVIEW_ROUNDS[choice]
    typewriter_print(f"\n--- Preparing for {round_data['title']} ---")
    typewriter_print(f"Goal: {position}")
    typewriter_print(f"Coach's Advice: {round_data['intro']}")
    print("-" * 60)

    user_transcript = ""
    
    for i, q in enumerate(round_data['questions']):
        print(f"\n[Question {i+1} of {len(round_data['questions'])}]")
        typewriter_print(f"Q: {q}")
        
        answer = input("Your Answer: ").strip()
        user_transcript += " " + answer.lower()
        
        # Simulating the interviewer processing the response
        print("... Recording notes ...")
        time.sleep(1.5)

    generate_human_report(user_transcript, round_data['title'], position)

def generate_human_report(transcript, round_name, position):
    """
    Analyzes the transcript for professional impact and situational awareness.
    """
    typewriter_print("\nAnalysis in progress... I'm reviewing your responses for key professional indicators.")
    time.sleep(2.5)

    # Categories for a holistic professional review
    power_indicators = {
        "Leadership and Initiative": ["lead", "organized", "coordinated", "initiative", "managed", "led", "took charge", "proactive", "ownership", "initiative"],
        "Analytical Problem Solving": ["logic", "solution", "debugged", "optimized", "efficient", "analytical", "problem-solving", "troubleshoot", "critical thinking", "data-driven", "insight", "analyzed", "evaluated", "synthesized"],
        "Interpersonal Skills": ["collaborated", "feedback", "team", "growth", "adapted", "communication", "relationship", "empathy", "mentored", "coached", "listened", "negotiated", "influenced", "conflict resolution", "emotional intelligence", "networking", "rapport", "cultural fit"],
        "Impact and Results": ["impact", "result", "improved", "success", "goal", "achieved", "delivered", "outcome", "value", "contributed", "performance", "exceeded", "milestone", "ROI", "efficiency gain", "customer satisfaction", "revenue growth", "cost savings", "innovation", "scalability", "sustainability", "long-term value", "measurable", "quantifiable", "business impact", "strategic impact", "competitive advantage", "market share", "user engagement", "retention", "conversion rate", "customer acquisition", "brand recognition", "thought leadership", "industry recognition", "awards", "publications", "patents", "speaking engagements", "community impact", "social impact", "environmental impact", "diversity and inclusion impact", "employee engagement", "talent development", "organizational culture", "change management", "risk management", "compliance", "governance"]
    }

    found_strengths = []
    score = 45  # Starting base score for completing the session

    for category, keywords in power_indicators.items():
        if any(word in transcript for word in keywords):
            score += 15
            found_strengths.append(category)

    final_score = min(score, 100)

    print("\n" + "="*60)
    print(f"PREPIQ READINESS REPORT: {round_name.upper()}")
    print(f"TARGET ROLE: {position.upper()}")
    print("="*60)
    print(f"Readiness Score: {final_score}/100")
    
    if found_strengths:
        print(f"Key Strengths Identified: {', '.join(found_strengths)}")
    else:
        print("Observation: Your answers were concise. For a real interview, try to expand on your specific contributions.")

    print("\n--- Final Feedback ---")
    if final_score >= 85:
        typewriter_print("You've demonstrated a high level of professional maturity. You are likely ready for the actual placement.")
    elif final_score >= 65:
        typewriter_print("Strong performance. Focus on using the STAR method (Situation, Task, Action, Result) to make your examples even more compelling.")
    else:
        typewriter_print("This was a good start. I recommend practicing your 'Action Verbs' and providing more detailed examples of your past work.")
    print("="*60)

if __name__ == "__main__":
    try:
        run_interview()
    except KeyboardInterrupt:
        print("\n\nSession ended. Good luck with your preparation.")
