from abc import ABC, abstractmethod


class db_factory(object):
    def get_db_connection(self, db):
        return db.connection(self)


class data_base(ABC):
    @abstractmethod
    def connection(self):
        pass


class mysql_server:
    def connection(self):
        return ("mysql db connection")


class oracle_server:
    def connection(self):
        return ("oracle db connection")


factory = db_factory()
mysql_conn = factory.get_db_connection(mysql_server)
oracle_conn=factory.get_db_connection(oracle_server)
print(mysql_conn)
print(oracle_conn)