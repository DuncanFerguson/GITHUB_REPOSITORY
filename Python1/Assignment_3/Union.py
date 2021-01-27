def Union(a,b):
    '''the Purpose of this is to remove any of the duplicates in the list
    while trying to keep the same order'''
    # Making a combo list
    comboList = a + b
    #Looping through the combo list one at a time and finding if that number exists more than once in the list. If it does
    #I am removing it. Then continuing to loop through the combo. Eventually, all the dubs will be removed
    for i in comboList:
        dub = comboList.count(i)
        if dub >= 2:
            comboList.remove(i)
            # print("Dub Removed: ", comboList[i])
    return comboList

a= [1,5,6,5,2]
b = [3,5,1,9]

print("'Dedubbed' 'a' & 'b' list: ", Union(a,b))
print("List 'a' ", a)
print("List 'b' ", b)


