#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
db = MySQLdb.connect("localhost", "root", "", "yayay", charset='utf8' ) 
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
cursor.execute("DROP TABLE IF EXISTS FileManagement")
sql = """CREATE TABLE FileManagement (
         id  INT,
         filename  CHAR(20),
         filesize CHAR(20),  
         uploadtime CHAR(10))"""
cursor.execute(sql)
sql = """INSERT INTO FileManagement(id,
         filename, filesize, uploadtime)
         VALUES (2,'Mac', 'Mohan', 'M')"""
cursor.execute(sql)
db.commit()
sql = """INSERT INTO FileManagement(id,
         filename, filesize, uploadtime)
         VALUES (3,'Mac', 'Mohan', 'M')"""
cursor.execute(sql)
db.commit()
sql = """INSERT INTO FileManagement(id,
         filename, filesize, uploadtime)
         VALUES (4,'Mac', 'Mohan','M')"""
cursor.execute(sql)
db.commit()
sql = "UPDATE FileManagement SET filesize = filesize + 1 WHERE uploadtime = '2022-02-02'"
cursor.execute(sql)
db.commit()
sql = "DELETE FROM FileManagement WHERE filesize=Mac"
cursor.execute(sql)
db.commit()
