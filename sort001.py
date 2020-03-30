from operator import itemgetter

a = [(1,2),(0,9),(0,6),(2,3)]

a.sort(key=itemgetter(0,1))
print(a)
