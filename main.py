from flask import Flask,render_template

app = Flask(__name__)
JOBS=[
  {
 'id':1,
 'title':"Data Analyst",
 'location': "Bengaluru, India",
 'salary': "Rs. 10,00,00"
},
  {
 'id':2,
 'title':"Data Scientist",
 'location': "Hyderabad, India",
 'salary': "Rs. 15,00,00"
},
  {
 'id':3,
 'title':"Front-end engineer",
 'location': "Remote",
 'salary': "Rs. 12,00,00"
},
  {
 'id':4,
 'title':"Back-end engineer",
 'location': "New York, USA"
}
  
]

@app.route('/')
def hello_jovian():
    return render_template('home.html',jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)
