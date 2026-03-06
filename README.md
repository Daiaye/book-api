# Books API

## **Project Overview**
This project is a RESTful API built with **FastAPI** and **SQLite**. It manages a dataset of over **5,000 book records** sourced from Kaggle, providing full CRUD (Create, Read, Update, Delete) functionality and multi-parameter search capabilities.
Link to Kaggle dataset: (https://www.kaggle.com/datasets/saurabhbagchi/books-dataset)

### **Key Features**
* **Full CRUD Lifecycle**: Managed via industry-standard HTTP methods (GET, POST, PUT, DELETE).
* **Search Engine**: Filtering by title, author, publisher, year, and average rating.
* **Automated Documentation**: Interactive Swagger UI for API testing.
* **Data Integrity**: Utilises Pydantic for strict input validation and type safety.

## **Setup & Installation**

### **1. Prerequisites**
Ensure you have **Python 3.10+** installed on your machine.

### **2. Environment Setup**
Create and activate a virtual environment to isolate project dependencies:

Create the environment
```bash
python -m venv .venv
```

Activate (Windows)
```bash
.\.venv\Scripts\activate
```

Activate (Mac/Linux)
```bash
source .venv/bin/activate
```

### **3. Install Dependencies**
This project uses several libraries for the API and database management. Install them using the included requirements file:
```bash
pip install -r requirements.txt
```

### **4. Add csv files to the project**
Create a folder called `data` in the root directory and paste the downloaded CSV files inside it.

```
BOOK-API/
├── data/
│   ├── books.csv
│   ├── ratings.csv
│   └── users.csv
```

### **5. Create the database**
```bash
python database.py
```

### **6. Import the records**
```bash
python import_data.py
```

### **7. Launch the API**
```bash
uvicorn main:app --reload
```

## API Access and Documentation
* Base URL: http://127.0.0.1:8000
* Interactive Documentation: http://127.0.0.1:8000/docs