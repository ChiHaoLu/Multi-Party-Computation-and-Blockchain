# C2-report-2023
> - **Title:** Multi-Party Computation and Blockchain
> - **Team Code:** C2
> - **Project Type:** Implementation
> - **Presentation date:** 06/01/2023
> - **Teammate:** 
>   - [B08303113 ECON Senior 陸紀豪](https://chihaolu.me)
>   - B08303116 ECON Senior 游景恩
> - **Link Tree**
>   - [Repository](https://github.com/ChiHaoLu/Multi-Party-Computation-and-Blockchain)
>   - [Live Demo](https://colab.research.google.com/drive/19cTcPrbXMXNiOM10nfsrL5IxJZX-WLXV?usp=sharing)
>   - [Slides]()

### Timeline & Requirements
1. ✅ Proposal to cllei@ntu.edu.tw by 04/13
1. ⚠️ Presentation in class in 06/01
2. ⚠️ Make an appointment with professor on 06/09, and demonstrate how your system works.
3. ⚠️ Turn in your final report, a revised powerpoint file of your presentation and executable program(s) to cllei@ntu.edu.tw by 06/12. Your term report should include:
    * (required) Description of the prototype system:
        * Introduction
        * specification and functionalities of the system
        * purpose and applications of the system
        * solutions or techniques adopted in the system
        * scenarios of the system
        * comparisons with existing approaches
        * conclusions
        * executable programs (better packaged with VM)
    * (required) References.


---

## 1. Introduction

### 1.1 Background

In our daily lives, we heavily rely on Public-key cryptography for various applications such as digital certificates, identity authentication, and digital signatures. Whether it's HTTPS, SMTPS, or blockchain technology, Public-key cryptography is an essential part of our lives.

A user can encrypt plaintext with their private key, and anyone can decrypt the ciphertext with the user's public key. By confirming that the private key is exclusively held by the user, it can be established that the file originated from that user. The publicly available public key allows anyone to verify the integrity and authenticity of data or files published by the user. As a result, the recipient can trust that the data or files indeed come from the user.

### 1.2 Blockchain & Signature Algorithms

In the context of Blockchain, it's important to highlight signature algorithms commonly used, such as ECDSA, EDDSA, and ECDH. For this discussion, we'll primarily focus on ECDSA.

ECDSA finds a significant use case in the secp256k1 protocol used by Ethereum. Users sign transaction objects with their private keys, which are then submitted for verification and inclusion in a block by the nodes.

Node verification relies on the "ecrecover" function to verify the signature. If the recovered result matches the expected value, it confirms that the transaction was signed by the private key owner. In simpler terms, possessing the private key on the blockchain indicates ownership of all assets associated with the corresponding address.

### 1.3 Potential Problems

In cryptography and digital ownership, a "signer" is the individual who possesses the private key used for signing transactions or data. On the other hand, the "owner" refers to the person who holds the account or assets associated with that private key.

In traditional off-chain systems like bank accounts, if a user loses their password, alternative methods such as identification or contacting the bank can be used to establish ownership. However, in the on-chain world of blockchain, there is typically no central authority for verifying ownership.

In blockchain networks, transactions and data are cryptographically signed with private keys, and the validity of these signatures confirms ownership and ensures transaction integrity.

Losing a private key in the on-chain world presents challenges in proving ownership. Unlike traditional systems, there is no central authority to reset or recover the password. Ownership solely relies on possessing the private key. This highlights the critical importance of securely managing and safeguarding private keys in blockchain systems.

Thus, ensuring the security of private keys in blockchain systems (and applications utilizing public key algorithms) becomes crucial. It involves secure storage, addressing theft or loss scenarios, and handling forgotten keys. Unlike the traditional off-chain world with a "forgot password" option, such mechanisms are not easily achievable in the blockchain realm.

As a result, discussions around blockchain account design primarily revolve around decoupling the signer from the owner or avoiding the private key becoming a single point of failure. The main objective is to establish the correct identity of the account owner. Even if a private key is stolen, measures can be taken to deactivate it. In cases of forgotten keys, recovery options can be explored.

### 1.4 Possible Solution

Our target solution is using Multi-Signature. The primary objective of a multi-sig wallet is to enhance security and minimize the vulnerability associated with a single private key by requiring multiple independent private keys to sign a transaction.

There are two primary methods for implementing a multi-sig wallet: Contract-Level and Key-Level. 

Contract-Level implementation involves the use of multi-sig wallet contracts, leveraging the programmability of smart contracts to enforce multi-signature authorization. A MultiSignature Wallet Contract allows multiple parties to jointly manage and control the funds stored in the wallet. Unlike a regular wallet where one private key is sufficient to access the funds, a multi-signature wallet requires multiple signatures from authorized parties to approve transactions. This adds an extra layer of security and prevents any single individual from having sole control over the funds. It is commonly used in situations where shared ownership and consensus are required, such as cryptocurrency exchanges or collaborative financial arrangements.

On the other hand, Key-Level implementation, known as MPC (Multi-Party Computation) Wallet, involves dividing a private key into multiple parts and distributing them among different parties to ensure secure storage. By employing multi-sig wallets, users can significantly enhance the security of their transactions and assets, reducing the risk of a single point of failure.

Besides, we will also comapre the social recovery wallet in the end. A social recovery wallet is a type of cryptocurrency wallet that incorporates a social element for account recovery. In addition to the traditional recovery methods like seed phrases or private key backups, a social recovery wallet allows users to designate a group of trusted individuals (e.g. your relatives) who can collectively help recover access to the wallet in case of loss or forgotten credentials. This approach leverages the network of trusted contacts to provide an additional layer of security and redundancy, reducing the risk of permanent loss of funds.

---

## 2. Multi-Party Computation

### 2.1 Introduction

Multi-Party Computation (MPC) is a cryptography field that enables two or more parties to compute a function output together without disclosing their inputs. This concept has been in existence for 30 years and has found applications in various domains, including cryptocurrency wallets.

MPC provides the ability to create a secure key management system without relying on a single private key. In an MPC-based system, multiple parties can collaboratively perform cryptographic functions like key generation, transaction signatures, and transaction verification without revealing their confidential information. This approach offers several advantages, including easy recovery, protection against phishing attacks, and user control over the entire system.

### 2.2 Use Shamir Secret Sharing as a Solution

In this project, we will use the Shamir Secret Sharing (SSS) as MPC implementation, consumer-focused wallets and institutional services can develop more secure on-chain asset management systems. These systems help mitigate the risks associated with private key theft and loss.

Shamir Secret Sharing (SSS) is an incredibly popular implementation of a secret sharing scheme developed by Adi Shamir, a renowned Israeli cryptographer who also played a significant role in the creation of the AES algorithm. SSS enables the division of a secret into an arbitrary number of shares, with a customizable threshold (as long as it is lower than the total number of participants). The underlying principle of SSS is based on polynomial interpolation, which states that a polynomial of degree t-1 can be reconstructed if the knowledge of t or more points lying on the curve is available.

To illustrate, consider the reconstruction of a degree 1 curve (a straight line). At least 2 points lying on the line are required for successful reconstruction. Conversely, it is mathematically impossible to reconstruct a curve when the number of unique points available is less than the degree of the curve plus 1. This can be visualized by imagining the infinite number of possible straight lines that can be formed from just one point in a two-dimensional space.

By employing Shamir Secret Sharing, sensitive information, which will be the private key in out project, can be securely distributed among multiple participants while maintaining the confidentiality of the original secret.



---

## 3. Implementation

### 3.1 Glossary

The glossary and background of our project are:
1. The signature algorithm in this project chooses secp256k1(ECDSA).
1. The $WalletOwner$ will create a key-pair of secp256k1, which can be used to sign the transaction, and the asset will be stored in the corresponded address(`address := "0x" + SHA3(pubKey).split(0:40)`).
1. $Device_A$ owns the $Share_A$ of the key. We assume $Share_A$ is just stored by writing on a Paper. The $Share_A$ will be directly record without any encryption.
1. $Device_B$ owns the $Share_B$ of the key. We assume $Share_B$ is stored in the Computer of $WalletOwner$. The $Share_B$ will be encrypted by a $password$ set by user in AES.
1. $TrustedThirdParty$ owns the $KEK$ of the $Share_C$ of the key. We assume $TrustedThirdParty$ is the wallet software supplier which is choosen and trusted by the $WalletOwner$.
2. $KEK$ means users can use their iCloud/Google Drive as a recovery method. The process works as follows: $TrustedThirdParty$ generates a random number called the key-encryption-key (KEK) and uses it to encrypt the secret. The encrypted secret is then stored in the cloud storage, while the $KEK$ is sent to the database of $TrustedThirdParty$ for safekeeping.


### 3.2 Goals & Scenarios

Our goals to acheive this project are:

Scenario 1: If $WalletOwner$ want to send a signed message or signed transaction.
1. He/She need to choose two out of the following three options: $Share_A$, $Share_B$ and $Share_C$. In our assumption, user will use the $Share_A$ and $Share_B$ to sign transaction.
1. Calculating the signature by the choosen shares.
1. Verifying the signature is valid.

Scenario 2: When $WalletOwner$ lost one of shares, $Share_A$ or $Share_B$:
1. He/She can request the $KEK$ of the $Share_C$ which belongs to $TrustedThirdParty$.
1. He/She can decrypt the encrypted $Share_C$ stored in their Cloud with $KEK$.
1. Then he/she can use the not-lost one share and $Share_C$ to access the Asset.
1. Finally, he/she can create a new wallet and transfer the asset to this new wallet.

### 3.3 Trust Assumption
1. $TrustedThirdParty$ can not access the $WalletOwner$, because it only stores the $KEK$ of $Share_C$, and the calculation is done by $WalletOwner$ (in his/her local device).
1. Without the $KEK$ provided by $TrustedThirdParty$, individuals with access to the cloud storage cannot decrypt your secret. 
1. When anyone requests the $KEK$ from $TrustedThirdParty$, they need to pass two-factor authentication (such as SMS or email verification) in order to receive the $KEK$. 
1. From another perspective, $TrustedThirdParty$ (or anyone who hacks into $TrustedThirdParty$'s database) cannot obtain your secret because they do not have the authorization to access your cloud storage.

### 3.4 SSS Algorithm 

The polynomial P(x) represents coefficients in the form of a₁ * x^p + a₂ * x^(p-1) + … + aₙ * x^(p-p). Constructing a polynomial involves selecting these coefficients as placeholders to store their values.

Using p+1 points on the curve, we can represent the entire curve based on polynomial interpolation principles. For example, a degree 4 curve can be reconstructed with a minimum of 5 unique points. Lagrange's interpolation or similar methods are utilized for this purpose.

By concealing a secret value within a polynomial and using different curve points as shares, a secret sharing scheme is achieved. In a (t, n) secret sharing scheme, a polynomial of degree t-1 is constructed, and n points on the curve are selected as shares. The polynomial can only be reconstructed when t or more shares are combined. The secret value (s) is hidden in the polynomial's constant term, which can only be revealed through successful curve reconstruction.

Shamir's Secret Sharing employs polynomial interpolation for threshold sharing in two phases: Share Generation and Secret Reconstruction.

During Share Generation, the system is set up, and shares are generated. The number of participants (n) and the threshold (t) are determined, specifying the minimum participants required for secret reconstruction. A random polynomial P(x) of degree t-1 is created, with randomly chosen coefficients and the secret value (s) as the constant term. n points on the polynomial are selected as shares and distributed among participants.

In the Secret Reconstruction phase, a minimum of t shares is pooled to reconstruct the secret. Participants with the required shares come together, using an interpolation algorithm like Lagrange's Interpolation to reconstruct the original polynomial P'(x). The value of the polynomial at x = 0, P'(0), reveals the constant term, which corresponds to the original secret (s). Thus, the secret is successfully reconstructed.

Shamir's Secret Sharing provides a secure method to distribute secrets among multiple participants, ensuring that the secret remains hidden unless a sufficient number of shares are combined. It finds applications in various fields where secure sharing and reconstruction of sensitive information are vital.

### 3.5 Demo Program

We will use the python to implement the demo program, and import the library `secretshare` to achive the SSS and `eth_account` for secp256k1 signing which is used in Ethereum Protocol.

```python
from secretshare import Secret, SecretShare
from eth_account import Account
```

First, we random generate the private key of secp256k1 key pair, which will be used to sign transaction. 
```python
# Construct the account object
account = Account.create('0x8676e9a')
privateKey = int(account.key.hex(), 16)
print("Private Key: ", privateKey)
secret = Secret(privateKey)
>
Private Key: 136400....176519
```

We construct the transaction object which will send `0x5af3107a4000` amount of ETH to address `0x09616C3d61b3331fc4109a9E41a8BDB7d9776609`.

```python
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
```

Sign the transaction with the original private key, and get the signature.

```python
print("\nUse the original key to sign the transaction:")
signed = Account.sign_transaction(dynamic_fee_transaction, account.key.hex())
transaction_hash = signed.hash.hex()
print("Transaction Hash: ", transaction_hash)
print("Signature: ")
print("    - v:", signed.v)
print("    - r:", signed.r)
print("    - s:", signed.s)
>
Use the original key to sign the transaction:
Transaction Hash:  0x03d7...bfd2
Signature: 
    - v: 1
    - r: 115534...916390
    - s: 226513...619208
```

Generate the shares from the original private key, with the `share_count=3` and `threshold=2`.

```python
# Share the secret(private key)
share_count = 3
threshold = 2
shamir = SecretShare(threshold, share_count, secret=secret)
shares = shamir.split()
shareA = shares[0]
shareB = shares[1]
shareC = shares[2]
```

We store the $Share_A$ just by writing on a Paper without any encryption. And we use a $password$ to encrypt $Share_B$ to store it in the computer. Then we collaborate with the $TrustedThirdParty$ by storing the $Share_C$ with $KEK$.
```python
print("\nShare A (Stored by writing on the Paper): ", shareA)

print("\nShare B (Stored in the Computer): ", shareB)
print('\t- Please enter your password, which is used to encrypt your share B:')
password = input()
encrypted_share_b = Account.encrypt(shareB.value, password)
pointB = shareB.point
print("\t- Encrypted with the Password by AES:")
printDict(encrypted_share_b)

print("\nShare C (Kept by wallet software supplier): ", shareC)
print("\t- Encrypted with the KEK by AES")
kek = random.randint(0,17898947891374192)
encrypted_share_c = Account.encrypt(shareC.value, kek)
pointC = shareC.point
print("\t- The KEK=", kek, "will be stored in the Wallet Supplier Server")
print("\t- The encrypted_share_c=", encrypted_share_c, "will be stored in the User's iCloud/GoogleDrive")
>
Share A (Stored by writing on the Paper):  AQCNPOD+s+PW677h7Nr1uPol0CtcjtNAfFRqsioBtCvyMw==

Share B (Stored in the Computer):  AgAXdcInXTAADP6+5YyiLlX4Z8VFfA8lnUqIZV5mGMbx9g==
	- Please enter your password, which is used to encrypt your share B: 1234
	- Encrypted with the Password by AES:
{
    "address": "a2a152b998200b5dba78b8f2aa80f2f321a6d753",
    "crypto": {
        "cipher": "aes-128-ctr",
        "cipherparams": {
            "iv": "f063028896f0eb5353c79fd9b69967f4"
        },
        "ciphertext": "6185e8b407d807b5f0e013d383fdc11887691032b51bda57f48273eb4fc4ab96",
        "kdf": "scrypt",
        "kdfparams": {
            "dklen": 32,
            "n": 262144,
            "r": 1,
            "p": 8,
            "salt": "edefa3a1f4bd632c454536dabb0a2bdf"
        },
        "mac": "4cdba2a01199d7174207432a513e5ceeacdf734bad07501ccece9448dd73c726"
    },
    "id": "69edff0b-454e-4abb-8f3f-22d299cd29e3",
    "version": 3
}

Share C (Kept by wallet software supplier):  AwChrqNQBnwpLj6b3j5Oo7HK/18uaUsKvkCmGJLKfWHy4g==
	- Encrypted with the KEK by AES
	- The KEK= 3030923849674283 will be stored in the Wallet Supplier Server
```

In our first scenario, the user will hold the $Share_A$ and $Share_B$, which can sign the transaction and control the asset belongs to the original key pair.

```python
print("\nUser sign the transaction with Share A & Share B")

# Decrypt Share B
print("\t- Please enter your password to decrypt the Share B: ")
password = input()
hex_decrypted_share_b = int((Account.decrypt(encrypted_share_b, password).hex()), base=16)
decrypted_share_b = Share(point=pointB, value=hex_decrypted_share_b)

# Use decrypted Share A & decrypted Share B to sign the transaction
shamirAB = SecretShare(threshold, share_count, shares=[shareA, decrypted_share_b])
secretAB = shamirAB.combine()
signedAB = Account.sign_transaction(dynamic_fee_transaction, int(secretAB))
transaction_hash_AB = signedAB.hash.hex()
print("Transaction Hash: ", transaction_hash_AB)
print("Signature: ")
print("\t- v:", signedAB.v)
print("\t- r:", signedAB.r)
print("\t- s:", signedAB.s)
>
User sign the transaction with Share A & Share B
	- Please enter your password to decrypt the Share B: 1234
Transaction Hash:  0x03d7...bfd2
Signature: 
    - v: 1
    - r: 115534...916390
    - s: 226513...619208
```
In our second scenario, the $KEK$ of the $Share_C$ will be kept by the wallet software supplier or any trusted third party. If the users lost/forget one of the $Share_A$ or $Share_B$, they can request the $KEK$ with any mechanism (e.g. Biometric authentication, 2FA, 3FA...) and use it to decrypt the $Share_C$ in cloud.

Then, he/she can recover his/her account by re-control the asset with signing transaction with 2 Share.
```python
print("\nIf users lost/forget their share A...")

# Decrypt Share B
print("\t- Please enter your password to decrypt the Share B: ")
password = input()
hex_decrypted_share_b = int((Account.decrypt(encrypted_share_b, password).hex()), base=16)
decrypted_share_b = Share(point=pointB, value=hex_decrypted_share_b)

# Decrypt Share C
print("\t- Get the kek from cloud to decrypt the Share C: ")
hex_decrypted_share_c = int((Account.decrypt(encrypted_share_c, kek).hex()), base=16)
decrypted_share_c = Share(point=pointC, value=hex_decrypted_share_c)

# Use decrypted Share B & decrypted Share C to sign the transaction
print("User sign the transaction with Share B & Share C")
shamirBC = SecretShare(threshold, share_count, shares=[decrypted_share_b, decrypted_share_c])
secretBC = shamirBC.combine()
# print("Recover Private Key: ", int(secretBC))
signedBC = Account.sign_transaction(dynamic_fee_transaction, int(secretBC))
transaction_hash_BC = signedBC.hash.hex()
print("Transaction Hash: ", transaction_hash_BC)
print("Signature: ")
print("\t- v:", signedBC.v)
print("\t- r:", signedBC.r)
print("\t- s:", signedBC.s)
>
If users lost/forget their share A...
	- Please enter your password to decrypt the Share B: 1234
	- Get the kek from cloud to decrypt the Share C: 
User sign the transaction with Share B & Share C
Transaction Hash:  0x03d7...bfd2
Signature: 
    - v: 1
    - r: 115534...916390
    - s: 226513...619208
```

To re-acheive the account safety, the user can produce new shares by split the private key(`secretBC`).

```python
new_shamir = SecretShare(threshold, share_count, secret=secretBC)
new_shares = new_shamir.split()
new_shareA = new_shares[0]
new_shareB = new_shares[1]
new_shareC = new_shares[2]
```

---

## 4. Conclusion

### 4.1 Comparison

The table below provides definitions for the terms used:

1. "Lost": It refers to the scenario where the account owner forgets the private key.
1. "Stolen": It indicates that the private key has been unlawfully taken by someone else.
1. "Recover": This term signifies the ability to modify the signer of the account. In the case of a contract wallet, the signer is typically represented by a variable. If we mention that the wallet can be recovered, it means that this variable can be safely changed.

| | Social Recovery Wallet | MultiSig Contract Wallet |  MPC Wallet |
| :--------: | :--------: | :--------: | :--------: |
| **Level** | Contract Level | Contract Level | **Key Level** |
| **Cost(Gas Fee)** | High | Highest | **Lowest** |
| **If Key Lost**| Can Recover | Can Recover | **Can Recover** |
| **If One Key Stolen** | Asset will be transferd |  Asset is safe | **Asset is safe** |
| **User Experience**| Low|Low|**High** |


The table compares three solutions: Social Recovery Contract Wallet, MultiSig Contract Wallet, and MPC Wallet.
* The Social Recovery Contract Wallet operates at the contract level. It allows for key recovery if lost, but it incurs a high gas fee.
* The MultiSig Contract Wallet also operates at the contract level. It enables key recovery if lost and ensures asset safety if one signing key is stolen. However, it incurs the highest gas fee.
* The MPC Wallet operates at the key level. It has the lowest gas fee, allows for key recovery if lost, and ensures asset safety if one share is stolen. Moreover, it provides a high user experience with seamless operation similar to a native account (EOA) on the blockchain.

### 4.2 Summary

In our implementation and comparison, the MPC Wallet offers the lowest cost because it does not require navigating through various functions in a smart contract to execute operations when sending a transaction. Instead, it functions similarly to an externally owned account (EOA), allowing for direct transaction sending.

Furthermore, the MPC Wallet provides the highest User Experience (UX) due to its streamlined operation. Unlike other contract wallets that may have additional features implemented in their smart contracts, which necessitate users' understanding and consensus from other signers to execute certain actions correctly, the MPC Wallet operates akin to a native account (EOA) on the blockchain. By addressing the private key issue at the key level and performing operations through the wallet provider's interface, the MPC Wallet delivers a seamless user experience without added complexity.

Besides, the MPC Wallet does not require additional trust assumptions. In contrast, both the MultiSig Contract Wallet and the Social Recovery Contract Wallet carry the risk of collusion among other signers or guardians, which could result in the theft of your account assets. However, by entrusting the $KEK$ of $Share_C$ to a centralized entity (the wallet provider's server), the level of decentralization is slightly reduced. Nevertheless, this aspect poses no risk to the assets themselves, but rather introduces regulatory oversight risks.

---

## 5. References

1. Brunner, Clemens & Eibl, Günther & Fröhlich, Peter & Sackl, Andreas & Engel, Dominik. (2021). Who Stores the Private Key? An Exploratory Study about User Preferences of Key Management for Blockchain-based Applications. 23-32. 10.5220/0010173200230032.
2. Lindell, Yehuda. (2017). Fast Secure Two-Party ECDSA Signing. 613-644.10.1007/978-3-319-63715-0_21.
3. Gennaro, Rosario & Goldfeder, Steven. (2018). Fast Multiparty Threshold ECDSA with Fast Trustless Setup. 1179-1194.10.1145/3243734.3243859.
3. Castagnos, Guilhem & Catalano, Dario & Laguillaumie, Fabien & Savasta,Federico & Tucker, Ida. (2019). Two-Party ECDSA from Hash Proof Systems and Efficient Instantiations. 10.1007/978-3-030-26954-8_7.
4. Gennaro, Rosario and Steven Goldfeder. “One Round Threshold ECDSA with Identifiable Abort.” IACR Cryptol. ePrint Arch. 2020 (2020): 540.
