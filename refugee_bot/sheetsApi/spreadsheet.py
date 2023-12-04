import os
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import httplib2


def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "/refugee-telegram-bot-10551ef6a319.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)

sheet_id = '1pgFTzzf89PeUBkOzNpl02JhPZB74XMQmcraSgzFxnFQ'

def get_data(range):
    return get_service_sacc().spreadsheets().values().get(spreadsheetId=sheet_id, range=range).execute()

def batchGet_data(ranges):
    return get_service_sacc().spreadsheets().values().batchGet(spreadsheetId=sheet_id, ranges=ranges).execute()

ranges = ["Лист1!B1:E1",
          "Лист1!A2:A82",
          "Лист1!B2:E82"]

sheet_data = get_service_sacc().spreadsheets().values().batchGet(spreadsheetId=sheet_id, ranges=ranges).execute()

sheet_values = []

sheet_values.append(sheet_data['valueRanges'][0]['values'][0])
sheet_values.append([])

print(sheet_values)

count = 0
index = 0
for i in range(len(sheet_data['valueRanges'][1]['values'])):
    
    if sheet_data['valueRanges'][1]['values'][i] != []:
        sheet_values[1].append(sheet_data['valueRanges'][1]['values'][i])
        # print(sheet_values)
        if index != 0:
            sheet_values[1][index-1].append(count)
        index = index + 1
        # print(index)
        if i != len(sheet_data['valueRanges'][1]['values']) - 1:
            count = 0
        else: 
            sheet_values[1][index-1].append(count + 1)
            
    else: 
        count = count + 1
        
sheet_values.append(sheet_data['valueRanges'][2]['values'])
    
print(sheet_values[2])
print(sheet_values[1][0][1])
print(sheet_values[2][0][0])

issues_index = []

for j in range(len(sheet_values[1])):
    for i in range(sheet_values[1][j][1]):
        if sheet_values[2][i][1].find('t.me/') == -1:
            issues_index.append([j, i])

print(issues_index)

print(len(sheet_values[2]), sheet_values[2][9][1])