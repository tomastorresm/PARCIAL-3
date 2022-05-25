from datetime import date

class User:
  UserId:str
  Password:str
  RegisterDate:date
  def __init__(self,UserID,Password,RegisterDate):
      self.UserId=UserID
      self.Password=Password
      self.RegisterDate=RegisterDate

  def login(self):
      ()
    

class Administrador:
  Name:str
  Email:str
  User:User
  def __init__(self,Name,Email,User):
      self.Name=Name
      self.Email=Email
      self.User=User



  def updateproducts(self):
    print()

class Costumer:
  Name:str
  Address:str
  Email:str
  CostumerId:str
  AccountBalance:float
  def __init__(self,Name,Addres,Email,CustomerId,AccountBalance):
      self.Name=Name
      self.Address=Addres
      self.Email=Email
      self.CostumerId=CustomerId
      self.AccountBalance=AccountBalance


  def register(self):
    print()
  
  def purchase(self):
    print()

class Order:
  Orderid:str
  Date:date
  CostumerName:str
  CostumerId:str

  def _init_(self,costumer:Costumer):
    self.usuario=costumer

  def placeorder(self):
    print()

class OrderDetails:
  Orderid:str
  ProductId:str
  ProductName:str
  Quatity:int
  UnitCost:float
  Total:float

  def _init_(self,order:Order):
    self.Orden=order

  def calculatetotal(self):
    print()
    