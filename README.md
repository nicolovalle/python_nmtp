## Python NMTP

### About Bootstrap...

:+1:
> L'aumento della varianza extracampione si compensa con la diminuzione della varianza intracampione...

> Non funziona per una certa classe di problemi: casi limite, estremi, disuguaglianze in generale...


## Useful links



* GitHub page : https://github.com/nicolovalle/python_nmtp

* Altri link utili:
  * https://github.com/prtkm/ising-monte-carlo/blob/master/ising-monte-carlo.org (Ising with Python)
  * http://young.physics.ucsc.edu/jackboot.pdf (jacknife e bootstrap)
  * http://www.helsinki.fi/~rummukai/simu/fss.pdf (Binder cumulants for Ising)
  * https://arxiv.org/pdf/cond-mat/0701515.pdf (Un articolo che fa la simulazione)




## Git commands

* Cloning the repository (verrà creata la directory _pytoh_nmtp_ nella directory in cui esegui il programma)

```sh
git clone https://github.com/nicolovalle/python_nmtp
```


* Setting up your credentials (da eseguire in _python_nmtp_):
```sh
git config user.name "Name Surname"
git config user.email "name.surname@cern.ch"
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

2. Oppure usare lo script _upload.sh_ da eseguire con
```sh
./upload.sh miofile.py "Adding_miofile"
```
oppure
```sh
./upload.sh miofile.py
```
che esegue tutti i comandi del punto 1. Verranno chieste le credenziali di accesso a GitHub. (_La nota tra virgolette non è necessaria: se usata, deve essere una sola parola..._)

3. To create and upload folders, it is necessary that they are not empty.
```sh
./upload.sh nuovadirectory ["Comment..."]
```
