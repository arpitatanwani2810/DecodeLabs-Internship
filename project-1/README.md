Welcome to my first chatbot! This is a clean, lightweight, 
and predictable rule-based Python chatbot designed to bring instant utility (and a bit of dev humor) right to your terminal.
No complex machine learning weights, no unpredictable AI hallucinations—just pure, hard-coded, lightning-fast execution.  

Features:  
- Atomic Dictionary Lookups: Leverages Python dictionaries to ensure response lookups happen in instant constant time.
- Contextual Fallbacks: Includes smart keyword routing for weather, time, and developer tips if an exact command isn't matched.
- Clean Session Management: Gracefully handles user exits and terminal interrupts without throwing ugly stack traces.
- Built-in Dev Humor: Packed with tailored responses celebrating the small victories of coding (like compiling on the first try).

The script is built with simplicity and resilience in mind:  
- Input Sanitization: Automatically strips whitespace and normalizes text to lowercase, making user input case-insensitive.
- Graceful Degredation: If an exact key isn't found in the response dictionary, a fallback chain scans the input for broader 
keywords before resorting to a standard default message.

Future Milestones:  
- Transition from static dictionary matching to regular expression (Regex) pattern matching.
- Implement external API integrations for real-time weather and live schedule updates.
- Build a sleek UI/UX wrapper using Figma prototypes as a structural blueprint.
