import hashlib

string = "pythonpool.com"
encoded = string.encode()
result = hashlib.sha256(encoded)

print(result.hexdigest())
