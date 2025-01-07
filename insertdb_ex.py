import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect("fastapi.db")
cursor = conn.cursor()

# 데이터 삽입
cursor.execute("""
INSERT INTO Board (writer, title, content) 
VALUES ("홍길동", "board 기본게시판", "테스트");
""")
cursor.execute("""
INSERT INTO Board (writer, title, content) 
VALUES ("김 구", "제목", "내용");
""")
conn.commit()

conn.close()