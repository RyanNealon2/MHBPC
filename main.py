from scorecard.api import ScoreCard
import requests
import pandas as pd

sc = ScoreCard('4HYJoiEQMYhtUcoVK9K7dFmJNmDArviXBizfvdzi')
for college in sc.search('Marist'):
    dict = {'College Name': college.data['latest.school.name'], 'state': college.data['latest.school.state'],'Zip': college.data['latest.school.zip'], 'Average Price': college.data['latest.cost.avg_net_price.private']}
dictionaryDataFrame = pd.DataFrame(dict, index=[0])


with pd.ExcelWriter('output.xlsx') as engine:
    dictionaryDataFrame.to_excel(excel_writer=engine, sheet_name='CollegeData', index=False)




