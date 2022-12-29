import sqlite3 

def read_db(db, table, column):
	list = [k[(0)] for k in sqlite3.connect(db).cursor().execute('SELECT '+ column +' FROM '+ table +'')]
	return list

def write_db(db, tool_category, tool_item):
	conn = sqlite3.connect(db)
	sql = ''' INSERT INTO temp_tools(tool_category,tool_item)
              VALUES(?,?); '''
	cur = conn.cursor()
	cur.execute(sql,(tool_category,tool_item))
	conn.commit()
	return