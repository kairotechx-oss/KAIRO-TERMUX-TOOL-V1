import time
import sys
import os

# ==========================================================
# 1. MESSAGES LÉGAUX
# ==========================================================

PHRASES_BAN = [
    """Bonjour équipe d'assistance,

Je souhaite signaler un problème concernant un compte associé au numéro :
{num}

Merci de vérifier la situation et de prendre les mesures appropriées
conformément à vos règles et conditions d'utilisation.

Cordialement,
KAIRO DEV
"""
]

PHRASES_UNBAN = [
    """Bonjour équipe d'assistance,

Je souhaite demander une révision de la restriction appliquée au compte
associé au numéro :

{num}

Je vous remercie d'examiner la situation et de m'indiquer les étapes
nécessaires pour résoudre le problème.

Cordialement,
KAIRO DEV
"""
]

# ==========================================================
# 2. COULEURS
# ==========================================================

BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

# ==========================================================
# 3. HEADER
# ==========================================================

def header():
    os.system("clear")

    print(BLUE + "=" * 52 + RESET)
    print(WHITE + "          KAIRO DEV • SUPPORT TOOL" + RESET)
    print(BLUE + "=" * 52 + RESET)
    print()

    print(CYAN + "  +--------------------------------------------+" + RESET)
    print(CYAN + "  |              SUPPORT TOOL                 |" + RESET)
    print(CYAN + "  +--------------------------------------------+" + RESET)
    print(CYAN + "  |  [1] BAN    -> Signaler un problème       |" + RESET)
    print(CYAN + "  |  [2] UNBAN  -> Demander une révision      |" + RESET)
    print(CYAN + "  +--------------------------------------------+" + RESET)
    print()


# ==========================================================
# 4. FINALISATION
# ==========================================================

def animation_fin():
    print()

    for i in range(21):
        barre = "#" * i + "-" * (20 - i)

        sys.stdout.write(
            f"\r{GREEN}  KAIRO DEV [{barre}] {i * 5}%{RESET}"
        )

        sys.stdout.flush()
        time.sleep(0.04)

    print("\n")

    print(
        GREEN
        + "+--------------------------------------------+"
        + RESET
    )
    print(
        GREEN
        + "|              ACTION TERMINEE              |"
        + RESET
    )
    print(
        GREEN
        + "+--------------------------------------------+"
        + RESET
    )
    print()


# ==========================================================
# 5. PROGRAMME PRINCIPAL
# ==========================================================

def kairo_tool():
    try:
        header()

        choix = input(
            YELLOW + "[?] Choisis une action : " + RESET
        ).strip()

        if choix not in ("1", "2"):
            print(
                RED + "\n[!] Choix invalide." + RESET
            )
            return

        num_tel = input(
            YELLOW + "[?] Numero concerne : " + RESET
        ).strip()

        if not num_tel:
            print(
                RED + "\n[!] Numero obligatoire." + RESET
            )
            return

        if choix == "1":
            message = PHRASES_BAN[0].replace(
                "{num}",
                num_tel
            )
            action = "BAN"

        else:
            message = PHRASES_UNBAN[0].replace(
                "{num}",
                num_tel
            )
            action = "UNBAN"

        print()
        print(BLUE + "-" * 52 + RESET)
        print(
            CYAN + f"[+] ACTION : {action}" + RESET
        )
        print(
            CYAN + f"[+] NUMERO : {num_tel}" + RESET
        )
        print(BLUE + "-" * 52 + RESET)

        print()
        print(
            WHITE + "Message prepare :" + RESET
        )
        print()
        print(CYAN + message + RESET)

        animation_fin()

    except KeyboardInterrupt:
        print(
            RED + "\n\n[!] ARRET DU SYSTEME." + RESET
        )
        sys.exit()

    except Exception as e:
        print(
            RED + f"\n[!] ERREUR : {e}" + RESET
        )


# ==========================================================
# 6. START
# ==========================================================

if __name__ == "__main__":
    kairo_tool()
