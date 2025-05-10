import pandas as pd
from typing import List
from fastapi import HTTPException

class ExcelProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        try:
            print(f"Reading Excel file: {file_path}")
            self.excel_data = pd.ExcelFile(file_path)
            self.cached_data = {sheet: pd.read_excel(self.excel_data, sheet_name=sheet, header=None) for sheet in self.excel_data.sheet_names}
            # print(f"Excel file read successfully with sheets: {self.excel_data.sheet_names}")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error reading Excel file: {str(e)}")
        
    def get_table_names(self) -> List[str]:
        """Return the list of table names within each sheet in the Excel file."""
        table_names = []
        
        for sheet_name in self.excel_data.sheet_names:
            df = self.cached_data[sheet_name]
            
            # Loop through the sheet to find the potential table names
            for i in range(df.shape[0]):
                row = df.iloc[i]
                
                # If the first column has a non-null value (assuming it is the table name)
                if pd.notnull(row[0]):
                    table_names.append(row[0])  # Append the first non-empty cell in each table section as the table name
        return table_names
    
    def get_row_names(self, table_name: str) -> List[str]:
        """Returns the first column values (row names) of the specified table."""
        for sheet_name in self.excel_data.sheet_names:
            df = self.cached_data[sheet_name]
            
            # Check for the table within the sheet
            for i in range(df.shape[0]):
                row = df.iloc[i]
                
                if pd.notnull(row[0]) and row[0] == table_name:
                    # This is the start of the table, extract row names
                    row_names = df.iloc[i+1:, 0].dropna().tolist()  # Get the first column from the next row onward
                    return row_names
        
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found.")
        
    def get_row_sum(self, table_name: str, row_name: str) -> float:
        """Calculates the sum of numerical values in the specified row of a table."""
        for sheet_name in self.excel_data.sheet_names:
            df = self.cached_data[sheet_name]
            
            # Look for the table name and find the rows
            for i in range(df.shape[0]):
                row = df.iloc[i]
                
                if pd.notnull(row[0]) and row[0] == table_name:
                    # Once the table is found, look for the row in that table
                    row_data = df.iloc[i+1:, :]
                    target_row = row_data[row_data.iloc[:, 0] == row_name]
                    
                    if not target_row.empty:
                        # Extract numerical values and sum them up
                        values = target_row.iloc[0, 1:].dropna()
                        numeric_values = [float(val) for val in values if isinstance(val, (int, float))]
                        total_sum = sum(numeric_values) if numeric_values else 0.0
                        return total_sum
        
        raise HTTPException(status_code=404, detail=f"Row '{row_name}' not found in table '{table_name}'.")
