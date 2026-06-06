myDict = {"옷": 100, "컴퓨터": 2000, "모니터": 320}

total = 0

for v in myDict:
    total = total + myDict[v]

print("총 합계=", total)