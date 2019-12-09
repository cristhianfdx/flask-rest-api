# REST API WITH FLASK

## Test program

- You must have python installed on the computer, the version for this project is 3.6.7, a virtual environment is created so   that the sea is easier to execute.
- MYSQL must be installed.
- Create the database in MYSQL with the name flask_users.
- Edit the connection string in the index.py file according to the configuration you have in MYSQL.
![Screenshot from 2019-06-10 19-38-10](https://user-images.githubusercontent.com/40704923/59235543-75044180-8bb7-11e9-9dc5-706d76b5e705.png)

- "root" is the user
- database "password"

- In case you get some error for some package run from venv / bin   
  pip install -r ../../requirements.txt


### Steps

1. Enter by console to the project folder
2. Enter the virtual environment folder with the following command: cd venv / bin
3. Run the command
source activate

### Create DataBase
 From folder venv/bin run:
 - python
 - from ../../index import db
 - db.create_all()
 - exit()

## Start App
From folder venv/bin run the command   
python ../../index.py 

 
 ## Main URL
 http://localhost:3000/api
 
 # ENDPOINTS
 
 - http://localhost:3000/api/users             => GET api/users
 - http://localhost:3000/api/users             => POST api/users
 - http://localhost:3000/api/users/<user_id>   => GET api/users/:id
 - http://localhost:3000/api/users/<user_id>   => PUT api/users/:id
 - http://localhost:3000/api/users/<user_id>   => DELETE api/users/:id 
  
 # Create user
 ![post_user](https://user-images.githubusercontent.com/40704923/59235001-ea224780-8bb4-11e9-8e6a-b2b0e7a0df64.png)
 
  # Data saved in the database
 ![db](https://user-images.githubusercontent.com/40704923/59235286-0d99c200-8bb6-11e9-9d25-864f2c03db4d.png)
 
 # Get all users
 ![get_users](https://user-images.githubusercontent.com/40704923/59235163-9cf2a580-8bb5-11e9-84c7-8b418313f92a.png)
  
 # Update user
 ![put_user](https://user-images.githubusercontent.com/40704923/59235087-58ffa080-8bb5-11e9-8cf0-296ebb54da89.png)
  
 ![get_updated](https://user-images.githubusercontent.com/40704923/59235204-b98edd80-8bb5-11e9-8582-cb6f118a818b.png) 
 
 # Delete user 
 ![delete](https://user-images.githubusercontent.com/40704923/59235121-7e8caa00-8bb5-11e9-802e-426cbcae844c.png)
 
 ![clean](https://user-images.githubusercontent.com/40704923/59235246-e04d1400-8bb5-11e9-88cb-6af0d7d1e663.png)
 
 
