# ai-file-organizer-agent# AI Desktop Automation

This project demonstrates two approaches for automating desktop file organization:

1. **Rule-based automation using Python scripts**
2. **Generative AI automation using an AI agent powered by Ollama**

Both systems organize files on your Desktop but use different architectures.

---

# What is Generative AI Automation?

Generative AI automation uses large language models (LLMs) to interpret natural language instructions and decide which actions to perform.

Instead of hardcoded logic, the AI agent:

1. Understands a user prompt
2. Plans actions
3. Calls tools (Python functions)
4. Executes tasks autonomously

Example prompt:

```
Organize my desktop files
```

The AI agent will:

1. Scan desktop files
2. Create required folders
3. Move files into appropriate folders

---

# Project Structure

```
ai-desktop-automation
│
├── python_scripts
│
├── ai_agents
│
├── README.md
└── requirements.txt
```

---

# 1. Python Scripts (Traditional Automation)

Location:

```
python_scripts/
```

This implementation uses predefined rules to categorize files by extension.

Example mapping:

```
Images → .png .jpg .jpeg
Documents → .pdf .docx .txt
Videos → .mp4 .mkv
```

Run:

```
python desktop_organizer.py
```

---

# 2. AI Agent (Generative AI Automation)

Location:

```
ai_agents/
```

The AI agent uses **Ollama LLM** to interpret user prompts and decide actions dynamically.

Example:

```
python agent.py run "Clean my desktop"
```

The agent will:

1. Scan desktop files
2. Decide folders
3. Move files automatically

---

# Requirements

Install dependencies:

```
pip install -r requirements.txt
```

Install Ollama:

https://ollama.com

Run a model:

```
ollama run llama3
```

---

# Edge Cases Handled

• Desktop already organized
• File already moved
• Folder already exists
• Missing files

---

# Learning Goals

This project demonstrates:

- Python automation
- CLI tools
- Local LLM usage with Ollama
- AI agent tool calling
- Autonomous task execution

---

# Future Improvements

- Duplicate file detection
- AI file classification
- GUI dashboard
- Multi-agent architecture
- Voice commands

---
