import json
from solution import urgent_open
assert urgent_open([]) == []
assert urgent_open([{"id":"x","status":"open","priority":4,"age_hours":0,"message":"hi"}]) == ["x"]
with open("examples.json") as stream:
    samples=json.load(stream)
assert urgent_open(samples) == ["real"]
print("public_smoke: 3 assertions passed")
