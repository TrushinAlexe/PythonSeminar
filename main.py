# 1Task

a = 123
print(a//100 + a//10%10 + a%10)

# 2Task

n = int(input())
m = n // 6
print(m, m * 4, m)

# 3Task

n = int(input())
s1 = n[0] + n[1] + n[2]
s2 = n[3] + n[4] + n[5]
if s1 == s2:
  print("YES")
else:
  print("NO")

# 4Task

n,m,k = int(input('В-те 1-ю сторону: ')),int(input('В-те 2-ю сторону: ')),int(input('В-те кол-во долек: '))
if k%n == 0 or k%m == 0:
    print('Yes')
else: print('No')
