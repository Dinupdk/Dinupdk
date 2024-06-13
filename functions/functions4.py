#with parameter, with return value
def get_count(arr,size,target_value):
    cnt=0
    for i in range(0,size):
        if arr[i]==target_value:
            cnt=cnt+1
    return cnt

mylist=[1,2,3,1,4,2,4,1,3,3,4,1,2,4,2]
print('1 occur :',get_count(mylist,len(mylist),1))
print('2 occur :',get_count(mylist,len(mylist),2))
print('3 occur :',get_count(mylist,len(mylist),3))
print('4 occur :',get_count(mylist,len(mylist),4))

'''
#recursion
def fun():
    print('hiii')
    fun()
fun()'''