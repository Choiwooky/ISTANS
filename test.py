import os
import pandas as pd
'''
tmp = pd.read_excel('CleaningData/2015년08월_통계표_시군구.xlsx')
len(tmp)
tmp1 = pd.read_excel('CleaningData/2015년09월_통계표_시군구.xlsx')
len(tmp)
del tmp1
'''

# 시군구 변동사항 확인을 위한 체크
path = './통계표_시군구'
file_list = os.listdir(path)
#year = ['15', '16', '17', '18', '19', '20']
#month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']


for name in file_list:
    file_dir = "{}/{}".format(path, name)
    tmp = pd.read_excel(file_dir)
    print(file_dir[10:18], len(tmp['시군구'].unique()))




