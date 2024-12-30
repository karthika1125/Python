                        #   uppercase
class String:
    def __init__(self):
        self.input_string=""
    def get_string(self):
            self.input_string= input("Enter a string :")
    def upper_case(self):
         print(self.input_string.upper())
handler = String() 
handler.get_string() 
handler.upper_case()