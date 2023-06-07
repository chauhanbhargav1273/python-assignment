FruitsTP = ('Apple', 'Orange', 'Banana', 'Kiwi', 'Grape', 'Blackberry')
tp = (9, 4, -5, 0, 22, -1, 2, 14)

#fruitsTP = (apple,banana,blackberry,grape,kiwi,orange)
#tp = (-5,-1,0,2,4,9,14,22)

#Finding Sum of all item in a  using Sum() Method
print('Sum of all items in a tp  = ', sum(tp))

#Calculating Length of a  using len() Method
print('Length of a FruitsTP  = ', len(FruitsTP))
print('Length of a tp  = ', len(tp))

#Finding Minimum item in a  using min() Method
print('Minimum item in a FruitsTP  = ', min(FruitsTP))
print('Minimum item in a tp  = ', min(tp))

#Finding Maximum item in a  using max() Method
print('Maximum item in a FruitsTP  = ', max(FruitsTP))
print('Maximum item in a tp  = ', max(tp))

# Using Sorted() Method
print('After Sorting FruitsTP  = ', sorted(FruitsTP))
print('After Sorting tp  = ', sorted(tp))

# Index position of an item in a  using index() Method
print('The Index position of Banana = ', FruitsTP.index('Banana'))
print('The Index position of -1 = ', tp.index(-1))

# Counting items in a  using count() Method
tp2 = (9, 4, 1, 4, 9, -1, 2, 4)
print('Number of Times 4 is repeated = ', tp2.count(4))
print('Number of Times 9 is repeated = ', tp2.count(9))

# Converting List
tp3 = [1, 2, 3, 4, 5]
print(tuple(tp3))
