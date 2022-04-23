from web3 import Web3

def connect_smart_contract():
    url = "HTTP://127.0.0.1:8545"
    web3 = Web3(Web3.HTTPProvider(url))
    print(web3.isConnected())

    web3.eth.defaultAccount = web3.eth.accounts[0]

    address="0x7104aa15Ee07Ad97d8011c1019e4c162446B1494"
    abis =[
        {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
        },
        {
        "inputs": [
            {
            "internalType": "string",
            "name": "",
            "type": "string"
            }
        ],
        "name": "certificados",
        "outputs": [
            {
            "internalType": "string",
            "name": "alumno",
            "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
        },
        {
        "inputs": [],
        "name": "cod",
        "outputs": [
            {
            "internalType": "string",
            "name": "",
            "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
        },
        {
        "inputs": [],
        "name": "cursoName",
        "outputs": [
            {
            "internalType": "string",
            "name": "",
            "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
        },
        {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
            "internalType": "address",
            "name": "",
            "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
        },
        {
        "inputs": [
            {
            "internalType": "string",
            "name": "hash_pdf",
            "type": "string"
            },
            {
            "internalType": "string",
            "name": "alumno_",
            "type": "string"
            }
        ],
        "name": "cargarDiploma",
        "outputs": [
            {
            "internalType": "bool",
            "name": "",
            "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
        },
        {
        "inputs": [
            {
            "internalType": "string",
            "name": "hash_pdf",
            "type": "string"
            }
        ],
        "name": "revisaDiploma",
        "outputs": [
            {
            "internalType": "string",
            "name": "",
            "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
        }
    ]

    return web3.eth.contract(address=address, abi = abis)

def cargar_hash_diploma(hash, user_name):
    Diploma = connect_smart_contract()

    return Diploma.functions.cargarDiploma(hash, user_name).call()

def consulta_diploma(hash):
    Diploma = connect_smart_contract()
    return Diploma.functions.revisaDiploma(hash).call()