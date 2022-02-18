
class library:
    
    def __init__(self,library_name):
        self.list_of_book='hello'
        self.nameL=library_name
        self.list={}
    def display_book(self):
        for i,j in enumerate(self.list_of_book):
            print(i+1,':',j)        
    def lend_book(self):
        pass
    def add_book(self):
        pass
    def return_(self):
        pass
book_list=['Harry potter','Rich dad poor dad','Zero to one','Mechatronics']
satya=library(book_list,'satya')