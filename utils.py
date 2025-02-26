def dire_bonjour(nom, langue="fr"):
    """Retourne une phrase de bienvenue dans la langue choisie."""
    salutations = {
        "fr": "Bonjour",
        "en": "Hello",
        "es": "hola"
    }

    # Vérifier si la langue est supportée
    if langue not in salutations:
        return f"Langue non supportée : {langue}"

    return f"{salutations[langue]}, {nom} !"

