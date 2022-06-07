import csv
import re

class Interface:
    def __init__(self, file_location):
        self.file = file_location
        self.extract = []
        self.destination = None
        with open(self.file) as f:
            data = f.read().split("$")
            self.extract = [item.split("\n") for item in data]
            # print(self.extract)

    def generate_interface(self, destination):
        with open(destination, "w", newline='') as f:
            file = csv.writer(f)
            file.writerow(["Interface", "Description", "VRF", "WAN IP","INTERFACE STATUS", "SERVICE NUMBER"])

            for item in self.extract:
                num = 0
                if not item[0].strip():
                    item.pop(0)
                if len(item) > 2:
                    if not item[1].lstrip().startswith("description"):
                        item.insert(1, "description")
                    else:
                        x = re.findall('[0-9]+', item[1])
                        for number in x:
                            if int(number) > num:
                                num = int(number)
                        if num > 10000000:
                            item.insert(5, num)
                    if not item[2].lstrip().startswith("ip vrf"):
                        item.insert(2, "no vrf")
                    else:
                        item[2] = item[2].removeprefix("  ip vrf forwarding")
                    if not item[3].lstrip().startswith("ip address"):
                        item.insert(3, "no ip address")
                    else:
                        item[3] = item[3].removeprefix("  ip address ")
                        item[3] = item[3].split(" ")
                        if item[3][1] == "255.255.255.252":
                            item[3][0] += " /30"
                        elif item[3][1] == "255.255.255.248":
                            item[3][0] += " /29"
                        item[3] = item[3][0]
                    if not item[4].lstrip().startswith("shutdown"):
                        item.insert(4, "NO SHUT")

                    if "  ip vrf forwarding DATA" not in item and \
                            "  ip vrf forwarding VIPVPN" not in item \
                            and "  ip vrf forwarding UPLOAD-ONLY" not in item \
                            and item[0].startswith("interface smartgroup1.") and (item[3].endswith("/29") or item[3].endswith("/30")):
                        if item[1] != '' or item[2] != '':
                            item.remove("")
                            file.writerow(item)
                        print(item)

