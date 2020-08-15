import web
render=web.template.render('mvc/views/alumnos/')

class Lista:
    def GET(self):
        try:
            return render.list(None,None,None,None,None,None,None,None)
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result