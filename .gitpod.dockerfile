FROM gitpod/workspace-mysql

USER root
# Setup Heroku CLI
RUN curl https://cli-assets.heroku.com/install.sh | sh

USER gitpod
# Local environment variables
# C9USER is temporary to allow the MySQL Gist to run
ENV C9USER="$USER"

USER root
# Switch back to root to allow IDE to load