import management
import datetime as t


# 변경된 재고 정보를 텍스트 파일에 저장
def re_stock(goods) :
    f = open("재고/goods.txt","w")

    for i in goods.keys() :
        f.write("{}/{}/{}/{}/{}\n".format(i,goods[i]['분류'],goods[i]['품목'],goods[i]['가격'],goods[i]['재고']))

    f.close()


# 일 매출 정보를 텍스트 파일에 저장
def make_day_sale(yearmonth,day,day_sale) :

    f = open("관리/"+yearmonth+day+".txt","w")

    for i in day_sale.keys() :
        f.write("{}/{}\n".format(i,day_sale[i]))

    f.close()

    
# 월 매출 정보를 불러와서 일 매출 정보를 더한 다음에 다시 텍스트 파일에 저장
def make_month_sale(month,day_sale) :
    tmp_dic = management.month_margin(month)
    month_sale = tmp_dic[month]
    f_dic = {}

    for i in month_sale.keys() :
        total = month_sale[i] + day_sale[i]
        f_dic[i] = total
    
    f = open("관리/"+month+"-total.txt","w")

    for i in f_dic.keys() :
        f.write("{}/{}\n".format(i,f_dic[i]))

    f.close()

 #(물품 정보 및 재고, 일 매출)
def main(goods,day_sale) :
    
    now = t.datetime.now()

# 수정 이전 -20241216-1000 #
#     month = now.month
#     day = now.day
#
#     #day나 month가 1의 자리면 앞에 0 추가
#     if month < 10 :
#         month = '0'+str(month)
#     else :
#         month = str(month)
#
#     if day < 10 :
#         day = '0'+str(day)
#     else :
#         day = str(day)
#
#     re_stock(goods)
#     make_day_sale(month,day,day_sale)
#     make_month_sale(month,day_sale)

# 수정1. -20241216-1239 #
    #년, 월, 일 설정
    yearmonth = now.strftime("%Y%m")
    month = now.month
    day = now.strftime("%d")

    #변경 재고 정보 저장
    re_stock(goods)
    # 일매출 기록 생성
    make_day_sale(yearmonth, day, day_sale)
    make_month_sale(month, day_sale)
