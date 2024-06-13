class Driver:
    def __init__(self,f_name,l_name,age,mobile_no):
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
        self.mobile_no=mobile_no
    def full_details(self):
        return f'fullname:{self.f_name} {self.l_name} age={self.age}  mobileno={self.mobile_no}'
        
    def full_name(self):
        return f'full name is :{self.f_name} {self.l_name}'
class License(Driver):
    def __init__(self,f_name,l_name,age,mobile_no,license_id,validity_year):
        Driver.__init__(self,f_name,l_name,age,mobile_no)
        self.license_id=license_id
        self.validity_year=validity_year
    def is_valid_license(self):
        if self.validity_year>=2024:
            return  f'valid license'
        else:
            return f'invalid license'

class Vehical(License):
    def __init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vechical_no,vechical_age):
        License.__init__(self,f_name,l_name,age,mobile_no,license_id,validity_year)
        self.vechical_no=vechical_no
        self.vechical_age=vechical_age
    def is_validity_driver(self):
        if self.age>=20:
            return True
        else:
            return False


user1=Vehical('Dinesh','potta',20,7013418146,21062003,300,'AP39GH8998',5)
print(user1.full_name())
print(user1.full_details())
print(user1.is_valid_license())
print(user1.is_validity_driver())
