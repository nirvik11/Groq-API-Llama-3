import streamlit as st
import pandas as pd
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_csv_agent

st.title("Financial Data Query Application")

csv_file_path = "final_csv.csv"

st.write("### Query the CSV File:")
query = st.text_input("Enter your query")

if query:
    try:
        # The 'model' specifies the architecture and configuration, here "llama3-70b-8192" which signifies a LLaMA 3 model with 70 billion parameters and an 8192 token context window.
        llm = ChatGroq(temperature=0, model="llama3-70b-8192", api_key='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')
        
        # The create_csv_agent function ties the LLM with the provided CSV file.
        agent = create_csv_agent(llm, csv_file_path, verbose=True, allow_dangerous_code=True)
        
        # The invoke function sends the user's query to the agent. 
        # Behind the scenes, the query is interpreted and converted into instructions for analyzing the CSV file.
        # The LLM processes the query contextually, applying operations like filtering, aggregation, or computation directly on the data.
        # The response returned by the LLM is then presented in a structured format suitable for display.
        response = agent.invoke(query)
        
        st.write("### Response:")
        st.write(response['output'])
        
    except Exception as e:
        st.error(f"Error: {str(e)}")

