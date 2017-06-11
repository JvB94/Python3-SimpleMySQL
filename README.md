# Python3-SimpleMySQL

Usage:

```
from classes import simpleMysql
connect_mysql = simpleMysql.SimpleMysql('localhost', 'root', '', 'cms')

id = 10

test = connect_mysql.query("SELECT * FROM users WHERE id = %s" % (id))
print(test)
```

For more information look in the Code. It's very simple :)
