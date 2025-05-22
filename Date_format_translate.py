'''
Given a date in the format "1st Mar 2025"
Write a method to translate this into "2025-03-01"
Assume that the string is always correctly formatted
'''

def date_translate(date):
    day, month, year = date.split(' ')
    new_day =  translate_day(day)
    new_month = translate_month(month)
    final_date = f'{year}-{new_month}-{new_day}'
    print("==> Result: ", final_date)
    return final_date

def translate_day(day):
    new_date = day[:-2]
    return new_date.zfill(2)

def translate_month(month):
    month_translation = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
                         "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                         "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    return month_translation[month]



assert date_translate("1st Mar 2025")  == "2025-03-01"
assert date_translate("2nd Jan 1994")  == "1994-01-02"
assert date_translate("3rd Apr 1778")  == "1778-04-03"
assert date_translate("25th Dec 2000")  == "2000-12-25"