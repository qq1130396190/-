#!/bin/sh

# Step 1: Edit Nginx Configuration
cat <<EOL > /etc/nginx/nginx.conf
user nginx;
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log /var/log/nginx/access.log main;
    error_log /var/log/nginx/error.log;

    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;  # Add this line

    server {
        listen 80;
        server_name localhost;

        location / {
            root /var/www/html;
            index index.html;
        }

        # Additional server configurations can be added here
    }
}
EOL

# Step 2: Create Basic HTML Page
mkdir -p /var/www/html
cat <<EOL > /var/www/html/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to My Website</title>
</head>
<body>
    <h1>Hello, World! This is my Nginx server on Alpine Linux.</h1>
</body>
</html>
EOL

# Step 3: Start Nginx
rc-service nginx start

echo "Nginx configuration and HTML page created. Nginx started."
