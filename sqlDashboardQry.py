from sqlalchemy import create_engine, textde
from sqlalchemy.orm import sessionmaker
import yaml
from yaml.loader import SafeLoader

def get_credentials(user):
    dbcredentials = yaml.load(open("db_credentials.yaml"), SafeLoader)
    if user in dbcredentials and 'db' in dbcredentials[user] and 'user' in dbcredentials[user] and 'password' in dbcredentials[user]:
        return dbcredentials[user]['db'], dbcredentials[user]['user'], dbcredentials[user]['password']
    return None, None, None
def get_dburl():
    dbcredentials = yaml.load(open("db_credentials.yaml"), SafeLoader)
    if "database_url" in dbcredentials: return dbcredentials["database_url"]
    return '127.0.0.1'
db, user, password = get_credentials('all')
host = get_dburl()
# Create an engine with connection pooling
connection = 'mysql+pymysql://{user}:{password}@{host}/{db}'.format(user=user, password=password, host=host, db=db)
# print(connection)
engine = create_engine( connection, pool_size=20, max_overflow=0, pool_timeout=30, pool_recycle=1800)
Session = sessionmaker(bind=engine)
# # Query function
# def get_count(database_name):
#     session = Session()
#     query = text(f"SELECT COUNT(*) FROM {database_name}.omds_digital_manuscript WHERE"
#                  f" IsDeleted=0")
#     result = session.execute(query).scalar()
#     session.close()
#     return result
def getDataQryResults(dbn):
    yamlFile = yaml.load(open("db_credentials.yaml"), SafeLoader)
    keys = {1:'Manuscripts', 2:'Books', 3:'Articles'}
    jsonKeys = yamlFile['jsonKeys']
    dictDocs = {jsonKeys[dbn]: {'Manuscripts': 0, 'Books': 0, 'Articles': 0, 'Users': 0}}
    dictUsers = {}
    qryDocs = '''
        SELECT :dbn AS dbname, DocumentType, COUNT(DocumentType) 
        FROM {dbn}.omds_digital_manuscript 
        WHERE isDeleted=0 
        GROUP BY DocumentType
        '''.format(dbn=dbn)
    qryUsers = 'SELECT :dbn as dbname, COUNT(*) FROM {dbn}.omds_employeemaster WHERE IsDeleted=0'.format(dbn=dbn)

    session = Session()
    try:
        result = session.execute(text(qryDocs), {'dbn': dbn})
        for row in result.fetchall():
            dictDocs[jsonKeys[row[0]]][keys[row[1]]] = row[2]
        result = session.execute(text(qryUsers), {'dbn': dbn})
        for row in result.fetchall():
            # print('%18s %4d'%(row[0], row[1]))
            dictUsers[row[0]] = row[1]
    finally:
        session.close()
    for k, v in dictUsers.items(): dictDocs[jsonKeys[k]]['Users'] = v
    return dictDocs
def getDataQryResultsAll():
    yamlFile = yaml.load(open("db_credentials.yaml"), SafeLoader)
    keys = {1:'Manuscripts', 2:'Books', 3:'Articles'}
    dictUsers = {}; dictDocs = {}
    jsonKeys = yamlFile['jsonKeys']; mdrDatabases = list(jsonKeys.keys())
    for dbn in mdrDatabases: dictDocs[jsonKeys[dbn]] = {'Manuscripts': 0, 'Books': 0, 'Articles': 0, 'Users': 0}
    dbn = mdrDatabases[0]
    qryDocs = '''
            SELECT :dbn AS dbname, DocumentType, COUNT(DocumentType) 
            FROM {dbn}.omds_digital_manuscript 
            WHERE isDeleted=0 
            GROUP BY DocumentType
            '''.format(dbn=dbn)
    qryUsers = 'SELECT :dbn as dbname, COUNT(*) FROM {dbn}.omds_employeemaster WHERE IsDeleted=0'.format(dbn=dbn)
    for dbn in mdrDatabases[1:]:
        txt = ' UNION SELECT :dbn as dbname, DocumentType, COUNT(DocumentType) FROM {dbn}.omds_digital_manuscript WHERE isDeleted=0 GROUP BY DocumentType'
        qryDocs += txt.format(dbn=dbn)
        txt = ' UNION SELECT "{dbn:s}", COUNT(*) FROM {dbn:s}.omds_employeemaster WHERE IsDeleted=0'
        qryUsers += txt.format(dbn=dbn)
        dictDocs[jsonKeys[dbn]] = {'Manuscripts': 0, 'Books': 0, 'Articles': 0, 'Users': 0}
    qryDocs += ';'; qryUsers += ';'
    session = Session()
    try:
        result = session.execute(text(qryDocs), {'dbn': dbn})
        for row in result.fetchall():
            dictDocs[jsonKeys[row[0]]][keys[row[1]]] = row[2]
        result = session.execute(text(qryUsers), {'dbn': dbn})
        for row in result.fetchall():
            dictUsers[row[0]] = row[1]
    finally:
        session.close()
    for k, v in dictUsers.items(): dictDocs[jsonKeys[k]]['Users'] = v
    return dictDocs

if __name__ == '__main__':
    # Example usage
    yamlFile = yaml.load(open("db_credentials.yaml"), SafeLoader)
    mdrDatabases = yamlFile['jsonKeys'].keys()
    print('all: %s\n%s' % (getDataQryResultsAll(), [getDataQryResults(dbn) for dbn in mdrDatabases]))
