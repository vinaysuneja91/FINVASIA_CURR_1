import pygsheets
import pandas as pd
# authorization


def read_from_gsheet(gsheet_name, sheet_no):
    gc = pygsheets.authorize(
        service_file='gstocks-api.json')
    sh = gc.open(gsheet_name)
    wks = sh[sheet_no]
    #cell_data = wks.cell((1,1))
    #all_records = wks.get_all_records()
    all_records = wks.get_as_df()
    return  all_records

def write_to_gsheet(df, gsheet_name, sheet_no):
    gc = pygsheets.authorize(
        service_file='gstocks-api.json')
    # open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open(gsheet_name)
    # select the first sheet
    wks = sh[sheet_no]
    # clear sheet
    wks.clear()
    # update the first sheet with df, starting at cell B2.
    wks.set_dataframe(df, (1, 1))

def write_to_gsheet_cell(gsheet_name, sheet_no, cell_no,cell_value):
    gc = pygsheets.authorize(
        service_file='gstocks-api.json')
    # open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open(gsheet_name)
    # select the first sheet
    wks = sh[sheet_no]
    wks.update_value(cell_no, cell_value)
    return 'completed'