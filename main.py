import csv
import re

from interface import Interface
from qos import Qos
SOURCE_FILE = "C:\\Users\\dawit.mulugetae\\Documents\\github\\VPN customers\\NZ_B_interface"
DESTINATION_FILE = "C:\\Users\\dawit.mulugetae\\Documents\\github\\output\\nz_b_interface.csv"
SOURCE_QOS_FILE = "C:\\Users\\dawit.mulugetae\\Documents\\github\\VPN customers\\NZ_B_qos"
DESTINATION_QOS_FILE = "C:\\Users\\dawit.mulugetae\\Documents\\github\\output\\nz_b_QOS.csv"
# interface = Interface(SOURCE_FILE)
# interface.generate_interface(DESTINATION_FILE)

qos = Qos(SOURCE_QOS_FILE)
qos.generate_qos(DESTINATION_QOS_FILE)

string = "  description 70100272370-TSEHAY INSURANCE S.C-12-DEC-2019"

# x = re.findall('[0-9]+', string)
# print(x)
#
# num = 0
# for item in x:
#     if int(item) > num:
#         num = int(item)
# print(num)