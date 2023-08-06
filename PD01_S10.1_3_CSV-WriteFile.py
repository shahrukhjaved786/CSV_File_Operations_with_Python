import csv

with open(r"H:\Pycharm_Projects\pythonProject\PracticeProject\Python\CSV_File_Operations_with_Python\csvFile_userdata.csv", "a") as file_data:
    csv_obj = csv.writer(file_data)
    csv_obj.writerow(["Angy","Pending"])

