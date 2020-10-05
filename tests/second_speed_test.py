import time
import random
import tests.config as config


test_values = [
    "app_name",
    "credentials.username",
    "credentials.password",
    "db_connections.0.host",
    "db_connections.1.username"
]

start = time.time()

for i in range(1000):
    config.get_config(random.choice(test_values))

print(time.time() - start, 'seconds')
