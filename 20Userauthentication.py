from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    def login(self):
        pass
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print(f"Logged in to Google")
    def logout(self):
        print("Logged out of Google")
class FacebookAuth(UserAuthentication):
    def login(self):
        print(f"Logged in to Facebook")
    def logout(self):
        print("Logged out of Facebook")

fcebook=FacebookAuth()
fcebook.login()
fcebook.logout()
print()
google=GoogleAuth()
google.login()
google.logout()