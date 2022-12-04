# Zapiš funkci pro převod vybraných klíčů z json do csv
import os
import sys
import csv
import json


def hlavni():
    # TODO: dodelat spousteni pomoci argumentu z terminalu
    adresar = "data/"
    zadouci_klice = ["date", "temperature", "humidity"]
    json_to_csv(adresar, zadouci_klice)


def json_to_csv(adresar: str, zadouci: list) -> None:
    """
    TODO 1. Nacist vsechny potrebne '.json' soubory (fce:'najdi_json_soubory()'),
    TODO 2. ^- nacist obsah vsech nalezenych '.json' (fce:'nacti_obsah_jsonu()'),
    TODO 3. ^- upravit nact. obs. podle naseho vyberu (fce:'filtruj_nepotrebne_klice()'),
    TODO 4. ^- ulozit upr. obs. do lokalniho souboru (fce:'zapis_upravene_do_csv()').
    """
    print(f"Zpracovavam json soubory ve slozce {adresar}...")



def najdi_json_soubory(adresar: str) -> list:
    """
    TODO: V seznamu vsech souboru zadaneho adresare najdi jen soubory s priponou '.json'.
    """
    pass


def nacti_obsah_jsonu(adresar: str, soubor: str) -> list:
    # TODO idealne s kontextovym managerem
    pass


def filtruj_nepotrebne_klice(zadouci: list, puvodni_sl: dict) -> dict:
    """
    TODO: Zapis do noveho slovniku vsechny klice v par. 'zadouci' z puvodniho slovniku.
    """
    upravene_klice = dict()
    return upravene_klice


def zapis_upravene_do_csv(soubor: str, udaje: list):
    """
    TODO Do zadaneho souboru (par. 'soubor') zapis filtrovane udaje (par. 'udaje').

    TODO Z prvniho indexu par. 'udaje' zkus vzit jmena klicu a vytvorit z nich
    zahlavi souboru.
    """


if __name__ == "__main__":
    hlavni()
