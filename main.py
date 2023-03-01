from scorecard.api import ScoreCard
import requests
import pandas as pd

sc = ScoreCard('4HYJoiEQMYhtUcoVK9K7dFmJNmDArviXBizfvdzi')
for college in sc.search('Marist'):
   dict = {'College Name': college.name, 'state': college.location['state'], 'Tuition': college.}
dictionaryDataFrame = pd.DataFrame(dict, index=[0])


with pd.ExcelWriter('output.xlsx') as engine:
    dictionaryDataFrame.to_excel(excel_writer=engine, sheet_name='CollegeData', index=False)



