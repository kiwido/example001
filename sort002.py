a = [[1,2],[0,9],[0,6],[2,3]]

def g(a1,a2):
    x1, y1 = a1
    x2, y2 = a2

    if x1 == x2:
        if y1 > y2:
            return True
    if x1>x2:
        return True
    else:
        return False
    
"""
5 8 1 6 2
1 8 5 6 2 
"""
def sort(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if g(a[i],a[j]):
                swap = a[i]
                a[i] = a[j]
                a[j] = swap
sort(a)
print(a)
