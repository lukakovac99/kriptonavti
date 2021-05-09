# kriptonavti

2|Kriptonavti 

Kratek opis:
Naš prgram je spisan tako, da postavimo mrežo. Le-ta deluje na podlagi treh vrst uporabnikov. 
(NET - simulira večje število uporabnikov (potrjujejo transakcije), SHOP - določa ceno izdelkov in sprejema plačila, USER - kupuje izdelke in plačuje)

Postopek uporabe:
1.) Postavimo 3 uporabnike
2.) Poskeniramo izdelke, ki jih kupec hoče kupiti
3.) Zaključimo nakup
4.) Izberemo naslov trgovine kateri želimo nakazati sredstva
5.) Izvrši se prenos sredstev, potrdijo ga "minerji", katere simuliramo z NET

Namen:
Uporabiti Bitcoin SV blockchain v praktični uporabi.



--------------
Navodila za uporabo:

Zahteve: 
- python3.8.5
- subprocess
- numpy
- pyzbar
- playsound

Inicializacija:
(Ker je zmanjkalo časa za dokončno optimizacijo je treba zaenkrat določeni poti še ročno vnašati.)

- Preneseš 6 python datotek (oz. 2, če želiš postaviti samo enega uporabnika)

- V vsaki izmed datotek popravimo path na mapo kjer imamo datoteke #tukaj še nujna opcija optimizacije

- Možnost treh uporabnikov, ki jih trenutno lahko povežem na lokalno omrežje:

- NET (Miner, ki skrbi, da omrežje stoji):

 	-Odpremo terminal z dvema zavihkoma

	-V terminalu se premaknemo v mapo, kjer imamo python datoteke,

	-v terminalu poženemo kodo: 
		/bin/python3 /home/user/kriptonavti/createNET.py
		(gremo skozi korake inštalacije)

 	-v sosednjem zavihku zaženemo mine-anje z zagonom datoteke: 
		/bin/python3 /home/user/kriptonavti/NETnod.py

- SHOP(Prodjalec, ki ima trenutno zgolj dve funkciji: 1.Pregled stanja na računu, 2.Izpis lastnega addressa

	-Odpremo nov terminal z dvema zavihkoma
	
	-Povežemo se v omrežje z zagonom datoteke:
		bin/python3 /home/user/kriptonavti/createSHOP.py

	-Zaženemo še terminalni vmesnik v novem zavihku z zagonom datoteke:
		/bin/python3 /home/user/kriptonavti/SHOPnod.py

- USER(Uporabnik, ki vidi svoje stanje na računu in ima možnost skeniranja ter plačevanja izdelkov)

	-Odpremo nov terminal z dvema zavihkoma
	
	-V prvem se povežemo na mrežo z pogonom datoteke:
		v enega: /bin/python3 /home/user/kriptonavti/createUSER.py

	V drugem zavihku poženemo terminalni vmesnik z zagonom datoteke:
		v drugega: /bin/python3 /home/user/kriptonavti/USERnod.py


Opomba:
Mi smo sistem postavili na lokalnem bitcoinsv omrežju. Bi pa enak koncept lahko skalirali na testno ali pravo omrežje.
Le da v tem primeru, ne bi potrebovali večih terminalov, temveč bi bil vsak uporabnik svoja ločena naprava, povezana v omrežje.
