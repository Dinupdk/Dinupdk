class Amazon:
    overall_discount=5
    def __init__(self,p_id,name,price,discount):
        self.id=p_id
        self.name=name
        self.price=price
        self.discount=discount
    def get_final_price(self):
        print(self.price-self.price*self.discount/100-Amazon.overall_discount*self.price/100)
    def get_data(self):
        print('id=',self.id) 
        print('name=',self.name)
        print('price=',self.price)
        print('discount=',self.discount)

    def change_overall_discount(self,dis):  #class method
        Amazon.overall_discount=0
        Amazon.overall_discount=dis
        print('overall discount=',Amazon.overall_discount())

    def static_method():
        print('static function')


p1=Amazon(1,'sugar',50,10)
p2=Amazon(2,'salt',20,10)

p1.get_data()
p1.get_final_price()
Amazon.change_overall_discount(100)
p1.get_data()
