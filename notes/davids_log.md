# 11/19/20

Python's import system is dumb.
I converted the project over to a package to improve import functionality.
(Packages allow for sub-packages, which improves the folder structure)
Although, I'm not even sure if that was necessary.
It's good to make your projects packages anyways, because packages come with added functionality.
Pretty much all important python projects end up as packages before they are distributed.
Whatever.

To make pylint happy, you have to install the package: (your cwd needs to be the RoboMaze folder)
```
python3 -m pip install -e robomaze
```

The -e flag installs the package in developer mode. This way, you can make changes to the package without having to reinstall it. (This is obviously what we want, since we're changing it a bunch while coding...)

Also, to run the project (package), just use this command in the RoboMaze folder:
```
python3 robomaze
```
