import redis


class RedisSingleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(RedisSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.pool = redis.ConnectionPool(host='localhost', port=6379, db=0)  # remote connection, just set host='*.*.*.*'
        self.r = redis.StrictRedis(connection_pool=self.pool)


def get_redis():
    redis_global = RedisSingleton()
    return redis_global.r
