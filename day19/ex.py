d={'name':'Dinesh'}

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
d['age']=20


#Add a color item to the dictionary by using the update() method:
d.update({'class':'b.com'})

#The pop() method removes the item with the specified key name:
#d.pop('age')

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
#d.popitem()

#The del keyword removes the item with the specified key name:
#del d['name']

#The clear() method empties the dictionary:
#d.clear()

#Print all key names in the dictionary, one by one:
'''for i in d:
    print(i)
'''
#Print all values in the dictionary, one by one:
'''for i in d:
    print(d[i])
'''
#You can also use the values() method to return values of a dictionary:
'''for i in d.values():
    print(i)'''

#You can use the keys() method to return the keys of a dictionary:
'''for i in d.keys():
    print(i)'''
#oop through both keys and values, by using the items() method:
'''for i in d.items():
    print(i)'''
#Make a copy of a dictionary with the copy() method:
'''mydictionary=d.copy()
print(mydictionary)'''

#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Dinesh",
    "year" : 2004
  },
  "child2" : {
    "name" : "rupanand",
    "year" : 2010
  },
  "child3" : {
    "name" : "indu",
    "year" : 2011
  }
}
#print(myfamily)
#Print the name of child 2:
#print(myfamily["child2"]["name"])








#print(d)