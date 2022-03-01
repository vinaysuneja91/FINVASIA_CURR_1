## Read from GSheet
## Read PriceData
## Read Open Orders and Position
## Place Orders based on GSheet data
## Write back to Gsheet
## Stop/Terminate ?
##pip install -r requirements.txt
## delpoy this on gcloud

import pandas as pd

from gsheets import write_to_gsheet,read_from_gsheet,write_to_gsheet_cell
from finvasia import api

# read_from_gsheet
print('Read from gsheet')
all_records_df = read_from_gsheet( 'finvasia-algo', 1)
print(all_records_df)
#print (cell_data.get_json())
#print (type(cell_data.fetch('value')))
#print (cell_data.fetch('value'))


return_status = write_to_gsheet_cell('finvasia-algo', 1,'N2', 'FROM ALGO')
print(return_status)
ret = api.place_order(buy_or_sell='B', product_type='C',
                       exchange='NSE', tradingsymbol='CANBK-EQ', 
                       quantity=1, discloseqty=0,price_type='SL-LMT', price=200.00, trigger_price=199.50,
                       retention='DAY', remarks='my_order_001')


#list1 = ['1','2','3']
#df = pd.DataFrame(list1,columns = ['SNO'])
## write_to_gsheet
#print('Writing to gsheet')
#write_to_gsheet(df, 'finvasia-algo', 1)

# Update a single cell.
#wks.update_value('A1', "Numbers on Stuff")

#

