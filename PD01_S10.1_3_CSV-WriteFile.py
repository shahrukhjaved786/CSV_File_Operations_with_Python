import csv

with open(r"/Python/CSV/csvFile_userdata.csv", "a") as file_data:
    csv_obj = csv.writer(file_data)
    csv_obj.writerow(["Dorsy","Rejected"])

