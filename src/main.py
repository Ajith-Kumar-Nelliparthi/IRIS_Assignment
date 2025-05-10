from fastapi import FastAPI, Query, HTTPException
from src.excel_processor import ExcelProcessor
from src.models import TableListResponse, TableDetailsResponse, RowSumResponse

app = FastAPI(
    title="FastAPI Excel Processor",
    description="A FastAPI application to process Excel files and perform operations on them.",
    version="1.0.0"
)

# Initialize the ExcelProcessor with the path to your Excel file
excel_processor = ExcelProcessor("data/capbudg.xls")

@app.get("/list_tables", response_model=TableListResponse)
async def list_tables():
    """
    Returns a list of all table names in the Excel file.
    """
    tables = excel_processor.get_table_names()
    print("Table Names:", tables)
    return {"tables": tables}



@app.get("/get_table_details", response_model=TableDetailsResponse)
async def get_table_details(table_name: str = Query(..., description="Name of the table to retrieve details for")):
    """
    Returns the row names for the specified table.
    """
    try:
        row_names = excel_processor.get_row_names(table_name)
        print(f"Row Names for {table_name}:", row_names)
        return {"table_name": table_name, "row_names": row_names}
    except HTTPException as e:
        raise e  # Re-raise the HTTPException for FastAPI to handle it

@app.get("/row_sum", response_model=RowSumResponse)
async def row_sum(
    table_name: str = Query(..., description="Name of the table"),
    row_name: str = Query(..., description="Name of the row")
):
    """
    Returns the sum of numerical values in the specified row of the table.
    """
    try:
        sum_value = excel_processor.get_row_sum(table_name, row_name)
        return {"table_name": table_name, "row_name": row_name, "sum": sum_value}
    except HTTPException as e:
        raise e  
