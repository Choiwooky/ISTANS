'''
df = pd.DataFrame()
tmp = pd.read_excel('./통계표_시군구/2016년04월_통계표_시군구.xlsx', header=0)
df['16.04_합물특'] = tmp['승합_계'] + tmp['화물_계'] + tmp['특수_계']
'''

'''
print(file_list)
file_list[0][2:4]
file_list[0][5:7]
'''
# string은 '+' 연산자를 안쓰는것이 좋음
# 가비지 메모리가 많이 나오기 때문

#########################################################################
# and 가 안되고 & 를 활용하니 됨
# 조건 각각을 괄호로 싸줘야함
'''
pop[(pop['시도'] == seoul) and (pop['시군구'] == '동작')] 
-> 오류
pop[(pop['시도'] == seoul) & (pop['시군구'] == '동작')]['2015. 08 월']
-> 조건 각각을 괄호로 묶어야함
'''

#######################################################################################################################

#car_target = car_pd['승합_계'] + car_pd['화물_계'] + car_pd['특수_계']
import os
import numpy as np
import pandas as pd
'''
pop = pd.read_csv('./Result/인구자료.csv', encoding='cp949')
temp = pd.read_excel('./통계표_시군구/2015년08월_통계표_시군구.xlsx')
a = temp[(temp['시도'] == '서울') & (temp['시군구'] == '강남')]
print(a)
car_target = a['승합_계'] + a['화물_계'] + a['특수_계']
print(car_target)
b = pop[(pop['시도'] == '서울') & (pop['시군구'] == '강남')]
pop_target = b['2015. 08 월']
print(pop_target)
car_target = int(car_target)
pop_target = int(pop_target)
round(pop_target/car_target, 1)
'''
year = ['15', '16', '17', '18', '19', '20']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

result = pd.DataFrame()
file_list = os.listdir('./통계표_시군구')
pop = pd.read_csv('./Result/인구자료.csv', encoding='cp949')

result[['시도', '시군구']] = pop[['시도', '시군구']]

for col in pop.columns:
    if col in result:
        continue
    result[col] = pd.Series()   # 추천하지 않는 방식이라고 빨간 글자 나오지만 돌아감
'''
result.at[(result['시도'] == '서울') & (result['시군구'] == '강남'), '2015. 08 월'] = 1.0 
result[(result['시도'] == '서울') & (result['시군구'] == '강남')]['2015. 08 월']

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_row', 500)
'''

for y in year:
    for m in month:
        fileName = '20{}년{}월_통계표_시군구_전처리.xlsx'.format(y, m)
        print(fileName)
        if fileName not in file_list:
            continue
        file_dir = './통계표_시군구/{}'.format(fileName)
        car = pd.read_excel(file_dir, header=0)
        pop_val = '20{}. {} 월'.format(y, m)

        for si in result['시도'].unique():
            for gu in result['시군구'].unique():
                a = car[(car['시도'] == si) & (car['시군구'] == gu)]

                car_target = a['승합_계'].astype(float) + a['화물_계'].astype(float) + a['특수_계'].astype(float)
                pop_target = pop[(pop['시도'] == si) & (pop['시군구'] == gu)][pop_val].astype(float)
                target = np.round(pop_target.values/car_target.values, 1)
                if target.size == 0:
                    continue
                else:
                    result.at[(result['시도'] == si) & (result['시군구'] == gu), pop_val] = target[0]


result.to_csv('./Result/sample.csv', encoding='cp949')

for y in year:
    for m in month:
        fileName = '20{}년{}월_통계표_시군구_전처리.xlsx'.format(y, m)
        print(fileName)
        if fileName not in file_list:
            continue
        file_dir = './통계표_시군구/{}'.format(fileName)
        car = pd.read_excel(file_dir, header=0)
        pop_val = '20{}. {} 월'.format(y, m)

        for si in result['시도'].unique():
            for gu in result['시군구'].unique():
                a = car[(car['시도'] == si) & (car['시군구'] == gu)]

                car_target = a['승합_계'].astype(float) + a['화물_계'].astype(float)
                pop_target = pop[(pop['시도'] == si) & (pop['시군구'] == gu)][pop_val].astype(float)
                target = np.round(pop_target.values/car_target.values, 1)
                if target.size == 0:
                    continue
                else:
                    result.at[(result['시도'] == si) & (result['시군구'] == gu), pop_val] = target[0]

result.to_csv('./Result/sample0.csv', encoding='cp949')