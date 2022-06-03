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
        return render.index()

class Webpy:
    def GET(self):
        return render.webpy()

class Javascript:
    def GET(self):
        return render.javascript()

if __name__ == "__main__":
    app.run()
