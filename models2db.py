import os
import sqlite3

def create_database(db_file):
    # 连接到 SQLite 数据库
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    # 创建表，并设置model字段的全文检索索引
    c.execute('''CREATE VIRTUAL TABLE IF NOT EXISTS models
                 USING FTS5(model)''')
    
    # 提交更改并关闭连接
    conn.commit()
    conn.close()

def insert_models(db_file, models):
    # 连接到 SQLite 数据库
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    # 插入数据
    for model in models:
        c.execute("INSERT INTO models (model) VALUES (?)", (model,))
    
    # 提交更改并关闭连接
    conn.commit()
    conn.close()

def main():
    # 数据库文件名
    db_file = 'android.db'
    # 待读取的目录
    directory = 'android'
    
    # 创建数据库
    create_database(db_file)
    
    # 获取目录下的所有文件名（去除后缀）
    files = os.listdir(directory)
    
    # 获取机型信息（去除文件名的扩展名）
    models = [os.path.splitext(file)[0] for file in files]
    
    # 将机型信息存储到数据库中
    insert_models(db_file, models)
    
    print("Models have been inserted into the database.")

if __name__ == "__main__":
    main()