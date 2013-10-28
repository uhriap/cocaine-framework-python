#!/usr/bin/env python

from cocaine.server.worker import Worker
from cocaine.logging import Logger

__author__ = 'EvgenySafronov <division494@gmail.com>'

log = Logger()


def echo(request, response):
    response.write('Hi!')
    message = yield request.read()
    log.debug('Message received: \'{0}\'. Sending it back ...'.format(message))
    response.write(message)
    response.write('Another message.')
    message = yield request.read()
    log.debug('Message received: \'{0}\'. Sending it back ...'.format(message))
    response.write(message)
    response.close()


worker = Worker()
worker.run({
    'ping': echo,
})
