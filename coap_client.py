import time
from coapthon.client.helperclient import HelperClient

host = "192.168.29.128"
port = 5683
path = "basic"

def put():
    client = HelperClient(server=(host, port))
    response = client.put(path,"Hello world!")
    print(response.pretty_print())
    time.sleep(5)
    client.stop()

def get():
    client = HelperClient(server=(host, port))
    response = client.get(path)
    print(response.pretty_print())
    time.sleep(5)
    client.stop()

def post():
    client = HelperClient(server=(host, port))
    response = client.post(path,"POST MSG")
    print(response.pretty_print())
    time.sleep(5)
    client.stop()

def delete():
    client = HelperClient(server=(host, port))
    response = client.delete(path)
    print(response.pretty_print())
    time.sleep(5)
    client.stop()

if __name__ == '__main__':
    post()
