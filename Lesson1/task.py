import ray

@ray.remote
def square(x):
    return x * x

# Launch four parallel square tasks.
futures = [square.remote(i) for i in range(100)]

# Retrieve results.
print(ray.get(futures))