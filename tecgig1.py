#testCase = int(input())
#output = []
#def fun1():
#  n = int(input())
#  st1 = input()
#  en1 = input()
#  st2 = st1.split()
#  en2 = en1.split()
#  st3 = [int(j) for j in st2]
#  en3 = [int(k) for k in en2]
#  for l, m in zip(st3, en3):
#    if l > m:
#      return "LOSE"
#  return "WIN"
# #

#for i in range(testCase):
#  output.append(fun1())
#for i in output:
#  print(i)

testCase = int(input())
output = []
def fun1():
  n = int(input())
  st1 = input()
  en1 = input()
  st2 = st1.split()
  en2 = en1.split()
  st3 = [int(j) for j in st2]
  st3.sort()
  en3 = [int(k) for k in en2]
  en3.sort()
  for l, m in zip(st3, en3):
    if l >= m:
      return "LOSE"
  return "WIN"

for i in range(testCase):
  output.append(fun1())
for i in output:
  print(i)




