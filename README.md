# pythonstudy24

 관리자가 커피 가격과 커피명 정하고 개수 입력
# 소비자가 커피를 구매, 구매후 잔돈 배출
# 판매 종료 후 관리자가 매출을 확인해야함

# Jakobie's coffee 커피 자판기운영을 시작합니다.




     

arr1 = ['a','a','c']
arr1[0] = 'x'
print(arr1)
del arr1[1]
print(arr1)
'c' in arr1
arr1 = arr1 + ['y']
print(arr1)

     
['x', 'a', 'c']
['x', 'c']
['x', 'c', 'y']

# 커피 정보, 재고 입력
# [[커피 제품명, 커피 수량, 가격, 판매량, 매출]]
coffeeName = [] # 커피 제품명
coffeeAmount = [] # 커피 수량
coffeePrice = [] # 커피 가격
coffeeSold = [] # 커피 판매량
coffeeIncome = [] # 커피 매출
coffeeInfo = []
coffeeInform = [["밀크커피", 50, 300, 0, 0], ["프림커피", 30, 300, 0, 0]]
print(coffeeInform)
print(coffeeInform[1][0])

if len(coffeeInfo) < 1:
  print("판매할 커피 정보를 입력합니다.")
  print("%d번째 커피 정보" % (len(coffeeInfo)+1))
coffeeName = input("커피 이름을 입력해주세요.")
coffeeAmount = input("커피 이름을 입력해주세요.")
     
[['밀크커피', 50, 300, 0, 0], ['프림커피', 30, 300, 0, 0]]
프림커피
판매할 커피 정보를 입력합니다.
1번째 커피 정보


     

# 현금 투입
cash = ('100', '500', '1000', '5000', 'admin')
currentCash = 0;
inserted = '1'
keepInsert = True
print("현재 투입금액: %d" %currentCash)
while keepInsert:

  inserted = input("현금을 투입해주세요")
  for i in cash:
    if i == inserted and i != 'admin':
      currentCash = currentCash + int(i)
      break
    elif i == inserted and i == 'admin':
      if currentCash>0: print("투입된 금액은 모두 배출하였습니다")
      print("관리자 설정 메뉴로 이동합니다")
      keepInsert = False
      break
    elif i == 'admin' and inserted != i:
      print("사용할 수 없는 화폐입니다")


  # if currentCash>=500: print("투입 가능 금액을 초과했습니다.")
  if inserted != 'admin':
     print("그만 투입하시려면 'Y'를 입력하십시오")
     if input("'Y'이외의 문자는 계속 투입하는 것으로 간주됩니다.") == 'y' and input("'Y'이외의 문자는 계속 투입하는 것으로 간주됩니다.") == 'Y':
      print("현금 투입을 중단합니다.5");
      keepInsert = False
     print("현재 투입금액: %d" %currentCash)


     
현재 투입금액: 0
현금을 투입해주세요a
사용할 수 없는 화폐입니다
그만 투입하시려면 'Y'를 입력하십시오
'Y'이외의 문자는 계속 투입하는 것으로 간주됩니다.Y
현재 투입금액: 0
현금을 투입해주세요admin\
사용할 수 없는 화폐입니다
그만 투입하시려면 'Y'를 입력하십시오
'Y'이외의 문자는 계속 투입하는 것으로 간주됩니다.ad
현재 투입금액: 0
현금을 투입해주세요admin
관리자 설정 메뉴로 이동합니다

currentCash = 2000;
coffeeInform = [["밀크커피", 50, 300, 0, 0], ["설탕커피", 30, 300, 0, 0], ["블랙커피", 30, 200, 0, 0]]
coffeeChoice = 0
location = 0
canPurchase = False
keepPurchase = True
print("현재 투입금액: %d" %currentCash)
print("현재 판매가능한 커피 현황입니다.")

print("선택\t커피종류\t수량\t가격")
for i in coffeeInform:
  location = location + 1
  print("%d\t%s\t%d\t%d" %(location, i[0], i[1], i[2]))

location = input("선택번호를 보고 주문하실 커피를 선택해주십시오: ")

while not canPurchase:
  if location.isdigit() and int(location)<=len(coffeeInform) and int(location)>0:
    print("%s 1잔이 나오는 중입니다." %coffeeInform[int(location)-1][0])
    coffeeInform[int(location)-1][1] = coffeeInform[int(location)-1][1] - 1
    coffeeInform[int(location)-1][3] = coffeeInform[int(location)-1][3] + 1
    coffeeInform[int(location)-1][4] = coffeeInform[int(location)-1][4] + coffeeInform[int(location)-1][2]
    canPurchase = True
  else: location = input("다시 입력해주십시오")

for i in coffeeInform:
  print(i)

# for i in coffeeInform:
#   if location.isdigit():
#     print(location.isdigit())
     
현재 투입금액: 2000
현재 판매가능한 커피 현황입니다.
선택	커피종류	수량	가격
1	밀크커피	50	300
2	설탕커피	30	300
3	블랙커피	30	200
선택번호를 보고 주문하실 커피를 선택해주십시오: 1
밀크커피 1잔이 나오는 중입니다.
['밀크커피', 49, 300, 1, 300]
['설탕커피', 30, 300, 0, 0]
['블랙커피', 30, 200, 0, 0]
