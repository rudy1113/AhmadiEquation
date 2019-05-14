import cgi

form = cgi.Fieldstorage()

hdl = form.getvalue('hdl')
tc = form.getvalue('tc')
tg = form.getvalue('tg')

print ("<html>")
print ("<body>")
print ("Your HDL is {}.".format(hdl))
print ("<\body>")
print ("<\html>")
