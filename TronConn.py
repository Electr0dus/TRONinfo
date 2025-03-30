from tronpy import Tron
from tronpy.providers import HTTPProvider



example_address = 'TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK'
API_KEY = 'fe0752f6-b01c-4ec1-9443-ee3ee1506db8'

client = Tron(HTTPProvider(api_key=API_KEY))



def get_info_tron(address: str):
    try:
    # Узнаём баланс
        balance = client.get_account_balance(address)
        # Получаем данные о ресурсах (bandwidth, energy)
        account_resources = client.get_account_resource(address)
        bandwidth = account_resources.get("free_net_used", 0)
        energy_used = account_resources.get("energy_used", 0)
        energy_limit = account_resources.get("energy_limit", 0)
        
        print(f"Balance {balance}")
        print(f"Bandwidth used: {bandwidth}")
        print(f"Energy used: {energy_used} / {energy_limit}")
        return {'Balance': balance, 'Bandwidth used': bandwidth, 'Energy used': f'{energy_used} / {energy_limit}'}
    except Exception as e:
        print("Error:", e)
        return {'Error': e}
        
