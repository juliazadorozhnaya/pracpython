import re
import sys
import ast
import difflib
import textdistance


def check(text):
    text = re.sub(r"#[^\n]*\n", r"\n", text)
    tree = ast.parse(ast.unparse(ast.parse(text)))
    result = ast.dump(ast.NodeTransformer().generic_visit(tree), annotate_fields=False)
    result = re.sub(r"(\s)", r"", result)
    result = re.sub(r"\'[^\']*\'", r"", result)
    result = re.sub(r"\"[^\"]*\"", r"", result)
    return result


with open(sys.argv[1], 'r') as f:
    file_first_text = f.read()
with open(sys.argv[2], 'r') as f:
    file_second_text = f.read()
plagiarism = textdistance.damerau_levenshtein.normalized_distance(check(file_first_text), check(file_second_text))
if plagiarism < 0.1:
    print(difflib.HtmlDiff().make_file(file_first_text, file_second_text))
    print(f'plagiarism! {plagiarism}')
else:
    print(f'Not plagiarism! {plagiarism}')
