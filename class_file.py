'''import constants
class Employee:
    def __init__(self, id, nm, ag, sal, desgn):
        self.EmpID = id
        self.EmpName = nm
        self.EmpAge = ag
        self.EmpSalary = sal
        self.EmpDesignation = desgn


    def __str__(self):     #string method
        return f"\n{self.__dict__}"

    def __repr__(self):
        return str(self)

e1 = Employee(id=101, nm="ABC101", ag=24, sal=45000, desgn=constants.SOFTWARE_ENGINEER)
e2 = Employee(id=102, nm="ABC102", ag=25, sal=46000, desgn=constants.TESTER)       
e3 = Employee(id=103, nm="ABC103", ag=26, sal=47000, desgn=constants.LINUX_ADMIN)       
e4 = Employee(id=104, nm="ABC104", ag=27, sal=48000, desgn=constants.DEVOPS_ENGINEER)       
e5 = Employee(id=105, nm="ABC105", ag=28, sal=49000, desgn=constants.SOFTWARE_ENGINEER)

emp_list = [e1, e2, e3, e4, e5]
# print(emp_list)

# for emp in emp_list:
#     print(emp)

# def get_emp_by_id(eid):
#     filtered_emp_list = list()
#     for emp in emp_list:
#         if emp.EmpID in [eid,105]:
#             filtered_emp_list.append(emp)
#     return filtered_emp_list


# res = get_emp_by_id(103)
# print(res)              


def incremented_salary():
    for emp in emp_list:
        incremented_list = list()
        if emp.EmpSalary < 50000:
            emp.EmpSalary =emp.EmpSalary + ((10/100)* emp.EmpSalary)
            incremented_list.append(emp)  
    return emp_list    
        

res = incremented_salary()
print(res)

# output:
# {'EmpID': 101, 'EmpName': 'ABC101', 'EmpAge': 24, 'EmpSalary': 49500.0, 'EmpDesignation': 'software engineer'},
# {'EmpID': 102, 'EmpName': 'ABC102', 'EmpAge': 25, 'EmpSalary': 50600.0, 'EmpDesignation': 'tester'},
# {'EmpID': 103, 'EmpName': 'ABC103', 'EmpAge': 26, 'EmpSalary': 51700.0, 'EmpDesignation': 'linux admin'},
# {'EmpID': 104, 'EmpName': 'ABC104', 'EmpAge': 27, 'EmpSalary': 52800.0, 'EmpDesignation': 'devops engineer'},
# {'EmpID': 105, 'EmpName': 'ABC105', 'EmpAge': 28, 'EmpSalary': 53900.0, 'EmpDesignation': 'software engineer'}'''


#crud = create , Read-singlr ,multi   ,Update, Delete.

class Product:
    Ecommerce_platform = "Amazon"
    list_of_product =[]
    def __init__(self, pid, pname, pprice, pqty, pcat):
        self.ProductID = pid
        self.ProductName = pname
        self.ProductPrice = pprice
        self.ProductQTY = pqty
        self.ProductCat = pcat
 
    def __str__(self):
        return f"\n{self.__dict__}"

    def __repr__(self):
        return str(self)
            
    
    def show_details(self):
        print(f"""
Product ID:- {self.ProductID}
Product Name:- {self.ProductName}
Product Price:- {self.ProductPrice}
Product Qty:- {self.ProductQTY}
Product cat:- {self.ProductCat}
         """)                       


    def total_price(self):
        total = self.ProductPrice * self.ProductQTY
        return f"Total price for {self.ProductName}:- {total}"

    @classmethod
    def set_idslist(cls):        #set satic varibale
        cls.ids_list = list(map(lambda x: x.ProductID, cls.list_of_product))



    @classmethod
    def add_product(cls, prod):
        """  create product (single product or list of product) """
        if type(prod) == cls:
            cls.list_of_product.append(prod)
        elif type(prod) == list:
            cls.list_of_product.extend(prod)
        print("products added successfully in amazon...!")
        cls.set_idslist()    # call static varibale for execute id list otherwise it is empty for other classmethods like get_single_prod, update prod
    @classmethod
    def get_all_products(cls):
        print(cls.list_of_product)

    @classmethod
    def get_single_prod(cls,pid):
        # print(cls.ids_list)
        if pid in cls.ids_list: 
            for prod in cls.list_of_product:
                
                if prod.ProductID == pid:
                    return prod   
                
        else:
            print(f"product is not available for given id..Available product id are {cls.ids_list}")   

    # @classmethod
    # def multi_product(cls, *argv):
    #     cls.list_of_product.extend(argv)
    #     print("All provided product added successfully in amazon...!")    
    
    
    @classmethod
    def update_prod (cls, pid, data):
        for item in cls.list_of_product:
            if item.ProductID == pid:
                name = data.get("name")
                price = data.get("price")
                qty = data.get("qty")    
                cat = data.get("cat")    

                if name:  #True             
                    item.ProductName = name
                if price:  #True             
                    item.ProductPrice = price
                if qty:  #True             
                    item.ProductQTY = qty
                if cat:  #True             
                    item.ProductCat = cat

                if data.get("id"):
                    print("Product updated successfully but id can not be updated as it is unique...!")
                else:
                    print("Product updated successfully")        
                break    

        else:
            print(f"product is not available for given id..Available product id are {cls.ids_list}")


    @classmethod
    def delete_prod(cls, pid):
        if pid in cls.ids_list:
            for item in cls.list_of_product:
                if item.ProductID == pid:
                    cls.list_of_product.remove(item)
                    print("item deleted succesfully")
                    break           
        else:
            print(f"product is not available for given id..Available product id are {cls.ids_list}")



                    
                  




p1 = Product(pid=101, pname="Laptop", pprice=54000, pqty=6, pcat="Electronics")
p2 = Product(pid=102, pname="Table", pprice=2500, pqty=17, pcat="Furniture")
p3 = Product(pid=103, pname="chain", pprice=50000, pqty=5, pcat="Gold")
p4 = Product(pid=104, pname="Wings of fire", pprice=250, pqty=75, pcat="bookk")
p5 = Product(pid=105, pname="Bicyle", pprice=12000, pqty=5, pcat="vehicle")
p6 = Product(pid=106, pname="Tshirt", pprice=350, pqty=50, pcat="clothing")

# list_of_product = [p1, p2, p3, p4, p5, p6]
# for item in list_of_product:
    # print(item.total_price())
Buket = [p1, p2 ,p3, p4, p5]
# Product.add_product(p1)
Product.add_product(Buket)
# Product.add_product(p2)
# Product.multi_product(p1, p2, p3) 
# print(Product.list_of_product)

Product.get_all_products()
# print(Product.get_single_prod(103))   
# Product.update_prod(107, {"price":54000, "name":"Ring", "qty":7, "cat":"24 Gold"})
# print(Product.get_single_prod(103))

# Product.delete_prod(103)



for i in range(100):
    print(i)    