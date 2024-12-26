import pay
import update
import management
import gmanagement
import ep


#재고 및 물품 정보를 텍스트 파일에서 읽기
# goods , day_sale 딕셔너리 생성
goods = {}                       # 물품 정보 및 재고 저장
day_sale = {"card":0,"cash":0}  # 일 매출 정보 저장
can_operate = True # 작동할 수 없으면 False
try: f = open("재고/goods.txt","r")   # 현재 재고 읽어오기
except: can_operate = False #
else:
    while(True) :
        tmp_dic = {}
        line = f.readline()         # 한 줄 읽기
        line = line.rstrip("\n")    # 오른쪽 공백 없애기
        if(line==""):               # 더 이상 읽을 것이 없으면 stop
            break

        st_list = line.split("/") # (ex) ["1", "라면","진라면","800","135"])

        tmp_dic["분류"] = st_list[1] # {"분류":"라면"}
        tmp_dic["품목"] = st_list[2] # {"분류":"라면","품목":"진라면"}
        tmp_dic["가격"] = int(st_list[3]) # {"분류":"라면","품목":"진라면","가격":"800"}
        tmp_dic["재고"] = int(st_list[4]) # {"분류":"라면","품목":"진라면","가격":"800","재고":"135"}

        goods[st_list[0]] = tmp_dic # {"1":{"분류":"라면","품목":"진라면","가격":"800","재고":"135"}}
        day_sale[st_list[0]] = 0 # {"card":0, "cash":0, "1":0}

    # 결론
    # goods = {"1":~,"2":~,"3":~,...}
    # day_sale = {"card":0,"cash":0,"1":0,"2":0,"3":0,...}

# goods가 비어있지 않거나 file이 있어 작업이 가능하다면 menu 불러오고 그렇지 않으면 자동으로 종료하기
if len(goods) > 0 and can_operate:
    while True:
        print("="*30)
        print("1. 결제 \n2. 물품 관리 \n3. 매출 관리 \n9. 종료")
        print("="*30,end="\n")
        select_num = input('선택 : ')

        # 판매 및 재고, 일매출 정리
        if select_num == '1':
            tmp = pay.main(goods)
            update.main(goods,tmp,day_sale)

        # 재고 및 발주 관리
        elif select_num == '2':
            gmanagement.main(goods)

        # 일매출 및 월매출 확인
        elif select_num == '3':
            management.main(goods,day_sale)

        # 프로그램 종료 전에 메모리에 있는 정보를 텍스트 파일로 저장
        elif select_num == '9':
            ep.main(goods,day_sale)
            break
        else:
            print("다시 선택 하세요\n")

    print("\n시스템을 종료합니다.")
#   print("\nSystem down")

else: print("\n죄송합니다. 재고 목록을 가져오는데 오류가 발생하였습니다.\n시스템을 종료합니다.")