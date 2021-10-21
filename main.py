'''
For in Loop 
'''

Students = ['Bob', 'Adriana', 'Felix']
for x in Students: 
  print ('hi')

#==========================

print(range(10))
print(list(range(10)))
print(list(range(3,6)))
print(list(range(3, 12,3)))

#============================

for x in range (1, 6, 2):
  print(x*2)

#==============================

#For in loop within a for in loop 

for i in range(1, 6):
  for j in range (i):
    print ('*',end='')
  print()

#================================

'''
while loop 
'''

i = 6 
while i < 10:
  print(i)
  i+=1

#=============================
#break staments 

i = 1 
while i < 10:
  print(i)
  if i == 5:
    break
  i+=1

#==================================
#continue Statement 
i = 1 
while i < 7:
  i+=1
  if i == 4:
    continue
  print(i)

#=======================================

for i in range (1,10):
  if i == 3: 
    break
    print(i)
  


