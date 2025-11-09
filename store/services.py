from .enumStore.colors import Colors
from .enumStore.size import Size
from .enumStore.icons import Icons
from .enumStore.chassis import ChassisBox
from .enumStore.phrases import Phrases
from .enumStore.typography import Typographys

import requests
import uuid

class ProductServiceTable:
    BASE_URL = "http://52.1.197.112:3000"
    def AssembleForTable(self, product):
        product_color = Colors[product.color]
        product_icon = Icons[product.icon]
        product_size = Size[product.size]
        chassis = ChassisBox[product.name]
        phrase_typography = Typographys[product.typography]
        phrase = Phrases[product.phrase]

        body_to_send = {
            "payload": {
                "orderId": "INKLUA",
                "order": {
                    "codigoProduto": 1,
                    "bloco1": {
                        "cor": chassis.value,
                        "lamina1": product_color.value,
                        "lamina2": product_icon.value["frontBlade"],
                        "lamina3": product_icon.value["rightBlade"],
                        "padrao1": phrase.value,
                        "padrao2": product_size.value,
                        "padrao3": phrase_typography.value
                    },
                    "bloco2": {
                        "lamina1": 0,
                        "lamina2": 0,
                        "lamina3": 0,
                        "padrao1": "0",
                        "padrao2": "0",
                        "padrao3": "0"
                    },
                    "bloco3": {
                        "lamina1": 0,
                        "lamina2": 0,
                        "lamina3": 0,
                        "padrao1": "0",
                        "padrao2": "0",
                        "padrao3": "0"
                    }
                },
                "sku": "KIT-01"
            },
            "callbackUrl": "http://localhost:3333/callback"
        }

        # ProductServiceTable.SendToTable(body=body_to_send)

        print("======================BODY======================")
        print(body_to_send)

        return 'AAAAAAAAAAAAAAAAAAAA'


    @staticmethod
    def SendToTable(body):
        url = f"{ProductServiceTable.BASE_URL}/queue/items"
        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url=url, json=body, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None




#         {
#   "codigoProduto": 1,
#   "bloco1": {
#     "cor": 1,
#     "lamina1": 1,
#     "lamina2": 1,
#     "lamina3": 1,
#     "padrao1": "1",
#     "padrao2": "1",
#     "padrao3": "1"
#   },
#   "bloco2": {
#     "cor": 1,
#     "lamina1": 1,
#     "lamina2": 1,
#     "lamina3": 1,
#     "padrao1": "1",
#     "padrao2": "1",
#     "padrao3": "1"
#   },
#   "bloco3": {
#     "cor": 1,
#     "lamina1": 1,
#     "lamina2": 1,
#     "lamina3": 1,
#     "padrao1": "1",
#     "padrao2": "1",
#     "padrao3": "1"
#   }
# }
