# FastAPI Excel Processor

## Overview
This FastAPI application processes Excel files (`.xls` or `.xlsx`) and exposes endpoints to interact with their data. It supports uploading Excel files dynamically and processes them to list tables, retrieve row names, and calculate row sums.

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ajith-Kumar-Nelliparthi/IRIS_Assignment.git
   cd IRIS_ASSIGNMENT

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Run the Application**:
   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 9090 --reload

## Endpoints
- POST /upload_excel: Upload an .xls or .xlsx file to be processed.
- GET /list_tables: Lists all table (sheet) names in the uploaded Excel file.
- GET /get_table_details?table_name=<table_name>: Returns the row names (first column values) for the specified table.
- GET /row_sum?table_name=<table_name>&row_name=<row_name>: Calculates the sum of numerical values in the specified row.

## Testing
- Run tests using:
   ```bash
   pytest

## Results
- ![Screenshot 2025-05-10 100842](https://github.com/user-attachments/assets/f054eac8-0715-4a74-86a0-c016dfb3618d)
- ![Screenshot 2025-05-10 100919](https://github.com/user-attachments/assets/84cd63e6-d1a8-40e3-b132-21fbcf68b85a)
- ![Screenshot 2025-05-10 100951](https://github.com/user-attachments/assets/962823c3-4283-4441-b3d8-692b68f09ec5)



## Postman Collection
Import postman_collection.json into Postman to test the endpoints. First, upload an Excel file using the /upload_excel endpoint, then test the other endpoints.

## Potential Improvements
- Support for additional file formats (e.g., .csv).
- Advanced data operations (e.g., filtering, aggregations).
- Frontend UI for file upload and data visualization.
- Caching parsed Excel data for faster responses.
- Authentication to secure endpoints.

## Missed Edge Cases
- Empty or corrupted Excel files.
- Malformed table or row names (e.g., special characters).
- Non-numerical data in rows for /row_sum.
- Large Excel files causing memory issues.
- Concurrent file uploads overwriting existing files.




