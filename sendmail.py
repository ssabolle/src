import MySQLdb
import smtplib
from email.MIMEText import MIMEText

db = MySQLdb.connect(db='newdb', user='ori', passwd='2wsx3edc' )

cursor = db.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("select emp_no, emp_name, email from emplmst")

HOSTNAME = 'localhost'
fromAddr = 'ssabolle@gmail.com'

for row in cursor:
    rec      = cursor.fetchone()
    toAddr   = rec['email']
    contents = "mail test - OK"
    
    msg = MIMEText(contents, _charset='utf-8')
    msg['Subject'] = 'test python mail'
    msg['From']    = fromAddr
    msg['To']      = toAddr
    
    s = smtplib.SMTP(HOSTNAME)
    s.sendmail(fromAddr, [toAddr], msg.as_string())
    s.quit()

print "success"

