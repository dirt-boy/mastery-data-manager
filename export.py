import gspread
import json
import aggregate_classroom_info as aggregate

SERVICE_ACCOUNT_PATH = "/Users/gg/NerdStuff/mastery-data-manager/data/etc/gspread_service_account.json"
LIVE_DATA_01_ID =	"19zeDtQOfzGAkhrl6fcX23E1D3_3_wSVFFzvMk6Sn6a8"
LIVE_DATA_02_ID =	"1yplB1cUQN9KPfWQR2O1_RkZ3izxVmjw1Pk4b7ClKehY"
TEST = "1IDIfxXiHGLR_LLuyEt2pNBVvcNoNfDZtUqo0YG5UHm0"
SHEET_UPDATE_CELL_REFERENCE = "Raw Data!A1"
HEADERS = ["title", "criteria_tag", "criteria_content_description", "criteria_content_level_title", "criteria_content_point_value", "student", "flag", "class"]



gsheets = gspread.service_account(SERVICE_ACCOUNT_PATH)
data_01 = gsheets.open_by_key(LIVE_DATA_01_ID)
data_02 = gsheets.open_by_key(LIVE_DATA_02_ID)
test = gsheets.open_by_key(TEST)

DATA_01_LIST = [data_01, "Independence 20-21", "JOCHS 20-21", "Life Academy 20-21", "Lighthouse & Balboa 20-21", "TMAHS 20-21", "Intrinsic S1 20-21", "JCP 20-21", "DDC 20-21", "Eagle 20-21", "SSCHS 20-21", "ChiTech/UICCP 20-21"]
DATA_02_LIST = [data_02, "20-21 UAG/Code Nation: Intro to Web Development", "Code Nation @ DRW", "Code Nation @ Noble Triangle", "Code Quickstart 20-21", "WCHS Intro to Coding", "WHSAT Intro to Web Development (T/Th)", "WHSAT Intro to Web Development (W/F)"]
ALL_DATA_LIST = [DATA_01_LIST, DATA_02_LIST]

csv = open("results/grades.csv", "r").read()


def csvToList(csv):
	csv = csv.split('\n')
	csv = [item.split(',') for item in csv]	
	return csv


##wtf is going wrong here????
def split(csv, dataList):
	dataset = []
	classIndex = csv[0].index(' class')
	for val in dataList:
		res = [HEADERS]
		className = val[0]
		for row in csv:
			if classIndex < len(row) and row[classIndex] in val:
				res.append(row)
		dataset.append({className:res})
	return dataset

def export(csv, worksheet, sheet):
	#aggregate.run()
	worksheet.values_update(
	    sheet,
	    params={
	        'valueInputOption': 'USER_ENTERED'
	    },
	    body={
	        'values': csv
	    }
	)

if __name__ == '__main__':
	csv = csvToList(csv)
	splitList = split(csv, ALL_DATA_LIST)
	#print(splitList)
	for i, item in enumerate(splitList):
		#export(vals.values(), vals.keys(), SHEET_UPDATE_CELL_REFERENCE)
		key = list(item.keys())[0]
		export(item[key], key, SHEET_UPDATE_CELL_REFERENCE)
	



	
