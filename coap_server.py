from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

Host = "0.0.0.0"  # 本机IP地址
Port = 5683  # 端口号


class BasicResource(Resource):
    def __init__(self, name="BasicResource", coap_server=None):
        super(BasicResource, self).__init__(name,
                                            coap_server,
                                            visible=True,
                                            observable=True,
                                            allow_children=True)
        self.payload = "Basic Resource"

    def render_GET(self, request):
        res = BasicResource()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_POST(self, request):
        res = BasicResource()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('basic', BasicResource())


def main():
    print("CoAPServer IP addr : %s port : %d " % (Host, Port))
    server = CoAPServer(Host, Port)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")
    except UnicodeDecodeError:
        return main()


if __name__ == '__main__':
    main()