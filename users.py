from random import randint

BASE64ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def random_password():
    s = ""
    for i in range(8):
        s += BASE64ALPH[randint(0, 63)]
    return s

def random_uid(uids):
    r = randint(0, 255)
    while r in uids:
        r = randint(0, 255)
    return r


def check_user(users, u, p=""):
    unames = list(map(lambda x: x["username"], users))
    passwords = list(map(lambda x: x["passwd"], users))
    if p != "":
        if u in unames and p in passwords:
            return True
    else:
        if u not in unames:
            return True
    return False
