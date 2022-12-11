from tornado.escape import json_decode
from tornado.web import RequestHandler
import netphos.api
import settings


class BaseHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("access-control-allow-origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET, PUT, DELETE, OPTIONS')
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type")

    def options(self):
        self.set_status(204)
        self.finish()

class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")

class NetphosHandler(BaseHandler):
    def post(self):
        req = json_decode(self.request.body)
        print(req)
        with open(settings.NETPHOS_TEMP+req["id"]+".fasta", "wt") as fastaFile:
            fastaFile.write(req["fasta"])
        data = netphos.api.run(settings.NETPHOS_APE, settings.NETPHOS_TEMP+req["id"]+".fasta")
        self.write({"data": data})