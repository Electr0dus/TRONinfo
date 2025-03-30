from tronpy import Tron
from tronpy.providers import HTTPProvider
from dotenv import load_dotenv
import os

load_dotenv()

example_address = 'TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK'
API_KEY = os.getenv("API_KEY")
client = Tron(HTTPProvider(api_key=API_KEY))




def get_info_TRX(address: str):
    try:
        # Узнаём баланс
        balance = client.get_account_balance(address)
        # Получаем данные о ресурсах (bandwidth, energy)
        account_resources = client.get_account_resource(address)
        bandwidth = account_resources.get("free_net_used", 0)
        energy_used = account_resources.get("energy_used", 0)
        energy_limit = account_resources.get("energy_limit", 0)
        return {'Balance': str(balance), 'Bandwidth': bandwidth, 'Energy': f'{energy_used} / {energy_limit}'}
    except Exception as e:
        return {'Error': e}

