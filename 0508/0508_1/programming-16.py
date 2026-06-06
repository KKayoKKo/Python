import random

chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password_list = random.sample(chars, 8)

password = ""

for c in password_list:
    password = password + c

print("생성된 암호 =", password)

#362p 16번 문제