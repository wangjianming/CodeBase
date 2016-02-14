from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
 
         
class PackagesHandler(tornado.web.RequestHandler):
    def post(self):
        packageURI = self.get_argument("packageURI")
        self.write(packageURI)
        #TODO:  get package from url and store at local repository
        
class DeployHandler(tornado.web.RequestHandler):
    def post(self):
        response = { 'result': 0,  'url':"http://xxxx:8080"}
        self.write(response)

application = tornado.web.Application([
    (r"/rest/v1/change/packages", PackagesHandler),
    (r"/rest/v1/change/deployments", DeployHandler)
])
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()