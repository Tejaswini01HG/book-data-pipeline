# End-to-End Book Data Pipeline & Analytics System

## 1. Project Overview

This project is an end-to-end book data pipeline developed using Python. It collects book information from the Books to Scrape website, stores the data in a SQLite database, provides REST APIs using FastAPI, and performs data processing and visualization using Pandas and Matplotlib.

The project demonstrates the complete flow of data from web scraping to database storage, API access, data processing, CSV export, and visualization.

## 2. End-to-End Pipeline 

1.Books to Scrape
       
2.Web Scraping
(scraper.py)
       
3.SQLite Database
(books.db)
       
4.FastAPI REST API
(main.py)
       
5.Python API Client
(client.py)
       
6.Pandas DataFrame
       
7.CSV Export + Visualization
       
8.Price vs Rating Graph

## 3. Features
    
-Scrapes the first 20 books from Books to Scrape
-Extracts the following information:
-Book title
-Price
-Stock availability
-Rating
-Converts book ratings from text values such as One, Two, Three, Four, and Five into numeric values from 1 to 5
-Stores scraped data in a SQLite database
-Implements CRUD operations using an object-oriented database manager
-Provides REST API endpoints using FastAPI
-Uses Pydantic for API data validation
-Retrieves API data using Python Requests
-Loads API data into a Pandas DataFrame
-Exports book data to a CSV file
-Generates a Price vs Rating scatter plot using Matplotlib
## Technologies Used

- Python
- Requests
- BeautifulSoup
- SQLite
- FastAPI
- Pydantic
- Uvicorn
- Pandas
- Matplotlib
  ## Project Structure

```text
book_pipeline_project/
├── scraper.py
├── database.py
├── main.py
├── client.py
├── requirements.txt
├── books.db
├── exported_books.csv
└── price_vs_rating.png

## How to Run the Project

### Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Web Scraper

```bash
python scraper.py
```

### Step 5: Start FastAPI Server

```bash
uvicorn main:app --reload
```

### Step 6: Open FastAPI in Browser

```text
http://127.0.0.1:8000
```

### Step 7: Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

### Step 8: Run the Python Client

Open a new terminal, navigate to the project folder, and activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Then run:

```bash
python client.py
```



