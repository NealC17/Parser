import pandas as pd
import numpy as np
import sys
import xml.etree.ElementTree as ET

def parse_file(filename):
    df = pd.read_csv(filename, sep="\t")
    #print(df.axes)
    return df


#parse_file("file.txt")
#for arg in sys.argv:
#    print(arg)

filename = sys.argv[1]
mode = sys.argv[2]
df = parse_file(filename)
#print(df)

if mode == "-j":
    df.to_json('out.json', orient = 'split', compression = 'infer', index=False)

elif mode == "-c":
    df.to_csv('out.csv', sep = ",")

elif mode == "-x":
    root = ET.Element("root")
    for _, row in df.iterrows():
        entry = ET.SubElement(root, "entry")
        for col_name, col_value in row.items():
            sub_element = ET.SubElement(entry, col_name.replace(' ', '_'))
            sub_element.text = str(col_value)
    tree = ET.ElementTree(root)
    tree.write('out.xml')

