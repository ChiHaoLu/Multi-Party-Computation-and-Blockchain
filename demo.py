from secretshare import Secret, SecretShare
from eth_account import Account

# Construct the account object
account = Account.create('0x8676e9a8c86c8921e922e61e0bb6e9e9689aad4c99082620610b00140e5f21b8')
privateKey = int(account.key.hex(), 16)
print("Private Key: ", privateKey)
secret = Secret(privateKey)

# Construct the transaction object
dynamic_fee_transaction = {
        "type": 2,  # optional - can be implicitly determined based on max fee params  # noqa: E501
        "gas": 100000,
        "maxFeePerGas": 2000000000,
        "maxPriorityFeePerGas": 2000000000,
        "data": "0x616263646566",
        "nonce": 34,
        "to": "0x09616C3d61b3331fc4109a9E41a8BDB7d9776609",
        "value": "0x5af3107a4000",
        "accessList": (  # optional
            {
                "address": "0x0000000000000000000000000000000000000001",
                "storageKeys": (
                    "0x0100000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
                )
            },
        ),
        "chainId": 1900,
    }

print("\nUse the original key to sign the transaction:")
signed = Account.sign_transaction(dynamic_fee_transaction, account.key.hex())
transaction_hash = signed.hash.hex()
print("Transaction Hash: ", transaction_hash)
print("Signature: ")
print("    - v:", signed.v)
print("    - r:", signed.r)
print("    - s:", signed.s)

# Share the secret(private key)
share_count = 3
threshold = 2
shamir = SecretShare(threshold, share_count, secret=secret)
shares = shamir.split()
shareA = shares[0]
shareB = shares[1]
shareC = shares[2]
print("\nShare A (Stored in Mobile or any Hardware Signer): ", shareA)
print("Share B (Stored in the Computer): ", shareB)
print("Share C (Kept by wallet software supplier): ", shareC)

print("\nUser sign the transaction with Share A & Share B")
shamirAB = SecretShare(threshold, share_count, shares=[shareA, shareB])
secretAB = shamirAB.combine()
# print("Recover Private Key: ", int(secretAB))
signedAB = Account.sign_transaction(dynamic_fee_transaction, int(secretAB))
transaction_hash_AB = signedAB.hash.hex()
print("Transaction Hash: ", transaction_hash_AB)
print("Signature: ")
print("    - v:", signedAB.v)
print("    - r:", signedAB.r)
print("    - s:", signedAB.s)

print("\nIf users lost/forget their share A...")
print("User sign the transaction with Share B & Share C")
shamirBC = SecretShare(threshold, share_count, shares=[shareB, shareC])
secretBC = shamirBC.combine()
# print("Recover Private Key: ", int(secretBC))
signedBC = Account.sign_transaction(dynamic_fee_transaction, int(secretBC))
transaction_hash_BC = signedBC.hash.hex()
print("Transaction Hash: ", transaction_hash_BC)
print("Signature: ")
print("    - v:", signedBC.v)
print("    - r:", signedBC.r)
print("    - s:", signedBC.s)
