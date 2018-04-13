"""
Life is short, I use Python!!
"""

account = 'greentea'
password = 123456

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if account == user_account and password == user_password:
    print('success')
else:
    print('error')
