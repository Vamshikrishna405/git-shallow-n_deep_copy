class Customer:
    def __init__(self,id,name,mobile,email):
        self.__id=id
        self.__name = name
        self.__mobile=mobile
        self.__email=email

    def set_id(self,id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self,name):
            self.__name = name
    
    def get_name(self):
        return self.__name

    def set_mobile(self,mobile):
            self.__mobile = mobile
    
    def get_mobile(self):
            return self.__mobile

    def set_email(self,email):
            self.__email = email
    
    def get_email(self):
            return self.__email

    def __str__(self):
          return f'({self.__id},{self.__name},{self.__mobile},{self.__email})'

    def __lt__(self, other):
          return self.__name < other.__name 
          
def main():
    n=int(input('enter the number of customers'))
    my_list=[]
    for i in range(n):
        lst=input('enter the customer details \n').split(',')
        c = Customer(100+i,lst[0],int(lst[1]),lst[2])
        my_list.append(c)
    print('before sorting')
    for i in my_list:
        print(i)
    my_list.sort(key=lambda c : c.get_mobile())
    print('after sorting')
    for i in my_list:
        print(i)

if __name__ == '__main__':
    main()

          
    
