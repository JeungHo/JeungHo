https://www.mois.go.kr/frt/bbs/type001/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000052&nttId=94196
# 행정동 법정동 코드 행정자치부
# 시군구 코드 228개(자치구가 아닌 구 제외, 출장소 제외)

xls_file = r'..\code\KIKcd_H.20220901.xlsx'
xls_bfile = r'..\code\KIKcd_B.20220901.xlsx'

import pandas as pd

df = pd.read_excel(xls_file)
df_b = pd.read_excel(xls_bfile)

df['행정동'] = df['시도명'] +' '+df['시군구명'] +' '+df['읍면동명']
df_b['법정동'] = df_b['시도명'] +' '+df_b['시군구명'] +' '+df_b['읍면동명']

# print(df_b.columns)
# print(df.dtypes)
# print(df.info)

# 시도 + 시군구 + 음면동

dv_work = input('작업을 선택하세요 1.법정동 2.행정동 \n ==>')
if dv_work == '1':
    df.query('시군구명 == "의정부시" and 행정동.notnull()')[['행정동코드','읍면동명','행정동']]
    df
else:
    df_b.query('시군구명 == "의정부시" and 읍면동명.notnull() and 동리명.isnull() ')[['법정동코드','읍면동명','법정동']]
    df_b
