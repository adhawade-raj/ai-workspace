s = {1,2,2,2,3}

print("----------add() # This will add the element 4 to the set----------")
s.add(4)  # This will add the element 4 to the set
print(s)  # This will print {1, 2, 3, 4} because sets do not allow duplicate elements

print("----------remove() # This will remove the element 2 from the set----------")
s.remove(2)  # This will remove the element 2 from the set
print(s)  # This will print {1, 3, 4} because the element 2 has been removed from the set

print("----------pop() # This will remove and return an arbitrary element from the set----------")
popped_element = s.pop()  # This will remove and return an arbitrary element from the set
print(f"Popped element: {popped_element}")
print(s)  # This will print the remaining elements in the set

print("----------clear() # This will remove all elements from the set----------")
s.clear()  # This will remove all elements from the set
print(s)  # This will print an empty set


s1={1, 2, 3}
s2={3, 4, 5}

print("----------union() # This will return a new set with all elements from both sets----------")
union_set = s1.union(s2)  # This will return a new set with all elements from both sets
print(union_set)  # This will print {1, 2, 3, 4, 5} because it contains all unique elements from both sets

print("----------intersection() # This will return a new set with elements common to both sets----------")
intersection_set = s1.intersection(s2)  # This will return a new set with elements common to both sets
print(intersection_set)  # This will print {3} because it is the only element common to both sets

