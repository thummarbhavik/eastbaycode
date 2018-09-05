import redis

con_redis = redis.Redis(host="127.0.0.1", port=6379, db=0)

# method to push the code into queue
def push_msg(qname, msg):
    conn = con_redis
    conn.rpush(qname, msg)
    print("push to " + qname + " : \n" + msg)

# get the result from redis queue
def get_result(qname):
    conn = con_redis
    result = (conn.lpop(qname)).decode('utf-8')
    if result != None:
        return result
