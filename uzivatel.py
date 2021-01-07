from pony.orm import db_session
import random
import string
from webface.models import User, Shortener
from werkzeug.security import generate_password_hash, check_password_hash

login = input('zadej jmeno > ')
heslo = input('zadej heslo > ')

with db_session:
    uzivatel = User.get(login=login)
    if not uzivatel:
        uzivatel = User(login=login, password=generate_password_hash(heslo))

    while True:
        adresa = input('zadej adresu >')
        if adresa == '':
            break
        shortcut = "".join([random.choice(string.ascii_letters) for i in range(7)]) 
        shortener = Shortener(shortcut=shortcut, url=adresa, user=uzivatel)
        
    for adresa in uzivatel.addresses:
        print(adresa.shortcut, adresa.url)

    adresy = tuple(uzivatel.addresses) 
    for adresa in adresy:
        print(adresa.shortcut, adresa.url)
