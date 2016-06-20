currentYear = int(2016)
currentDay =int (172)
daysBeforeBDay = int(365-11)
daysSincebirthday = int(11+currentDay)
birthYear = int(1975)
leapYears = int(10)
daysAlive = (((currentYear-1)-birthYear)*365)+leapYears+daysSincebirthday
print ("DOB: Dec 20, ", birthYear, end="\n")
print("Due: June 20, ", currentYear, end="\n")
print("Days: ", daysAlive, " days", end="\n")



