from abc import ABC, abstractmethod
import re
import pdb


class User:
    def __init__(self, fullname, username, password) -> None:
        self.fullname = fullname
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f"""
                {self.fullname}
                {self.username}
                {self.password} 
        """


class Chain(ABC):
    def __init__(self, next=None) -> None:
        self.next: Chain = next

    def execute(self, user: User):
        result = self._do_execute(user)

        if result and self.next:
            self.next.execute(user)

    @abstractmethod
    def _do_execute(self, user: User):
        pass



class FullnameConfirm(Chain):

    def _do_execute(self, user: User):
        pattern = r'[a-zA-Z\s]{4}'
        if re.search(pattern, user.fullname):
            print(f"fullname assigned: {user.fullname}")
            return True


class UsernameConfirm(Chain):
    def _do_execute(self, user: User):
        pattern = r'[a-zA-Z\d_]{6}'
        if re.search(pattern, user.username):
            print(f"username assigned: {user.username}")
            return True


class PasswordConfirm(Chain):
    def _do_execute(self, user: User):
        pattern = r'^(?=.*[!@#$%^&*()_+{}[\]:;<>,.?~\\/\-=|])(?=.*\d)[\w!@#$%^&*()_+{}[\]:;<>,.?~\\/\-=|]{8,}$'
        if re.search(pattern, user.password):
            print(f"password assigned: {user.password}")
            return True


class CreateAccount(Chain):
    def _do_execute(self, user: User):
        print("user created successfully!!!")
        return True


class SignUp:
    def execute(self, user: User, chain: Chain):
        chain.execute(user)


if __name__ == "__main__":
    user = User('john week', 'john2002', 'p@sword123')
    signup = SignUp()

    create_account = CreateAccount()
    pass_confirm = PasswordConfirm(create_account)
    username_confirm = UsernameConfirm(pass_confirm)
    fullname_confirm = FullnameConfirm(username_confirm)

    signup.execute(user, fullname_confirm)
