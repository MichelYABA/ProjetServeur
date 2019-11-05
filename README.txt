Auteur : YABA BILONGO Michel Davel

Date : 09/06/18

Fonctionnalités : 
	- chargement d’un fichier csv depuis le téléphone
	- Envoie du fichier chargé vers le serveur
	- Extraction des données du fichier csv
	- Enregistrement des données extraites dans une base de données

Logiciels de développement nécessaires :
	- Android Studio 3.0 (Pour développer l'application Android)
	- XAMPP (utilisé pour servir d'hébergeur local et par conséquent pour stocker les informations dans  une base de données)
	- Sublim Text 3 (Pour écrire notre programme de développement du serveur) 

Utilisation :
	1 - Tout d'abord choisir un ordinateur qui va servir à faire fonctionner l'API
	2 - Après avoir choisi l'ordinateur, on installe d'abord XAMPP qui contient le module MySQL nous permettant de stocker nos données
	  - Le téléchargement de XAMPP se fait sur ce site (choisir en fonction de son OS)
		https://www.apachefriends.org/fr/download.html
	4 - L'installation de XAMPP effectuée. On lance l'interface graphique de notre base de données (PHPMYADMIN) en tapant depuis la barre 		d'adresse  de notre navigateur : 
				"http://localhost/phpmyadmin/" ou "http://localhost/phpmyadmin/:80" pour préciser le port
	  - Lors de l'installation de XAMPP laisser les paramètres par défaut. Le serveur de base de donnée a pour administrateur "root" et 		n'a pas de mot de passe
	5 - il faut à présent importer le fichier sql "axelife.sql" depuis l'interface PHPMYADMIN situé dans le repertoire BaseDeDonnée
	6 - Ensuite, on installe les librairies nécessaires au fonctionnement du Serveur.
	  - Il faut se rassurer que Python est installé dans son OS. Si ce n'est pas le cas, l'installer. 
	  - Dans le cadre de ce projet, on a travaillé avec Python 3.6. Il en va de même pour pip; en fonction de son OS l'installer.
	7 - Peu importe le système d'exploitation, pour installer les librairies, on tape dans l'invite de commande :
		* pip install Flask
		* pip install werkzeug.utils
		* pip install flask-mysql 
		* pip install mysql-connector-python
	8 - Une fois toutes ces librairies installées, Depuis l'invite de commande de son OS, on se place dans le dossier où se trouve le 	  programme Serveur
	9 - Pour lancer le serveur, toujours depuis notre invite de commande et dans le repertoire où se trouve le programme Serveur, on tape   	la commande :
		python Serveur.py
	  - Serveur.py c'est le nom de notre programme API REST
	  - Si l'exécution s'est bien effectué, on va lire sur l'invite de commande un message :
		"running on http://0.0.0.0:5000/
	  - Si ce n'est pas le cas, vérifier si XAMPP a été démarré au préalable. Sur LINUX on tape la commande "sudo lampp start" pour lancer 		  XAMPP et tous ses modules. Sur Windows on double-clique tout simplement l'icone correspondant au XAMPP pour le démarrer
	  - A présent l'API REST est prêt à exécuter les requêtes provenant du client
	10 - Pour envoyer les requètes depuis un téléphone Androidn en recupère l'apk
	   - l'apk se trouve dans le dossier "client rest" sous le nom "apk-debug.apk"
	   - On copie l'apk dans son téléphone puis on l'installe
	11 - Pour modifier l'url de l'API REST, le code source du projet Android contenu dans le dossier "client rest"
	   - On ouvre le projet Android depuis Android Studio, si ce n'est déjà installé le télécharger puis l'installer de préférence la 		     version 3.0
	   - On modifie l'url du serveur à partir du fichier "app.js" situé dans le repertoire "Assets" depuis Android Studio
	   - Cette url correspond à l'adresse IP de la machine sur laquelle fonctionne notre API REST dans un réseau local.
	   - Pour vérifier l'adresse IP de la machine, taper depuis l'invite de commande :
		* ipconfig (sur Windows)
		* ifconfig (sur Linux et Mac OS)
	   - Dans le fichier "app.js", à la ligne : "http://0.0.0.0:5000/inputcsv", On remplace 0.0.0.0 par l'adresse ip de la machine où 			fonctionne l'API dans un réseau local
		Par exemple : "http://192.168.0.4:5000/inputcsv"
	12 - On génère l'APK depuis Android Studio en suivant les étapes suivantes :
		* Build
		* Build APK(s)
	13 - Pour récupérer l'APK généré, on suit le chemin suivant : 
		"C:\Users\Axelife\AndroidStudioProjects\WebApplication\app\build\outputs\apk\debug\"
	14 - l'apk est généré sous le nom "apk-debug.apk". C'est un apk non signé
	15 - Depuis l'application Android,
	   	* On appuie sur le bouton "choisir un fichier" qui ouvre l'explorateur de fichier
		* Se diriger dans le dossier où se trouve le fichier à envoyer au serveur
		* Après avoir choisi le fichier, en l'envoie au serveur en appuyant sur le bouton "Envoyer"

Informations complémentaires :
	Un autre moyen d'envoyer les fichiers csv au Serveur c'est de passer par le client web.
	Ce dernier se trouve dans le dossier Client_web qui se trouve dans le dossier "Client_rest"

Ressources :
	* Les fichiers à envoyer au serveur se trouvent dans le répertoire "Ressources"
	* il y'a deux fichiers :
		- ExemplePatientMedecinParam.csv
		- bioAlertExemple.csv
	* Copier ces fichiers dans son téléphone
	  
		

