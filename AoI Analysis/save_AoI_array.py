import csv
from AoI_of_SRARQ import AoIOfSRARQ

def saveAoIData(data, filename='aoi_data.csv'):

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    