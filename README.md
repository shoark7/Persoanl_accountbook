# expenditure-tracker

> ### :bowtie: This project is my very first python project in my life.
> The project is for tracking my money expenditure over time and supplies basic statistical features.
> And I put this file on window batch list and it pops up when I boot up my window.
> It's over 200 lines long(it's very long to me) and I feel nice when I look up this project sometimes.

> ### :bulb: It has 3 major files
> * *Functions_for_tracker.py*
> : It has my personal functions for the project.<br>

> * *daily_expenditure.txt*
> : It saves my expenditure data by `pickle` module in Python.
> Every time I load and put data semipermanently, data is encoded or decoded by pickle module.

> * *expenditure_tracker.py*
> : This is the main part of my project. It operates on CMD and asks user input and calculates.
<br>

> ### :memo: Functions this program has.
> 0. Log in
    - This is for my personal use and requires my password.
    - On CMD, I have to write password as a second argument into a python interpreter.
    - If I don't supply a password, it demans for the password. If I don't give it a right one in 3 times, it exits
> 1. Money input
    - I can wrtie my expenditure into the program. Data load or dump from/into *daily_expenditure.txt*
    - It tells between first input of the day and others.
<br/>
> 2. Search for specific day's expenditure data.
    * Sometimes I want to check specific's day's expenditure data. I can input date and check how much I spent that day.
    * For Koreans, `'오늘'`(today in Korean) and `'어제'`(yesterday in Korean) can be written and automatically searches for today's data or yesterday's data.
> 3. Basic statistics
    - When expenditure data is written, today's month, weekday information is written together.
    - So if I demand statistics it provides me with monthly average expediture and weekday's average expenditure.
> 4. Exit
    - Program exits.
    
> ### :sob: Limits of the project
> When we input ```import this```, we can see a poem about a good python code. In line 7, you can check `"Readability counts"`. It's my first job and readability is really bad.

```python

		print("\t요일별 사용한 금액을 말씀드리겠습니다.")
		for i, weekday in enumerate(weekday_total):
			try:
				print(weekdays[i], "-"*4+"> 총금액 : *{:,}*원, ".format(weekday_total[weekdays[i]][0]) \
					+"평균 : {:,}원".format(weekday_total[weekdays[i]][0] // weekday_total[weekdays[i]][1]))
			except ZeroDivisionError:
				print(weekdays[i], "-"*4+"> 총금액 : "+ "0원, " +"평균 :", "0원")
		print('\n')

```
> This code is from *expenditure_tracker.py* and this part outputs weekday's average expenditure data. As you can see, code is really massy I can't even understand it now. To be frank, I want to make this project whole new again someday. But I will leave this code as it is to compare to my awesome code after lots of study and practice. Also, who knows? This code may be the humble beginnings of my career someday.

And my super thanks to you for checking out this page. I really appreciate. :thumbsup:
