#
# Regular cron jobs for the tugas4oss package
#
0 4	* * *	root	[ -x /usr/bin/tugas4oss_maintenance ] && /usr/bin/tugas4oss_maintenance
