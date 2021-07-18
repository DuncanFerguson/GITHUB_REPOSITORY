# When adding things to a list, you can just append to the end of a list, but then you have to search the whole list
# you can append to the end of the list, then sort the list.  We showed how you can jump into the middle, see if the value is 
# above or below, then jump into the middle of the half, etc.
# A hashtable allows for very fast searches because you can immediately jump to the nearest location of the data you are seeking

hashstatus=[]  # create empty hashstatus table, will hold Empty, Filled and Deleted
hashtable = []   # create empty hashtable, will hold the names

for i in range(10):  # create empty table 10 long
    hashtable.append(None)
    hashstatus.append("Empty")
print(hashstatus)
print(hashtable)
def insert(elem):
    global hashstatus
    global hashtable
    
    hash = ord(elem[0]) % len(hashtable)  # compute hash value
    if hashstatus[hash] == "Empty":  # if hashstatus is empty, fill it with new name
        hashstatus[hash] = "Filled"  # change status to filled
        hashtable[hash] = elem    # add name to table
    else:     # if that location in table is full, start searching for the next empty spot
        i = hash
        while hashstatus[i] != "Empty":
            i = i + 1
            if i >= len(hashtable):   # if we roll over to end of list, start over at zero
                i = 0
        hashstatus[i] = "Filled"  # found an empty spot, change status
        hashtable[i] = elem  # found an empty spot, add name
    
insert("amy")
print("table:",hashtable)
print("status: ", hashstatus)

insert("chase")
print("table:",hashtable)
print("status: ", hashstatus)

insert("chris")
print("table:",hashtable)
print("status: ", hashstatus)

insert("alphonso")
print("table:",hashtable)
print("status: ", hashstatus)

insert("adam")
print("table:",hashtable)
print("status: ", hashstatus)