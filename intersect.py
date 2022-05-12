group_One= [float(a) for a in input("Enter group number 1:"). split()]
group_Two= [float(a) for a in input("Enter group number 2:"). split()]
print("Result:")
setGroup_One= set(group_One)
intersection= setGroup_One.intersection(group_Two)
intersectlist= list(intersection)

print(intersectlist)

