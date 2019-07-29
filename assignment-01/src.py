from flask import Flask
import redis

app = Flask(__name__)

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def number_refresh():
    r = redis.Redis(host='redis', port=6379, db=0)
    r.set('number_of_refresh_hits', n)
    return r.get('number_of_refresh_hits')

@app.route('/')
def print_msg():
    user = 'User'
    r = redis.Redis(host='redis', port=6379, db=0)
    if r.exists("num_hits"):
        num_hits = int(r.get('num_hits'))
        r.set('num_hits', num_hits + 1)
    else:
        r.set('num_hits', 1)
    num_hits = int(r.get('num_hits'))
    str =  'Hello, {}. The {}th fibonacci number is {}'.format(user, num_hits, fibonacci(num_hits))
    return str
