import redis

con_redis = redis.Redis(host="eastbaycode_redis_1", port=6379, db=0)

# method to push the code into queue
def push_msg(qname, msg):
    conn = con_redis
    conn.rpush(qname, msg)

# get the result from redis queue
def get_result(qname):
    conn = con_redis
    result = conn.lpop(qname)
    if result != None:
        result = result.decode('utf-8')
        return result
