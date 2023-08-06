import csv

with open(r"/Python/CSV/csvFile_userdata.csv", "r") as file_data:
    csv_obj = csv.reader(file_data,delimiter=",")
    #print(list(csv_obj))

    for key,value in list(csv_obj):
        print(f"{key}:{value}")
