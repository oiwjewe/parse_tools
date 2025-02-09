#!/usr/bin/env python3 #change path if necessary

import xml.etree.ElementTree as ET
import csv

tree = ET.parse('arquivo.xml') #change file name
root = tree.getroot()

# Abrindo o arquivo CSV para escrever
with open('dados.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Escrevendo os cabeçalhos
    writer.writerow(['First Name', 'Last Name', 'Email', 'Username', 'Password']) #change colluns name to the ones you need

    # Iterando sobre os dados e escrevendo no CSV
    for si in root.findall('.//si'):
        row = [t.text for t in si.findall('.//t')]
        writer.writerow(row)
