import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'virtual-zoo-sql-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'virtual-zoo-sql-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'virtual-zoo-sql-server-admin-login'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Thislittlemonkey23'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'virtualzoostorageaccount'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'q8o5WonI/F7qqZlaLt4LLGaYJDxQ34iT2/0F0f4qbjEE9vUgMQXNTMZ6e42rsZ5vK8/EXxcSwgMkN6t3z9tItQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'virtual-zoo-storage-container'
