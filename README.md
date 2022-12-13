  Welcome to your free open source website to start selling stuff online for free


Front end guide to clone repo and run it
Download docker
Download pip
download gitbash
dowload VSCode (blue)
download git (commands for github)

1st step
create a new folder in desktop
git clone https://github.com/esejosue1/pointOfSale
cd (change directory) into that file
Type docker build .     //build the attached docker file
Type docker-compose build    //run the docker file
Type docker-compose up    //run the application
Default web browser port, 127.0.0.1:8000    //go to this url for web application

2nd
stop server
type "python manage.py makemigrations"
type "python manage.py migrate"
type python manage.py runserver or docker-compose up

3rd
stop the server
type "python manage.py" createsuperuser
fill in the email, username, password with info in doc file
type "python manage.py runserver" or docker-compose up
in the url, type after local host "/admin"
login with user credentials
add some items in products
