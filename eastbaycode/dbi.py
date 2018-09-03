from eastbaycode import config
import MySQLdb

# Config MySQL
def connection():
    conn = MySQLdb.connect(host=config.dbhost,
                           user=config.dbuser,
                           passwd=config.dbpw)

    # save data output to dictionaryself.
    # output type: cursorclass=MySQLdb.cursors.DictCursor
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return cur, conn

def getProblems(id):
    problem = {}
    cur, conn = connection()
    query1 = '''SELECT id, title, content from eastbaycode.problems where id={}'''.format(id)
    query2 = '''SELECT id, input, output from eastbaycode.examples where problem_id={}'''.format(id)
    cur.execute(query1)
    question = cur.fetchone()
    problem['id'] = question['id']
    problem['title'] = question['title']
    problem['question'] = question['content']
    cur.execute(query2)
    examples = cur.fetchall()
    problem['example'] = examples
    conn.close()
    return problem

def getTestCase(id):
    cur, conn = connection()
    query = '''SELECT input from eastbaycode.testcases where problem_id={}'''.format(id)
    cur.execute(query)
    input = [item['input'] for item in cur.fetchall()]
    conn.close()
    return input
