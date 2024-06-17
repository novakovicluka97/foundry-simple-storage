print(len("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"))
print(len("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"))

# import random
# import requests
# from eth_account import Account
# 
# def generate_random_private_key():
#     return ''.join([random.choice('0123456789abcdef') for _ in range(64)])
# 
# def get_eth_balance(address):
#     api_url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey=YourApiKeyToken"
#     response = requests.get(api_url)
#     data = response.json()
#     return int(data['result'])
# 
# while True:
#     private_key = generate_random_private_key()
#     account = Account.from_key(private_key)
#     address = account.address
#     balance = get_eth_balance(address)
#     if balance > 0:
#         print(f"Found address with balance! Address: {address}, Balance: {balance}, Private Key: {private_key}")
#         break