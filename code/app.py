import web

urls = (
    '/','Index',
    '/webpy','Webpy',
    '/javascript','Javascript'
)
app = web.application(urls,globals())
render = web.template.render('templates/',base='layout')

class Index:
    def GET(self):
        return render.Index()

class Webpy:
    def GET(self):
        return render.Webpy()

class Javascript:
    def GET(self):
        return render.Javascript()
