# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash,  redirect, url_for, session
import hashlib, uuid, os
from werkzeug.utils import secure_filename
import csv

import mysql.connector as MS
connection = MS.connect(user='root', password='', host='127.0.0.1', buffered=True)
cursor = connection.cursor()

utiliser_bd = "USE axelife2"
cursor.execute(utiliser_bd)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def enregistrer_medecin():
	if request.method == "GET":
		return render_template("enregistrer_medecin.html")
	
	if request.method == "POST":
		"""Informations Client"""
		id_medecin = 20
		prenom = request.form["prenom"]
		nom = request.form["nom"]
		e_mail = request.form["mail"]
		telephone= request.form["telephone"]

		req_enregister_medecin = "INSERT INTO Medecin (Nom, Prenom, Mail, Telephone) VALUES(%s,%s,%s,%s)"
		cursor.execute(req_enregister_medecin, (nom, prenom, e_mail, telephone))
		connection.commit()
		return "enregistrement effectue"
		#return redirect(url_for('infos'))

@app.route('/inputcsv', methods=['POST'])
def csvtraitement():
	# On crée des variables globales associées aux données qui seront extraites du fichier csv
	global Id, Nom, Prenom, Age, Poids, Taille, sexe, Mail, TelM, Numero
	
	# On récupère le fichier envoyé
	f = request.files['InputCSV']
	
	# On sauvegarde le fichier envoyé puis on le renomme
	f.save('csvfile.csv')

	# On ferme le fichier après sauvegarde
	f.close()
	
	#On crée et on inialise une liste dans laquelle seront ajoutée les données
	list1=[]
	list2=[]
	
	GrandeListe=[]			
	# récupération et lecture du fichier sauvegardé
	with open('csvfile.csv', 'r') as csvfile:
		#dialect=csv.Sniffer().sniff(csvfile.read(1024))
		#csvfile.seek(0)
		#reader = csv.reader(myFile, dialect)
		#on stocke le contenu du fichier dans la variable "reader" en précisant la manière dont les lignes sont délimitées
		reader = csv.reader(csvfile)

		#on parcourt le fichier csv puis on récupère les informations ligne par ligne
		for row in reader:          
			if row[0] == "Nom":
				Nom = row[1]
				list1.append(Nom)
			elif row[0] == "Prenom":
				Prenom = row[1]
				list1.append(Prenom)
			elif row[0] == "Prénom":
				Prenom = row[1]
				list1.append(Prenom)
			elif row[0] == "Age":
				Age = row[1]
				list1.append(Age)
			elif row[0] == "Poids":
				Poids = row [1]
				list1.append(Poids)
			elif row[0] == "Taille":
				Taille = row[1]
				list1.append(Taille)
			elif row[0] == "Sexe":
				Sexe = row[1]
				list1.append(Sexe)
			elif row[0] == "Mail":
				Mail = row[1]
				list1.append(Mail)
			elif row[0] == "Numéro de téléphone":
				Numero = row[1]
				list1.append(Numero)
			elif row[0] == "Numéro":
				TelM = row[1]
				list1.append(TelM)				
			elif row[0] == "N°id":
				Id = row[1]
				list1.append(Id)
			elif row[0] == "\ufeffDonnées utilisateur:":
				list2.append(row[1])
			elif row[0] == "Contact d'urgence:":
				list2.append(row[1])
			elif row[0] == "Données médecin:":
				list2.append(row[1])
			elif row[0] == "Pression systolique périphérique":
				list2.append(row[1])
			elif row[0] == "Pression diastolique périphérique":
				list2.append(row[1])
			elif row[0] =="":
				list2.append(row[1])
			else :
				liste=[]
				#reader_2 = csv.reader(csvfile)
				reader = csv.reader(csvfile, delimiter=';')
				for row in reader :
					for i in range(len(row)):
						liste=[i for i in row]						
						
					GrandeListe.append(liste)
				#GrandeListe.append(row[0])
					
					
					
	print(len(list1))
	print(list1)
	print(len(list2))
	print(list2)
	print(len(GrandeListe))
	
	for i in range(1,len(GrandeListe)) :
		liste=GrandeListe[i]
		print(liste)
	
	if (len(list1) != 0):
		# On enregistre les données dans table "users" des utilisateurs 
		req_enregister_users = "INSERT INTO users (ID, NOM, PRENOM, AGE, POIDS, TAILLE, SEXE) VALUES(%s,%s,%s,%s,%s,%s,%s)"
		cursor.execute(req_enregister_users, (list1[6], list1[0], list1[1], list1[2], list1[3], list1[4], list1[5]))
		connection.commit()

		# On enregistre les données dans table "Medecin" des médecins 
		req_enregister_medecin = "INSERT INTO Medecin (Nom, Prenom, Mail, Telephone, ID_USERS) VALUES(%s,%s,%s,%s,%s)"
		cursor.execute(req_enregister_medecin, (list1[11], list1[12], list1[13], list1[14], list1[6]))
		connection.commit()
	
	if (len(GrandeListe) != 0):
		# On enregistre les données dans table "users" des utilisateurs 
		req_enregister_datas = (  # Requête pour créer la table user_data
			"INSERT INTO user_data ("
			"Dates,"
			"Horaire,"
			"bpm,"
			"csp,"
			"cdp,"
			"psp,"
			"pdp,"
			"si,"
			"oxymetrie,"
			"temp,"
			"Alert_PSP,"
			"Alert_BPM,"
			"Alert_CSP,"
			"Alert_PDP,"
			"Alert_SI,"
			"Alert_Oxy,"
			"Alert_Temp,"
			"LimitBasse_BPM,"
			"LimitHaute_BPM,"
			"LimitBasse_CSP,"
			"LimitHaute_CSP,"
			"LimitBasse_CDP,"
			"LimitHaute_CDP,"
			"LimitBasse_PSP,"
			"LimitHaute_PSP,"
			"LimitBasse_PDP,"
			"LimitHaute_PDP,"
			"LimitBasse_SI,"
			"LimitHaute_SI,"
			"LimitBasse_Oxy,"
			"LimitHaute_Oxy,"
			"LimitBasse_Temp,"
			"LimitHaute_Temp,"
			"Latitude,"
			"Longitude,"
			"City"
			")"
			"VALUES ("
			"%(Date)s,%(heure)s,%(bpm)s,%(csp)s,%(cdp)s, %(psp)s,%(pdp)s,%(si)s,%(oxymetrie)s, %(temp)s, %(alert_psp)s,"
			"%(alert_bpm)s,%(alert_csp)s,%(alert_pdp)s,%(alert_si)s, %(alert_oxy)s,%(alert_temp)s,%(basse_bpm)s,"
			"%(haute_bpm)s,%(basse_csp)s, %(haute_csp)s,%(basse_cdp)s,%(haute_cdp)s,%(basse_psp)s,%(haute_psp)s,"
			"%(basse_pdp)s,%(haute_pdp)s,%(basse_si)s,%(haute_si)s,%(basse_oxy)s,%(haute_oxy)s,%(basse_temp)s,%(haute_temp)s,"
			"%(latitude)s,%(longitude)s,%(city)s"
			")")
		
		for i in range(1,len(GrandeListe)) :
			#print(liste[0])
			liste=GrandeListe[i]
			data_user_data = {# dictionnaire de paramètre qui implémente les variables de la requête SQL contenu dans VALUES()
				'Date': liste[0],
				'heure':liste[1],
				'bpm': liste[2],
				'csp': liste[3],
				'cdp': liste[4],
				'psp': liste[5],
				'pdp': liste[6],
				'si': liste[7],
				'csp': liste[8],
				'oxymetrie': liste[9],
				'temp': liste[10],
				'alert_psp': liste[11],
				'alert_bpm': liste[12],
				'alert_csp': liste[13],
				'alert_pdp': liste[14],
				'alert_si': liste[15],
				'alert_oxy': liste[16],
				'alert_temp': liste[17],
				'basse_bpm': liste[18],
				'haute_bpm': liste[19],
				'basse_csp': liste[20],
				'haute_csp': liste[21],
				'basse_cdp': liste[22],
				'haute_cdp': liste[23],
				'basse_psp': liste[24],
				'haute_psp': liste[25],
				'basse_pdp': liste[26],
				'haute_pdp': liste[27],
				'basse_si': liste[28],
				'haute_si': liste[29],
				'basse_oxy': liste[30],
				'haute_oxy': liste[31],
				'basse_temp': liste[32],
				'haute_temp': liste[33],
				'latitude': liste[34],
				'longitude': liste[35],
				'city': liste[36],
			}
			cursor.execute(req_enregister_datas, data_user_data)
			connection.commit()
			
				#connection.commit()
	
			#print(liste[0])		

	return "enregistrement effectué"

if __name__ == '__main__':	
	#app.run(debug=True)
	app.run(host='0.0.0.0', port='5000')
