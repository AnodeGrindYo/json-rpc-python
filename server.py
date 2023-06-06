from jsonrpcserver import Success, method, serve, InvalidParams, Result, Error
import re


@method
def validEmail(email) -> Result:
    """
    Cette méthode valide un email en utilisant une expression régulière. 
    Elle renvoie une erreur si l'email est vide et un résultat de succès avec True ou False en fonction de la validation.
    Args:
        email (str): L'email à valider
    Returns:
        Result: Résultat de la validation de l'email
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
    Args:
        zip (str): Le code postal à valider
    Returns:
        Result: Résultat de la validation du code postal
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