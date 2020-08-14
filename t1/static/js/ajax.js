



function disp() {
           var cn = document.getElementById("one").value;
           var param = "cname="+ cn;
           var request = new XMLHttpRequest();
           request.onreadystatechange = checkname;
           request.open("POST","http://127.0.0.1:8000/check/",true);
           request.setRequestHeader('Content-Type','application/x-www-form-urlencoded')
           request.send(param);

           function checkname(){
               if(request.readyState == 4){
                  var val =request.responseText;
                  var json_data = JSON.parse(val); // converting string into json type
                  if(json_data.error == 'Name is present already')
                  {
                      document.getElementById('span1').innerText = json_data.error
                      document.getElementById('b1').disabled =true;
                  }
                  else {
                      document.getElementById('span1').innerText = json_data.msg
                      document.getElementById('b1').disabled = false;
                  }
               }
           }
         }

function contact(){
           var con = document.getElementById("two").value;
           var param = "contact="+ con;
           var request = new XMLHttpRequest();
           request.onreadystatechange = CheckContactNo;
           request.open("POST","http://127.0.0.1:8000/checkcontact/",true);
           request.setRequestHeader('Content-Type','application/x-www-form-urlencoded')
           request.send(param);
           function CheckContactNo(){
               if(request.readyState == 4){
                  var val =request.responseText;
                  var json_data = JSON.parse(val); // converting string into json type
                  if(json_data.error == 'Contact is present already')
                  {
                      document.getElementById('span2').innerText = json_data.error
                      document.getElementById('b1').disabled =true;
                  }
                  else {
                      document.getElementById('span2').innerText = json_data.msg
                      document.getElementById('b1').disabled = false;
                  }
               }
           }
}
function email(){
           var con = document.getElementById("three").value;
           var param = "email="+ con;
           var request = new XMLHttpRequest();
           request.onreadystatechange = CheckEmail;
           request.open("POST","http://127.0.0.1:8000/checkemail/",true);
           request.setRequestHeader('Content-Type','application/x-www-form-urlencoded')
           request.send(param);
           function CheckEmail(){
               if(request.readyState == 4){
                  var val =request.responseText;
                  var json_data = JSON.parse(val); // converting string into json type
                  if(json_data.error == 'Email is present already')
                  {
                      document.getElementById('span3').innerText = json_data.error
                      document.getElementById('b1').disabled =true;
                  }
                  else {
                      document.getElementById('span3').innerText = json_data.msg
                      document.getElementById('b1').disabled = false;
                  }
               }
           }
}