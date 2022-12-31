from xmlrpc import client


conn = client.ServerProxy("http://www.pythonchallenge.com/phonebook.php")
print(conn.system.listMethods())

conn.system.methodHelp("phone")

conn.system.methodSignature("phone")

# "Bert" name from previous levels
conn.phone("Bert")