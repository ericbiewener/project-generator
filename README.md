# Project Generator

Simple utility scripts for cloning and renaming directories and related file text.

## project_generator.py
Clones & renames all files and file text with the workd `__Base` and `__base` to a new name. Useful for maintaining directories than can serve as project templates.

Example usage:

```zsh
project_generator.py /Path/To/Template/Project MyNewProject
```

Example output:

```zsh
/Path/To/Template/Project/__baseApp.py > myNewProject.py
/Path/To/Template/Project/__BaseClass.py > MyNewProjectClass.py
```

```python
class __BaseClass:
  # ...

# becomes...

class MyNewProjectClass:
  # ...

```

## project_renamer.py
Clones & renames all files and file text with the provided `old_name` to the provided `new_name`. This script is destructive -- the old files/directories are destroyed.

Example usage:

```zsh
project_rename.py /Path/To/MyProject MyProject YourProject
```
