# Promille Rechner:
#
# Variabeln: A = alkmenge = Alkoholmenge in Gramm
#            C = blutalkkonzPro = Blutalkoholkonzentration in Promille
#            P = gewicht = Körpergewicht in Kg
# 
# Formel: A = C x P | C = A / P

#Texte:
    
einführung = """
    Heute schon wieder zu tief in's Glas geschaut?
    Kein Problem.
    Mit einigen Informationen von dir kann dieses
    Programm in kürzester Zeit deinen Blutalkohol
    berechen und wie lange es dauert, bis du das
    schwanken wieder los wirst.
    """
promille02 = """
    Bei Menschen, die sehr empfindlich gegenüber Alkohol
    sind oder den Konsum nicht gewohnt sind, tritt bereits
    eine enthemmende Wirkung ein. Die Redseligkeit steigt
    damit ebenfalls.
    
    - verlangsamte Reaktionen
    - verminderte Koordination von Bewegungen
    - weniger empfänglich für Kritik
    - erhöhte Risikobereitschaft
    - Distanzlosigkeit
    """
promille03 = """
    - erste Einschränkung des Sehfeldes
    - Probleme bei der Einschätzung von Entfernungen
    """
promille05 = """
    - deutliches Nachlassen der Reaktionsfähigkeit, insbesondere auf rote Signale (Rotlichtschwäche)
    - verminderte Konzentrationsfähigkeit
    - schlechteres Hörvermögen
    - erhöhte Reizbarkeit
    """
promille08 = """
    - erste Gleichgewichtsstörungen
    - eingeengtes Gesichtsfeld (Tunnelblick)
    - eingeschränkte Reaktionsfähigkeit
    - deutliche Enthemmung
    - Euphorie
    - verwaschene Sprache & Redseligkeit
    - Störungen beim Gehen
    """
promille10 = """
    - deutliche Sprachstörungen
    - Risikobereitschaft und Aggressivität steigen weiter
    """
promille15 = """
    - Realitätsverkennung
    - Stimmungsschwankungen
    - Schwere Koordinationsstörungen
    - Gleichgewichtsstörungen
    - Orientierungsstörungen
    - lallende Aussprache
    """
promille25 = """
    - Bewusstseinstrübungen
    - Lähmungserscheinungen
    - doppeltes Sehen
    - Ausschalten des Erinnerungsvermögens
    """
promille30 = """
    - starke Sedierung
    - Bewusstlosigkeit bis hin zu Koma
    - ab 3,5 Promille besteht die Gefahr einer Lähmung des Atemzentrums und somit Lebensgefahr
    """



print(einführung)

input("Bereit zum fortfahren? Drücke Enter.")

import time # Zeitverzögerung aktivieren
print("...")
time.sleep(1) # Zeitverzögerung für 2 Sekunden anwenden
print("...")
time.sleep(1)
print("...")
time.sleep(1)

print("Um Fortfahren zu können brauche ich einige Informationen von dir.")

# Variabeln definieren:

# Gewicht:  \033[91mXXXXXXXX\033[0m = Rot Färben 92m = Grün 93m = Gelb 94m = Blau
gewicht = float(input("gib dein \033[91mKörpergewicht\033[0m in Kilogramm an: "))
# Was wurde getrunken:
bier = float(input("Wie viele Gläser (250ml) \033[91mBier\033[0m hast du getrunken?: "))
wein = float(input("Wie viele Gläser (200ml) \033[91mWein\033[0m hast du getrunken?: "))
schnaps = float(input("Wie viele Gläser (4cl) \033[91mSchnaps\033[0m hast du getrunken?: "))

# Berechnungen:
# A = alkmenge = Alkoholmenge in Gramm

# alkmengeBier = 250ml * (5/100) * 0,8 = Reiner Alkohol in Gramm = 10 Gramm
alkmengeBier = bier*10
# alkmengeWein = 200ml * (11/100) * 0,8 = Reiner Alkohol in Gramm = 17,6 Gramm
alkmengeWein = wein*17.6
# alkmengeSchnaps = 40 * (40/100) * 0,8 = Reiner Alkohol in Gramm = 12,8 Gramm
alkmengeSchnaps = schnaps*12.8

# Gesamte Alkoholmenge in Gramm:
alkmenge = alkmengeBier+alkmengeWein+alkmengeSchnaps

# C = blutalkkonzPro = Blutalkoholkonzentration in Promille | C = A / P
blutalkkonzPro = alkmenge/gewicht

print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)

print("Meine berechnungen haben ergeben, dass du\033[91m",blutalkkonzPro,"\033[0m Promille hast")
print("___________________________________________________________________________________________")

if blutalkkonzPro == 0.0:
    print("Du bist nüchtern.")
elif blutalkkonzPro >=4.0:
    print("Du hast so viel getrunken, du müsstest Tot sein.")    
elif blutalkkonzPro >=3.5:
    print("Alkoholvergiftung, Lebensgefahr!")    
elif blutalkkonzPro >=3.0:
    print(promille30)
elif blutalkkonzPro >=2.5:
    print(promille25)
elif blutalkkonzPro >=1.5:
    print(promille15)
elif blutalkkonzPro >=1.0:
    print(promille10)
elif blutalkkonzPro >=0.8:
    print(promille08)
elif blutalkkonzPro >=0.5:
    print(promille05)
elif blutalkkonzPro >=0.3:
    print(promille03)
elif blutalkkonzPro >=0.2:
    print(promille02)
elif blutalkkonzPro >=0.1:
    print("Du bist quasi nüchtern")
    
print("Quelle: \033[94mwww.kenn-dein-limit.de\033[0m")
