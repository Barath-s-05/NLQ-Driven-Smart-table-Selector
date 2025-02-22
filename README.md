# NLQ-Driven-Smart-table-Selector

An AI-driven system that intelligently selects the most relevant tables from a database schema based on natural language queries (NLQs). It seamlessly integrates with an NL-to-SQL model (such as OpenAI's GPT) to generate precise SQL queries.

---

## 🚀 Features
- **Natural Language Understanding**: Extracts essential keywords from user input.
- **Table Relevance Ranking**: Implements fuzzy matching to determine the most relevant tables.
- **Dynamic Table Selection**: Filters and selects only necessary tables for the query.
- **AI-Powered SQL Query Generation**: Uses an NL-to-SQL model to construct SQL queries.
- **Interactive UI**: Provides a user-friendly interface for query input and execution.

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/nl-to-sql-selector.git
cd nl-to-sql-selector
```

### 2️⃣ Install Dependencies
Ensure you have Python 3 installed, then run:
```sh
pip install -r requirements.txt
```

---

## 📌 Usage

### Run the Application
To start the backend:
```sh
python app.py
```
To launch the UI:
```sh
streamlit run ui.py
```

### Example Query
```python
query = "Get all customer emails and names"
```
#### Output:
```json
{
  "customers": {
    "columns": ["id", "name", "email", "created_at", "total_spent"]
  }
}
```
#### Generated SQL Query:
```sql
SELECT name, email FROM customers;
```

---

## 📂 Project Structure
```
nl-to-sql-selector/
 ├── app.py           # Core application logic
 ├── ui.py            # User interface implementation
 ├── schema.json      # Database schema in JSON format
 ├── requirements.txt # Project dependencies
 ├── README.md        # Documentation
```

---

## 🔧 Configuration
- **Schema File**: Ensure `schema.json` contains the correct database schema.
- **Threshold Score**: Adjust the threshold in `select_relevant_tables()` to fine-tune table selection accuracy.
- **OpenAI API Key**: Configure OpenAI properly to generate SQL queries.

---

## 📌 Dependencies
- `nltk`
- `openai`

---

## 🚀 Future Enhancements
📌 Planned features for future updates:
- **Visual Representation of Schema**: Graphical representation of selected tables and relationships.
- **Improved Table Ranking**: Leverage transformer-based models for more accurate table selection.
- **Multi-Language Support**: Expand NLP capabilities to support multiple languages.
- **Customizable SQL Output**: User-configurable SQL formatting and optimization.

---

