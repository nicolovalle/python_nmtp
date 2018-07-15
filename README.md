## Python NMTP

## Useful links



* GitHub page : https://github.com/nicolovalle/python_nmtp

* Altri link utili:
  * www.google.com
  * http://young.physics.ucsc.edu/jackboot.pdf (jacknife e bootstrap)
  * http://www.helsinki.fi/~rummukai/simu/fss.pdf (Binder cumulants for Ising)




## Git commands

* Cloning the repository

```sh
git clone https://github.com/nicolovalle/python_nmtp
```
verrà creata la directory **pythn_nmtp** nella directory in cui esegui il programma.

* Setting up your credentials
```sh
git config --global user.name "Name Surname"
git config --global user.email "name.surname@cern.ch"
```





* Checking the status of your repository
```sh
git status
```


* To get the latest changes (update the repository)
```sh
git pull --rebase
```




## Committing (basic workflow)


3. Add, commit, pull, push
```sh
git add miofile.py
git commit -m "Adding miofile"
git pull --rebase
git push -u origin master
```

