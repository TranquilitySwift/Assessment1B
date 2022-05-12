group_One= [int(a) for a in input("Enter group number 1:"). split()]
group_Two= [int(a) for a in input("Enter group number 2:"). split()]
print("Result:")
setGroup_One= set(group_One)
setGroup_Two= set(group_Two)
print(setGroup_One or setGroup_Two)