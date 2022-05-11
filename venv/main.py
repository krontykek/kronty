m = []
c = 0
s = 0
while c != -1:
 m.append(c)
 c = int(input("Введите значение стороны. Ввод -1 означает конец списка. :"))
for i in range(0,len(m)):
 for j in range(i+1,len(m)):
  for n in range(j+1,len(m)):
   if m[i] + m[j] > m[n] and m[i] + m[n] > m[j] and m[n] + m[j] > m[i]:
    p = (m[i] + m[j] + m[n])/2
    x = (p * (p - m[i]) * (p - m[j]) * (p - m[n])) ** 0.5
    if x > s:
     s = x
print(s)
