#expenditure_tracker.py
""" 
컴퓨터 시작 시 자동으로 시작되고, 
그래서 매일의 돈 지출의 기록을 기록, 추적할 수 있도록 하는 것이 핵심이다.
간단하게 매일 쓴 돈을 기록하고, 달별로 계산해주는 것을 목표로 한다.
"""

import datetime
import json
import sys
import time

# 비밀번호 설정. 내가 아닌 다른 사람이 입력하는 것을 방지한다.
try:
	input_password = sys.argv[1]

except:
	input_password = input("비밀번호를 입력하셔야 합니다. : ")
	for i in range(2):
		if input_password != "696238":
			input_password = input("틀렸습니다. 다시 입력하세요 : ")

	if input_password != "696238":
		sys.exit()
else:
	for i in range(2):
		if input_password != "696238":
			input_password = input("틀렸습니다. 다시 입력하세요 : ")

	if input_password != "696238":
		sys.exit()



# 오늘에 대한 정보 입력. 이후 각각 파일에 저장될 것임.
today = datetime.date.today()
def which_day(date):
	return ['월', '화','수','목','금','토','일'][date.weekday()]



""" 메뉴 선택 기능 Section """
# 기능은 크게 1. 일일 지출금액 추가기능, 2. 지난 월별 합계 및 일일 평균 기능, 3. 특정 날짜 검색 기능, 4~. To be continued.
print("반갑습니다. 현재 시각", str(datetime.datetime.now())+"입니다.")
print("본 기능은 당신이 용돈지출을 어떻게 하는지 추적하고 그 활용을 돕고자 하는 데 의의가 있습니다.")
print()

while True:
	print("""용돈 지출 입력은 1,
월별 합계 기능은 2,
특정 날짜 지출금액 검색은 3,
종료는 9를 입력해주세요.""")
	print(">" * 50)
	menu_selected = input("원하시는 기능을 입력해주세요. : ")

	while menu_selected not in ["1","2","3","9"]:
		input("4가지의 숫자 중 원하시는 것을 정확히 입력해주세요. : ")

	if menu_selected == "9":
		print("감사합니다. 프로그램을 종료합니다.")
		for i in range(3):
			print("종료까지.. "+str(3-i))
			time.sleep(1)
		break	



#####################################
#### menu 1. 지출금액 추가 기능.
#####################################
#### 만약 오늘 처음 금액 지출을 입력한다면 입력되고, 두 번째 이상일 경우 기존 입력된 금액에 추가한다.


# 전체 날짜에 대한 지출을 받는다. 변수명은 daily_spent_all 로 하겠다.
