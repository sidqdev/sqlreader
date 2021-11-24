<h1>Simple sql reader</h1>

<code>
<p>To read file</p>
import sqlreader as sql


sql.set_base_dir('sql_queries/') # default '/'
q = sql.read('query_name')

OR 

q = sql.read('sql_queries/query_name')


TO CLEAR CACHE:
    sql.clear_cache()
</code>

<hr>

<code>
<p>To creat class SQLReader</p>
import sqlreader
sql = sqlreader.SQLReader() # params 'directory_name' and 'auto_clear'
q = sql.read('query_name')
</code>