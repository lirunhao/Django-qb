from redis import Redis

config = {
    'host': '10.36.174.43',
    'port': 6379,
    'db': 9,
    'decode_responses': True
}


rd_client = Redis(**config)

if __name__ == '__main__':
    rd_client.keys('*')