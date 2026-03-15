import gspread
from google.oauth2.service_account import Credentials

def append_expense_row(expense_data: dict):
    """
    Append expense data to Google Sheets
    """

    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credentials/service_account.json",
        scopes=SCOPES
    )


    client = gspread.authorize(creds)
    sheet = client.open_by_key("1C7DohR-yZI4S1h1rzdHeag2e7ebAjG_mz1KVy_z7TjE").sheet1

    row = [
        expense_data.get("document_date"),
        expense_data.get("vendor_name"),
        expense_data.get("document_number"),
        expense_data.get("subtotal"),
        expense_data.get("vat_amount"),
        expense_data.get("wht_amount"),
        expense_data.get("total_amount"),
        expense_data.get("payment_method"),
        expense_data.get("VAT"),
        expense_data.get("WHT")
    ]

    sheet.append_row(row)

    return {"status": "success"}
