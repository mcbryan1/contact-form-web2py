from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL("sqlite://storage.sqlite")
db.define_table("users",
                Field('db_name'),
                Field('db_email'),
                Field('db_phone'),
                Field('db_message'))