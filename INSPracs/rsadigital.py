from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.exceptions import InvalidSignature
import base64

# Generate a key pair
def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Sign a message with the private key
def sign(message, private_key):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature)

# Verify a signature with the public key
def verify(message, signature, public_key):
    try:
        signature_bytes = base64.b64decode(signature)
        public_key.verify(
            signature_bytes,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

# Example usage
private_key, public_key = generate_key_pair()
message = b'This is a message to be signed'
signature = sign(message, private_key)

print(f'Message: {message}')
print(f'Signature: {signature}')

is_valid = verify(message, signature, public_key)
print(f'Is the signature valid? {is_valid}')