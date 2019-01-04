#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""This scripts contains function that help dealing with language file for android

    Created by vietnh
"""

import re
import requests
from openpyxl import load_workbook
from openpyxl.styles import Font, colors

FILE_LANGUAGE = 'schedule.xlsx'

# Import language from excel files to android language files
def import_schedule():
    wb = load_workbook(filename = FILE_LANGUAGE, read_only=True)
    ws = wb.active


    for idx, row in enumerate(ws.rows):
        if idx >= 1: #ignore first row
            tableId = str(row[0].value)
            liftIds = str(row[1].value)
            siteId = str(row[2].value)
            customerId = str(row[3].value)
            workerId = str(row[4].value)
            goodIds = str(row[5].value)
            times = str(row[6].value)
            departure = str(row[7].value)
            arrival = str(row[8].value)
            startDate = str(row[9].value)
            endDate = str(row[10].value)
            token = str(row[11].value)
            loginUserId = str(row[12].value)
            deviceType = str(row[13].value)
            timezone = str(row[14].value)
            language = str(row[15].value)
            categoryId = str(row[16].value)
            packingMethodIds = str(row[17].value)
            isForkLift = str(row[18].value)
            note = str(row[19].value)
            scheduleType = str(row[20].value)
            gate = str(row[21].value)
            vehicleNames = str(row[22].value)
            startTime = str(row[23].value)
            endTime = str(row[24].value)
            status = str(row[25].value)

            url = "http://localhost:9000/api/schedule/update"

            payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"tableId\"\r\n\r\n" + tableId \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"liftIds\"\r\n\r\n" + liftIds \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"siteId\"\r\n\r\n" + siteId \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"customerId\"\r\n\r\n" + customerId \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"workerId\"\r\n\r\n" + workerId \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"goodIds\"\r\n\r\n" + goodIds \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"times\"\r\n\r\n " + times \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"departure\"\r\n\r\n" + departure \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"arrival\"\r\n\r\n" + arrival \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"startDate\"\r\n\r\n" + startDate \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"endDate\"\r\n\r\n" + endDate \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"token\"\r\n\r\n419e573248391a0e060a6db703fa4aa2\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"loginUserId\"\r\n\r\n" + loginUserId \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"deviceType\"\r\n\r\nA\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"timezone\"\r\n\r\nAsia/Ho_Chi_Minh\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\nen\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"categoryId\"\r\n\r\n" + categoryId \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"packingMethodIds\"\r\n\r\n" + packingMethodIds \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"isForkLift\"\r\n\r\n" + isForkLift \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"note\"\r\n\r\nThis is from postman\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"scheduleType\"\r\n\r\n " + scheduleType \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"gate\"\r\n\r\n" + gate \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"vehicleNames\"\r\n\r\n" + vehicleNames \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"startTime\"\r\n\r\n" + startTime \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"endTime\"\r\n\r\n" + endTime \
            + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"status\"\r\n\r\n" + status+ "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
            headers = {
                'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
                'Cache-Control': "no-cache",
                'Postman-Token': "58da3bfe-8f0e-abe5-efb7-33de280e7328"
                }

            response = requests.request("POST", url, data=payload, headers=headers)
            print "response for row", idx,":"
            print(response.text)



if __name__ == '__main__':
    import_schedule()
    

