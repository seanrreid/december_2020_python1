day_of_week = int(input('What Day of the Week (0-6)?'))

sleep = False

if day_of_week == 0 or day_of_week == 6:
    sleep = True

if sleep:
    print('Sleep in!!')
else:
    print('Go to work.')

# If the day of the week is 0 or if the day of the week is 6
# If the VALUE of the VARIABLE sleep is True