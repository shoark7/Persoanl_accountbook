#auto_open_16_6_18.py
""" 
컴퓨터 시작 시 자동으로 시작되고, 
그래서 매일의 돈 지출의 기록을 기록, 추적할 수 있도록 하는 것이 핵심이다.
간단하게 매일 쓴 돈을 기록하고, 달별로 계산해주는 것을 목표로 한다.
"""

import datetime
import json
import sys

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



""" 메뉴 선택 기능 Section """




#####################################
#### menu 1. 지출금액 추가 기능.
#####################################
#### 만약 오늘 처음 금액 지출을 입력한다면 입력되고, 두 번째 이상일 경우 기존 입력된 금액에 추가한다.


# 전체 날짜에 대한 지출을 받는다. 변수명은 daily_spent_all 로 하겠다.
