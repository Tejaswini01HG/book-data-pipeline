# End-to-End Book Data Pipeline & Analytics System

## 1. Project Overview

This project is an end-to-end book data pipeline developed using Python. It collects book information from the Books to Scrape website, stores the data in a SQLite database, provides REST APIs using FastAPI, and performs data processing and visualization using Pandas and Matplotlib.

The project demonstrates the complete flow of data from web scraping to database storage, API access, data processing, CSV export, and visualization.

## 2. End-to-End Pipeline

Books to Scrape
       ↓
Web Scraping
(scraper.py)
       ↓
SQLite Database
(books.db)
       ↓
FastAPI REST API
(main.py)
       ↓
Python API Client
(client.py)
       ↓
Pandas DataFrame
       ↓
CSV Export + Visualization
       ↓
Price vs Rating Graph

FEATURES:

Scrapes the first 20 books from Books to Scrape
Extracts the following information:
Book title
Price
Stock availability
Rating
Converts book ratings from text values such as One, Two, Three, Four, and Five into numeric values from 1 to 5
Stores scraped data in a SQLite database
Implements CRUD operations using an object-oriented database manager
Provides REST API endpoints using FastAPI
Uses Pydantic for API data validation
Retrieves API data using Python Requests
Loads API data into a Pandas DataFrame
Exports book data to a CSV file
Generates a Price vs Rating scatter plot using Matplotlib

Technologies Used:

Python
Requests
BeautifulSoup
SQLite
FastAPI
Uvicorn
Pandas
Matplotlib

