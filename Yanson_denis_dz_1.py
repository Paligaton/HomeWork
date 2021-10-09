import re


def email_parse(email):
    RE_EMAIL = re.compile(r'^(\w+@\w+[.][a-zA-Z]+)')
    email_plus = {}
    if email in RE_EMAIL.findall(email):
        email_plus['username'], email_plus['domain'] = re.compile(r'(\w+){1}@(\w+.[a-z]+){1}').findall(email)[0][0], \
                                              re.compile(r'(\w+){1}@(\w+.[a-z]+){1}').findall(email)[0][1]
        return email_plus

    else:
        return "wrong email: email: " + email


print(email_parse(input('Впишите электронную почту: \n')))