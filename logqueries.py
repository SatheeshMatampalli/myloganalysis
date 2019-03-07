# python 3 version
import psycopg2
from datetime import datetime

# database
MydataBaseName = "news"
# connecting to database


def connect(MydataBaseName="news"):
    try:
        conn = psycopg2.connect("dbname={}".format(MydataBaseName))
        curr = conn.cursor()
        return conn, curr
    except:
        print("check your database its wrong")

# query_1
# this query is for what are the most popular articles of all time
My_query_Articles = ("select articles.title, count(*) as num "
                     "from log, articles "
                     "where log.status='200 OK' "
                     "and articles.slug = substr(log.path,10) "
                     "group by articles.title "
                     "order by num desc limit 3")
# second_Query
# second query foe who are the most popular article authors in all time
My_query_Authors = ("SELECT c.name, count(*) AS views "
                    "FROM articles a INNER JOIN log b "
                    "on a.slug=replace(path,'/article/','') INNER JOIN "
                    "authors c on (c.id=a.author) "
                    "WHERE status='200 OK' AND length(path)>1 GROUP by "
                    "c.name ORDER by views DESC")

# third_query
# thia query is for on which days did more than 1% of requests lead to errors
My_query_Errors = ("SELECT day, perc FROM ("
                   "SELECT day, round((sum(requests)/(SELECT count(*) "
                   "FROM log WHERE substring( "
                   "cast(log.time as text), 0, 11) = day) * 100), 2) as "
                   "perc FROM (select "
                   "substring(cast(log.time as text), 0, 11) as "
                   "day, count(*) as requests FROM log "
                   "WHERE status like '%404%' GROUP by day) "
                   "as log_percentage GROUP by day ORDER by perc desc) "
                   "as final_query "
                   "WHERE perc >= 1")


# queries execution part
def query_execute(query):
    conn, curr = connect()
    curr.execute(query)
    return curr.fetchall()
    conn.close()


def print_results(ques_results):
    for i, j in enumerate(ques_results):
        print("\t"+str(i+1)+"."+str(j[0])+" - "+str(j[1])+"views")


def print_errors(query_results):
    for res in query_results:
        date = res[0]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = datetime.strftime(date_obj, "%B %d,%Y")
        print("\t"+str(formatted_date)+" - "+str(res[1])+"% errors")


if __name__ == '__main__':
    try:
        print("             logs analysis queries execution process  ")
        print("!. . . . . . . . . . . . . . . . . . . . . . . . . . . !")
        print("what are the most popular three articles in all time?")
        My_articles = query_execute(My_query_Articles)
        print_results(My_articles)
        # second execution
        print("who are the most popular article authors in all time?")
        My_authors = query_execute(My_query_Authors)
        print_results(My_authors)

        print("on which days did more than 1% of requests lead to errors?")
        My_error_days = query_execute(My_query_Errors)
        print_errors(My_error_days)
    except Exception as e:
        print(e)
