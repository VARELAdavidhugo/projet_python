from utils import dire_bonjour

def main():
    """Demande un prénom et une langue, puis affiche un message de bienvenue."""
    nom = input("Entrez votre prénom : ")
    
    print("\nChoisissez une langue :")
    print("1 - Français 🇫🇷 (fr)")
    print("2 - Anglais 🇬🇧 (en)")
    print("3 - Espagnol 🇪🇸 (es)")
    
    choix = input("Entrez le code de la langue (fr/en/es) : ").strip().lower()

    print(dire_bonjour(nom, choix))

if __name__ == "__main__":
    main()
