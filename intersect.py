group_One= [int(a) for a in input("Enter group number 1:"). split()]
group_Two= [int(a) for a in input("Enter group number 1:"). split()]
print("Result:")
setGroup_One= set(group_One)
intersection= setGroup_One.intersection(group_Two)
intersectlist= list(intersection)

print(intersectlist)

