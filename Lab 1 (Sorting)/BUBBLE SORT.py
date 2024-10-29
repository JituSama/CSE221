def MarkSort(mark, next):
  
  for i in range(next-1):
    flag = False
    for j in range(next-i-1):
      if mark[j]>mark[j+1]:
        mark[j],mark[j+1] = mark[j+1],mark[j]
        flag = True
    if flag == False:
      break
  return mark

marks = ['80','60','80','50']
next = 4
print(MarkSort(marks,next))