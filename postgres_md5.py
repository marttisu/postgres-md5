#!/usr/bin/env python
"""Get PostgreSQL credentials MD5 hash."""

import getpass
import hashlib
import random
import string
import subprocess
import time


def main(n_pw_suggestion=3, pw_len=15):
    """Print PostgreSQL credentials MD5 hash."""
    username = input('Username: ')
    print('')
    try:
        pw_suggestion = subprocess.check_output(
            ['apg', '-m', str(pw_len), '-n', str(n_pw_suggestion),
             '-c', str(time.time()), '-M', 'NCL']).decode()
    except FileNotFoundError as e:
        pw_suggestion = '\n'.join([''.join(random.choices(
            string.ascii_lowercase + string.ascii_uppercase +
            string.digits, k=pw_len)) for i in range(n_pw_suggestion)])+'\n'
    print('Here are some random password suggestions:\n{}'.format(
        pw_suggestion))
    password = getpass.getpass('Password: ')
    while password != getpass.getpass('Confirm password: '):
        password = getpass.getpass('Password: ')
    print("\nPassword md5 hash: " + "md5" + hashlib.md5(
        (password + username).encode("utf-8")).hexdigest())


if __name__ == '__main__':
    main()
