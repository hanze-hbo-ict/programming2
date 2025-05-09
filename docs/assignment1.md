# Assignment 1: Static code analysis

During the plenary part, we discussed the necessity of static code analysis. We looked at the ontology of Python-applications, going from functions to classes to modules to systems. We also had a look at more high-level descriptions of code, using [the c4-model](https://c4model.com/) to describe any software system.

For this assignment, you are required to write a small report of your findings on one of [the code bases listed below](#the-list). This report should be written in a file `report.md` in the corresponding directory (i.e. `assigment1/`). If you want to include images (which should be considered good practice), please put them in the directory `assignment1/imgs`. We suggest [plantuml](https://plantuml.com/) to create technical images.

## Report

Start your analysis with a short discription of the code-base: what it does, its intended use-case and public (basically a summary of the project's `readme`-file). Also give a description of its status on github (number of PR's, issues, pulse etc.). After that, give a high-level overview of the code-base: how is the code organized, what is the architectural setup, dependencies, build strategies etc. Images such as class- or sequence-diagrams are helpful at this level.

Next, give a *short quantitative description* of the code-base: how many LoC, how many functions/methods/classes, how many modules/packages/namespaces, etc.

After this overview, you should look in some more depth to your code-base. You can make use of one of the technical tools [that are suggested on c4model.com/tooling](https://c4model.com/tooling). Also, run at least one static analysis tool (e.g. `pylint`, `flake8`, `sonarqube`, `bandit`, `cloc`, or a language-specific alternative). Give attention to at least the following items:

- Complexity metrics for each function/method
- Code smells
- Dead code, unused imports
- Security issues (if any)

Conclude with a reflection about the project: what do you think of it, where do you see refactoring candidates and what would your advice be to the ones that made the it.

## The list

Here is the list of projects that you can choose from. If you have another project you would like to analyse, please discuss this with the teacher.

Name | Language(s) | Short desciption | url
---|---|---|---
tldr-pages | Node/Python (and a lot of markdown) | Community driven collection of man-page alternatives | https://github.com/tldr-pages/tldr
httpie | Python | CLI: human-friendly HTTP client for the API era | https://github.com/httpie/cli
glances | Python | Open-source system cross-platform monitoring tool | https://github.com/nicolargo/glances
poetry | Python | Basically a dependency manager manager | https://github.com/python-poetry/poetry
jq | C | Lightweight and flexible command-line JSON processor | https://github.com/stedolan/jq
micromark | JavaScript | Yet another markdown parser | https://github.com/micromark/micromark
fizzbuzz-enterprise-edition | Java | Example (parodie) of over-engineered enterprise code | https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition
thefuck | Python | Tool to corrects errors in previous console commands | https://github.com/nvbn/thefuck
jsonlint | JavaScript | Yet another json-linter | https://github.com/zaach/jsonlint
htop | C | Cross-platform interactive process viewer | https://github.com/htop-dev/htop





