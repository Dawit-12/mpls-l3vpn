import csv
import re

from interface import Interface
SOURCE_FILE = "C:\\Users\\SPECTRE 2017\\Downloads\\VPN customers\\KK_A_interface"
DESTINATION_FILE = "C:\\Users\\SPECTRE 2017\\Downloads\\VPN customers\\new4.csv"

interface = Interface(SOURCE_FILE)
interface.generate_interface(DESTINATION_FILE)




string = "  description 70100272370-TSEHAY INSURANCE S.C-12-DEC-2019"

# x = re.findall('[0-9]+', string)
# print(x)
#
# num = 0
# for item in x:
#     if int(item) > num:
#         num = int(item)
# print(num)