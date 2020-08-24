Project Name: Market-Place

Project Overview:It is a web application.It enables the users  to buy goods through online.

Clone my project: git clone 

     1.command prompt
     2.install packages using requirements.txt 
	cmd: pip install -r requirements.txt

   
    List of files:
                                                                          Resource Api                     	 		method                    
    1.database.py  	#Database connection
    2.login.py     	#For User login                                  http://localhost:8000/login           			POST                                  
    3.categories.py     #To display categories                           http://localhost:8000/categories      			GET
    4.categories.py   	#To get item details                             http://localhost:8000/categories/<category_id>         GET
    5.carts.py     	#Add to cart                                     http://localhost:8000/cart            			POST
                   	#update quantity in cart                         http://localhost:8000/cart            			PUT
                   	#Delete item from cart                           http://localhost:8000/cart            			DELETE
                   	#View items                                      http://localhost:8000//cart            		GET
    6.main_api.py      	#To run all the files


    



Database Configuration:

    server:localhost  http://localhost:8000/
    Server :localhost
    Database :shopping
    Port :5432
    Username :postgres
    Password for user postgres:7538821247
    Run description: python main_api.py

    
    