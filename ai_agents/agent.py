from agent_loop import run_agent

print("AI Desktop Agent")
print("Type 'exit' to quit\n")

while True:

    prompt = input("Prompt > ")

    if prompt.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    print("\nRunning AI Agent...\n")

    run_agent(prompt)

    print("\n")