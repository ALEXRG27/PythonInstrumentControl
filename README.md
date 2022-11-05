# PythonInstrumentControl
Functions to control laboratory intruments, like Power supplies, multimeters Signal Waveform generators...
<!-- TOC -->

- [Tools Installation](#tools-installation)
    - [VS Code Coding Pack for Python all-in-one](#vs-code-coding-pack-for-python-all-in-one)
    - [Python and VS Code separated installation](#python-and-vs-code-separated-installation)
        - [Python](#python)
        - [Visual Studio Code (Optional)](#visual-studio-code-optional)
    - [Visual Studio Code additional extensions](#visual-studio-code-additional-extensions)
    - [Git](#git)
        - [Tortoise Git](#tortoise-git)
- [Test Automation Project Installation](#emkeyfob-ui-project-installation)
    - [Cloning git repository](#cloning-git-repository)
    - [Checkout dev branch, which contains the last version of development](#checkout-dev-branch-which-contains-the-last-version-of-development)
    - [Setup Python for the project](#setup-python-for-the-project)
- [Running GUI](#running-gui)
- [Create your own custom UI](#create-your-own-custom-ui)
    - [Create UI with Qt Designer](#create-ui-with-qt-designer)
    - [Generate UI python code using Handler Generator](#generate-ui-python-code-using-handler-generator)
    - [Add UI in config file](#add-ui-in-config-file)
    - [Implementing and testing your code](#implementing-and-testing-your-code)
- [Python API interface](#python-api-interface)
    - [Read & Write memory](#read--write-memory)
    - [Cached mode](#cached-mode)
- [JTAG low level access](#jtag-low-level-access)
    - [Code samples](#code-samples)
- [Creating your own application with custom configuration](#creating-your-own-application-with-custom-configuration)
- [Create release using installer](#create-release-using-installer)

<!-- /TOC -->

<!-- title -->
 <font size="6"> INBRAIN Test Automation</font>

<!-- # Introduction
To be completed... -->

# Tools Installation

Python and Git are necessary for using the developement repository. An IDE  is also necessary for coding in Python.

## VS Code Coding Pack for Python all-in-one

Visual Studio code, Python and all required extensions and libraries can be installed at once with [Coding Pack for Python](https://code.visualstudio.com/learntocode)

## Python and VS Code separated installation

If you already have Python, VS Code, or your want to use another IDE, you can follow this chapter to install only what you need.

### Python

Python 64 bits 3.11 . You can install
the latest Python 3 release from [here](https://www.python.org/downloads/)
Don't forget to setup environment variables

### Visual Studio Code (Optional)

Although it is not mandatory, it is highly recommended to install [Visual Studio Code](https://code.visualstudio.com/) 

Once installed, add the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
extension.

## Visual Studio Code additional extensions

For more confort, you can also install these extensions in Visual Studio Code:

[Align by RegEx](https://marketplace.visualstudio.com/items?itemName=janjoerke.align-by-regex)<br>
Aligns selected lines of text by a regular expression.

[Bracket Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)<br>
A customizable extension for colorizing matching brackets

## Git

Download [Git](https://git-scm.com/downloads) and install it on your system.

### Tortoise Git

You can optionnaly also install [Tortoise Git](https://tortoisegit.org/download/) which is the equivalent of Tortoise SVN vof Git.

# TestAutomation Project Installation

[Git](https://git-scm.com/downloads) is required to retrieve the project.

## Cloning git repository

!!! warning
    If git is not installed on your system, you need to install it first

Create a dedicated folder for cloning the project inside, example ```TestAutomation```.

Open a terminal in the new folder created, you can use VS code integrated terminal, git bash, powershell or your prefered one.

Then clone the resository with this command, where `TestAutomation` is the folder
where you want to clone the repository:

```bash
    git clone http..
```

## Checkout dev branch, which contains the last version of development
```bash
    git checkout dev
```

Alternatively you can switch to a specific version using tags:
```bash
    git checkout tags/v...
```

## Setup Python for the project

```
python -m venv pyenv 
```
```
pyenv\Scripts\activate.ps1
```

From this point you are working into the virtual environment.

!!! warning
    Ensure that you are always inside the virtual environment before
    using `python`, `pip` or running code

You can deactivate the environment with the command:

```bash
    (pyenv) TestAutomation> deactivate
```
