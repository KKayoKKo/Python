date_in = input("날짜를 입력하시오: ")

parts = date_in.split("/")

m = parts[0]
d = parts[1]
y = parts[2]

result = y + m + d

print(date_in, "->", result)

#362p 14번 문제