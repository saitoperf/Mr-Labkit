FROM nginx

COPY ./ssl/ssl/ /etc/nginx/ssl
COPY ./index.html /usr/share/nginx/html/index.html
COPY ./ssl/ssl.conf /etc/nginx/conf.d/ssl.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
