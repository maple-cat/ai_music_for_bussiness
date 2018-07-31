#--**coding:utf-8**--

import os,json,requests
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import options, define
from SVM_Classifier import lyric,sentence
import jsonify
define("port", default=8000, type=int)


class IndexHandler(RequestHandler):
    def get(self):
        # 获取get方式传递的参数
        # items = ["安静", "思念", "伤感",'运动','古风','浪漫']
        items = {'One':['quiet',"安静"],'Two':['miss',"思念"] ,'Three': ['sad',"伤感"],'Four':['sport','运动'],'Five':['antiquity','古风'],'Six':['romance','浪漫']}
        self.render("t.html", title="My title", items=items, query_result='')

    def post(self):
        song_detail = self.get_argument('song_detail')

        self.render('t.html', query_result=song_detail)

class SectionOneHandler(RequestHandler):
    def get(self):
        # 获取get方式传递的参数
        # items = ["安静", "思念", "伤感",'运动','古风','浪漫']
        items = {'One':['quiet',"安静"],'Two':['miss',"思念"] ,'Three': ['sad',"伤感"],'Four':['sport','运动'],'Five':['antiquity','古风'],'Six':['romance','浪漫']}
        self.render("SectionOne.html", title="My title", items=items, query_result='')

    def post(self):
        song_detail = self.get_argument('lyrics')
        lyric_rec = lyric(song_detail)




        # return json.dumps()
        self.finish({'result':[lyric_rec]})

class SectionTwoHandler(RequestHandler):
    def get(self):
        # 获取get方式传递的参数
        # items = ["安静", "思念", "伤感",'运动','古风','浪漫']
        items = {'One':['music',"音乐类"],'Two':['non_music',"非音乐类"] }
        self.render("SectionTwo.html", title="My title", items=items, query_result='')

    def post(self):
        song_detail = self.get_argument('query')
        sentence_rec,output = sentence(song_detail)


        print(sentence_rec,output)
        # return json.dumps()
        self.finish({'result':[[sentence_rec,output]]})

class SectionThreeHandler(RequestHandler):
    def get(self):


        self.render("SectionThree.html",results = [],song_detail = '')

    def post(self):
        song_detail = self.get_argument('query')

        url = 'http://10.139.74.226:8080/submit'

        a = requests.post(url, params={'wish': song_detail}).text
        results = json.loads(a)
        self.render('SectionThree.html',results = results,song_detail = song_detail)





class MusicType(RequestHandler):



    def post(self, *args, **kwargs):
        song_detail = self.get_argument('song_detail')

        print(song_detail)


if __name__ == "__main__":
    settings = {

        'template_path': os.path.join(os.path.dirname(__file__), "template"),
        'static_path': os.path.join(os.path.dirname(__file__), "static"),
        # 'static_url_prefix': '/sss/',
        # 'cookie_secret': "asdasd",
        # 'xsrf_cokkies': True,

        'debug': True

    }

    app = Application([(r"/", IndexHandler),
                       (r"/section1", SectionOneHandler),
                       (r"/section2", SectionTwoHandler),
                       (r"/section3", SectionThreeHandler),
                       (r'/musictype',MusicType)

                       ], **settings

                      )

    http_server=HTTPServer(app)
    http_server.listen(8000)

    IOLoop.instance().start()

