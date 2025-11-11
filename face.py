from openpyxl import load_workbook

# Path to the Excel file (adjust your username if needed)
file_path = r'"C:\Users\Meraj\Desktop\Book1.xlsx"'

# Load the workbook and select the active sheet
wb = load_workbook(file_path)
sheet = wb.active

# Add headings to the first row (change as needed)
sheet['A1'] = 'Name'
sheet['B1'] = 'ID'
sheet['C1'] = 'Attendance'

# Save the workbook
wb.save(file_path)
