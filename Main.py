from flask import Flask , render_template  , request , redirect
import csv

app = Flask(__name__)



@app.route('/')
def home():
   return render_template('index.html')

@app.route('/<string:p_name>')
def hello_world(p_name):
    return render_template(p_name)

def write_txt(data):
      with open('test1.txt' , mode='a+' ,encoding='utf-8') as textfile:
         email = data['email']
         subject = data['subject']
         message = data['message'] 
         textfile.write(f'\n\nemail : {email} \n subject : {subject} \n message : {message} \n\n -----------')
         textfile.close()

def write_csv(data):
      with open('test11.csv' , mode='a+') as textfile2:
         email = data['email']
         subject = data['subject']
         message = data['message'] 
         csv_writer = csv.writer(textfile2 ,lineterminator='\n' ,delimiter = ',' , quotechar = '"' , quoting = csv.QUOTE_MINIMAL)
         csv_writer.writerow([email,subject,message])


@app.route('/submit_form' , methods = ['GET','POST'])
def sub (name=None):
    if request.method == 'POST':
      data = request.form.to_dict()
      write_csv(data)
      print(data)
      return render_template('thankyou.html',name=name)
    else:
       return 'wrnf'

    






if __name__ == "__main__":
  app.run(debug=True)
  app.run(host='0.0.0.0', port=80)
  