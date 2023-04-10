import string

class BasePasswordManager:
    def __init__(self, password):
        self.old_passwords = [password]
        
    def get_password(self):
        return self.old_passwords[-1]
    
    def is_correct(self, password):
        return password == self.get_password()

class PasswordManager(BasePasswordManager):
    def __init__(self, password):
        super().__init__(password)
        self.security_level = self.get_security_level(password)
    
    def set_password(self, new_password):
        if len(new_password) < 6:
            print("Error: Password length must be at least 6.")
            return
        
        new_security_level = self.get_security_level(new_password)
        if new_security_level < self.security_level:
            print("Error: Password security level is too low.")
            return
        
        if self.security_level == 2 and new_security_level < 2:
            print("Error: Password must contain special characters.")
            return
        
        self.old_passwords.append(new_password)
        self.security_level = new_security_level
        print("Password changed successfully.")
    
    def get_level(self, password=None):
        if password is None:
            password = self.get_password()
        return self.get_security_level(password)
    
    @staticmethod
    def get_security_level(password):
        if all(char.isalnum() for char in password):
            return 0
        elif any(char.isalpha() for char in password) and any(char.isdigit() for char in password):
            return 1
        elif any(char in string.punctuation for char in password):
            return 2
        else:
            return 0
password_manager = PasswordManager("Sbo@1234ts1956os")
print(password_manager.get_password())  
print(password_manager.is_correct("Sbo@1234ts1956os"))  
print(password_manager.is_correct("wrong_password"))  
print(password_manager.get_level())  

password_manager.set_password("new_password")  
print(password_manager.get_password())  
print(password_manager.get_level())  

password_manager.set_password("new")  
password_manager.set_password("Sbo@1234ts1956os") 
password_manager.set_password("newpassword") 
