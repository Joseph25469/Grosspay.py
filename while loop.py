#while statement

#continue
i = 0 
while i < 5:
    i+=1
    if i==3:
        continue
    print(i)
    


#break
i = 1 
while i < 5:
    print(i)
    if i==4:
        break
    i+=1

#else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")