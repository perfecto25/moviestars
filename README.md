# Movie Star Website

## Backend

Create new virtual env and install Py packages

    cd moviestar
    pipenv install  (installs py dependencies, change your python version in Pipfile to match what you have on your computer)

## Front End

Install Node JS

    curl -sL https://rpm.nodesource.com/setup_14.x | sudo bash -
    yum install nodejs

Install Vue JS

    npm install -g @vue/cli

Create new project

    vue create web (choose default options)

## Apache config + SSL certs

    yum install httpd mod_ssl certbot python2-certbot-apache

Create a new cert for your domain (make sure to open port 80,443 on your firewall):

     certbot --apache -d site.domain.com
