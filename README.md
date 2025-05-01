MyHabits – backend-rakendus
See on harjumuste jälgimise rakenduse taustasüsteem (backend), mis on loodud FastAPI ja Microsoft SQL Serveri abil. Kasutaja saab registreeruda, lisada harjumusi, märkida ära täidetud tegevused, koguda punkte ja tasemeid ning määrata endale preemiaid. Administraator näeb kasutajate aktiivsust ja saavutatud tasemeid.

Kasutatud tehnoloogiad
Python 3.11
FastAPI
SQLAlchemy ORM
Microsoft SQL Server
JWT autentimine
GitHub versioonihalduseks

API ülevaade
Autentimine
Endpoint	Meetod	Kirjeldus
/auth/register	POST	Registreerib uue kasutaja
/auth/login	POST	Tagastab JWT tokeni

Harjumused
Endpoint	Meetod	Kirjeldus
/habits	GET	Tagastab kõik kasutaja harjumused
/habits	POST	Loob uue harjumuse
/habits/{id}	PUT	Uuendab olemasolevat harjumust
/habits/{id}	DELETE	Kustutab harjumuse

Näide:

{
  "name": "Jogging",
  "description": "Jog in the park every Monday, Wednesday, Friday",
  "schedule_type": "custom",
  "days_of_week": ["Monday", "Wednesday", "Friday"]
}


Harjumuste logid

Endpoint	Meetod	Kirjeldus
/habit_logs	GET	Tagastab kõik logid
/habit_logs	POST	Salvestab uue logikirje

Näide:

{
  "habit_id": 1,
  "date": "2025-04-26",
  "status": "done",
  "points_earned": 3
}

Preemiad

Endpoint	Meetod	Kirjeldus
/rewards	GET	Tagastab kasutaja preemiad
/rewards	POST	Loob uue preemia

Kasutaja statistika

Endpoint	Meetod	Kirjeldus
/user-profile	GET	Tagastab punktid ja streak'i
/user-levels	GET	Tagastab saavutatud tasemed

Andmebaasi struktuur

Rakendus kasutab järgmisi tabeleid:

Users – kasutaja andmed (id, e-mail, parool jne)
User_profiles – punktid, streak ja aktiivsuse info
Habits – harjumuste info ja ajakava
Habit_logs – tehtud harjumuste logid
Rewards – kasutaja preemiad
Levels – võimalikud tasemed
User_levels – saavutatud tasemed kasutajate lõikes

JSON väljad (nt days_of_week) on salvestatud tekstina.