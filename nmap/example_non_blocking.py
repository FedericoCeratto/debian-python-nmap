#!/usr/bin/env python
# By Steve 'Ashcrow' Milner

import nmap

try:
    from multiprocessing import Process, Queue
except ImportError:
    # For pre 2.6 releases
    from threading import Thread as Process
    from Queue import Queue


class NmapProcess(object):
    """
    Process scans in a non-blocking way.
    """

    def __init__(self, host):
        """
        Creates an instance.

        :Parameters:
           - `host`: host to scan
        """
        self.__host = host
        self.__queue = Queue()
        self.__nm = nmap.PortScanner()
        self.__process = None

    def scan(self, ports=None, arguments='-sV', callback=None):
        """
        Starts the scan taking the same input as nmap scan except the host.

        :Parameters:
           - `ports`: ports to scan
           - `arguments` arguments for nmap
           - `callback`: optional callback to execute when results are available
        """

        def scan_process(ports, arguments, callback=None):
            self.__nm.scan(self.__host, ports, arguments)
            self.__queue.put(self.__nm)
            if callback and callable(callback):
                callback(self.__nm)

        self.__process = Process(
            target=scan_process, args=(ports, arguments, callback))
        self.__process.daemon = True
        self.__process.start()

    def __get_results(self):
        """
        Returns results if they are available, else None.
        """
        if self.__queue.empty():
            return None
        return self.__queue.get()[self.__host]

    def __del__(self):
        """
        Clean up.
        """
        self.__process.join()

    # Properties
    results = property(__get_results)
    results_available = property(lambda s: not s.__process.is_alive())


if __name__ == '__main__':
    n = NmapProcess('127.0.0.1')

    def p(s):
        print("From Callback: " + str(s['127.0.0.1']))
    n.scan(arguments="-sV -T4 -A", callback=p)
    # Do stuff here ...
    from time import sleep
    while not n.results_available:
        print("Waiting ...")
        sleep(3)
    print("From property: " + str(n.results))
