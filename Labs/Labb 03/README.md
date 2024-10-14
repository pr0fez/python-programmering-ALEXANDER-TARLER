# Klassificering av datapunkter med olika linjer

Detta program används för att visualisera och analysera klassificeringar av datapunkter i förhållande till flera olika linjer. Programmet plottar både datapunkterna och linjerna i grafer och jämför hur de olika linjernas funktioner klassificerar punkterna som antingen "ovanför" eller "nedanför" linjerna.

### Vad programmet gör

    Först så laddar den in en CSV-fil med datapunkter. Därefter så klassificerar den varje datapunkt baserat på dess position i förhållande till dessa fyra linjer:

        **y = x**
        **f(x)=−0.489xf(x)=−0.489x**
        **g(x)=−2x+0.16g(x)=−2x+0.16**
        **h(x)=800x−120h(x)=800x−120**

    Efter klassificering så plottas datapunkterna ut tillsammans med varje linje och färgkodar dem baserat på om de ligger "ovanför" eller "nedanför" linjen.
    Slutligen så jämförs klassificeringarna mellan linjerna och visar hur många punkter som klassificerats olika mellan varje par av linjer.

### Installation

För att köra detta program behöver du ha följande installerat:

    Python 3.x
    matplotlib: Används för att plotta grafer.
    csv: Används för att läsa in CSV-filen.

Du kan installera matplotlib genom att köra följande kommando:

**bash**

**pip install matplotlib**

Användning
**Steg 1**: Förbered en CSV-fil

Förbered en CSV-fil (t.ex. unlabelled_data.csv) som innehåller två kolumner med x- och y-värden. För att ha rätt format så rekommenderar jag att använda **unlabelled_data.csv** som guide.

**Steg 2**: Kör programmet

    Ifall du inte vill använda en egen CSV-fil så finns **unlabelled_data.csv** tillgänglig som data, och i så fall är det bara att köra programmet.

    Om du vill använda din egna CSV-fil så ska du börja med att placera din CSV-fil i samma mapp som din Python-fil. Du antingen namnge den som "unlabelled_data.csv", men först efter att du har tagit bort eller bytt namn på originalet, eller ändra namnet på den fil som koden anropar.
    Kör sedan Python-filen från terminalen eller via den utvecklingsmiljö du använder.

**Steg 3**: Analysera graferna och resultaten

Programmet kommer att skapa grafer där varje linje visas tillsammans med datapunkterna som är färgkodade baserat på klassificering. Efter graferna kommer programmet att skriva ut skillnaderna i klassificering mellan de olika linjerna i terminalen eller konsolen.
Exempel på körning

När programmet körs med CSV-filen unlabelled_data.csv kan du förvänta dig följande:

En graf för varje ovannämnda linje där punkter är färgkodade som "ovanför" eller "nedanför" respektive linje. Terminalen eller konsollen bör visa en jämförelse mellan klassificeringarna för varje par av linjer, t.ex:

Skillnader i klassificeringar:
y_eq_x vs f: 315 punkter skiljer sig (52.50%)
y_eq_x vs g: 317 punkter skiljer sig (52.83%)
y_eq_x vs h: 278 punkter skiljer sig (46.33%)
