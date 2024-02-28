from pyzbar.pyzbar import decode
from PIL import Image
import os
import csv

# Reads all barcodes in a jpg image
traverse_me = '/barcode_images'

data_file = open('serial_numbers.csv', 'a')
csv_writer = csv.writer(data_file)
header = ['1','2','3','4','5','6','7','8']
csv_writer.writerow(header)

for root, dir, files in os.walk(traverse_me):
    print(files)
    for image in files:
        list = []
        if not image.endswith('.jpg'):
            continue
        for bar in decode(Image.open(os.path.join(root, image))):
            list.append(str(bar.data).removeprefix('b'))

        csv_writer.writerow(list)
data_file.close()
