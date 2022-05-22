import glob
import shutil

def task_test():
    """Preform tests."""
    return {'actions': ['python3 -m unittest']}


def task_extract():
    """
    Extract the translation.
    """
    return {
        "actions": ["pybabel extract -o po/solver.pot solver", "pybabel init -D solver -i po/solver.pot -d po -l ru",
        "pybabel init -D solver -i po/solver.pot -d po -l en"],
        "targets": ["po/solver.pot"]
    }

def task_update():
    """
    Update the translation.
    """
    return {
        "actions": ["pybabel update -D solver -i po/solver.pot -d po -l ru",
                    "pybabel update -D solver -i po/solver.pot -d po -l en"],
        "file_dep": ["po/solver.pot"],
        "targets": ["po/ru/LC_MESSAGES/solver.po"]
    }

def task_compile():
    """
    Compile the translation.
    """
    return {
        "actions": ["pybabel compile -D solver -d po -l ru",
                    "pybabel compile -D solver -d po -l en"],
        "targets": ["po/ru/LC_MESSAGES/solver.mo"]
    }


def task_wheel():
    """Create wheel."""
    return {
            "actions": ['python3 -m build -w'],
            "file_dep": ["solver", "po/ru/LC_MESSAGES/solver.mo"],
    }

def task_sdist():
    """Build a cdist"""
    return {
        "actions": ["python3 -m build -s"],
        "file_dep": ["task.py", "po/ru/LC_MESSAGES/solver.mo"],
        "targets": ["dist/solver-0.0.1.tar.gz"]
    }


def task_cleanup():
    """Remove all."""
    return {
            "actions": ["rm -f po/solver.pot", "rm -f po/ru/LC_MESSAGES/solver.mo", "rm -f po/en/LC_MESSAGES/solver.mo"],
   }

