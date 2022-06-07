import csv

SOURCE_FILE = "C:\\Users\\SPECTRE 2017\\Downloads\\VPN customers\\KK_A_qos"
DESTINATION_FILE = "C:\\Users\\SPECTRE 2017\\Downloads\\VPN customers\\qos.csv"

with open(SOURCE_FILE) as file:
    data = file.read().split("$")

new_list = [item.split("\n") for item in data]
print(new_list)

with open(DESTINATION_FILE, "w", newline='') as file:
    data = csv.writer(file)
    for item in new_list:
        if not item[0].strip():
            item.pop(0)
        data.writerow(item)