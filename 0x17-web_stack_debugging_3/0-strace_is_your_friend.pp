# Puppet manifest to fix Apache 500 error

# Define variables
$apache_conf_dir = '/etc/apache2/sites-available'
$virtual_host_file = 'example.com.conf' # Replace with the actual name of your virtual host file

# Ensure the virtual host file is present and contains correct configuration
file { "${apache_conf_dir}/${virtual_host_file}":
  ensure => file,
  content => template('apache/virtual_host.conf.erb'), # You'll need to create this template with the correct configuration
  notify => Service['apache2'], # Restart Apache service when the configuration file changes
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure => running,
  enable => true,
}

