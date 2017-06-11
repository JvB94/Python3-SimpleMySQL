import MySQLdb

############################################################
################## Simple MySQL ############################
############################################################

class SimpleMysql:
    # Set Connection Details
    __host = None
    __user = None
    __password = None
    __db = None

    # Temp Objects for Connection
    __instance = None
    __connection = None

    # Def Charset
    __charset = None

    def __init__(self, host='localhost', user='root', password=None, db=None, charset='utf8'):

        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db

        self.__charset = charset

    def __open(self):
        try:
            con = MySQLdb.connect(self.__host, self.__user, self.__password, self.__db)

            self.__connection = con
            self.__connection.set_character_set(self.__charset)

            self.__session = con.cursor()

            self.__session.execute("SET NAMES '{}';".format(self.__charset))
            self.__session.execute("SET CHARACTER SET '{}';".format(self.__charset))
            self.__session.execute("SET character_set_connection='{}';".format(self.__charset))

        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def __close(self):
        self.__session.close()
        self.__connection.close()

    def query(self, query, commit=True, values=None):
        mode = query.split(" ")[0].upper()

        self.__open()

        if values == None:
            self.__session.execute(query)
        else:
            self.__session.execute(query, values)

        if (mode == "SELECT"):
            number_rows = self.__session.rowcount
            number_columns = len(self.__session.description)

            if number_rows >= 1 and number_columns > 1:
                result = [item for item in self.__session.fetchall()]
            else:
                result = [item[0] for item in self.__session.fetchall()]

            return result

        elif mode == "DELETE":
            if commit == True:
                self.__connection.commit()

            delete_rows = self.__session.rowcount

            return delete_rows

        elif mode == "INSERT":
            if commit == True:
                self.__connection.commit()

            return self.__session.lastrowid

        elif mode == "UPDATE":
            if commit == True:
                self.__connection.commit()

            update_rows = self.__session.rowcount

            return update_rows

        self.__close()