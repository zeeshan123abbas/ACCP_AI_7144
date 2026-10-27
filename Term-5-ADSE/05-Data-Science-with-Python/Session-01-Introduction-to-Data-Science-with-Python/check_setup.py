# check_setup.py - confirm your data science libraries are installed
# Run: python check_setup.py

import sys
print("Python version:", sys.version.split()[0])

# Try to import each library and print its version
libraries = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn"]

for name in libraries:
    try:
        module = __import__(name)                 # import by name
        print(f"OK   {name:<11} {module.__version__}")
    except ImportError:
        print(f"MISSING {name}  ->  pip install {name if name != 'sklearn' else 'scikit-learn'}")
