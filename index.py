#coding:utf-8

import cgi 

print("Content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<html lang="fr"> 
 <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<head>
    <meta charset="utf-8">
    <title>TELLMe</title>
    <style>
        
      * {
        box-sizing: border-box;
      }

      form.example input[type=text] {
        padding: 10px;
        font-size: 17px;
        border: 1px solid black;
        float: left;
        width: 80%;
        background: #f1f1f1;
      }

      form.example button {
        float: left;
        width: 20%;
        padding: 10px;
        background: #20B2AA;
        color: black;
        font-size: 17px;
        border: 1px solid black;
        border-left: none;
        cursor: pointer;
      }

      form.example button:hover {
        background: black;
          color: #20B2AA;

      }

      form.example::after {
        content: "";
        clear: both;
        display: table;
      }
        center{
            font-size: 300%;
            /*position: absolute;*/
            left: 0;
            /*top: 500%;*/
            width: 100%;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
    <br></br><br></br><br></br><br></br>
        <div class="row">
            <div class="col-sm-12">
                <h1><center>TELLMe</center></h1>
            </div>
        </div>
        <div class = "row">
            <div class="col-sm-12">    
                <form class="example" action="server.py" style="margin:auto;max-width:500px">
                    <input type="text" placeholder="Your search..." name="search">
                    <button type="submit"><i class="fa fa-search"></i></button>
                </form>
            </div>
        </div>
    
    </div>
</body>
</html>
"""

print(html)
