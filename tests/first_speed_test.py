import time
import tests.config as config


test_value = "db_connections.0.host"

start = time.time()

for i in range(1000):
    config.get_config(test_value)

print(time.time() - start, 'seconds')
