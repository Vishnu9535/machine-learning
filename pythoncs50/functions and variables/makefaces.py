# st=input("input a string")
# ta={":)":"🙂",":(":"🙁"}
# vi=str.maketrans(ta)
# # print(table)
# st=st.translate(vi)
# print(st)
# string = input("Enter a string: ")
# table = {":)": "🙂", ":(": "🙁"}
# table = str.maketrans(table)
# result = string.translate(table)
# print(result)
string = input("Enter a string: ")

table = {":)": "🙂", ":(": "🙁"}


string = string.replace(":)","🙂")
string = string.replace(":(","🙁")

print(string)

