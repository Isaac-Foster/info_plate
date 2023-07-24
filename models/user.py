from string import punctuation
from re import search, escape
from random import choice
from dataclasses import dataclass
from base64 import b64encode


from database.sql import cur, commit

def is_strong_pass(
    passwd: str, 
    chars: int = 10, 
    lowers: int = 3, 
    uppers: int = 1, 
    digits: int = 1
    ) -> bool:

    is_strong = search(
        (
            "(?=^.{%i,}$)"
            "(?=.*[a-z]{%i,})"
            "(?=.*[A-Z]{%i})"
            "(?=.*[0-9]{%i,})"
            "(?=.*[%s}]+)"
        ) % 
        (
            chars, lowers, uppers,
            digits, escape(punctuation)
        ),
        passwd
    )

    return True if is_strong else False


@dataclass
class Response:
    _id: int = None
    login: str = None
    passwd: str = None
    type: str = None

    def encode(self):
        self.passwd = b64encode(
            self.passwd.encode("utf-8")
            ).decode("utf-8")

        return self.passwd


@dataclass
class HTTPresponse:
    message: dict
    status: bool | None


@dataclass
class UserLogin:
    login: str
    passwd: str 
    type: str = "standard"


    def encode(self):
        self.passwd = b64encode(
            self.passwd.encode("utf-8")
            ).decode("utf-8")
        return self.passwd


    def verify(self) -> tuple:
        r = None
        try:
            cur.execute(
                "SELECT * FROM users WHERE login LIKE %s",
                [self.login]
                )
            
            r = cur.fetchone()

        except Exception as e:
            print(e)
        finally:
            commit()
        
        return Response(*r) if r else self , (True if r else False)


    def insert(self) -> HTTPresponse:
        _, exists = self.verify()

        if exists:
            return {"message": f"this login `{self.login}` already exists."}

        if is_strong_pass(self.passwd):
            self.encode()
            cur.execute(
                "INSERT INTO users(login, passwd) VALUES(%s, %s)",
                [self.login, self.passwd]
            )
            commit()
            return HTTPresponse(
                {"message": "your account created successful."}, True)
        
        return HTTPresponse({
            "message": f"Your password `{self.passwd}`is weak"}, False)
        
    
    def auth(self) -> HTTPresponse:
        data, exists = self.verify()
        self.encode()

        if exists and data.passwd == self.passwd:
            return HTTPresponse({"message": "Login successful"}, True)

        if exists and data.passwd != self.passwd:
            return HTTPresponse({"message": "incorrect password"}, False)
        
        return HTTPresponse({"message": f"your account `{data.login}` not found"}, None)
    

@dataclass
class DataUser:
    name: str
    address: str
    

@dataclass
class User(UserLogin, DataUser):
    pass

