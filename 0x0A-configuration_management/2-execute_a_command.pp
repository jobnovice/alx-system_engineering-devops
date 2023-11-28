#a puppet manifest that kills a process using the exec resource with the command attribute


#a puppet manifest that kills process using the exec resource along with the command to pkill
exec {'killingAprocess':
    command => '/usr/bin/pkill -f example_process_name',
    path    => '/usr/bin:/bin'
}
