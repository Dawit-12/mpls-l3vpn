import csv


class Qos:
    def __init__(self, source_file):
        self.source = source_file
        self.destination = None
        with open(self.source) as file:
            data = file.read().split("$")

        self.new_list = [item.split("\n") for item in data]

    def generate_qos(self, destination_file):
        self.destination = destination_file
        with open(self.destination, "w", newline='') as file:
            data_1 = csv.writer(file)
            for item in self.new_list:
                if not item[0].strip():
                    item.pop(0)
                data_1.writerow(item)