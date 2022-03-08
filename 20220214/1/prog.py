import sys
from shlex import join
import zlib


def print_branches():
    for branch in listdir(heads_path):
        print(branch)


def get_head_commit_id(branch_name):
    branch_head_path = join(heads_path, branch_name)
    with open(branch_head_path) as branch_head_file:
        return branch_head_file.read().strip()
