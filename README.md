# 🤖 PyBot – Rule Based Python Chatbot

PyBot is a **simple rule-based chatbot built using Python**.  
It interacts with users through predefined responses, greets them based on the current time, and supports basic conversations related to greetings, motivation, and Python programming.

This project is ideal for **beginners learning Python**, especially concepts like functions, dictionaries, loops, and string handling.

---

## ✨ Features

- 🕒 Time-based greeting (Morning / Afternoon / Evening / Night)
- 💬 Interactive chatbot conversation
- 🧠 Rule-based response system using dictionaries
- 🧩 Modular code using functions
- 📚 Programming-related responses (Python basics)
- 💪 Motivation & small-talk support
- ❌ Exit command using `bye`

---

## 🧠 Concepts Used

- 🧾 Variables  
- 📚 Dictionaries (key–value pairs)  
- 🧠 User-defined Functions  
- 🔄 While Loop  
- 🔀 Conditional Statements (`if-elif-else`)  
- ⌨️ User Input Handling  
- 🧵 String Formatting (f-strings)  
- 🕒 Date & Time module (`datetime`)  

---

## ⚙️ How the Program Works

1. 🟢 The program starts by asking the user’s name.
2. 🕒 Based on the current system time, PyBot greets the user:
   - Morning
   - Afternoon
   - Evening
   - Night
3. 🤖 PyBot introduces itself and waits for user questions.
4. 💬 User input is matched with predefined keywords.
5. 📖 If a keyword matches, PyBot replies accordingly.
6. 🔁 The chat continues until the user types **`bye`**.

---

## 🧩 Functions Overview

| Function Name | Description |
|--------------|------------|
| `greet_user()` | Greets the user based on current time |
| `get_pybot_response()` | Returns chatbot reply based on user input |
| `start_pybot()` | Runs the main chatbot conversation loop |

---

## 📂 Project Structure

```text
PyBot/
├── main.py
└── README.md
