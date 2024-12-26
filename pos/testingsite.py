# try: f = open("재고/empty.txt","r")   # 현재 재고 읽어오기
# except: print("NO FILE!")
# else:
#     lines = []
#     while(True) :
#         line = f.readline()  # 한 줄 읽기
#         line = line.rstrip("\n")  # 오른쪽 공백 없애기
#         if (line == ""): break
#         else: lines.append("line")
#
#     if len(lines) <= 0: print("EMPTY")
#     else:
#         for i in lines :
#             (print(i))


# dic = {"a":1,"b":2}
# # for i in dic: print(i)
# print(len(dic))

# dic = {"name":"Jake","age":"31","nationality":"Korean","scolarship":"B.D"}
# print(dic.keys())
# listing = list(dic.keys())
# for i in listing:print("{}:{}".format(i,dic[i]))
#
# print("name" in dic)
# print(dic["name"])
# print(dic[1])

li = [1,2,3,4,5]
print((10 and 9) in li)
