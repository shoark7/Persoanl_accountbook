# Function for expenditure_tracker.py

def checkRightFormat(str):
	try:
		if str[0:4].isnumeric() and str[4] == '-' and str[5:7].isnumeric() \
		and str[7] == '-' and str[-2:].isnumeric() and len(str) == 10:
			return True
	except:
		return False
	else: return False