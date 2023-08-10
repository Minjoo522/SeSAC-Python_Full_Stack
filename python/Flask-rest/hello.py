from flask import Flask
# 문서 자동으로 생성
from flask_restx import Api, Resource

app = Flask(__name__)
# 문서 생성 틀
# http://127.0.0.1:8008/으로 들어가면 API 생성됨
api = Api(app)

# 헤더를 root가 아니라 다른 걸로 만든 이유
# api를 통해서 app과 연결
@api.route('/hello')
class HelloWorld(Resource):
  # 내 아래의 함수는 모두 api 함수임
  def get(self):
      return "<h1>Hello, world!</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=8008)

# 백엔드 : 일반적으로 json 기반의 데이터를 출력