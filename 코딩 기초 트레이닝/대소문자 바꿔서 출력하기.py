str = input()
res=""

for s in str:
    res += s.upper() if s.islower() else s.lower()
    
print(res)