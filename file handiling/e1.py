#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content
#The open() function returns a file object,
#  which has a read() method for reading the content of the file


#f = open("myfile.txt", "x") create a file
#f = open("myfile.txt", "w")
'''f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
'''
'''
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())'''
'''
import os
os.remove("demofile2.txt")'''
'''import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")'''
'''import os
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
else:
    print("The file does not exist")
'''