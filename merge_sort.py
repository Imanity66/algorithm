def merge(a,b):
  c=[]
  i = j = 0
  while i<len(a) and j<len(b):
    if a[i] < b[j]:
      c.append(a[i])
      i +=1
    else:
      c.append(b[j])
      j+=1

    # while i < len(a):
    #     c.append(a[i])
    #     i += 1
    # while j < len(b):
    #     c.append(b[j])
    #     j += 1
    if i<len(a):
      c.extend(a[i:])
    if j<len(b):
      c.extend(b[j:])
    return c
def merge_sort(x):
  if len(x) == 0 or len(x)==1:
    return x
  else:
    mid = int(len(x)/2)
    a = merge_sort(x[:mid])
    b = merge_sort(x[mid:])
    return merge(a,b)

alist=[2,1,0,3,-1,5,4,4,8,9,15,16,22,36]
print (merge_sort(alist))
