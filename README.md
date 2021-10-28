# reg-main

## Requisiti
- python 3.10
- librerie da installare:
	* termcolor					#libreria usata per dare magiore visiblita al venditore con il prezzo piu basso

## Database

Questo programma parte dal presuposto che il database venga gia fornito con le seguenti strutture:
1. tabella stocks:
    - vendor text PRIMARY KEY 	# indica il nome del fornitore 
    - item text NOT NULL      	# indica il nome del oggetto
    - time int NOT NULL			# indica il tempo di spedizione impiegato dal fornitore
    - qty int NOT NULL			# indica la quantita dell'oggetto 
    - price real NOT NULL			# indica il prezzo per pezzo

2. tabella discount:
	- vendor text NOT NULL		# indica il nome del fornitore
	- price real					# indica il prezzo totale da raggiungere o superare per avere lo sconto 
	- pice_1 int					# indica il numero di pezzi da raggiungere  o superare per ottenere lo sconto
	- pice_2 int					
	- month int					# indica un eventuale sconto applicato all'ordine se fatto in quel mese
	- discount_1 int				# indica lo sconto da applicare per price,pice_1 e month
	- discount_2 int				# indica lo sconto da applicare per pice_2

la tabella discount va popolota seguendo questo ragionamento lo sconto per i pezzi puo essere applicato per un range che va da pice_1 a pice_2 ,
se il campo pice_2 e vuoto allora diventa un maggiore o ugale di pice_1

3. tabella ordini:
	- vendor text NOT NULL
	- item text NOT NULL
	- time int NOT NULL
	- qty int NOT NULL
	- tot_price real NOT NULL		# indica il prezzo totale speso per questo ordine

## Programma

* Il programma è composto da:
	- aggiungi.py
	- crea_db.py
	- crea.py
	- main.py
	- sconti.py
	- test_reg.py

il programma puo partire con un db creato con i dati dal esempio 
da un db fornito 
basta che sia nominato database.db e messo nella stessa directory


per creare il db basta far partire 

>python3 crea_db.py

che provedera alla creazione e popolazione delle tabelle
dopodiche bastera far partire 

>python3 main.py

esempio di esecuzione

>Prodotto: Philips monitor 17       
>Quantita?: 12


- Numero selezione 1 
	* Venditore: Supplier_2 
	* Oggetto: Philips monitor 17 
	* Tempi di spedizione: 7.0 
	* Quantità: 15.0 
	* Prezzo totale 1459.2

- Numero selezione 2
	* Venditore: Supplier_3
	* Oggetto: Philips monitor 17
	* Tempi di spedizione: 4.0
	* Quantità: 23.0
	* Prezzo totale 1470.6

>Quale scegli? 1

- Selezionato
	* Venditore: Supplier_2
	* Oggetto: Philips monitor 17
	* Tempi di spedizione: 7.0
	* Quantità: 12
	* Prezzo totale 1459.2

### Descrizone dei file
crea.py 

> contiene i metodi per la creazione delle tabelle 

aggiungi.py 

> contiene i metodi per la popolazione delle tabelle

sconti.py 

> contiene i metodi per applicare gli sconti dalla tabella discount

test_reg.py 

> contiene gli esempi dell'esercizio gia come input per dar modo di verificare l'esercizio svolto 
