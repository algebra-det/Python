from datetime import date, datetime

# strftime() can work with date, datetime, time objects

date_object = date(2020, 10, 25)
print date_object.strftime("%Y/%m/%d")

b = datetime(2019, 9, 20, 4, 55, 38)

print b.strftime("%Y-%m-%d %H:%M:%S")
print b.strftime("%Y/%m/%d")
print b.strftime("%H:%M:%S")
print b.strftime("%I:%M:S %p")
print b.strftime("%a, %b, %d, %Y")
print b.strftime("%c")
print b.strftime("%j")
print b.strftime("%U")
print b.strftime("%w")


"""
%Y = Year like 2019,2020,...
%m = month like 01,02,...
%d = day like 23,24,25,...
%H = Hour like 11,12,13,14,...  in 24-hour formatt
%M = Minutes like 55,56,57,...
%S = Seconds like 55,56,57,...

%I = Hour in 12-hour format

%a = weekdays name (short) like mon, tues,...
%A = weekday name (full) like monday, tuesday,...

%b = Month like jan, feb,...
%B = Month like January, February,...

%j = Day of the year as a decimal number like 001, 366

%U = Week number of the year (sunday as the first day of the week) like [00,53]

%w = weekday as a decimal number [0(sunday), 6]

"""
