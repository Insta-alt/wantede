from flask import Flask,render_template,url_for,request,session
import uuid
import os
import schedule
app = Flask(__name__)
app.secret_key = 'rjtutjtyfghhgrtrt'

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/page')
def page():
      return render_template('page.html')
    
@app.route('/form/<string:design>',methods = ['GET','POST'])
def form(design):
      session["design_sess"] = design
      return render_template('form.html')
    
@app.route('/upload', methods=['GET','POST'])
def upload():
      desging_upload = session.get("design_sess")
      if desging_upload == "design1":
            desging_name = "design1.html"
      elif desging_upload == "design2":
            desging_name = "design2.html"
      if request.method=='POST':
            name=request.form.get('firstname')
            lastname=request.form.get('lastname')
            school=request.form.get('schoolname')
            college=request.form.get('collegename')
            phone=request.form.get('phonenumber')
            email=request.form.get('email')
            skill1=request.form.get('skill1')
            skill2=request.form.get('skill2')
            skill3=request.form.get('skill3')
            skill4=request.form.get('skill4')
            about=request.form.get('about')
            insta=request.form.get('instagram')
            git=request.form.get('github')
            key = uuid.uuid1()
            # image uploading method
            img = request.files["dp"]
            img.save(f"static/images/{img.filename}")
            img_new_name = f"{key}{img.filename}"
            os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")
            
      return render_template(desging_name,git=git,insta=insta,img=img_new_name,dname=name,dlname=lastname,ds1=skill1,ds2=skill2,ds3=skill3,ds4=skill4,no=phone,email=email,school=school,college=college,about=about)
def delete():
      files = os.listdir("static/images")  
      for f in files:
          os.remove(f"static/images{f}")   
                 
      

if __name__=='__main__':
   schedule.every().day.at("23:59").do(delete)   
   app.run(debug=True)