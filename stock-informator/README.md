# Projekt stock-informator pobiera informacje o wartosci firmy na giełdzie.

Po pobraniu danych z API (https://www.alphavantage.co) projekt oblicza różnicę w zamknięciu w ciągu dwóch ostatnich dni.
Następnie pobierane są 3 najnowsze artykuły na temat danej firmy przez API https://newsapi.org/ i wysyłane są powiadomienia SMS
przez Twilio API https://www.twilio.com. Program pobierane wymagane klucze API z konsoli od użytkownika oraz numer telefonu podany na stronie Twilio. Pobrany zostaje również numer, na który wysłana ma zostać wiadomość (Numer musi być zweryfikowany w Twilio).
Do poprawnego działania należy wprowadzić w folderze projektu również zmienne środowiskowe w pliku twilio.env. (http://twil.io/secure)
Przykład działania:
<a href="url"><img src="https://raw.githubusercontent.com/jaksio/mycv-python/main/stock-informator/effect.jpg" align="left" height="48" width="48" ></a>
