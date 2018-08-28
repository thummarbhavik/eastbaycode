from eastbaycode import config
import MySQLdb

# Config MySQL
def connection():
    conn = MySQLdb.connect(host=config.dbhost,
                           user=config.dbuser,
                           passwd=config.dbpw)
    # save data output to dictionary
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return cur, conn

def getProblems(id):
    problem = {}
    cur, conn = connection()
    query1 = '''SELECT title, content from eastbaycode.problems where id={}'''.format(id)
    query2 = '''SELECT input, output from eastbaycode.examples where problem_id={}'''.format(id)
    cur.execute(query1)
    question = cur.fetchone()
    problem['title'] = question['title']
    problem['question'] = question['content']
    cur.execute(query2)
    examples = cur.fetchall()
    problem['example'] = examples
    conn.close()
    return problem
