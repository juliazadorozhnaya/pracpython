import glob
import shutil

def task_test():
    """Preform tests."""
    return {'actions': ['python3 -m unittest']}


def task_update():
    """Updates the translation."""
    return {
        "actions": ["pybabel update -D solve -i po/solve.pot -d po -l ru",
                    "pybabel update -D solve -i po/solve.pot -d po -l en"],
        "file_dep": ["po/solve.pot"],
        "targets": ["po/en/LC_MESSAGES/solve.po"]
    }

def task_compile():
    """Compiles the translation."""
    return {
        "actions": ["pybabel compile -D solve -d po -l ru",
                    "pybabel compile -D solve -d po -l en"],
        "targets": ["po/ru/LC_MESSAGES/solve.mo"]
    }

    
def task_cleanup():
    """Clearing all generations include, translation template."""
    return {
        "action": [
            (shutil.rmtree("/_build", ignore_errors=True)),
        ]
    }


def task_wheel():
    """Wheel builds using build."""
    return {
        'actions': ['python -m build -w'],
        'file_dep': ['solve', 'po/ru/LC_MESSAGES/prog.mo'],
        'targets': ['dist/prog-0.0.1-py3-none-any.whl']
    }


def task_sdist():
    """Building an archive with sources using build."""
    return {
        'actions': ['python -m build -s'],
        'file_dep': ['solve', 'po/ru/LC_MESSAGES/prog.mo'],
        'targets': ['dist/prog-0.0.1.tar.gz']
    }
