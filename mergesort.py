def merge(a,b):
    c=[]
    index_a = index_b =0
    while index_a < len(a) and index_b < len(b):
        if a[index_a] < b[index_b]:
            c.append(a[index_a])
            index_a += 1
        else:
            c.append(b[index_b])
            index_b += 1
        if index_a < len(a):
            c.extend(a[index_a:])
        if index_b < len(b):
            c.extend(a[index_b:])
        return c
def merge_sort(x):
    if len(x) == 0 or len(x) ==1:
        return x
    else:
        middle = int(len(x)/2)
        a = merge_sort(x[:middle])
        b = merge_sort(x[middle:])
        return merge(a,b)
