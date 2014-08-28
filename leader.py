import pandas as pd
import vincent

xl = pd.ExcelFile("../Sales.xlsx")
df = xl.parse("CaseSale")


df2 = df[['Sale_Date', 'DS', 'HB4', 'HW', 'KNold', 'PP4', 'PTT', 'SP', 'KP', 'KNnew', 'DS2', 'Demo']]
df2['quant'] = df2.DS.fillna(0) + df2.DS2.fillna(0) + df2.HB4.fillna(0) + df2.HW.fillna(0) + df2.KNnew.fillna(0) + df2.KNold.fillna(0) + df2.KP.fillna(0) + df2.PP4.fillna(0) +  df2.PTT.fillna(0) + df2.SP.fillna(0)
agg = df2[['Demo', 'quant']]
leaderboard = agg.groupby(['Demo']).aggregate(sum)
leaderboard_sorted = leaderboard.sort(['quant'], ascending=[0])



bar = vincent.Bar(leaderboard_sorted)
bar.to_json('bar.json', html_out=True, html_path='index.html')

