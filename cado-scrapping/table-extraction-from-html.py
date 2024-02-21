import re 
import pandas  as pd

with open('table.html') as page:
    html_page = page.read()

table_vals = re.findall('<a\sid="rptCompanyNameSearchResults__.*?">(.*?)<\/a>.*?lblStatusItem">(.*?)<\/span>.*?"CompanyNumberText">(.*?)<\/td>.*?<td width="110">(.*?)<\/td>.*?lblDisplayDateItem">(.*?)<\/span>',html_page,re.S)


print(len(table_vals))

#Name	Status	Number	Corporation Type	Date
details = []
for i in table_vals:
    my_dict = {}
    my_dict['Name'] = i[0]
    my_dict['Status'] = i[1]
    my_dict['Number'] = i[2]
    my_dict['Corporation_Type'] = i[3]
    my_dict['Date'] = i[4]
    details.append(my_dict)

df = pd.DataFrame(details)

df.to_csv("ailan.csv")




