# Multi-Party Computation and Blockchain

- [Documentation](https://hackmd.io/@ChiHaoLu/C2-report-2023)
- [Repository](https://github.com/ChiHaoLu/Multi-Party-Computation-and-Blockchain)

## Usage
```sh
$ pip install secretshare eth_account
$ python demo.py
> 
Private Key:  92219659477489278322886626613986939005780640791210988442364524380600182286952

Use the original key to sign the transaction:
Transaction Hash:  0x9373d01bd79321a844fa7c6085df4ad43fb34947edb11f028df1384a5a3d3692
Signature: 
    - v: 0
    - r: 6493961586402747623124943311170637382090348104894738095928884747462402704591
    - s: 25419744352572691878069492034925470780423267168734478109196436220800867250879

Share A (Stored in Mobile or any Hardware Signer):  AQDcLlMa3SHaccADabJx0CbnFZcYM11ZOuQUMfz+vWP+xw==
Share B (Stored in the Computer):  AgDseiv0Pt2Hun8CRtTTvQbyf2Q1IoHNb4EVIIFtA19TJg==
Share C (Kept by wallet software supplier):  AwD8xgTNoJk1Az4BI/c1qeb96TFSEaZBpB4WDwXbSVqnhQ==

User sign the transaction with Share A & Share B
Transaction Hash:  0x9373d01bd79321a844fa7c6085df4ad43fb34947edb11f028df1384a5a3d3692
Signature: 
    - v: 0
    - r: 6493961586402747623124943311170637382090348104894738095928884747462402704591
    - s: 25419744352572691878069492034925470780423267168734478109196436220800867250879

If users lost/forget their share A...
User sign the transaction with Share B & Share C
Transaction Hash:  0x9373d01bd79321a844fa7c6085df4ad43fb34947edb11f028df1384a5a3d3692
Signature: 
    - v: 0
    - r: 6493961586402747623124943311170637382090348104894738095928884747462402704591
    - s: 25419744352572691878069492034925470780423267168734478109196436220800867250879
```