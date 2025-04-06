import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
from langchain import hub
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(override=True)

SQL_HOST = os.getenv("SQL_HOST")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DB_NAME = os.getenv("SQL_DB_NAME")
SQL_PORT = os.getenv("SQL_PORT")

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Connect to the PostgreSQL database
connection_Uri = f"postgresql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DB_NAME}"
db = SQLDatabase.from_uri(connection_Uri)

# Pull the SQL query prompt from LangChain Hub
query_prompt_template = hub.pull("langchain-ai/sql-query-system-prompt")


def write_query(question: str):
    """Generate SQL query from the user's question."""
    prompt = query_prompt_template.invoke(
        {
            "dialect": db.dialect,
            "top_k": 10,
            "table_info": db.get_table_info(),
            "input": question,
        }
    )
    response = llm.invoke(prompt.to_string())

    extraction_prompt = """
    Please extract the SQL query from the following text and return only the SQL query without any additional characters or formatting:

    {response}

    SQL Query:
    """
    # Format the prompt with the actual response
    prompt = extraction_prompt.format(response=response)
    parsed_query = llm.invoke(prompt)
    return parsed_query.content


def execute_query(query: str):
    """Execute the SQL query."""
    execute_query_tool = QuerySQLDatabaseTool(db=db)
    return execute_query_tool.invoke(query)


def generate_answer(question: str, query: str, result: str):
    """Generate an answer using the query results."""
    prompt = (
        "Given the following user question, corresponding SQL query, "
        "and SQL result, answer the user question.\n\n"
        f'Question: {question}\n'
        f'SQL Query: {query}\n'
        f'SQL Result: {result}'
    )
    response = llm.invoke(prompt)
    return response.content


# Streamlit UI
st.title("LangChain SQL Query Generator")
st.write("Ask a question, and the app will generate a SQL query, execute it, and provide an answer.")

# Sample questions
sample_questions = [
    "What is the salary of Alice Johnson?",
    "Who are the employees working in the Engineering department?",
    "Which employees were hired before 2020?",
    "How many employees are in each department?",
    "What are the details of Project Alpha?",
    "List employees along with the projects they are assigned to."
]

# Add a dropdown for sample questions
selected_question = st.selectbox("Select a sample question:", [""] + sample_questions)

# Add a text input for custom questions
question = st.text_input("Or enter your custom question:", value=selected_question)

if st.button("Submit"):
    if question:
        try:
            query = write_query(question)
            st.write("Generated SQL Query:")
            st.code(query)

            result = execute_query(query)
            st.write("Query Result:")
            st.write(result)

            answer = generate_answer(question, query, result)
            st.write("Answer to your question:")
            st.write(answer)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")