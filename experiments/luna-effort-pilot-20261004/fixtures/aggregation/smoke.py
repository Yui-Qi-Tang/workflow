from solution import aggregate
assert aggregate([]) == []
assert aggregate([{"sku":"A", "delta":2}]) == [{"sku":"A", "delta":2}]
print("public_smoke: 2 assertions passed")
