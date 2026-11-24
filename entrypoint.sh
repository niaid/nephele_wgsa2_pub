#!/bin/bash
set -e

# Fix ownership of the mounted directories at runtime
chown -R nephele:nephele /inputs /outputs \
  && chmod -R u+rwx /inputs /outputs
[ -f "/dbs" ] && chown -R nephele:nephele /dbs \
  && chmod -R u+rwx /dbs
[ -f "/docker_tmp" ] && chown -R nephele:nephele /docker_tmp \
  && chmod -R u+rwx /docker_tmp

# Drop root privileges and run the main container command
exec gosu nephele python main.py "$@"
