
# Visual Code and  useful extensions

1. Install **`Visual Studio Code`** [link](https://code.visualstudio.com/download)

2. Install **`Extensions`** from [vsixhub](https://www.vsixhub.com/) credit: [VSCode extensions you need to know for python programming](https://www.youtube.com/watch?v=SxzzFwzPYqo). Some extensions are need to be downloaded manually and installed without inxternet.

> **Python**

`Python`: A Visual Studio Code extension with rich support for the Python language (for all actively supported versions of the language: >=3.7), including features such as IntelliSense (Pylance), linting, debugging, code navigation, code formatting, refactoring, variable explorer, test explorer, and more! [link](https://www.vsixhub.com/vsix/116173/)

`Pylance`:  Pylance has the ability to supercharge your Python IntelliSense experience with rich type information, helping you write better code faster. [link](https://www.vsixhub.com/vsix/116403/) I don't kkkow

`Pylint`:  Pylint is a static code analyser for Python. It analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored. [link](https://www.vsixhub.com/vsix/112166/)

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

> **Experiences**

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

> **Extra**

`SQL Formatter`: Format SQL files using the sql-formatter-plus npm package. [link](https://www.vsixhub.com/vsix/5708/)

`Inline SQL`: Highlight and lint inline SQL strings. [link](https://www.vsixhub.com/vsix/76198/)

`Markdown Preview Enhanced`: Provides you with many useful functionalities such as automatic scroll sync, math typesetting, mermaid, PlantUML, pandoc, PDF export, code chunk, presentation writer, etc .[link](https://www.vsixhub.com/vsix/1953/)'

`markdownlint`:  Includes a library of rules to encourage standards and consistency for Markdown files. It is powered by the markdownlint library for Node.js (which was inspired by markdownlint for Ruby). Linting is performed by the markdownlint-cli2 engine. [link](https://www.vsixhub.com/vsix/1940/)