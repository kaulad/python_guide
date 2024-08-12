# Introduction

This repository aims to educate data scientist to write better and more beautiful python codes using available open-source tools.

Enjoy!

## PEP8 - Style Guide for Pyton Code [link](https://peps.python.org/pep-0008/)

- [Book: Beyond the Basic Stuff with Python](https://inventwithpython.com/beyond/) Chapter 1-14
- [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)
- [Nine simple steps for better-looking python code](https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf)
- [15 common coding mistakes data scientist make in Python (and how to fix them)](https://towardsdatascience.com/15-common-coding-mistakes-data-scientist-make-in-python-and-how-to-fix-them-7760467498af)
- [Python’s Missing Batteries: Essential Libraries You’re Missing Out On](https://betterprogramming.pub/pythons-missing-batteries-essential-libraries-you-re-missing-out-on-12853e5258d2)
- [How to Automate Python Code Formatting (using Black, YAPF and isort)](https://www.youtube.com/watch?v=q2d5vrw1Lss)
- [Markdown Tutorial](https://agea.github.io/tutorial.md/), [Markdown Basic Syntax](https://www.markdownguide.org/basic-syntax/)
- [Pythonic code](https://towardsdatascience.com/how-to-write-pythonic-code-208ec1513c49#:~:text=In%20the%20Python%20community%2C%20Pythonic,maintainability%2C%20readability%20and%20efficiency%20perspective)

![example_bad_pep8.py](/img/example_bad.PNG)

``` sh
pylint example_bad_pep8.py

************* Module example_bad_pep8
example_bad_pep8.py:19:0: C0304: Final newline missing (missing-final-newline)
example_bad_pep8.py:1:0: C0114: Missing module docstring (missing-module-docstring)
example_bad_pep8.py:2:0: C0103: Constant name "x" doesn't conform to UPPER_CASE naming style (invalid-name)
example_bad_pep8.py:6:0: C0115: Missing class docstring (missing-class-docstring)
example_bad_pep8.py:6:0: C0103: Class name "myrect" doesn't conform to PascalCase naming style (invalid-name)
example_bad_pep8.py:10:4: C0116: Missing function or method docstring (missing-function-docstring)
example_bad_pep8.py:6:0: R0903: Too few public methods (1/2) (too-few-public-methods)
example_bad_pep8.py:15:0: W0105: String statement has no effect (pointless-string-statement)
example_bad_pep8.py:1:0: W0611: Unused pandas imported as pd (unused-import)

-----------------------------------
Your code has been rated at 3.08/10
```

![example_good_pep8.py](/img/example_good.PNG)

```sh
pylint example_good_pep8.py

************* Module example_good_pep8
example_good_pep8.py:5:0: R0903: Too few public methods (1/2) (too-few-public-methods)

-----------------------------------
Your code has been rated at 9.00/10
```

``` python
class MyRect: # pylint: disable=too-few-public-methods
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.00/10, +1.00)
```

## Auto-formatter

- black [https://github.com/psf/black](https://github.com/psf/black)
- yapf [https://github.com/google/yapf](https://github.com/google/yapf) (own by Google)
- isort [https://github.com/PyCQA/isort](https://github.com/PyCQA/isort)

```sh
# command line
black example_bad_pep8.py
yapf -i --style=.style.yapf example_bad_pep8.py
isort example_bad_pep8.py
```

``` python
# before using yapf
x = {  'a':37,'b':42,

'c':927}

y = 'hello ''world'
z = 'hello '+'world'
a = 'hello {}'.format('world')
class foo  (     object  ):
  def f    (self   ):
    return       37*-+2
  def g(self, x,y=42):
      return y
def f  (   a ) :
  return      37+-+a[42-x :  y**3]
```

``` python
# after using yapf
x = {'a': 37, 'b': 42, 'c': 927}

y = 'hello ' 'world'
z = 'hello ' + 'world'
a = 'hello {}'.format('world')


class foo(object):
    def f(self):
        return 37 * -+2

    def g(self, x, y=42):
        return y


def f(a):
    return 37 + -+a[42 - x:y**3]

```

## Visual Code and  useful extensions

1. Install **`Visual Studio Code`** [link](https://code.visualstudio.com/download)

2. Install **`Extensions`** from [vsixhub](https://www.vsixhub.com/) credit: [VSCode extensions you need to know for python programming](https://www.youtube.com/watch?v=SxzzFwzPYqo). Some extensions are need to be downloaded manually and installed without inxternet.

> ## Python

`Python`: A Visual Studio Code extension with rich support for the Python language (for all actively supported versions of the language: >=3.7), including features such as IntelliSense (Pylance), linting, debugging, code navigation, code formatting, refactoring, variable explorer, test explorer, and more! [link](https://www.vsixhub.com/vsix/116173/)

`Pylance`:  Pylance has the ability to supercharge your Python IntelliSense experience with rich type information, helping you write better code faster. [link](https://www.vsixhub.com/vsix/116403/) I don't kkkow

`Pylint`:  Pylint is a static code analyser for Python. It analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored. [link](https://www.vsixhub.com/vsix/112166/), [Pylint Message Code Documentation](https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html)

`Code Runner`:  Run code snippet or code file for multiple languages: C, C++, Java, JavaScript, PHP, Python and custom command [link](https://www.vsixhub.com/vsix/43/)

- You can run your code with shortcut (Ctrl-Alt-n)
- Must system path of Conda in windows

`Jupyter`:  Provides basic notebook support for language kernels that are supported in Jupyter Notebooks today, and allows any Python environment to be used as a Jupyter kernel. This is NOT a Jupyter kernel--you must have Python environment in which you've installed the Jupyter package, though many language kernels will work with no modification [link](https://www.vsixhub.com/vsix/114775/)

`Path Intellisense`:  Eliminate context switching and costly distractions. Create and merge PRs and perform code reviews from inside your IDE while using jump-to-definition, your favorite keybindings, and other IDE tools. [link](https://www.vsixhub.com/vsix/3332/)

``` python
with open("./dir/filename") # will have auto-complete
```

`audoDocString`:  quickly generate docstrings for python functions.. [link](https://www.vsixhub.com/vsix/4771/)

``` python
def area(width: float, height: float) -> float:
    """_summary_

    Args:
        width (float): _description_
        height (float): _description_
    Returns:
        float: _description_
    """
    return width*height
```

`Tabnine Autocompelte AI`:  **Not all free** Tabnine is an AI code assistant that makes you a better developer. Tabnine will increase your development velocity with real-time code completions in all the most popular coding languages and IDEs. [link](https://www.vsixhub.com/vsix/4232/)

> **Git**

`Git Graph`: View a Git Graph of your repository, and easily perform Git actions from the graph. Configurable to look the way you want! [link](https://www.vsixhub.com/vsix/13/)

`Git History`:  View and search git log along with the graph and details. [link](https://www.vsixhub.com/vsix/2001/)

`GitLens`:  GitLens supercharges Git inside VS Code and unlocks untapped knowledge within each repository. It helps you to visualize code authorship at a glance via Git blame annotations and CodeLens, seamlessly navigate and explore Git repositories, gain valuable insights via rich visualizations and powerful comparison commands, and so much more. [link](https://www.vsixhub.com/vsix/112166/)

> ## Experiences

`Prettier - Code formatter`: Prettier is an opinionated code formatter. It enforces a consistent style by parsing your code and re-printing it with its own rules that take the maximum line length into account, wrapping code when necessary. [link](https://www.vsixhub.com/vsix/47/)

`Indent Rainbow`: This extension colorizes the indentation in front of your text, alternating four different colors on each step. Some may find it helpful in writing code for Python, Nim, Yaml, and probably even filetypes that are not indentation dependent. [link](https://www.vsixhub.com/vsix/1824/)

`Python Indent`:  Correct Python indentation in Visual Studio Code. [link](https://www.vsixhub.com/vsix/1004/)

``` python
df = pd.read_csv("file_pat",
                cols = ['col1', 'col2'],
                sep = '|'
)
```

`Error lens`:  ErrorLens turbo-charges language diagnostic features by making diagnostics stand out more prominently, highlighting the entire line wherever a diagnostic is generated by the language and also prints the message inline. [link](https://www.vsixhub.com/vsix/4148/)

``` python
print "This is a test"  invalid sytax
```

`Better Comments`:  Help you create more human-friendly comments in your code. With this extension, you will be able to categorise your annotations into: Alerts!, Queries?, TODOs, Highlights, Commented out code can also be styled to make it clear the code shouldn't be there [link](https://www.vsixhub.com/vsix/4148/)

`Bracket Pair Colorization Toggler`: Gives you a simple command to quickly toggle the global “Bracket Pair Colorization” setting. [link](https://www.vsixhub.com/vsix/76042/)

``` python
 [{()}]
```

`Trailing Spaces`: highlight trailing spaces and delete them in a flash! [link](https://www.vsixhub.com/vsix/4298/)

`Code Spell Checker`: A basic spell checker that works well with code and documents. The goal of this spell checker is to help catch common spelling errors while keeping the number of false positives low.[link](https://www.vsixhub.com/vsix/1949/)

`Todo Tree`:  Searches (using ripgrep) your workspace for comment tags like TODO and FIXME, and displays them in a tree view in the activity bar.[link](https://www.vsixhub.com/vsix/2047/)

> ## Extras

`SQL Formatter`: Format SQL files using the sql-formatter-plus npm package. [link](https://www.vsixhub.com/vsix/5708/)

`Inline SQL`: Highlight and lint inline SQL strings. [link](https://www.vsixhub.com/vsix/76198/)

`Markdown Preview Enhanced`: Provides you with many useful functionalities such as automatic scroll sync, math typesetting, mermaid, PlantUML, pandoc, PDF export, code chunk, presentation writer, etc .[link](https://www.vsixhub.com/vsix/1953/)'

`markdownlint`:  Includes a library of rules to encourage standards and consistency for Markdown files. It is powered by the markdownlint library for Node.js (which was inspired by markdownlint for Ruby). Linting is performed by the markdownlint-cli2 engine. [link](https://www.vsixhub.com/vsix/1940/), [Markdownlint code](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md032---lists-should-be-surrounded-by-blank-lines)


## Good Reading

`__init__.py Understanding-python-imports-init-py-and-pythonpath`: [link](https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355)

## Conda multiple environments

conda install ipykernel

conda install nb_conda_kernels
