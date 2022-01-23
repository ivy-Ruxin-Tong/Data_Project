from flask import Flask, render_template, request
import pandas as pd
from SnowflakeConnection import sfconnect

'''
We put double brackets into our template file as a way to tell our flask template to use a variable.
'''
app = Flask("my website")
@app.route('/')
def homepage():
  cur = cnx.cursor().execute("select color_name,  count(*) "
                            "from colors "
                            "group by 1 "
                            "having count(*) > 50 "
                            "order by 2 desc;")
  rows = pd.DataFrame(cur.fetchall(), columns= ['color name','votes'])
  dfhtml = rows.to_html(index= False)
  return render_template('index.html', dfhtml = dfhtml)
    # return '''
    # <html>
    #   </head>
    #   <body>
    #   <h2> You will love our rainbow colors! </h2>
    #   Colors table will go here
    # </html>
    # '''
    # return 'Welcome to my website! My account # is ' + str(account_name)
@app.route('/submit')
def submitpage():
  return render_template('submit.html')

@app.route('/thanks4submit', methods = ['POST'])
def thanks4submit():
  colorname = request.form.get('cname')
  username = request.form.get('uname')
  cnx.cursor().execute("INSERT INTO COLORS(COLOR_UID, COLOR_NAME) " +
           "SELECT COLOR_UID_SEQ.nextval, '" + colorname + "'") 
  return render_template("thanks4submit.html", colorname = colorname, username = username) 

@app.route('/coolcharts')
def coolcharts():
  cur = cnx.cursor().execute("select color_name,  count(*) "
                            "from colors "
                            "group by 1 order by 2 desc;")
  data4charts = pd.DataFrame(cur.fetchall(), columns = ['color', 'votes'])
  data4chartsJson = data4charts.to_json(orient= 'records')
  return render_template("coolcharts.html", data4chartsJson = data4chartsJson)

cnx = sfconnect()

# cur.execute("Select current_account()")
# account_name = cur.fetchone()[0]

app.run()

