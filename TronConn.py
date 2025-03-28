from tronpy import Tron



client = Tron(conf={'timeout': 20.0})

print(client.get_block())