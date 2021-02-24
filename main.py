import redis

r = redis.Redis()


r.pipeline().get("hello").execute()
