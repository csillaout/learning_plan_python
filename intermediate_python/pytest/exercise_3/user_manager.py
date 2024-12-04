class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, username, email):
        self.users.append({"username": username, "email": email})

    def get_users(self):
        return self.users