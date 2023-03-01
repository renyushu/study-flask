import redis

redis_conn = redis.Redis(host='127.0.0.1', port=6379, db=0)

redis_conn.set('name_2', 'Zarten_2')
v = redis_conn.get('name_2')

print(v)