import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'hellocmsstorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'FTLAj/gsNIF6rHQagiwZOVVIZm8Df4CZMQOCsNpVYLCNKr+Gd+kocAd7GfGXw8u+au2MtKydZY3E+AStaAd5aA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or 'DefaultEndpointsProtocol=https;AccountName=hellocmsstorage;AccountKey=FTLAj/gsNIF6rHQagiwZOVVIZm8Df4CZMQOCsNpVYLCNKr+Gd+kocAd7GfGXw8u+au2MtKydZY3E+AStaAd5aA==;EndpointSuffix=core.windows.net'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello-cms-dbserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'hello-cms-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '123@Well'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect={}".format(
        quote_plus(
            "Driver={ODBC Driver 17 for SQL Server};" + "Server={};Database={};UID={};PWD={};".format(SQL_SERVER,
                                                                                                      SQL_DATABASE,
                                                                                                      SQL_USER_NAME,
                                                                                                      SQL_PASSWORD)
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET") or '5f372b5c-edda-42b9-aa35-bc2167448325'
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name

    CLIENT_ID = os.environ.get("CLIENT_ID") or '00fa1f63-9312-4dc7-b50a-e7093fad439b'

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
