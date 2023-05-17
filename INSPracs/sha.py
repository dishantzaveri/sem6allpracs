from hashlib import sha256

message = b'HellO'

print(sha256(message).hexdigest())