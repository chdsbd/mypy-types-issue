import redis

r = redis.Redis()


r.pipeline().get("hell").execute()
