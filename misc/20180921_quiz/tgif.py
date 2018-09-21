'''
OUTPUT

Are you grinding? (y/n) y
what day is it? friday
What time is it? early
Good boy!
Are you grinding? (y/n) y
what day is it? friday
What time is it? late
Traceback (most recent call last):
  File "tgif.py", line 12, in work_hard
    print(1/0)
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "tgif.py", line 28, in <module>
    work_hard()			
  File "tgif.py", line 24, in work_hard
    raise RuntimeError("Please stop working - it's party time!") from exc
RuntimeError: Please stop working - it's party time!
'''


import time

def work_hard():
	while True:

		try:
			grinding = input("Are you grinding? (y/n) ")
			day = input("what day is it? ")
			hour = input("What time is it? ")

			if day == "friday" and hour == "late":
				print(1/0)
			
			if grinding != "y":
				print("Back to work!")
				continue
			else:
				print("Good boy!")
				continue

			print("grinding")

		except Exception as exc:
			raise RuntimeError("Please stop working - it's party time!") from exc

		time.sleep(2)

work_hard()			
