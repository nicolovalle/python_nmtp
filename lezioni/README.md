ising_lezione.py genera 1000 configurazioni e calcola per ognuna di esse la magnetizzazione.

L'idea credo sia la seguente:

* Scrivo le n=1000 magnetizzazioni su un file
* Lo faccio per B valori di beta, intorno a quello critico.
* Fissato beta, medio su tuttle le 1000 configurazioni le quantità m^4 e m^2 (m=magnetizzazione=somma degli spin)
* Calcolo Ul=1-<m^4>/3<m^2>^2 (vedi slide 15 di http://www.helsinki.fi/~rummukai/simu/fss.pdf)
* Fatto questo per tutti i valori di beta, ho la curva di Ul in funzione di beta.

* Ripeto per un'altra dimensione del reticolo --> ottengo un'altra curva che interseca la precedente. Definisco la mia stima del beta critico come il punto di intersezione delle due curve.

* Ora si pone il problema di stimare l'errore su questa stima. Descrivo di seguito solo come stimare l'errore su Ul fissato beta (ovvero l'errore su un singolo punto di una delle due curve).

  * **Bootstrap**
	* Per Nb volte genero un campione di n=1000 magnetizzazioni estraendo a caso con reimmissione dalle n generate in precedenza.
	* Per ognuna di queste copie del campione calcolo Ul con lo stesso metodo.
	* No Nb valori di Ul: ne faccio istogramma, vedo come si distribuiscono e (sperando che il valore centrale sia quello calcolato all'inizio) e stimo l'errore

  * **Jacknife**
	* Per n volte genero un campione di n-1=999 magnetizzazioni ottenuto usando le n=1000 di partenza ed escludendone una.
	* Altri due punti come per bootstrap
	* Ripeto escludendo, al posto di un solo valore, 2, 3, 4 ecc... e vedo se cambia qualcosa.