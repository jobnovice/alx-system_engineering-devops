# Ensure Nginx is installed and running
class { 'nginx': }

# Adjust worker processes and connections to handle higher loads
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  mode    => '0644',
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running and enabled to start at boot
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
}

# Define the contents of nginx.conf to fix the load issue
file { '/etc/nginx/nginx.conf':
  content => @("EOF"),
    user  nginx;
    worker_processes  auto;
    error_log  /var/log/nginx/error.log;
    pid        /var/run/nginx.pid;

    events {
      worker_connections  4096;  # Increase the number of allowed connections
      use epoll;  # Use epoll for better I/O handling on Linux
    }

    http {
      include       /etc/nginx/mime.types;
      default_type  application/octet-stream;

      log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';

      access_log  /var/log/nginx/access.log  main;

      sendfile        on;
      tcp_nopush      on;
      tcp_nodelay     on;
      keepalive_timeout  65;  # Optimize keepalive timeout for better connection reuse
      types_hash_max_size 2048;

      include /etc/nginx/conf.d/*.conf;

      server {
        listen       80;
        server_name  localhost;

        # Serve a static page for the root URL
        location / {
          root   /usr/share/nginx/html;
          index  index.html index.htm;
        }

        # Proxy settings for backends (optional)
        location /api/ {
          proxy_pass http://backend_server;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Adjust buffer sizes to handle larger requests
        client_body_buffer_size 16K;
        client_header_buffer_size 1k;
        large_client_header_buffers 4 8k;

        # Disable Gzip for improved load testing performance
        gzip on;
        gzip_disable "msie6";
      }
    }
  | EOF
}
