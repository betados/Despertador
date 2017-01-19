#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb

# Create instance of FieldStorage 
form = cgi.FieldStorage()

# Get data from fields
hora = form.getvalue('hora')
minutos  = form.getvalue('minutos')


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>DESPERTADOR</title>"
print "</head>"
print "<body>"
print "<h2>Alarma establecida a las  %s : %s</h2>" % (hora, minutos)
print "</body>"
print "</html>"
