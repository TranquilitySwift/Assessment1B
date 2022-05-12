group_One= [int(a) for a in input("Enter group number 1:"). split()]
group_Two= [int(a) for a in input("Enter group number 2:").split()]
print("Result:")
setGroup_Two= set(group_Two)
intersection= setGroup_Two.intersection(group_One)
intersectlist= list(intersection)

print(intersectlist)

