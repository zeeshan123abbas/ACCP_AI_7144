# Puppet manifest: make sure a web server is installed and running (declarative)
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => "<h1>Deployed by Puppet</h1>",
  require => Package['nginx'],
}
