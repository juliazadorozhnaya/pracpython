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


def is_tree(obj_id):
    with open(join(objects_path, obj_id[:2], obj_id[2:]), 'rb') as obj_file:
        obj = zlib.decompress(obj_file.read())
        header, _, _ = obj.partition(b'\x00')
        obj_type, _ = header.split()
        return obj_type == b'tree'


def print_commit_tree(tree_id, indent=1):
    tree_path = join(objects_path, tree_id[:2], tree_id[2:])
    with open(tree_path, 'rb') as tree_file:
        tree = zlib.decompress(tree_file.read())
        header, _, body = tree.partition(b'\x00')
        _, size = header.split()
        while body:
            treehdr, _, treetail = body.partition(b'\x00')
            git_id, body = treetail[:20], treetail[20:]
            treehdr = treehdr.decode()
            print(f'{"|" + "-" * indent + ">"}{treehdr}, {git_id.hex()}')
            if is_tree(git_id.hex()):
                print_commit_tree(git_id.hex(), indent + 1)


if len(sys.argv) == 1:
    print_branches()
elif len(sys.argv) == 2:
    print_commit(get_head_commit_id(sys.argv[1]))