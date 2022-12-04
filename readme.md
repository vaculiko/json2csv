# Lekce 11: Převodník `json` na `csv`

Ahoj, nestíhám dodělat tenhle projekt, hodil jsem ti tu všechno co potřebuješ na dodělání.

Stačí si repozitář naklonovat k sobě, dodělat pár věcí a poslat to na schválení.

## Data

Z meteostanice se pravidelně ukládají data na server ve formátu `json`.  

Všechna měření z jednoho roku jsou uložena v jednom `.json` souboru ve složce `data`.  

Jedno měření vypadá takto:

```json
{"id":5,
  "date":"2018-01-05",
  "temperature":20.01,
  "humidity":49.88,
  "pressure":986.9,
  "co2_ppm":59,
  "voc":170,
  "pm25":95}
```

## Zadání

1. Převést data z měření za poslední čtyři roky z `json` souborů do jednoho `csv`. 
2. Mít možnost vybrat jen některé typy měření (některé sloupce).
3. Celý program má být variabilní, měl by uživateli umožnit vybrat složku s `json` soubory 
a specifikovat požadované sloupce hodnot.

## TIP 

Zákazník chce dělat grafy v Excelu. Já bych jim zkusil nabídnout lepší řešení - Plotly. 

Stačí pár řádků a máš luxusní interaktivní graf, který se dá poslat mailem. 

Mrkni na https://plotly.com/python/plot-data-from-csv/

Pro rychlejší instalaci jsem ti nachystal soubor `requirements.txt`.  

> Díky moc!  
> Ondra
