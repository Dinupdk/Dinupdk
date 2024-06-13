#with parameter ,without return value

def wellcome_user(name,gender):
    if gender=='male':
        print('wellcome Mr.',name)
    elif gender=='female':
        print('wellcome mis.',name)
    else:
        print('gender in not selected')

wellcome_user('Dinesh','male')