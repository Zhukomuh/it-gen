import re


def email_validate(email: str):
    """validate email with regular pattern"""
    email_pattern = r'[a-zA-Z0-9]*(-?\.?[_a-zA-Z0-9])*@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*'
    if re.match(email_pattern, email):
        return email
    return 'Email is not validate'


emails = ['johnsmith@example.com',
          'yourname@yourcompany.com',
          'info@webdomain.com',
          'firstname.lastname@provider.com',
          'firstinitial.lastname@domain.tld',
          'username@hostname.net',
          'customername@isp.net',
          'me@myisp.com',
          'customer.support@company.com',
          'admin@mydomain.org']

with open('test.txt', 'a') as f:
    for text in emails:
        f.writelines(email_validate(text) + '\n')
