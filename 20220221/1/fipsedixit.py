import ipsedixit
import os
import sys

defaults = ['caesar', 'tacitus']

if len(sys.argv) < 3:
    generator = ipsedixit.Generator()
    paragraphs = generator.paragraphs(int(sys.argv[1]))
    print('\n\n'.join(paragraphs))
    
elif sys.argv[2] in defaults or os.path.isfile(sys.argv[2]):
    if sys.argv[2] in defaults:
        text = sys.argv[2]
        
    elif os.path.isfile(sys.argv[2]):
        try:
            with open(sys.argv[2], 'rt') as word_base:
                text = word_base.read()
        except FileNotFoundError as E:
            print("This file does not exist")
            sys.exit()
    generator = ipsedixit.Generator(text)
    sys.argv.pop(2)
else:
    generator = ipsedixit.Generator()
args = ipsedixit.parse_args()
print('\n\n'.join(generator.paragraphs(args.num, args.min, args.max)))