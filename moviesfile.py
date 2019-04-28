import pymysql
mysql_server="localhost"

class moviefile():
    def moviesfunc(self):
        db = pymysql.connect(mysql_server, "root", "c2b925ym", "movieRecommendation")
        cursor = db.cursor()
        sql = "select ID,poster_url,Movie from movies"
        results=""
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print("Error: unable to fetch data")
        db.close()
        return results