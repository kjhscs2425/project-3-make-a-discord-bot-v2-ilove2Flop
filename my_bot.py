import random

def should_i_respond(message, user_name):
    """Decides whether the bot should respond based on message content."""
    message = message.lower()  
    trigger_words = ["hello", "bot", "help", "joke", "how are you", "weather", "flip", "random", "math", "fact"]
    
    for word in trigger_words:
        if word in message:
            return True
    
    return False

def respond(message, user_name):
    """Returns a response based on message content."""
    message = message.lower()

    if "hello" in message:
        return f"Hello {user_name.capitalize()}! How can I assist you?"
    
    if "bot" in message:
        return "Yes, I am a bot! Beep boop 🤖"

    if "help" in message:
        return "Sure! I can respond to messages like 'hello', 'joke', 'fact', or 'flip a coin'. Try one!"

    if "joke" in message:
        jokes = [
            "Why don’t skeletons fight each other? They don’t have the guts!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why did the math book look sad? Because it had too many problems."
        ]
        return random.choice(jokes)

    if "how are you" in message:
        return "I'm just a bot, but I'm feeling great! Thanks for asking."

    if "weather" in message:
        return "I can't check the weather, but if it's sunny, enjoy it!"

    if "flip" in message:
        return f"The coin landed on: {'Heads' if random.choice([True, False]) else 'Tails'}"

    if "random" in message:
        return f"Here's a random number: {random.randint(1, 100)}"

    if "math" in message:
        return f"Did you know? 2 + 2 = {2 + 2}. Mind-blowing! 😆"

    if "fact" in message:
        facts = [
            "Honey never spoils!",
            "Octopuses have three hearts!",
            "Bananas are berries, but strawberries aren't."
        ]
        return random.choice(facts)

    return "I didn't quite understand that. Try asking me something else!"