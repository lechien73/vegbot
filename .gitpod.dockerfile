FROM gitpod/workspace-mysql

USER root
# Setup Heroku CLI
RUN curl https://cli-assets.heroku.com/install.sh | sh

# Setup MongoDB
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
RUN echo "deb http://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list
RUN apt-get update -y
RUN touch /etc/init.d/mongod
RUN apt-get -y install mongodb-org mongodb-org-server -y

USER gitpod
# Local environment variables
# C9USER is temporary to allow the MySQL Gist to run
ENV C9USER="gitpod"

USER root
# Switch back to root to allow IDE to load
RUN echo "Creating the gitpod user in MySQL"
RUN mysql -e "CREATE USER 'gitpod'@'%' IDENTIFIED BY '';"
RUN echo "Granting privileges"
RUN mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'gitpod'@'%' WITH GRANT OPTION;"
RUN echo "Done"