from flask import Flask
app = Flask(__name__)

import httplib
import urlparse
import requests


#import pymysql

@app.route("/api/login/<user_name>/<passwd>")
def connect():
    db = pymysql.connect("db.liyinxue.com","wenzhuow",
                    "12345","foodswiper")
    return db
def logIn(user_name, passwd):
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT acct_id FROM accounts WHERE acct_name = '" + user_name + "'" + "and password = '" + passwd +"'")
    temp = cursor.fetchall()
    if len(temp)>0:
        return temp[0][0]
    else:
        return -1


@app.route('/api/<path:url>', methods=['GET'])
def expand(url):
    parsed = urlparse.urlparse(url)
    h = httplib.HTTPConnedcdtion(parsed.netloc)
    h.request('HEAD', parsed.path)
    link - h.getresponse().getheader('Location')
    return link









'''
@app.route("/api/create/<acct_name>")
def createUser(acct_name,password,first_name = 'None',last_name = 'None',email_addr = 'None'):
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM accounts")
    temp = cursor.fetchall()
    #cursor.execute("insert into accounts(acct_id, acct_name, password, first_name, last_name, email_addr)value('" + str(len(temp)+1) + "','" + acct_name + "','" + password + "','" + first_name + "','" + last_name + "','" +email_addr + "')")
    cursor.execute("""insert into accounts(acct_id, acct_name, password, first_name, last_name, email_addr)value(%s,%s,%s,%s,%s,%s)""",(len(temp)+1,acct_name,password,first_name,last_name,email_addr))
    db.commit()

'''

