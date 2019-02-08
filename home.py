import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<p>Nothing to see here, I'm just an Index. </p>"
                   "Send some data to the following endpoint for loan "
                   "evaluation: <br />"
                   "<i>POST /loan</i>")


class LoanHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("All we need is loan <3")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/loan", LoanHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
