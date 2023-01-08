import os
import downloadgarf
import datetime
from datetime import date
from datetime import timedelta

file_path = os.getcwd()


months = ['January', 'February', 'March',
            'April', 'May', 'June',
            'July', 'August', 'September',
            'October', 'November', 'December']
count = 0
start_date = date(1978, 6, 19)
end_date = date(2022, 12, 27)
delta = timedelta(days=1)
while start_date <= end_date:
    year = str(start_date.year)
    month = str(start_date.month) + " " + str(months[int(start_date.month) - 1])
    filename = "Garfield " + str(start_date) + ".png"
    curr_path = os.path.join(file_path, year, month, filename)
    stats = os.stat(curr_path)
    if stats.st_size < 10000:
        downloadgarf.downloader(start_date)
        count = count + 1
    start_date += delta

print("-----DONE-----")
print("total failed files: " + str(count))
        


