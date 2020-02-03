import os
from github3 import authorize
from getpass import getuser, getpass

user = os.environ['GITHUB_USER']
password = os.environ['GITHUB_PASSWORD']

# password = ''
# while not password:
#     # The user could accidentally press Enter before being ready,
#     # let's protect them from doing that.
#     password = prompt('Github password: ')

while not password:
    password = getpass('Password for {0}: '.format(user))

try:
    # Python 2
    prompt = raw_input
except NameError:
    # Python 3
    prompt = input

def my_two_factor_function():
    code = ''
    while not code:
        # The user could accidentally press Enter before being ready,
        # let's protect them from doing that.
        code = prompt('Enter 2FA code: ')
    return code

# g = github3.login('sigmavirus24', 'my_password',
#                   two_factor_callback=my_two_factor_function)

note = 'github3.py example app'
note_url = 'http://example.com'
scopes = ['user', 'repo']

auth = authorize(user, password, scopes, note, note_url, two_factor_callback=my_two_factor_function)

with open('ghcreds', 'w') as fd:
    fd.write(auth.token + '\n')
    fd.write(auth.id)
