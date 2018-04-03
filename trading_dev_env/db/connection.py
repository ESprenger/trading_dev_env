from datetime import datetime
from psycopg2 import connect, Warning, Error, OperationalError, DatabaseError

from general.utils import Singleton
from trading_dev_env.db.config import config_setup


class PostGreSql(metaclass=Singleton):
    __slots__ = ('_conn', '_query_object', 'kwargs')

    def __init__(self, **kwargs):
        self.kwargs = kwargs if kwargs else {}
        self.create_conn()

    def create_conn(self):
        try:
            self._conn = connect(**config_setup())
        except Warning as w:
            print("Psycopg2 Warning: {0}".format(w))
        except Error as e:
            print("Psycopg2 Error: {0}".format(e))
        else:
            print("Connection made at ".format(datetime.now()))
        finally:
            self._query_object()

    def clear_query_object(self):
        self._query_object = None

    def _execute(self, statement):
        with self._conn.cursor() as curs:
            self._query_object = curs.execute(statement)
        return self

    def insert(self, query):
        # TODO
        pass

    def query(self, query):
        # TODO
        self._execute(query)

    def fetchone(self):
        if self._query_object:
            return self._query_object.fetchone()
        else:
            raise DatabaseError

    def fetchmany(self, size=None):
        if self._query_object:
            return self._query_object.fetchmany(size=size)
        else:
            raise DatabaseError

    def fetchall(self, size=None):
        if self._query_object:
            return self._query_object.fetchall(size=size)
        else:
            raise DatabaseError

    def ping_db(self):
        try:
            self.query('SELECT 1')
            self.clear_query_object()
        except OperationalError as oe:
            # Attempt to reconnect
            print("OperationalError: {0}".format(oe))
            self.create_conn()

    def __del__(self):
        if self._conn is not None:
            self._conn.close()
