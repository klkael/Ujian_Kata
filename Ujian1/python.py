a = {2,4,6,8,10,12,14,16,18,20}
b = {1,3,5,7,9,11,13,15,17,19}
c = {-9,-8,-7,-6,-5,-4,-3,-2,-1}
d = {2,3,5,7,11,13,17,19}
e = {4,6,8,9,10,12,14,15,16,18,20}

print(a|b|c|d|e)
print((a&b)|(d&e))
print((a|b)&(d|e))
print((a|b)-(d|e))
print((a|b|c)-(a&e))