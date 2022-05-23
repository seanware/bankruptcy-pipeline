# load commercial bankruptcy data from the web

import requests
import os

URL = "https://abi-org-corp.s3.amazonaws.com/articles/aacer-{}-2020-commercial-bankruptcy-filings-all-chapters-ch-11-focus.xlsx"
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul",
            "aug", "sep", "oct", "nov", "dec"]

curDir = os.getcwd()


for month in months:
    r = requests.get(URL.format(month))
    with open(f'{curDir}/{month}.xlsx', 'wb') as f:
        f.write(r.content)




