# measure_graphql.py
import requests, time, json
URL = "http://localhost:4000/graphql"
query = {"query": "{ users { id name email } }"}
results = []
for _ in range(100):
start = time.time()
r = requests.post(URL, json=query)
elapsed = time.time() - start
results.append({"time": elapsed, "size": len(r.content)})
with open("graphql_results.json", "w") as f:
json.dump(results, f, indent=2)
