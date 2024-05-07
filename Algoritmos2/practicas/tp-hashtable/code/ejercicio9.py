from dictionary import * 


#Time complexity --> O(S + T)
def isSubSet(S,T): 
    d = [[] for _ in range(10)] 
    for element in T: # O(T)
        insert(d,element,element) 

    for element in S: 
        if not search(d,element): #Asumiendo search en O(1) --> O(S)
            return False 
    return True 

#Test 
s = [1,2,3,4,5,14]
t = [1,2,3,4,5,6,7,8,9,10]

print(isSubSet(s,t)) 

