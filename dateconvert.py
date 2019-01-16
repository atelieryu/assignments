
#Try it
import datetime

birthday = "1-May-12"
date_format = "%d-%b-%y"

parsed_date = datetime.datetime.strptime(birthday, date_format)
# print date as "5/1/2012"

new_pattern = parsed_date.strftime("%-m/%-d/%Y")
print(new_pattern)
