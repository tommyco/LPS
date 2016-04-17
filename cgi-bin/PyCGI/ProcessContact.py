#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgi, cgitb, sys, SendMsg
cgitb.enable()

# Send errors to browser
sys.stderr = sys.stdout

# Parse data from form
form = cgi.FieldStorage()

name = ''
if 'name' in form:
   name = form['name'].value.strip()

email = ''
if 'email' in form:
   email = form['email'].value.strip()

phone = ''
if 'phone' in form:
   phone = form['phone'].value.strip()

msg = ''
if 'msg' in form:
   msg = form['msg'].value.strip()

subject = 'A message from %s' % name

if name != '' and email != '' and msg != '':
   SendMsg.SendMsg(subject, name, email, phone, msg)
   # redirect to main page
# DEV
   print "Location: http://www.mylocal.com/LPS/index.html","\r\n"
# LIVE
#   print "Location: http://drlinden.net/index.html","\r\n"

   print "Connection: close \r\n"
   print ""
else:
   # Send reponse to browser
   print "Content-type: text/html"
   print 
   print "<html><body>"
   print '<h2>ERROR: Missing Name, Email or Message. Cannot send message.</h2>'   
   print '<br/>'
# DEV
   print 'Please return to <a href="http://www.mylocal.com/LPS/index.html#contact">Contact</a><br/>'
# LIVE
#   print 'Please return to <a href="http://drlinden.net/index.html#contact">Contact</a><br/>'

   print "</body></html>"







