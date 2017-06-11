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

    def __init__(self, host='localhost', user='root', password=None, db=None):

        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db

    def __open(self):
        try:
            con = MySQLdb.connect(self.__host, self.__user, self.__password, self.__db)
            self.__connection = con
            self.__session = con.cursor()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def __close(self):
        self.__session.close()
        self.__connection.close()

    def query(self, query, commit=True):
        mode = query.split(" ")[0].upper()

        if (mode == "SELECT"):
            self.__open()
            self.__session.execute(query)
            number_rows = self.__session.rowcount
            number_columns = len(self.__session.description)

            if number_rows >= 1 and number_columns > 1:
                result = [item for item in self.__session.fetchall()]
            else:
                result = [item[0] for item in self.__session.fetchall()]
            self.__close()

            return result

        elif mode == "DELETE":
            self.__open()
            self.__session.execute(query)
            if commit == True:
                self.__connection.commit()

            delete_rows = self.__session.rowcount
            self.__close()

            return delete_rows

        elif mode == "INSERT":
            self.__open()
            self.__session.execute(query)
            if commit == True:
                self.__connection.commit()

            self.__close()

            return self.__session.lastrowid

        elif mode == "UPDATE":
            self.__open()
            self.__session.execute(query)
            if commit == True:
                self.__connection.commit()

            update_rows = self.__session.rowcount
            self.__close()
            return update_rows