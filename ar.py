day = 4

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")    
    case 7:
        print("Saturday")
    case _:
        print("Invalid day")


user_role = "student"

match user_role:
    case "admin":
        print("Welcome, Administrator")

    case "student":
        print("Welcome, Student")

    case "teacher":
        print("Welcome, Teacher")

    case _:
        print("Unknown user")


day = "saturday"

match day:
    case "saturday" | "sunday":
        print("It's the weekend")

    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It's a working day")

network = input("Your phone number?")
network_line = (network[0:4]) 

match network_line:
    case "0703" | "0906" | "0806" | "0810":
        print("mtn")
    case "0705" | "0811" | "0915" | "0905":
        print("Glo")
    case "0701" | "0904" | "0708" | "0812":
        print("airtel")
    case "0809" | "0818" | "0818" | "0912":jn#         print("9mobile")
    case _:
        print("invalid number")


agetoday = 20

match agetoday:
    case number if number >= 18:
        print("You are an adult")

    case number if number  < 18:
        print("you are a minor")


age = 12
status = (age > 12 and "Adult") or "Minor"
print(status)

num = 3
day = "Weekend" if num > 5 else "Weekday"
print(day)

num = 6
day = "Fri-day" if num == 5 else "Sat-day" if num == 6 else "sun" if num == 7 else "weekday"
print(day)

num2 = 1
days = "Monday" if num2 == 1 else("Tuesday" if num2 == 2 else "Invalid numbers")
print(days)

num = 1
prey = "positive numbers" if num > 0 else "negative numbers"
print(prey)

num4 = int(input("Enter the num: "))
status = "Even numbers" if num4 % 2 == 0 else "Odd numbers"
print(status)


network = input("Your phone number?")
network_line = (network[0:4]) 

if network_line in ("0703", "0906", "0806", "0810"):
    print("mtn")
elif network_line in ("0705", "0811", "0915", "0905"):
    print("Glo")
elif network_line in ("0701", "0904", "0708", "0812"):
    print("airtel")
elif network_line in ("0809", "0818", "0912"):
    print("9mobile")
else:
    print("invalid number")