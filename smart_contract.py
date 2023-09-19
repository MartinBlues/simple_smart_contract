from web3 import Web3, HTTPProvider

# Connect to local Ethereum node
w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

# Wallet and smart contract address
wallet_address = '0x4B043f73F26c067a0D234e8D189c3aF06E6113f4'
contract_address = '0x6D7fE7fC25d8b85767DdA77B8cAE1fBaA27B26a0'

# Smart contract ABI
abi = [
    {
        "constant": False,
        "inputs": [{"name": "x", "type": "uint256"}],
        "name": "multiply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Connect to a smart contract
contract = w3.eth.contract(address=contract_address, abi=abi)

# Call a smart contract function
result = contract.functions.multiply(7).call()

print("Result:", result)
