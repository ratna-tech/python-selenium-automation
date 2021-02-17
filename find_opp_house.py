house_num= int(input('Input any whole number  '))
street_len = int(input('Input any whole number  '))


str_1 = []
for i in range(1, street_len*2, 2):
  str_1.append(i)
print(str_1)

str_2 = []
for i in range(2, (street_len*2 +1), 2):
  str_2.append(i)
print(str_2)

def find_opp_house(house_num,str_1,str_2):
    opp_house = 0
    if house_num %2 ==0:
        if house_num == street_len:
            opp_house = str_2[house_num-1]
        else: opp_house = str_2[house_num]

    if house_num %2 !=0:
       if house_num == street_len:
           opp_house = str_1[house_num-1]
       else:
           opp_house = str_1[house_num]
    return opp_house
print(find_opp_house(house_num,str_1,str_2))