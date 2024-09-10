# import requests
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# def fetch_data(api_url):
#     response = requests.get(api_url)
#     response.raise_for_status()  # Check for request errors
#     return response.json()

# def post_to_google_sheets(data, spreadsheet_id, range_name):
#     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
#     credentials = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/service-account-key.json', scope)
#     client = gspread.authorize(credentials)

#     spreadsheet = client.open_by_key(spreadsheet_id)
#     worksheet = spreadsheet.sheet1  # You can also use .get_worksheet(index) for specific sheets

#     worksheet.update(range_name, data)

# # Example usage
# api_url = 'https://api.example.com/data'
# spreadsheet_id = 'your-google-spreadsheet-id'
# range_name = 'Sheet1!A1'

# data = fetch_data(api_url)
# post_to_google_sheets(data, spreadsheet_id, range_name)

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# def post_to_google_sheets(data, spreadsheet_id, range_name):
#     # Setup the credentials
#     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
#     credentials = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/service-account-key.json', scope)
#     client = gspread.authorize(credentials)

#     # Open the spreadsheet by ID
#     spreadsheet = client.open_by_key(spreadsheet_id)
#     worksheet = spreadsheet.sheet1  # You can also use .get_worksheet(index) for specific sheets

#     # Write data to the sheet
#     # Assuming `data` is a list of lists (rows of data)
#     worksheet.update(range_name, data)

# spreadsheet_id = 'your-google-spreadsheet-id'
# range_name = 'Sheet1!A1'  # Adjust range as needed
# post_to_google_sheets(data, spreadsheet_id, range_name)


# import requests

# def fetch_data(api_url):
#     response = requests.get(api_url)
#     response.raise_for_status()  # Check for request errors
#     return response.json()

# api_url = 'https://api.example.com/data'
# data = fetch_data(api_url)
# print(data)
