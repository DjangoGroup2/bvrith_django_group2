from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import MySQLdb

def get_fname(request, fid):
       conn = MySQLdb.connect (host = "localhost",
                  user = "micsuser",
                  passwd = "micspass",
                  db = "sis")
       cursor = conn.cursor ()
       cursor.execute ("select fname from sis_faculty where fid = '"+fid+"'")
       if cursor.rowcount == 0:
               html = "<html><body>There is no Faculty member with id %s.
                       </body></html>" % fid
       else:
               row = cursor.fetchone()
               html = "<html><body>The Faculty name is %s.
                       </body></html>" % row[0]
       return HttpResponse(html)

def get_cname(request, cnum):
       conn = MySQLdb.connect (host = "localhost",
                  user = "micsuser",
                  passwd = "micspass",
                  db = "sis")
       cursor = conn.cursor ()
       cursor.execute ("select cname,credits from sis_course where
                              cnum = '"+cnum+"'")
       if cursor.rowcount == 0:
               html = "<html><body>There is no Course with number %s.
                       </body></html>" % cnum
       else:
               row = cursor.fetchone()
               t = get_template('cname.html')
               c = Context({'cnum' : cnum, 'cname' : row[0], 'credits' : row[1]})
               html = t.render(c)
       return HttpResponse(html)
