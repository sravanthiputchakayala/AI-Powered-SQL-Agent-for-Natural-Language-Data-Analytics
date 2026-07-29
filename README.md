# AI-Powered SQL Agent for Natural Language Data Analytics

An AI-powered SQL Agent that enables users to interact with structured datasets using natural language. Instead of manually writing SQL queries, users can upload CSV/Excel files, ask questions in plain English, and receive AI-generated SQL queries with data-driven insights.

## 🚀 Project Overview

Traditional data analysis requires users to understand SQL and database structures. This project uses Large Language Models (LLMs) and AI Agents to bridge the gap between users and databases.

The system allows users to:

* Upload structured datasets (CSV/Excel)
* Automatically store data in PostgreSQL
* Ask questions using natural language
* Generate SQL queries automatically
* Execute queries on the database
* Receive meaningful analytical responses

---

## ✨ Features

✅ Natural Language to SQL Generation
✅ AI-powered database querying
✅ CSV and Excel dataset upload
✅ Automatic PostgreSQL table creation
✅ Conversational data analysis
✅ User authentication system
✅ Dynamic database schema understanding
✅ SQL-based insights generation

---

## 🏗️ Architecture

```
User
 |
 | Natural Language Question
 |
 v
Streamlit Application
 |
 v
LangChain SQL Agent
 |
 v
Large Language Model (Claude Sonnet 4)
 |
 v
Generated SQL Query
 |
 v
PostgreSQL Database
 |
 v
Analytical Response
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### AI / LLM

* Claude Sonnet 4
* OpenRouter API
* LangChain SQL Agent

### Database

* PostgreSQL
* SQLAlchemy

### Data Processing

* Pandas

### Frontend

* Streamlit

### Authentication

* PostgreSQL User Management
* Password Hashing

---

## 📂 Project Structure

```
AI-Powered-SQL-Agent/

│
├── app.py                  # Streamlit application
├── sql_agent.py            # SQL Agent implementation
├── auth.py                 # User authentication
├── db.py                   # Database connection testing
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files
```

---

## ⚙️ Installation and Setup

### 1. Clone Repository

```bash
git clone https://github.com/sravanthiputchakayala/SQL-AI-Agent.git

cd SQL-AI-Agent
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password

OPENROUTER_API_KEY=your_api_key
```

---

### 5. Run Application

Start Streamlit:

```bash
streamlit run app.py
```

---

## 💡 Example Usage

User uploads:

```
Loan_default.csv
```

User asks:

```
What factors contribute most to loan defaults?
```

The AI Agent:

1. Understands the question
2. Analyzes database schema
3. Generates SQL query
4. Executes query
5. Provides insights

---

## 📊 Future Improvements

* Automated data visualization generation
* SQL query explanation panel
* Cloud deployment
* Advanced data profiling
* Multi-user dataset management
* Chat history storage

---

## 🎯 Learning Outcomes

Through this project, I explored:

* Building LLM-powered applications
* AI Agent workflows
* Natural Language to SQL systems
* Database integration with Generative AI
* Building practical AI analytics solutions

---

## 👩‍💻 Author

**Sravanthi Putchakayala**

GitHub:
https://github.com/sravanthiputchakayala


---

## ⭐ If you find this project interesting, feel free to star the repository!
