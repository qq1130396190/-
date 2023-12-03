#!/bin/sh

# Install Nginx
apk add nginx

# Create a simple Web app
echo '<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alpine Linux Web后台控制面板</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Alpine Linux Web Control Panel</h1>
    <p>This is a simple example. Customize it according to your needs.</p>
</body>
</html>' > /path/to/your/web/app/index.html

# Create Nginx site configuration
echo '# /etc/nginx/sites-available/alpine_web_panel

server {
    listen 80;
    server_name localhost;

    location / {
        root /etc\/ginx/ui;
        index index.html;
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}' > /etc/nginx/sites-available/alpine_web_panel

# Enable the site
ln -s /etc/nginx/sites-available/alpine_web_panel /etc/nginx/sites-enabled/

# Restart Nginx
service nginx restart
