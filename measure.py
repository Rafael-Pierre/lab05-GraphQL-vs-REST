# measure_rest.py
import requests, time, json
URL = "http://localhost:4000/api/rest/test"
results = []
for _ in range(100):
start = time.time()
r = requests.get(URL)
elapsed = time.time() - start
results.append({"time": elapsed, "size": len(r.content)})
with open("rest_results.json", "w") as f:
json.dump(results, f, indent=2)

