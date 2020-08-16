import os
import pandas as pd
'''
df = pd.DataFrame()
tmp = pd.read_excel('./통계표_시군구/2016년04월_통계표_시군구.xlsx', header=0)
df['16.04_합물특'] = tmp['승합_계'] + tmp['화물_계'] + tmp['특수_계']
'''

path = './통계표_시군구'
file_list = os.listdir(path)

'''
print(file_list)
file_list[0][2:4]
file_list[0][5:7]
'''

# string은 '+' 연산자를 안쓰는것이 좋음
# 가비지 메모리가 많이 나오기 때문
df = pd.DataFrame()
for filename in file_list:
    var1_name = '{}.{}_시군구'.format(filename[2:4], filename[5:7])
    var2_name = '{}.{}_합물특'.format(filename[2:4], filename[5:7])
    file_dir = '{}/{}'.format(path, filename)
    tmp = pd.read_excel(file_dir, header=0)
    df[var1_name] = tmp['시군구']
    df[var2_name] = tmp['승합_계'] + tmp['화물_계'] + tmp['특수_계']

print(df)

df.to_csv("./Result/통계표_시군구_결과.csv", mode='w', encoding='cp949')

#########################################################################
import os
import pandas as pd

pop = pd.read_csv('./Result/인구자료.csv', encoding='cp949')
temp = pd.read_excel('./통계표_시군구/2015년08월_통계표_시군구.xlsx')
year = ['15', '16', '17', '18', '19', '20']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']



#for filename in file_list:
#    file_dir = './통계표_시군구/{}'.format(filename)
#    tmp = pd.read_excel(file_dir, header=0)


year = ['15', '16', '17', '18', '19', '20']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']



result = pd.DataFrame()
file_list = os.listdir('./통계표_시군구')
for y in year:
    for m in month:
        fileName = '20{}년{}월_통계표_시군구.xlsx'.format(y, m)
        if fileName not in file_list:
            continue
        file_dir = './통계표_시군구/{}'.format(fileName)
        car = pd.read_excel(file_dir, header=0)
        pop = pd.read_csv('./Result/인구자료.csv', encoding='cp949')
        pop_val = '20{}. {} 월'.format(y, m)
        idx = 0
        for si in pop['시도'].unique():
            for gu in pop[si]['시군구'].unique():
                pop_target = pop[(pop['시도'] == si) & (pop['시군구'] == gu)][pop_val]
                car_pd = car[(car['시도'] == si) & (pop['시군구'] == gu)]
                car_target = car_pd['승합_계'] + car_pd['화물_계'] + car_pd['특수_계']

                result.at[idx, '시도'] = si
                result.at[idx, '시군구'] = gu
                result.at[idx, pop_val] = round(pop_target/car_target, 1)
                idx += 1

print(result)



print(temp['시도'].unique())
temp['시도'] == '합 계'
pop['시도'] == '합 계'
print(pop['시도'].unique())
temp['시군구'].unique()
temp[(temp['시도'] == '서울') & (temp['시군구'] == '동작')]
seoul = '서울'
pop[pop['시도'] == '서울']['시군구'].unique()




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
import pandas as pd

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

year = ['15', '16', '17', '18', '19', '20']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

result = pd.DataFrame()
file_list = os.listdir('./통계표_시군구')
pop = pd.read_csv('./Result/인구자료.csv', encoding='cp949')

pop.columns
result['시도'] = pd.Series()
result['시군구'] = pd.Series()



for y in year:
    for m in month:
        fileName = '20{}년{}월_통계표_시군구.xlsx'.format(y, m)
        if fileName not in file_list:
            continue
        file_dir = './통계표_시군구/{}'.format(fileName)
        car = pd.read_excel(file_dir, header=0)
        pop_val = '20{}. {} 월'.format(y, m)

        for si in car['시도'].unique():
            for gu in car['시군구'].unique():
                print('{0} {1}'.format(si, gu))

                a = car[(car['시도'] == si) & (car['시군구'] == gu)]
                car_target = a['승합_계'] + a['화물_계'] + a['특수_계']
                b = pop[(pop['시도'] == si) & (pop['시군구'] == gu)]
                pop_target = b[pop_val]




