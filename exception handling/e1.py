'''try:
  print(x)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

'''
'''try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")'''
'''try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")'''
'''x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")'''