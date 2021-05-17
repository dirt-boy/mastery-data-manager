import gspread
import aggregate_classroom_info as aggregate

SERVICE_ACCOUNT_PATH = "/Users/gg/NerdStuff/mastery-data-manager/data/etc/gspread_service_account.json"
LIVE_DATA_01_ID =	"19zeDtQOfzGAkhrl6fcX23E1D3_3_wSVFFzvMk6Sn6a8"
LIVE_DATA_02_ID =	"1yplB1cUQN9KPfWQR2O1_RkZ3izxVmjw1Pk4b7ClKehY"
TEST = "1IDIfxXiHGLR_LLuyEt2pNBVvcNoNfDZtUqo0YG5UHm0"



gsheets = gspread.service_account(SERVICE_ACCOUNT_PATH)
data_01 = gsheets.open_by_key(LIVE_DATA_01_ID)
data_01 = gsheets.open_by_key(LIVE_DATA_02_ID)
test = gsheets.open_by_key(TEST)

csv = open("results/grades.csv", "r").read()

#ugh now i need to convert the csv into, like, an http request... list of rows (lists)


def export():
	#aggregate.run()
	test.values_update(
	    'RAW DATA!A1',
	    params={
	        'valueInputOption': 'USER_ENTERED'
	    },
	    body={
	        'values': [['HELLO']]
	    }
	)

if __name__ == '__main__':
	export()