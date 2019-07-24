FROM gitpod/workspace-mysql

USER root
RUN curl https://cli-assets.heroku.com/install.sh | sh