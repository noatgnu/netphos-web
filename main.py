import asyncio
import os
import sys
import tornado.httpserver
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.options import define, options

from netphos.handlers import NetphosHandler, MainHandler

define("port", default=8000, help="Port number")

settings = {
    # "static_path": os.path.join(os.path.dirname(__file__), "static"),
    #"x-header": True
    # "cookie_secret": "IVM/jkpE+1A4We2P/hVxkHe8EW8mW3TR574hEpCnuGrU3H5trJCSckecA9e2zYthBbI=",
    # "xsrf_cookies": True,
    "xheaders": True
}

if __name__ == "__main__":
    tornado.options.parse_command_line()
    rout = os.environ.get("HANDLERS_ROUTE",
                     r'(netphos|172\.25\.0\.4|web|curtain\.omics\.quest|curtain\.muttsu\.com|production_cactus|production_curtain|localhost|127\.0\.0\.1|62\.75\.251\.157|curtainptm\.proteo\.info|curtain\.proteo\.info|www\.conducto\.me|conducto\.me)')
    app = Application()
    app.add_handlers(
        rout,
        [
            (r"/", MainHandler),
            # (r"/uniprot", UniprotHandler),
            # (r"/file_data", FileHandler),
            # (r"/string/getid", StringDBGetIDHandler),
            # (r"/string/enrichment", StringDBGetIDHandler),
            # (r"/string/interaction", StringDBInteractionHandler),
            # (r"/proteomics/expression", ProteomicsDBExpressionHandler),
            # (r"/interactome/interact", InteractomeAtlasHandler),
            # (r"/netphos/predict", NetphosHandler),
            # (r"/api", MainHandler),
            # (r"/api/uniprot", UniprotHandler),
            # (r"/api/file_data", FileHandler),
            # (r"/api/string/getid", StringDBGetIDHandler),
            # (r"/api/string/enrichment", StringDBGetIDHandler),
            # (r"/api/string/interaction", StringDBInteractionHandler),
            # (r"/api/proteomics/expression", ProteomicsDBExpressionHandler),
            # (r"/api/interactome/interact", InteractomeAtlasHandler),
            (r"/api/netphos/predict", NetphosHandler)
            # (r"/static", StaticFileHandler, dict(path=settings['static_path']))
        ])
    server = tornado.httpserver.HTTPServer(app)
    server.bind(options.port)

    server.start(1)
    IOLoop.current().start()
