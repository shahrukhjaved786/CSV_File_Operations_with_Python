import csv

#Goal is to PUSH all NAMES in one List and STATUS in another list and get the loan status by passing name

username = input("Enter The Name to Get Loan Status: ")

with open(r"/Python/CSV/csvFile_userdata.csv", "r") as file_data:
    csv_obj = csv.reader(file_data,delimiter=',')
    #print(list(csv_obj))
    list_name = []
    list_status = []

    for value in list(csv_obj):
        list_name.append(value[0])
        list_status.append(value[1])

    # for name,status in list(csv_obj):
    #     list_name.append(name)
    #     list_status.append(status)

for indexpos , name in enumerate(list_name):
    if name == username:
        print(f"Loan Status of {username} is {list_status[indexpos]}")


# indexpos = list_name.index(username)
# loanstatus = list_status[indexpos]
# print(f"Loan status of {username} is {loanstatus}" )