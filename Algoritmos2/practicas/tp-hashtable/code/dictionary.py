#Hash function for alphanumeric chars --> h= ord(‘a’) - ord(‘a’)


def insert(D, key, value):
    #Determine the index at which the key-value pair will be stored
    index = hashFunction(key)
    if D[index] == None:
        D[index] = [(key, value)]
    else:
        D[index].append((key, value)) #Time complexity for .append for the average case is O(1)
    return D


def search(D, key):
    index = hashFunction(key)
    if D[index] is None:  #If the index is empty, the key is not present
        return None
    if len(D[index]) == 1:  #if only one element is present at the index
        bucket = D[index]
        k, v = bucket[0] #---->> O(1) 
        
    for k, v in D[index]:  #If there are collitions -->> O(n)
        if k == key:
            return v
        return None


def delete(D, key):
    index = hashFunction(key)
    if D[index] is not None: 
        if len(D[index]) == 1:  #there's only one element at the index -->> O(1)
            D[index] = None
            return D
    else: #There are collitions -->> O(n)
        for k, v in D[index]:
            if k == key:
                D[index].remove((k, v))
                return D
    return D


def hashFunction(k):
    k = int(k)  #key-value pairs will be inserted at index k
    return k % 9


def printHashTable(D):
    for index, slot in enumerate(D):
        print(f"slot {index}:")
    if slot:
        for key, value in slot:
            print(f"  Key: {key}, Value: {value}")
    else:
        print("None")

'''
dic = [[] for _ in range(10)]  #dictionary size 10
insert(dic, 1, 100)
insert(dic, 2, 200)
insert(dic, 3, 300)
insert(dic, 5, 500)
insert(dic, 6, 600)
insert(dic, 7, 700)
insert(dic, 10, "hola")

printHashTable(dic)
print("after deletion------------------------------------------------")
delete(dic, 1)
printHashTable(dic)
'''




