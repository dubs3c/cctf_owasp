# how to hack

När man loggar in sätts en kaka med följande värden:
username: <username>
logged_in: 1

Problemet är att dessa värden inte verifieras på server side, så att klienten
kan sätta dessa värden själv i kakan så kommer de in.
Genom att registrera sig och kolla på sidans innehåll bör folk inse att de ska
ändra kakan så att de blir inloggade som admin. Flaggan finns då i /profile
