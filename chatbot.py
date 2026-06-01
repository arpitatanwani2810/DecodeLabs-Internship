import datetime
import sys

def run_chatbot():
    exact_intents = {
        "hello": "Greetings! Glad to chat with you today.",
        "hi": "Hello there! How can I help you?",
        "hey": "Hey! Up for a quick chat?",
        "help": "I can assist you with basic navigation. Type 'exit' or 'bye' to quit.",
        "weather": "The current system environment is a comfortable 22°C with 0% chance of rain inside this terminal.",
        "forecast": "The upcoming conditions predict clear skies, high data throughput, and excellent processing speeds.",
        "time": f"The current system timestamp is: {datetime.datetime.now().strftime('%H:%M:%S')}.",
        "schedule": "Today's block is reserved for building logic foundations, refining code structures, and optimization.",
        "motivate": "Remember: Before you manage the chaos of a probability engine, you must master the precision of a logic engine!",
        "status": "System status is nominal. Logic gates are fully functional.",
        "tip": "Engineering Tip: Always use hash maps or dictionaries for lookup tables. It keeps your complexity at O(1) instead of cascading into O(n) linear slowdowns.",
        "tip1": "Logic Tip: Clean, sanitize, and normalize your inputs early (.strip().lower()) so your processing gates never have to guess.",
        "tip2": "Design Tip: A rule-based program is a 'white box'. Total predictability means zero hallucination risk—essential for production engineering.",
        "tip3": "Architecture Tip: Think of rule-based logic as a guardrail. In modern apps, these gates filter inputs before they ever touch an LLM core."
    }
    
    exit_commands = {"exit", "bye", "quit", "goodbye"}
    tip_keys = ["tip", "tip1", "tip2", "tip3"]
    tip_counter = 0
    
    print("Chatbot: Hello! I am a rule-based AI assistant. How can I help you today?")
    
    while True:
        try:
            raw_input = input("User: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Session interrupted. Goodbye!")
            sys.exit(0)
            
        cleaned_input = raw_input.strip().lower()
        
        if not cleaned_input:
            continue
            
        if cleaned_input in exit_commands:
            print("Chatbot: Goodbye! Have a great day ahead.")
            break
            
        if "tip" in cleaned_input or "advice" in cleaned_input:
            current_tip_key = tip_keys[tip_counter % len(tip_keys)]
            print(f"Chatbot: {exact_intents[current_tip_key]}")
            tip_counter += 1
            continue
            
        response = exact_intents.get(cleaned_input)
        if response:
            print(f"Chatbot: {response}")
            continue

        if "weather" in cleaned_input or "rain" in cleaned_input or "temp" in cleaned_input:
            print(f"Chatbot: {exact_intents['weather']}")
        elif "time" in cleaned_input or "clock" in cleaned_input:
            print(f"Chatbot: {exact_intents['time']}")
        elif "name" in cleaned_input:
            print("Chatbot: I am your Phase 1 Rule-Based Engine.")
        else:
            print("Chatbot: I'm sorry, I am a basic rule-based bot and I don't understand that command yet.")

if __name__ == "__main__":
    run_chatbot()
