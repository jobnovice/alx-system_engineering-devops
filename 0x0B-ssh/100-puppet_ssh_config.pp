#a puppet manifest that configures a web server
file { '/home/job/.ssh':
  ensure => directory,
  mode   => '0700',
}

file { '/home/job/.ssh/config':
  ensure  => present,
  content => "# Puppet-managed SSH client configuration\n\nHost school-server\n  HostName 100.26.217.2\n  User job\n  IdentityFile /home/job/.ssh/school\n  PasswordAuthentication no\n",
  mode    => '0600',
}
