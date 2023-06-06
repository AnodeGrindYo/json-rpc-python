# JSON-RPC avec Python

## Qu'est-ce que JSON-RPC ?

JSON-RPC est un protocole de type RPC (Remote Procedure Call) qui utilise JSON pour encoder ses données. Il permet l'appel de méthodes à distance en encapsulant les données dans une structure JSON. JSON-RPC peut être utilisé avec pratiquement tous les réseaux de transport qui permettent de transmettre du texte. Il est léger et facile à mettre en œuvre.

Le protocole est très similaire à XML-RPC, mais contrairement à XML, JSON est typé. De plus, JSON utilise moins de balisage que XML, ce qui le rend plus léger et plus rapide à parser.

## Exemple de serveur JSON-RPC en Python

Dans le premier fichier Python (server.py), j'ai créé un serveur JSON-RPC simple avec deux méthodes : validEmail et validZipCode.

```python
from jsonrpcserver import Success, method, serve, InvalidParams, Result, Error
import re

@method
def validEmail(email) -> Result:    
    """
    Cette méthode valide un email en utilisant une expression régulière. 
    Elle renvoie une erreur si l'email est vide et un résultat de succès avec True ou False en fonction de la validation.
    """
    if email == "":
        return Error(code=123, message="Empty email provided")
    if re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", email):    
        return Success(True)
    else:
        return Success(False)

@method
def validZipCode(zip) -> Result: 
    """
    Cette méthode valide un code postal en utilisant une expression régulière.
    Elle renvoie une erreur si le code postal est vide et un résultat de succès avec un dictionnaire indiquant la validité.
    """
    if zip == "":
        return InvalidParams("Null value")
    if re.match("^[0-9]{5}(?:-[0-9]{4})?$", zip):
        result = { "zip": zip, "result" : "Valid Zipcode" }
    else:
        result = { "zip": zip, "result" : "Invalid Zipcode" }
    return Success(result)

if __name__ == "__main__":
    """
    Cette partie du code est exécutée lorsque le script est lancé directement.
    Il instancie et démarre un serveur JSON-RPC sur l'adresse 'localhost' et le port 5001.
    """
    serve('localhost', 5001)
```

## Exemple de client JSON-RPC en Python

Dans le second fichier Python (test_server.py), j'ai créé un client simple qui envoie des requêtes JSON-RPC pour tester les méthodes du serveur.

```python
import jsonrpclib

def test_validEmail(server_url, email):
    """
    Teste la méthode validEmail du serveur JSON-RPC.
    """
    server = jsonrpclib.Server(server_url)
    response = server.validEmail(email)
    return response

def test_validZipCode(server_url, zip):
    """
    Teste la méthode validZipCode du serveur JSON-RPC.
    """
    server = jsonrpclib.Server(server_url)
    response = server.validZipCode(zip)
    return response

if __name__ == "__main__":
    """
    Ce code teste les méthodes validEmail et validZipCode du serveur JSON-RPC.
    Les résultats des tests sont imprimés sur la console.
    """
```

## Ressources supplémentaires

Pour plus d'informations sur JSON-RPC, veuillez consulter les spécifications officielles :

- [Spécifications JSON-RPC 2.0](https://www.jsonrpc.org/specification)
