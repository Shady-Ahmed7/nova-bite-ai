from agents.orchestrator import Orchestrator

def main():
    bot = Orchestrator()

    print("NovaBite AI Assistant")
    print("Type 'exit' to stop\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "exit":
            print("Goodbye!")
            break

        response = bot.handle(user_input)
        print("Bot:", response)
        print("-" * 40)

if __name__ == "__main__":
    main()
