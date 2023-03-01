from scorecard.api import ScoreCard
import requests
import pandas as pd

sc = ScoreCard('4HYJoiEQMYhtUcoVK9K7dFmJNmDArviXBizfvdzi')
list = ['Marist College', 'Vassar College', 'Ithaca College']
collegeData = {}

for x in list:
    for college in sc.search(x):
        dict = {'College Name': college.data['latest.school.name'], 'state': college.data['latest.school.state'],'Zip': college.data['latest.school.zip'],'Average Price': college.data['latest.cost.avg_net_price.private']}
        for key, value in dict.items():
            if key in collegeData:
                if isinstance(collegeData[key], type(list)):
                    collegeData[key].append(value)
                else:
                    temp_list = [collegeData[key], value]
                    collegeData[key] = temp_list
            else:
                collegeData[key] = value

dictionaryDataFrame = pd.DataFrame(collegeData)
with pd.ExcelWriter('output.xlsx') as engine:
    dictionaryDataFrame.to_excel(excel_writer=engine, sheet_name='CollegeData', index=False)


