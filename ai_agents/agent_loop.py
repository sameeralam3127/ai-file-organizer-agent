import json
import re
import inspect

from ollama_client import ask_llm
from tools import scan_desktop, create_folder, move_file


TOOLS = {
    "scan_desktop": scan_desktop,
    "create_folder": create_folder,
    "move_file": move_file,
}


SYSTEM_PROMPT = """
You are an AI desktop organizer agent.

Your job is to organize files on the user's Desktop.

You MUST respond ONLY with JSON.

Available tools:

scan_desktop()
create_folder(name)
move_file(filename, folder)

Rules:
- Return ONE action at a time
- Do NOT add explanations
- Do NOT invent parameters

Example:

{
 "tool": "scan_desktop",
 "args": {}
}

When the task is finished return:

DONE
"""


def extract_json(text):
    """Extract JSON from model output"""

    match = re.search(r"\{.*\}|\[.*\]", text, re.DOTALL)

    if match:
        return json.loads(match.group())

    raise ValueError("No JSON found in response")


def run_agent(task):

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": task},
    ]

    for step in range(15):

        reply = ask_llm(messages)

        print("AI:", reply)

        if "DONE" in reply:
            print("Task completed.")
            break

        try:

            action = extract_json(reply)

            if isinstance(action, list):
                actions = action
            else:
                actions = [action]

            for step_action in actions:

                tool_name = step_action["tool"]
                args = step_action.get("args", {})

                if tool_name not in TOOLS:
                    print("Unknown tool:", tool_name)
                    continue

                tool_function = TOOLS[tool_name]

                # filter invalid arguments
                allowed_params = inspect.signature(tool_function).parameters

                filtered_args = {
                    k: v for k, v in args.items()
                    if k in allowed_params
                }

                result = tool_function(**filtered_args)

                print("TOOL RESULT:", result)

                # Add messages safely (convert result to JSON string)
                messages.append({
                    "role": "assistant",
                    "content": reply
                })

                messages.append({
                    "role": "tool",
                    "content": json.dumps(result)
                })

        except Exception as e:

            print("Error:", e)
            break