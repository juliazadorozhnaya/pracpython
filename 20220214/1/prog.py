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


def print_commit(commit_id):
    commit_path = join(objects_path, commit_id[:2], commit_id[2:])
    with open(commit_path, 'rb') as commit_file:
        commit = zlib.decompress(commit_file.read())
        header, _, body = commit.partition(b'\x00')
        body = body.decode()
        _, size = header.split()
        print(f'Commit {commit_id} with size {int(size)}\n')
        print(body)
        tree_id = body.split('tree ')[1].split()[0]
        print_commit_tree(tree_id)
        if len(body.split('parent ')) == 2:
            parent_commit_id = body.split('parent ')[1].split()[0].replace(',', '')
            print_commit(parent_commit_id)

