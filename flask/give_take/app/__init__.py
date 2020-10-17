# file name : __init__.py
# pwd : /project_name/app/__init__.py

from flask import Flask

app = Flask(__name__)

# 추가할 모듈이 있다면 추가
# config 파일이 있다면 추가

# 앞으로 새로운 폴더를 만들어서 파일을 추가할 예정임
# from app.main.[파일 이름] --> app 폴더 아래에 main 폴더 아래에 [파일 이름].py 를 import 한 것임

# 위에서 추가한 파일을 연동해주는 역할
# app.register_blueprint(추가한 파일)


# 파일 이름이 index.py이므로
from app.main.index import main as main
from app.main.test import test as test

# 위에서 추가한 파일을 연동해주는 역할
# app.register_blueprint(main)  # as main으로 설정해주었으므로
app.register_blueprint(test)
