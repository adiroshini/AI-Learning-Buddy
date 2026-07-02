# 🎓 AI Learning Buddy

> Learn Smarter with AI ✨

An AI-powered educational assistant built using **Google Gemini**, **Streamlit**, and **Prompt Engineering** as part of the **Infosys Springboard AI Empower(H)ER Program**.

---

## 📌 Project Overview

AI Learning Buddy is an interactive web application designed to make learning easier for students.

The application uses Google's Gemini Large Language Model to explain concepts in simple language, provide practical examples, generate quizzes, and answer educational questions.

The project demonstrates how Prompt Engineering can be used to create an AI tutor capable of adapting to different learning needs.

---

## 🎯 Objective

The main objective of this project is to create a beginner-friendly AI learning assistant that:

- Explains concepts in simple language
- Provides real-life examples
- Generates multiple-choice quizzes
- Answers educational questions
- Makes learning interactive and engaging

---

# ✨ Features

## 📖 Explain Concept

Explains any topic using beginner-friendly language.

- Easy English
- Step-by-step explanation
- Real-life analogy
- Key takeaways

---

## 🌍 Real-Life Example

Provides practical examples that help learners understand how concepts are used in everyday life.

---

## 📝 Generate Quiz

Creates:

- 5 Multiple Choice Questions
- Four options
- Correct Answer
- Explanation

---

## 💬 Ask Anything

Allows users to ask educational questions on any topic and receive AI-generated answers.

---

# 🧠 Prompt Engineering

The application uses carefully designed prompts for each learning activity.

Instead of sending a simple question to the AI model, customized prompts guide Gemini to produce:

- Beginner-friendly explanations
- Practical examples
- Structured quizzes
- Educational responses

Prompt Engineering helps improve both the quality and consistency of AI responses.

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Streamlit | Web Application |
| Google Gemini API | AI Model |
| Prompt Engineering | Response Optimization |
| GitHub | Version Control |
| Streamlit Community Cloud | Deployment |

---

# 🚀 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Demo

👉 **https://ai-learning-buddy-4whf6l9nanyiczfwrvbir5.streamlit.app/**

---

# 📂 Project Structure

```
AI-Learning-Buddy/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/adiroshini/AI-Learning-Buddy.git
```

Move into the project

```bash
cd AI-Learning-Buddy
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🔐 API Key Configuration

This project uses the Google Gemini API.

For security purposes, the API key is **not stored in the source code**.

Instead, it is accessed securely using Streamlit Secrets.

```python
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
```

---

# 📸 Sample Workflow

1. Enter a topic.
2. Choose a learning activity.
3. Click **Generate Response**.
4. Receive an AI-generated explanation.

---

# 📖 Learning Outcomes

Through this project, I learned:

- Prompt Engineering
- AI Application Development
- Streamlit
- Google Gemini API Integration
- GitHub
- Cloud Deployment
- Secure API Management

---

# 🌟 Future Improvements

- Voice Input
- Speech Output
- Chat History
- Dark Mode
- Multi-language Support
- Personalized Learning Progress
- PDF Notes Generation

---

# 👩‍💻 Author

**Roshini Adi**

B.Tech Computer Science Student

Infosys Springboard AI Empower(H)ER Program

---

# 🙏 Acknowledgements

- Infosys Springboard
- AI Empower(H)ER Program
- Google Gemini API
- Streamlit Community Cloud
