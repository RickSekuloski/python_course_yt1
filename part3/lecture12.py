# Set Methods
new_set = {1, 2, 3, 4, 5, 6, 7}
new_set1 = {5, 6, 7, 8, 9, 10, 11}

#1) copy() method
new_set2 = new_set.copy()
print(new_set2)

#2) clear() method
new_set2.clear()
print(new_set2)

#3) difference() method
new_set = {1, 2, 3, 4, 5, 6, 7}
new_set1 = {5, 6, 7, 8, 9, 10, 11}
print(new_set.difference(new_set1))

#4) difference_update()
new_set.difference_update(new_set1)
print(new_set)

#5) discard() method
new_set = {1, 2, 3, 4, 5, 6, 7}
new_set.discard(7)
print(new_set)

#6) intersection() method
new_set = {1, 2, 3, 4, 5, 6, 7}
new_set1 = {5, 6, 7, 8, 9, 10, 11}
print(new_set.intersection(new_set1))

#7) intersection_update() method
new_set = {1, 2, 3, 4, 5, 6, 7}
new_set1 = {5, 6, 7, 8, 9, 10, 11}
new_set.intersection_update(new_set1)
print(new_set)

#8) isdisjoint() method
new_set = {1, 2, 3, 4, 5, 6, 7}
new_set1 = {5, 6, 7, 8, 9, 10, 11}
print(new_set.isdisjoint(new_set1))

#TRUE
new_set = {1, 2, 3, 4}
new_set1 = {5, 6, 7, 8, 9, 10, 11}
print(new_set.isdisjoint(new_set1))

#9) union()
new_set = {1, 2, 3, 4, 5, 6, 7}
new_set1 = {5, 6, 7, 8, 9, 10, 11}
print(new_set.union(new_set1))

#10) issubset()
new_set = {5, 6, 7}
new_set1 = {5, 6, 7, 8, 9, 10, 11}
print(new_set.issubset(new_set1))

#11) issuperset()
new_set = {5, 6, 7}
new_set1 = {5, 6, 7, 8, 9, 10, 11}
print(new_set.issuperset(new_set1))

#TRUE
new_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
new_set1 = {5, 6, 7, 8, 9, 10, 11}
print(new_set.issuperset(new_set1))