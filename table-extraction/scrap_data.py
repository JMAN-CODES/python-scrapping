import requests
import json
import re
from collections import defaultdict
import pandas as pd

# session = requests.session()
# homepage = session.get('https://stats.oecd.org/sdmx-json/data/DP_LIVE/.EXCH.TOT.NATUSD.A/OECD?json-lang=en&dimensionAtObservation=allDimensions&startPeriod=2000')
# with open('homepage.json','w') as fh:
#     fh.write(homepage.text)

f = open('homepage.json')
table = json.load(f)

my_dict = defaultdict(list)

def extract_first_number(input_string):
    match = re.search(r'\d+', input_string)
    if match:
        return int(match.group())
    return None 

def extract_last_number(input_string):
    match = re.search(r'(\d+)(?!.*\d)', input_string)
    if match:
        return int(match.group(1))
    return None

print(countries:=table['structure']['dimensions']['observation'][0]['values'])
print(values:=table['dataSets'][0]['observations'])

for x in countries:
    print(x)
    
print(len(countries),len(values))

ind = 0

for x in values:
    print(x)
    ind += 1
    first_number = extract_first_number(x)
    print(f"First number: {first_number}")
    last_number = extract_last_number(x)
    print(f"Last number: {last_number}")
    
    my_dict[countries[int(first_number)]['name']].append(values[x][0])

json_object = json.dumps(my_dict, indent=4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)

varii = pd.DataFrame(my_dict)
varii = varii.transpose()
print(varii)


for i in range(0,23):
     varii.rename(columns={i: 2000+i}, inplace=True)

print(varii)

varii.to_csv("extracted_data.csv")
