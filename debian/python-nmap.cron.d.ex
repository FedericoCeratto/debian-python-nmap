#
# Regular cron jobs for the python-nmap package
#
0 4	* * *	root	[ -x /usr/bin/python-nmap_maintenance ] && /usr/bin/python-nmap_maintenance
