months = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

n = int(input("달의 번호: "))

if n in months:
    print("달의 번호:", months[n])
else:
    print("달의 번호: Unknown")
    
#360p 8번 문제