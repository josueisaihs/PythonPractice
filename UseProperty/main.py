class User:
    def __init__(self, username: str = "") -> None:
        self._username = username

    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, value: str) -> None:
        if 4 >= len(value) >= 8:
            raise ValueError("The length of the username is incorrect, it must be between 4 and 8 characters")
        
        self._username = value
    
    @username.deleter
    def username(self) -> None:
        del self._username