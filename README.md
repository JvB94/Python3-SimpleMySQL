# Python3-SimpleMySQL

Usage:


from classes import simpleMysql
connect_mysql = simpleMysql.SimpleMysql('localhost', 'root', '', 'cms')

test = connect_mysql.query("SELECT * FROM users WHERE id = %s" % (specSearch[0]["assetId"]))
print(test)


For more information look in the Code. It's very simple :)