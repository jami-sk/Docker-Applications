# Use Official Ubuntu image as the base image
FROM ubuntu:20.04

# Installations for MySQL, Python etc
RUN apt update
RUN apt-get install -y python3 
RUN apt install -y pip 
RUN apt install -y mysql-server
RUN apt install -y vim 
RUN apt install -y mc 
RUN apt install -y get 
RUN apt install -y curl
RUN apt-get clean
RUN pip install mysql-connector-python

EXPOSE 3306

# Set Environment Variables
ENV MYSQL_ROOT_PASSWORD="MySql@123"
ENV MYSQL_DATABASE="sample_db"

# Create a folder for all the files
RUN mkdir sample_mysql

# Copy all the files into the folder
COPY . /sample_mysql/

# Grant permissions to the sql script file
RUN chmod +r /sample_mysql/*.sql

RUN service mysql start
RUN cd ./sample_mysql
RUN mysql -u root <first_queries.sql
CMD ["python", "app.py"]


