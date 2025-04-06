# LangChain SQL Query Generator

This project is a **Streamlit application** that allows users to generate SQL queries, execute them on a PostgreSQL database, and get answers to their questions. It leverages **LangChain**, **Google Generative AI (Gemini model)**, and **Streamlit** to provide an interactive interface for querying databases.

---

## Features

- **Generate SQL Queries**: Automatically generate SQL queries based on natural language questions.
- **Execute Queries**: Run the generated SQL queries on a connected PostgreSQL database.
- **Answer Generation**: Provide human-readable answers based on the query results.
- **Predefined Questions**: Includes a set of sample questions for quick testing.
- **Custom Questions**: Users can input their own questions for SQL query generation.

---

## Installation

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repo-name>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your database credentials.

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser (usually at `http://localhost:8501`).

---

## Usage

1. **Select a Sample Question**:
   - Use the dropdown menu to select a predefined question.
   - Example: *"What is the salary of Alice Johnson?"*

2. **Enter a Custom Question**:
   - Type your own question in the text input field.

3. **Submit the Question**:
   - Click the **Submit** button to generate the SQL query, execute it, and get the answer.

4. **View Results**:
   - The app will display:
     - The generated SQL query.
     - The query result from the database.
     - A human-readable answer to the question.

---

## Sample Questions

The app includes the following predefined questions:
1. What is the salary of Alice Johnson?
2. Who are the employees working in the Engineering department?
3. Which employees were hired before 2020?
4. How many employees are in each department?
5. What are the details of Project Alpha?
6. List employees along with the projects they are assigned to.

---
