import datetime
import sys

def run_chatbot():
    responses = {
        responses = {
        "hello": "Hey there, human! Glad you dropped by. Ready to look at some clean code?",
        "hi": "Oh, hello! Let's see what logic gears we're turning today.",
        "hey": "Yo! High-five for running a script that actually compiles on the first try.",
        "help": "Don't panic! I can help you navigate this logic terminal. If you want to bail, just type 'exit' or 'bye'.",
        "weather": "am sorry, i dont know about the weather but would definitely tell you about the cloud storages",
        "forecast": "Clear skies ahead! Excellent processing speeds, high focus levels, and zero unexpected runtime errors.",
        "time": f"Time flies when you're optimizing! It's currently {datetime.datetime.now().strftime('%I:%M %p')}. Sleep is for the weak, right?",
        "schedule": "Today's schedule is to complete project 1 for DecodeLabs",
        "motivate": "Keep pushing! Remember: Before you manage the chaos of a probability engine, you must master the absolute precision of a logic engine.",
        "status": "All systems nominal. Logic gates are fully functional, guardrails are locked in, and the code is stable.",
        "name": "I'm your Phase 1 Logic Engine! No mysterious AI hallucinations here—just pure, hard-coded, predictable engineering perfection.",
        "tip": "Pro-tip: Always use hash maps or dictionaries for lookup tables. It keeps your code performing at instant O(1) constant time instead of dragging down to O(n) linear slowdowns."
    }
    
    exit_commands = {"exit", "bye", "quit", "goodbye"}
    
    print("Chatbot: Hello! I am a rule-based AI assistant. How can I help you today?")
    
    while True:
        try:
            raw_input = input("User: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Session interrupted. Goodbye!")
            sys.exit(0)
            
        user_input = raw_input.strip().lower()
        
        if not user_input:
            continue
            
        if user_input in exit_commands:
            print("Chatbot: Goodbye! Have a great day ahead.")
            break
            
        default_fallback = (
            responses["weather"] if any(w in user_input for w in ["weather", "rain", "temp"]) else
            responses["time"] if any(t in user_input for t in ["time", "clock"]) else
            responses["tip"] if "advice" in user_input else
            "I'm sorry, I am a basic rule-based bot and I don't understand that command yet."
        )
        
        reply = responses.get(user_input, default_fallback)
        print(f"Chatbot: {reply}")

if __name__ == "__main__":
    run_chatbot()
