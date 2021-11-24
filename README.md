<h1>Simple sql reader</h1>
<br>
<h3>To read file</h3>
<code>
import sqlreader as sql<br>


sql.set_base_dir('sql_queries/') # default '/'<br>
q = sql.read('query_name')<br>

OR <br>

q = sql.read('sql_queries/query_name')<br>


TO CLEAR CACHE:<br>
    sql.clear_cache()
</code>

<hr>
<br>
<h3>To creat class SQLReader</h1>
<code>
import sqlreader<br>
sql = sqlreader.SQLReader() # params 'directory_name' and 'auto_clear'<br>
q = sql.read('query_name')<br>
</code>