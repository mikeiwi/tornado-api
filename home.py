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
        requested_amount = float(self.get_argument('requested_amount'))

        if requested_amount < 50000:
            self.write({'message': 'Approved'})
        elif requested_amount > 50000:
            self.write({'message': 'Declined'})
        else:
            self.write({'message': 'Undecided'})


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/loan", LoanHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
