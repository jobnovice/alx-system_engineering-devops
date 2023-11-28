#a puppet manifest that kills a process using the exec resource with the command attribute


#a puppet manifest that kills process using the exec resource along with the command to pkill
exec {'killstheProcess':
    command => 'pkill -f killmenow'
    path    => '/usr/bin/'
}
