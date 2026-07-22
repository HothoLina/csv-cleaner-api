# CSV Cleaner API

> A professional FastAPI service for automated CSV data cleaning, quality analysis, and reporting.

## Overview

CSV Cleaner API is a backend service built with **FastAPI** that automates the process of cleaning and analyzing CSV datasets. Instead of manually inspecting spreadsheets, users can upload a CSV file and receive a cleaned dataset along with a comprehensive data quality report.

This project demonstrates modern backend engineering practices including API development, data processing, automated testing, Docker containerization, configuration management, structured logging, and continuous integration.

---

## Features

### Data Processing

* Upload CSV files through a REST API
* Remove duplicate rows
* Remove completely empty rows
* Standardize column names
* Preserve original dataset for comparison

### Data Quality Reporting

* Dataset overview
* Row and column counts
* Missing value analysis (count & percentage)
* Duplicate row detection
* Current data types
* Suggested data types
* Confidence score for type suggestions
* Overall data quality score

### API Features

* FastAPI
* Automatic Swagger UI documentation
* Structured JSON responses
* Custom exception handling
* Download cleaned CSV files

### Engineering Features

* Environment variable configuration
* Centralized logging
* Modular project architecture
* Unit testing
* Integration testing
* Docker support
* Docker Compose support
* GitHub Actions CI workflow

---

## Architecture

```text
                Client
                   │
                   ▼
            FastAPI Endpoints
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 Data Cleaning Service   Report Service
        │                     │
        └──────────┬──────────┘
                   ▼
             Clean DataFrame
                   │
          Generate API Response
                   │
                   ▼
                JSON + CSV
```

---

## Tech Stack

| Category         | Technologies           |
| ---------------- | ---------------------- |
| Backend          | FastAPI, Uvicorn       |
| Language         | Python 3.12            |
| Data Processing  | Pandas                 |
| Testing          | Pytest                 |
| Containerization | Docker, Docker Compose |
| Version Control  | Git & GitHub           |
| Documentation    | Swagger UI (OpenAPI)   |

---

## Project Structure

```text
csv-cleaner-api/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── models/
│   └── main.py
│
├── uploads/
├── my_logs/
├── tests/
├── .github/
│   └── workflows/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/HothoLina/csv-cleaner-api.git

cd csv-cleaner-api
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the API

Development

```bash
uvicorn app.main:app --reload
```

Production

```bash
uvicorn app.main:app
```

Swagger UI

```
http://localhost:8000/docs
```

---

## Run with Docker

Build and run

```bash
docker compose up --build
```

Run after the image already exists

```bash
docker compose up
```

Stop

```bash
docker compose down
```

---

## Running Tests

Run all tests

```bash
pytest
```

Expected result

```text
====================
4 passed
====================
```

---

## Example Response

```json
{
  "message": "CSV cleaned successfully!",
  "rows_before": 3986,
  "rows_after": 3777,
  "duplicates_removed": 209,
  "quality_score": 92,
  "download_url": "/download/cleaned_file.csv"
}
```

---

## Why This Project?

This project was built to demonstrate practical backend software engineering skills rather than simply cleaning CSV files.

It showcases:

* REST API development
* Clean project architecture
* Data engineering fundamentals
* Error handling
* Logging
* Automated testing
* Containerization
* Continuous Integration
* Production-ready development practices

---

## Roadmap

* [x] CSV upload
* [x] Data cleaning
* [x] Data quality reporting
* [x] Quality scoring
* [x] Suggested data types
* [x] Logging
* [x] Environment variables
* [x] Custom exceptions
* [x] Unit tests
* [x] Integration tests
* [x] Docker
* [x] Docker Compose
* [x] GitHub Actions
* [ ] PostgreSQL support
* [ ] Authentication
* [ ] Cloud deployment
* [ ] Background processing

---

## Author

**Hotho**

Software Engineer focused on Backend Development, Data Engineering, and Python Automation.

GitHub: https://github.com/HothoLina

---

## License

This project is released under the MIT License.
