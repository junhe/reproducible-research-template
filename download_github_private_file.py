#!/usr/bin/env python
import argparse
import subprocess
import os
import sys
import shlex
import time

WLRUNNER, LBAGENERATOR = ('WLRUNNER', 'LBAGENERATOR')

def main():
    #function you want to call
    # parse_blkparse('./bigsample', 'myresult')
    # shcmd("scp jun@192.168.56.102:/tmp/ftlsim.in ./FtlSim/misc/")
    download('doraemon', 'Makefile.py', '/tmp',
        '7c21a09b1bec29e5b264eae5e76bcedfbf07def5')

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = newPath

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def shcmd(cmd, ignore_error=False):
    print 'Doing:', cmd
    ret = subprocess.call(cmd, shell=True)
    print 'Returned', ret, cmd
    if ignore_error == False and ret != 0:
        raise RuntimeError("Failed to execute {}. Return code:{}".format(
            cmd, ret))
    return ret

def download(repo_name, file_path, target_dir, commit):
    print repo_name, file_path, target_dir, commit
    token = os.getenv("GITHUB_TOKEN")
    if token == None:
        raise RuntimeError("Environment Var GITHUB_TOKEN does not exist"\
            ". Search your Evernote to find it. "
            "intitle:github")

    cmd = "curl -H 'Authorization: token {token}' "\
        "-H 'Accept: application/vnd.github.v3.raw' -O "\
        "-L https://raw.githubusercontent.com/junhe/"\
        "{repo_name}/{commit}/{file_path}".format(token=token,
        repo_name=repo_name, commit=commit, file_path=file_path)

    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)

    with cd(target_dir):
        shcmd(cmd)

def _main():
    parser = argparse.ArgumentParser(
            description=""
            )
    parser.add_argument('--repo_name', action='store')
    parser.add_argument('--file_path', action='store')
    parser.add_argument('--target_dir', action='store')
    parser.add_argument('--commit', action='store')
    args = parser.parse_args()

    argdic = vars(args)
    if not all( v for _,v in argdic.items() ):
        parser.print_help()
        exit(1)

    download(**argdic)

if __name__ == '__main__':
    _main()
