from manage import DatabaseSetup

setup = DatabaseSetup()
conn = setup.connect
cur = setup.cursor