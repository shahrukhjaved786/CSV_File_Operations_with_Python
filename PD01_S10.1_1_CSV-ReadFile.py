import csv

with open(r"H:\Pycharm_Projects\pythonProject\PracticeProject\Python\CSV_File_Operations_with_Python\csvFile_userdata.csv", "r") as file_data:
    csv_obj = csv.reader(file_data,delimiter=",")
    #print(list(csv_obj))

    for key,value in list(csv_obj):
        print(f"{key}:{value}")
