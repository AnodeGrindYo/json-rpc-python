import jsonrpclib

def test_validEmail(server_url, email):
    """
    Teste la méthode validEmail du serveur JSON-RPC.
    Args:
        server_url (str): URL du serveur JSON-RPC
        email (str): L'email à tester
    Returns:
        bool: Résultat de la validation de l'email
    """
    server = jsonrpclib.Server(server_url)
    response = server.validEmail(email)
    return response

def test_validZipCode(server_url, zip):
    """
    Teste la méthode validZipCode du serveur JSON-RPC.
    Args:
        server_url (str): URL du serveur JSON-RPC
        zip (str): Le code postal à tester
    Returns:
        dict: Résultat de la validation du code postal
    """
    server = jsonrpclib.Server(server_url)
    response = server.validZipCode(zip)
    return response

if __name__ == "__main__":
    """
    Ce code teste les méthodes validEmail et validZipCode du serveur JSON-RPC.
    Les résultats des tests sont imprimés sur la console.
    """
    server_url = "http://localhost:5001"
    email_test = "test@example.com"
    zip_test = "12345"
    
    email_result = test_validEmail(server_url, email_test)
    print(f"Email test result: {email_test} is {'valid' if email_result else 'invalid'}")

    zip_result = test_validZipCode(server_url, zip_test)
    print(f"Zip code test result: {zip_result['zip']} is {zip_result['result']}")
