from .enumStore.colors import Colors
from .enumStore.size import Size
from .enumStore.icons import Icons
from .enumStore.chassis import ChassisBox
from .enumStore.phrases import Phrases
from .enumStore.typography import Typographys

from .models import SaleProduct
from django.shortcuts import get_object_or_404

import os
import requests
import uuid
import json
import time

class ProductServiceTable:
    BASE_URL = "http://52.72.137.244:3000"
    def AssembleForTable(self, product):
        product_color = Colors[product.color]
        product_icon = Icons[product.icon]
        product_size = Size[product.size]
        chassis = ChassisBox[product.name]
        phrase_typography = Typographys[product.typography]
        phrase = Phrases[product.phrase]

        body_to_send = {
            "payload": {
                "orderId": f"INKLUA-{uuid.uuid4()}",
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

        response = ProductServiceTable.SendToTable(body=body_to_send)
        if response.status_code == 201:
            data = response.json()
            self.OccupyPosition(data['id'], chassis.value)
            return data['id']

            # url = f"{self.BASE_URL}/queue/items/{data['id']}"
            # headers = {
            #     "Content-Type": "application/json"
            # }

            # try:
            #     response = requests.get(url=url, headers=headers, timeout=10)
            #     response.raise_for_status()

            #     product_queue = response.json()
            #     print("=======================PRODUCT QUEUE===========================")
            #     print(product_queue['history'])

    

            #     return response
            # except requests.RequestException as e:
            #     print(f"Error: {e}")
            #     return None
        # base_dir = os.path.dirname(__file__)
        # mock_path = os.path.join(base_dir, "mock.json")

        # with open(mock_path, "r", encoding='utf-8') as c:
        #     data = json.load(c)
        #     print("=============DATA============")  
        #     data["payload"]["orderId"] = body_to_send["payload"]["orderId"]
        #     data["payload"]["order"]["bloco1"]["cor"] = body_to_send["payload"]["order"]["bloco1"]["cor"]
        #     data["payload"]["order"]["bloco1"]["lamina1"] = body_to_send["payload"]["order"]["bloco1"]["lamina1"]
        #     data["payload"]["order"]["bloco1"]["lamina2"] = body_to_send["payload"]["order"]["bloco1"]["lamina2"]
        #     data["payload"]["order"]["bloco1"]["lamina3"] = body_to_send["payload"]["order"]["bloco1"]["lamina3"]
        #     data["payload"]["order"]["bloco1"]["padrao1"] = body_to_send["payload"]["order"]["bloco1"]["padrao1"]
        #     data["payload"]["order"]["bloco1"]["padrao2"] = body_to_send["payload"]["order"]["bloco1"]["padrao2"]
        #     data["payload"]["order"]["bloco1"]["padrao3"] = body_to_send["payload"]["order"]["bloco1"]["padrao3"]
        #     print(data)
        #     obj = {
        #         "queue_order_id": data["payload"]["orderId"],
        #         "sale_date": data['createdAt'],
        #         "status": data['status'],
        #         "status_start_date": data['createdAt'],
        #         "status_finished_date": data['createdAt'],
        #         "client": product.client,
        #         "product": product
        #     }
        # return obj


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
        
    def GetQueueProduct(self, product_id, client_id, flag=False):
        url = f"{self.BASE_URL}/queue/items/{product_id}"
        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url=url, headers=headers, timeout=10)
            response.raise_for_status()

            product_queue = response.json()
            history = product_queue['history'][-1] if len(product_queue['history']) > 0 else 0
            obj = {
                "queue_order_id": product_id,
                "sale_date": product_queue['createdAt'],
                "status": product_queue['status'],
                "status_start_date": product_queue['createdAt'],
                "status_finished_date": product_queue['createdAt'],
                "client": client_id
            }

            if flag:
                SaleProduct.objects.filter(queue_order_id=product_id).update(
                    status=product_queue['status'],
                    )

                return product_id


            return obj
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None
        
    def OccupyPosition(self, order_id, color):
        print("color")
        print(color)
        pos = 3
        url = f"{self.BASE_URL}/estoque/{pos}"
        headers = {
            "Content-Type": "application/json"
        }

        status_map = {
            1: "preto",
            3: "azul"
        }

        status_str = status_map.get(color, "azul")

        body = {
            "cor": status_str,
            "op": order_id
        }

        print("=======ORDER ID==========")
        print(order_id)

        saleAt = SaleProduct.objects.filter(queue_order_id=order_id).update(position_table=pos)
        print("===========oer===========")
        print(order_id)
        prod_queue = get_object_or_404(SaleProduct, queue_order_id=str(order_id))
        print(f"SALE AT: {prod_queue}")
        response = requests.put(url=url, json=body, headers=headers, timeout=10)
        response.raise_for_status()

        return response
    
    def ReleasePosition(self, pos):
        url = f"{self.BASE_URL}/estoque/{pos}"
        headers = {
            "Content-Type": "application/json"
        } 

        response = requests.delete(url=url, headers=headers, timeout=10)
        response.raise_for_status()

        return response
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
