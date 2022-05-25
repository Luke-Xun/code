import pandas as pd # data processing


d1={}
for i in range(2018,2023):
    m= f'C:/Users/lukex/Desktop/World Happiness {i}.csv'  
    n=pd.read_csv(m)    
    d1[i]=n['Country or region']

print('====',d1,'====')
a= list(set(d1[2022]).difference(set(d1[2021])))
b= list(set(d1[2021]).difference(set(d1[2022])))
c= list(set(d1[2020]).difference(set(d1[2021])))
d= list(set(d1[2019]).difference(set(d1[2021])))
e= list(set(d1[2018]).difference(set(d1[2021])))
l1=[a,b,c,d,e]
max_len= len(max(l1, key=len, default=''))
print(max_len)
for i in l1:
    while len(i)!=max_len:
        if len(i)<max_len:
            i.append('na')
    i.sort()
country_name_inconsistency=pd.DataFrame(data={'2022':a, '2021':b,'2020':c,'2019':d,'2018':e})
country_name_inconsistency.to_csv(r'C:\Users\lukex\Desktop\country name inconsistency.csv')

    
# wh_2022= pd.read_csv(r'C:\Users\lukex\Desktop\World Happiness 2022.csv')
# wh_2021= pd.read_csv(r'C:\Users\lukex\Desktop\World Happiness 2021.csv')
# wh_2020= pd.read_csv(r'C:\Users\lukex\Desktop\World Happiness 2020.csv')
# for col in wh_2022.columns:
#     print(col)
# a= list(set(wh_2022['Country or region']).difference(set(wh_2021['Country name'])))
# b= list(set(wh_2021['Country name']).difference(set(wh_2022['Country'])))
# c= list(set(wh_2020['Country name']).difference(set(wh_2021['Country name'])))
# l1 = [a,b,c]
# for i in l1:
#     print('***=============',i,len(i),'=============***')

# max_len= len(max(l1, key=len, default=''))
# for i in l1:
#     while len(i)!=max_len:
#         if len(i)<max_len:
#             i.append('na')

# for i in l1:
#     i.sort()
# country_name_inconsistency=pd.DataFrame(data={'2022':a, '2021':b,'2020':c})
# country_name_inconsistency.to_csv(r'C:\Users\lukex\Desktop\country name inconsistency.csv')