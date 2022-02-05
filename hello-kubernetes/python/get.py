import os
import requests
import time

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
dapr_url = "http://localhost:{}/v1.0/invoke/nodeapp/method/order".format(dapr_port)

while True:
    try:
        response = requests.get(dapr_url, timeout=5)
        print("HTTP %d => %s" % (response.status_code,
                                     response.content.decode("utf-8")), flush=True)
    except Exception as e:
        print(e, flush=True)

    time.sleep(1)