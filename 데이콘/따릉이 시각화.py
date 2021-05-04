import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib.pylab as plt
import numpy as np
import math
# import seaborn  as sns
import openpyxl


xl_name = 'log.xlsx'
api_name = '대여소.csv'
​
xl = pd.read_excel(xl_name)
api = pd.read_csv(api_name, encoding='utf-8')
​
#대여소 명이 '대여소명 없음'으로 되어있는 행 날리기
xl = xl[xl['대여소 명'] != '대여소명 없음']
​
# 정규표현식 사용하여 대여소명 + 대여소 번호 분리 (숫자 뭉텅이 꺼내기)
no = []
for i in xl['대여소 명'] :
   n = re.findall("\d+",i)
   no.append(n[0])
xl['대여소번호'] = no
​
#xl파일 필요한것만
xl = xl[['대여소번호','반납 일자 / 월', '반납 건수']]
​
​
##위도, 경도, 대여소번호, 대여소명 이름 변경
api = api.rename({'소재지(위치)':'소재지','대여소\n번호':'대여소번호','보관소(대여소)명':'대여소명','Unnamed: 4':'위도','Unnamed: 5':'경도'},axis ='columns')
​
##대여소번호, 대여소명, 위도, 경도로 된 테이블 생성
apidf = api[['소재지','대여소번호','대여소명','위도','경도']]
# #결측치 제거 --> 위도 경도 값이 없으면 제거
apidf = apidf.dropna(subset = ['위도'])
​
​
# 타입 변경
apidf = apidf.dropna(subset = ['대여소번호'])
apidf['대여소번호'] = apidf['대여소번호'].astype('int')
xl['대여소번호'] = xl['대여소번호'].astype('int')
apidf['위도'] = apidf['위도'].astype('float')
apidf['경도'] = apidf['경도'].astype('float')
​
# #대여소 번호 기준 join
df_join = pd.merge(xl, apidf, how = 'left', on = '대여소번호')
​
#엑셀 변환
# df_join.to_excel(excel_writer = 'df_join.xlsx')
# # print(df_join)
​
# join이후 -> 위도, 경도 값에 none값 발생.. -> 나중에 주소를 가지고 위경도 불러오는 코드 시도해봐도 좋을듯
df_join = df_join.dropna(subset = ['위도'])
​
# 반납건수.SUM (막대그래프)
# df_join.groupby('소재지')['반납 건수'].count().plot(kind = 'bar', legend=True)
# plt.show()
​
# 강남구만 추출
gangnam = df_join['소재지'] ==  '강남구'
df_join_gangnam = df_join[gangnam]
​
# '월'을 표시하는 컬럼 추가
df_join_gangnam['month'] = df_join_gangnam['반납 일자 / 월'].dt.strftime('%m')
​
#각 대여소 별 월 반납건수
df_join_gangnam['월별건수']  = df_join_gangnam.groupby(['대여소명','month'])['반납 건수'].transform('sum')
print(df_join_gangnam)
​
# 각 대여소의 월별 대여건수
df_plot = df_join_gangnam[['대여소명','위도','경도','month','월별건수']]
df_plot.drop_duplicates(['대여소명','month'])
df_plot = df_plot.reset_index(drop=True)
print(df_plot)
​
df_plot_july = df_plot[df_plot['month'] == '07']
print(df_plot_july)
​
​
def colors(x) :
   if  x < 100 : 
      return 'b'
   elif x < 300 : 
      return 'g' 
   else :
      return 'r'
​
area = df_plot_july['월별건수'].apply(lambda x: math.sqrt(x))
color = df_plot_july['월별건수'].apply(lambda x : colors(x))
a = pd.Series([0.05]*len(df_plot_july))
plt.scatter( df_plot_july['위도'], df_plot_july['경도'], label = "월별건수", c = color ,s=area*5, alpha=a)
# plt.legend(loc = "best") 
plt.xlabel('위도')
plt.ylabel('경도')
plt.show()

