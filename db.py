import sqlite3

def get_conn():
	conn = sqlite3.connect("test.db")
	cursor = conn.cursor()
	return cursor

def boolen_query(query):
	conn = sqlite3.connect("test.db")
	cursor = conn.cursor()
	answer=0
	try:
		cursor.execute(query)
		conn.commit()
		answer=1
	except Exception:
		answer=0
	conn.close()
	return answer

def create_database():
	query="create table robots(id INTEGER PRIMARY KEY AUTOINCREMENT,name text,datestart datetime TIMESTAMP default CURRENT_TIMESTAMP,isdeleted int DEFAULT 0,order_type int default 0,order_indent int,period_symbols text,lot real,ai_trade int default 0,sltp text,open_comm text,signal_comm text,istrail int default 0,trail_point int,is_few int,is_diff int,is_news,is_average,ai_name text,is_sended int default 0)"
	boolen_query(query)
	


def select_query(query):
	conn = sqlite3.connect("test.db")
	this_keys_arr=[]
	chk_union=query.split(" UNION ")
	query_keys_arr=query.split("SELECT ")
	if len(chk_union)>1:
		query_keys_arr=chk_union[0].split("SELECT ")
	new_query_keys_arr=[]
	j=1
	while(j<len(query_keys_arr)):
		new_query_keys_arr.append(query_keys_arr[j])
		j+=1
	query_keys_arr="SELECT ".join(new_query_keys_arr)
	query_keys_arr=query_keys_arr.split(" FROM")
	table_name=query.split("FROM ")
	table_name=table_name[len(table_name)-1].split(" ")[0]
	if len(query_keys_arr)>2:
		this_query_keys_arr=[]
		z=1
		while(z<len(query_keys_arr)):
			this_query_keys_arr.append(query_keys_arr[z-1])
			z+=1
		query_keys_arr=" FROM".join(this_query_keys_arr)
	else:
		query_keys_arr=query_keys_arr[0]
	if query_keys_arr=="*":
		cursor = conn.cursor()
		for row in cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND tbl_name='"+str(table_name)+"'"):
			row=row[0].split(str(table_name)+"(")[1].split(",")
			for r in row:
				r=r.split(" ")[0]
				this_keys_arr.append(r)
			break
	else:
		keys_arr=query_keys_arr.split(",")
		for k in keys_arr:
			chk_as=k.split("AS ")
			if len(chk_as)==1:
				chk_as=k.split("as ")
				if len(chk_as)==1:
					if k.find("(")>=0 or k.find(")")>=0:
						continue
					else:
						this_keys_arr.append(k)
				else:
					this_keys_arr.append(chk_as[1])
			else:
				this_keys_arr.append(chk_as[1])
	cursor = conn.cursor()
	answer=[]
	for row in cursor.execute(query):
		z=0
		min_ans={}
		for k in this_keys_arr:
			min_ans[k]=row[z]
			z+=1
		answer.append(min_ans)
	conn.close()
	return answer

