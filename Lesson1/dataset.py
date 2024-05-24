# ray start --head --dashboard-port=8265

import ray


items = [{"name": str(i), "data": i} for i in range(10000)] 
ds = ray.data.from_items(items)
ds.show(5)