url = "http://gatewayip/0/up"
my_username = "put_username_here"
my_password = "put_your_password_here"

from twill.commands import go, showforms, formclear, fv, submit

go(url)
#showforms()

formclear('1')
fv('1', 'username', my_username)
fv('1', 'password', my_password)
#showforms()

submit('0')