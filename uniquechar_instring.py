# Return first unique character from a string
def check_unique(str):
  str_list = " "
  str_list2 = "no unique character in string"
  for ch in str:
    if ch in str_list:
      str_list= str_list.replace(ch,'')
    else: str_list = str_list + ch
  if str_list != " ":
   return str_list[1]
  else: return str_list2

str = input("ENTER A STRING : ")
str1 = check_unique(str)
print(str1)
