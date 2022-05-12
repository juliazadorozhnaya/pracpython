DOIT_CONFIG = {"default_tasks": ['extract', 'update', 'compile', 'tests']}

def task_extract():
    """Extracts the translation."""
    return {
        "actions": ["pybabel extract -o po/solve.pot solve"],
        "targets": ["po/solve.pot"]
    }

def task_update():
    """Updates the translation."""
    return {
        "actions": ["pybabel update -D solve -i po/solve.pot -d po -l ru",
                    "pybabel update -D solve -i po/solve.pot -d po -l en"],
        "file_dep": ["po/solve.pot"],
        "targets": ["po/ru/LC_MESSAGES/solve.po"]
    }

def task_compile():
    """Compiles the translation."""
    return {
        "actions": ["pybabel compile -D solve -d po -l ru",
                    "pybabel compile -D solve -d po -l en"],
        "targets": ["po/ru/LC_MESSAGES/solve.mo"]
    }

def task_tests():
    """Tests the module."""
    return {
        "actions": ["python3 -m test_equ -v"]
    }


def task_translation():
    """Update and compile translation"""
    domain = "prog"
    return {
        'actions': [f"pybabel extract --output-file={domain}.pot --input-dirs={domain}.py",
                    f"pybabel update --domain={domain} --input-file={domain}.pot --output-dir=po --locale=ru",
                    f"pybabel compile --domain={domain} --directory=po --locale=ru"],
        'targets': [f'{domain}.pot', f'po/ru/LC_MESSAGES/{domain}.mo'],
        'file_dep': [f"{domain}.py"],
        'clean': True
    }

