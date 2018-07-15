## Python NMTP

## Useful links



* GitHub page : https://github.com/nicolovalle/python_nmtp

* Altri link utili:
  * www.google.com
  * http://young.physics.ucsc.edu/jackboot.pdf (jacknife e bootstrap)
  * http://www.helsinki.fi/~rummukai/simu/fss.pdf (Binder cumulants for Ising)




## Git commands

* Cloning the repository (verrà creata la directory _pytoh_nmtp_ nella directory in cui esegui il programma)

```sh
git clone https://github.com/nicolovalle/python_nmtp
```


* Setting up your credentials (da eseguire in _python_nmtp_):
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


1. Add, commit, pull, push
```sh
git add miofile.py
git commit -m "Adding miofile"
git pull --rebase
git push -u origin master
```

2. Oppure... lo script _upload.sh_ da eseguire con
```sh
./upload.sh miofile.py "Adding_miofile"
```
che esegue tutti i comandi del punto 1. Verranno chieste le credenziali di accesso a GitHub.