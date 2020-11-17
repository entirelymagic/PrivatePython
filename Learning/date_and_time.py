"""
You have to allways point to a central reference
when you speak about the time.

"""
from datetime import datetime, timezone, timedelta

print(datetime.now(timezone.utc)) # time with no offset

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))

user_date = input('Enter the date in YYYY--mm-dd format:')
user_date = datetime.strptime(user_date, '%Y-%m-%d')

print(user_date)

