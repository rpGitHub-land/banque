import mysql.connector 
import csv

conn = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "banque")
cursor = conn.cursor()


cursor.execute("CREATE TABLE `client` (id_Client INT PRIMARY KEY NOT NULL AUTO_INCREMENT , nom_Client VARCHAR(50), tel_client VARCHAR(50),")
cursor.execute("CREATE TABLE `compte` (id_Compte INT PRIMARY KEY NOT NULL AUTO_INCREMENT, argent_Compte INT, id_Client INT FOREIGN KEY NOT NULL AUTO_INCREMENT, id_Banque INT FOREIGN KEY NOT NULL AUTO_INCREMENT")
cursor.execute("CREATE TABLE `banque` (id_Banque INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nom_Banque VARCHAR(50), adresse_Banque VARCHAR(50)")



ref = (0, row[0], row[3], row[4],row[5], row[7], y, x)
	cursor.execute("INSERT INTO attaques (id_attaque, nom_attaque, puissance_attaque, prec_attaque, pp_attaque, descrip_attaque, id_cat, id_type ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",ref)

class banque:
	def __init__(self,id_Banque, nom_Banque, adresse_Banque):
		ref = (0,nom_Banque,adresse_Banque)
		cursor.execute("INSERT INTO banque (id_Banque,nom_Banque,adresse_Banque) VALUE (%s,%s,%s)" ,ref)

class compte:
	def __init__(self,id_banque, id_Compte,id_client, argent_Compte):
		ref = (0,id_Banque,id_client,argent_Compte)
		cursor.execute("INSERT INTO compte (id_Compte,id_Banque,id_client,argent_Compte) VALUE (%s,%s,%s,%s)" ,ref)

	def versement(id_Compte1,id_Compte2,somme):

		cursor.execute("SELECT argent_Compte WHERE id_Compte = id_Compte1")
		newmontant1 = cursor.fetchone() - somme 
		cursor.execute("SELECT argent_Compte WHERE id_Compte = id_Compte2")
		newmontant2 =  cursor.fetchone() + somme 

		ref1 = (newmontant1 ,id_Compte1,)
		ref2 = (newmontant2 ,id_compte2)
		cursor.execute("UPDATE compte SET argent_Compte = (%s) WHERE id_Compte = (%s) ",ref1)
		cursor.execute("UPDATE compte SET argent_Compte = (%s) WHERE id_Compte = (%s) ",ref2)

	def deposerArgent(id_Compte,somme):
		cursor.execute("SELECT argent_Compte WHERE id_Compte = id_Compte")
		newmontant = cursor.fetchone() + somme
		ref = (newmontant ,id_compte)
		cursor.execute("UPDATE compte SET argent_Compte = (%s) WHERE id_Compte = (%s) ",ref)

	def retirerArgent(id_Compte,somme):
		cursor.execute("SELECT argent_Compte WHERE id_Compte = id_Compte")
		newmontant = cursor.fetchone() - somme
		ref = (newmontant ,id_compte)
		cursor.execute("UPDATE compte SET argent_Compte = (%s) WHERE id_Compte = (%s) ",ref)

	def ConsulterCompte(id_compte):
		cursor.execute("SELECT argent_Compte WHERE id_Compte = id_Compte")
		montant = cursor.fetchone()
		print ("montant actuel " , montant , "$")

	def fermerCompte(id_Compte):
		ref = (id_Compte)
		cursor.execute("DELETE FROM compte where id_Compte = (%s)",ref)

	
		





