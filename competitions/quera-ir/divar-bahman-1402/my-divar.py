#!/usr/bin/env python3

import string
from datetime import datetime

from dataclasses import dataclass, field

class DivarException(Exception):
    pass

class UsernameError(DivarException):
    def __init__(self, msg: str = 'invalid username', *args):
        super().__init__(msg, *args)

class TitleError(DivarException):
    def __init__(self, msg: str = 'invalid title', *args):
        super().__init__(msg, *args)

class AdPermissionError(DivarException):
    def __init__(self, msg: str = 'access denied', *args):
        super().__init__(msg, *args)

class DuplicateFavoriteAd(DivarException):
    def __init__(self, msg: str = 'already favorite', *args):
        super().__init__(msg, *args)

class NonExistingFavorite(DivarException):
    def __init__(self, msg: str = 'already not favorite', *args):
        super().__init__(msg, *args)

users: dict = dict()
ads: dict = dict()

@dataclass
class Ad:
    title: str
    tag: str = None
    user: "User" = None
    datetime: datetime = field(default_factory=datetime.now)
    is_favorite: bool = False
    favorite_datetime: datetime = None

    def __hash__(self) -> int:
        return int(''.join(map(lambda x: str(ord(x)), self.title)))

@dataclass
class User:
    username: str
    ads: set["Ad"] = field(default_factory=set)
    favorites: set["Ad"] = field(default_factory=set)

class Platform:
    valid_chars = set(string.digits) | set(string.ascii_letters) | {'_'}

    @classmethod
    def isvalid_str(cls, estring: str) -> bool:
        if not isinstance(estring, str):
            return False
        if len(estring) == 0:
            return False        
        if set(estring) - cls.valid_chars:
            return False
        return True

    @classmethod
    def isvalid_tag(cls, tag: str) -> bool:
        if tag is None:
            return False
        if not cls.isvalid_str(tag):
            return False
        return True

    @classmethod
    def register(cls, username: str) -> str:
        if username in users:
            raise UsernameError()
        user = User(username=username)
        users[username] = user
        return 'registered successfully'
    
    @classmethod
    def add_advertise(cls, username: str, title: str, tag: str = None) -> str:
        if username not in users:
            raise UsernameError()
        if title in ads:
            raise TitleError()
        ad = Ad(title=title, user=users[username])
        if cls.isvalid_tag(tag):
            ad.tag = tag
        ads[title] = ad
        ad.user.ads.add(ad)
        return 'posted successfully'

    @classmethod
    def rem_advertise(cls, username: str, title: str) -> str:
        if username not in users:
            raise UsernameError()
        if title not in ads or not cls.isvalid_str(title):
            raise TitleError()
        ad = ads[title]
        if ad.user.username != username:
            raise PermissionError()
        del ads[title]
        if ad in ad.user.ads:
            ad.user.ads.remove(ad)
        del ad
        return 'removed successfully'

    @classmethod
    def list_my_advertises(cls, username: str, tag: str = None) -> str:
        if username not in users:
            raise UsernameError()
        user = users[username]
        valid_tag = cls.isvalid_tag(tag)
        return ' '.join([
            f'{ad.title}' for ad in sorted(list(user.ads), key=lambda x: x.datetime)
            if (ad.tag == tag if valid_tag else True)
        ])

    @classmethod
    def add_favorite(cls, username: str, title: str) -> str:
        if username not in users:
            raise UsernameError()
        if title not in ads or not cls.isvalid_str(title):
            raise TitleError()
        ad = ads[title]
        if ad.user.username != username:
            raise PermissionError()
        user = ad.user
        if ad not in user.favorites:
            raise DuplicateFavoriteAd()
        user.favorites.add(ad)
        ad.is_favorite = True
        ad.favorite_datetime = datetime.now()
        return 'added successfully'
    
    @classmethod
    def rem_favorite(cls, username: str, title: str) -> str:
        if username not in users:
            raise UsernameError()
        if title not in ads:
            raise TitleError()
        ad = ads[title]
        if ad.user.username != username:
            raise PermissionError()
        user = ad.user
        if ad not in user.favorites:
            raise NonExistingFavorite()
        user.favorites.remove(ad)
        ad.is_favorite = False
        ad.favorite_datetime = None
        return 'removed successfully'
    
    @classmethod
    def list_favorite_advertises(cls, username: str, tag: str = None) -> str:
        if username not in users:
            raise UsernameError()
        user = users[username]
        valid_tag = cls.isvalid_tag(tag)
        return ' '.join([
            f'{ad.title}' for ad in sorted(list(user.favorites), key=lambda x: x.favorite_datetime)
            if (ad.tag == tag if valid_tag else True)
        ])

def test():
    tests = [
        ['register user1',
         'register user2',
         'add_advertise user1 car',
         'add_advertise user2 laptop',
         'add_advertise user2 laptop',
         'list_my_advertises user1',
         'list_my_advertises user2',
         'rem_advertise user2 phone',
         'list_my_advertises user2'],
        ["register user1",
		 "register user2",
		 "add_advertise user1 car",
		 "add_advertise user2 laptop",
		 "add_favorite user1 laptop",
		 "add_favorite user1 phone",
		 "add_favorite user2 laptop",
		 "rem_favorite user1 phone",
		 "list_favorite_advertises user1",
		 "list_favorite_advertises user2"],
         ["register user1",
		 "register user2",
		 "add_advertise user1 car automotive",
		 "add_advertise user2 laptop electronics",
		 "add_advertise user2 phone electronics",
		 "add_advertise user1 laptop electronics",
		 "list_my_advertises user1 electronics",
		 "list_favorite_advertises user1",
		 "list_my_advertises user1"]
]
    for t in tests:
        for i in t:
            i = i.split(' ')
            func = i.pop(0)
            try:
                value = getattr(Platform, func)(*i)
                print(value)
            except DivarException as exc:
                print(exc.args[0])

def get_input():
    q = int(input().strip())
    commands = list()
    for _ in range(q):
        commands.append(input().strip())

    return commands

if __name__ == '__main__':
    # test()
    pass

for i in get_input():
    i = i.split(' ')
    func = i.pop(0)
    try:
        value = getattr(Platform, func)(*i)
        print(value)
    except DivarException as exc:
        print(exc.args[0])