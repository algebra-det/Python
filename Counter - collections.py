from collections import Counter

a = [1,2,3,2,6,9,8,4,5,2,1,6,3,2,1,5,6,4,9,7,9,9,4,6,1,21,2,1,2,2]
print(a)
p = Counter(a)      # It will automatically arrange most occured to the least occured
print(p)
print(p[1])     # It will give you the number of times 1 has occured
print(p.most_common(1))     # Will give you 1 of the mostly occured numbers
                            # try giving 2 in most_common(2)