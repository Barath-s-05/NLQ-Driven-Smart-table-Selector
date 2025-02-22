import json
import spacy
from fastapi import FastAPI

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Load database schema from JSON file
with open("schema.json", "r") as f:
    schema = json.load(f)

app = FastAPI()

def extract_keywords(query: str):
    """Extracts important keywords from a natural language query."""
    doc = nlp(query)
    return [token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"]]

def get_relevant_tables(schema, keywords):
    """Matches keywords with table names and columns in the schema."""
    relevant_tables = {}
    for table_name, table_details in schema.items():
        if any(word in table_name or any(word in col for col in table_details["columns"]) for word in keywords):
            relevant_tables[table_name] = table_details
    return relevant_tables

@app.get("/select_tables/")
def select_tables(query: str):
    """API endpoint to return relevant tables for a given query."""
    keywords = extract_keywords(query)
    relevant_tables = get_relevant_tables(schema, keywords)
    return {"selected_tables": relevant_tables}
