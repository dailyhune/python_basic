# gmae/__init__.py

from .graphic.render import render_test
from .sound.echo import echo_test

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}")

# 패키지 초기화 코드 작성
print("Initializing game...")
