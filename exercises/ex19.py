
class CurrentDate:
	def __init__(self, year: int, month: int, day: int,	weekday: int, leap_year: bool):
		self.year = year
		self.month = month
		self.day = day
		self.weekday = weekday
		self.leap_year = leap_year

	def skip_day(self):
		#print(f"{self.day} / {self.month} / {self.year} - weekday: {self.weekday}")
		if self.month == 2:
			if self.leap_year:
				if self.day == 29:
					self.skip_month()
				else:
					self.day += 1
			else:
				if self.day == 28:
					self.skip_month()
				else:
					self.day += 1
		elif self.month == 9 or self.month == 11 or self.month == 6 or self.month == 4:
			if self.day == 30:
				self.skip_month()
			else:
				self.day += 1
		else:
			if self.day == 31:
				if self.month == 12:
					self.skip_year()
				else:
					self.skip_month()
			else:
				self.day += 1

		if self.weekday == 8:
			self.weekday = 2
		else:
			self.weekday += 1		

	def	skip_month(self):
		self.month += 1
		self.day = 1

	def skip_year(self):
		self.year += 1
		self.month = 1
		self.day = 1
		self.is_leap_year()
		#print(f"New year {self.year}, leap year: {self.leap_year}.")

	def is_leap_year(self):
		if self.year % 4 == 0 and ( not self.year % 100 == 0 or self.year % 400 == 0):
			self.leap_year = True
		else:
			self.leap_year = False

def exercise19():
	current_date = CurrentDate(
		year=1901,
		month=1,
		day=1,
		weekday=3,
		leap_year=False
	)
	
	total_sum = 0

	while current_date.year < 2000 or current_date.month < 12 or current_date.day < 31:
		current_date.skip_day()
		if current_date.weekday == 7 and current_date.day == 1:
			total_sum += 1

	print(f"Result {total_sum}")


if __name__ == '__main__':
	exercise19()


# You are given the following information, but you may prefer to do some research for yourself.

# -	1 Jan 1900 was a Monday.

# -	Thirty days has September,
# 	April, June and November.
# 	All the rest have thirty-one,
# 	Saving February alone,
# 	Which has twenty-eight, rain or shine.
# 	And on leap years, twenty-nine.

# -	A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# 1900 nao é leap year
# 2000 é leap year