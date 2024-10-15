your_list= [200,15,"Programming",1+2,"lab3"]
len(your_list)
your_list.append(1)
your_list.insert(0,1+4)
print(your_list)
your_list.remove(200)
print(your_list)
len(your_list)
print(your_list[0])
your_list.insert(2,"fruit")
print(your_list)
your_list[1]= 2
print(your_list)
print(type(your_list))
your_tuple= tuple(your_list)
print(type(your_tuple))
print(your_tuple[0])
print(len(your_tuple))
your_list[0]= 4   #Can not change tuple 

another_tuple=(5,13,24)
joined_tuple= your_tuple + another_tuple
print(joined_tuple)
your_list= list(joined_tuple)
type(your_list)
your_set = set(your_list)
len(your_set)
your_set.add("Diego")
print(your_set)
your_set.add("fruit")
print(your_set)  #Duplication are not allowed
another_set= {1,3,4}
new_set= your_set & another_set
print(new_set)

def multiply(a,b):
    c= a*b 
    #return c 


