from pydantic import BaseModel
from typing import List, Optional

class TableListResponse(BaseModel):
    """Response model for listing all available table names in the Excel file."""
    tables: List[str]

class TableDetailsResponse(BaseModel):
    """Response model for providing details about a specific table, including its row names."""
    table_name: str
    row_names: List[str]

class RowSumResponse(BaseModel):
    """Response model for providing the sum of values in a specified row."""
    table_name: str
    row_name: str
    sum: float
