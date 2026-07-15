# ⚙️ MARK I
###  AI Asystent Jarvis — By CocaineNose


---

## ✨ Overview

MARK I — to asystent głosowy AI w czasie rzeczywistym, który potrafi słyszeć, widzieć, rozumieć i kontrolować Twój komputer — na każdym systemie operacyjnym. Obsługuje Windows, macOS i Linux. Zbudowany na bazie Gemini Live API z natywnym strumieniowaniem audio, bez żadnych subskrypcji i z pełną cyfrową autonomią.

---

## 🚀 Możliwości

### Główne funkcje
|---|---|
|🎙️ Głos w czasie rzeczywistymRozmowa z ultra-niskim opóźnieniem w dowolnym języku dzięki Gemini Live API|
|🖥️ Kontrola systemuUruchamianie aplikacji, regulacja głośności/jasności, WiFi, skróty, zasilanie — wszystko głosem|
|🧩 Zadania autonomiczneZaawansowane planowanie złożonych, wieloetapowych celów w trybie agenta|
|👁️ Świadomość wizualnaPrzechwytywanie ekranu i obrazu z kamery w czasie rzeczywistym przekazywane do głównej sesji Gemini|
|🧠 Trwała pamięćGłęboko zapamiętuje projekty, preferencje i kontekst osobisty między sesjami|
|⌨️ Hybrydowe wejścieBezproblemowe przełączanie między pisaniem na klawiaturze a komendami głosowymi|
|🌅 Poranne briefingiPrzy pierwszym uruchomieniu: wita Cię, podaje godzinę, pobiera aktualne nagłówki wiadomości i sprawdza pogodę|
|🔔 Proaktywne sprawdzaniePo 15 minutach ciszy JARVIS analizuje kontekst i proponuje coś naprawdę przydatnego — bez zakodowanych reguł, decyduje Gemini|
|📊 Monitorowanie sprzętuCiągłe telemetry CPU, RAM, GPU i temperatury z lokalnymi alertami głosowymi przy przekroczeniu progów|
|🌤️ Raport pogodowyAktualne dane pogodowe dla Twojego miasta, spersonalizowane na podstawie pamięci|
|🗺️ Dynamiczny panel treściPrzewijalna warstwa wyświetlania pod HUD-em, renderująca wyniki z sieci, wiadomości i dane wyszukiwania z znacznikami czasu|
|🔍 Wyszukiwanie wielotrybowenews / research / price / compare / search — najpierw Gemini Grounded, fallback na DDG|
|⏰ Inteligentne przypomnieniaNatywne zaplanowane powiadomienia systemu (Windows Task Scheduler / macOS LaunchAgent / Linux systemd)|
|✈️ Wyszukiwarka lotówSprawdzanie cen i dostępności lotów na żywo|
|🎮 Aktualizator gierSprawdza i uruchamia aktualizacje gier na żądanie|
|📂 Przetwarzanie plikówOdczyt, podsumowywanie i odpowiadanie na pytania o pliki lokalne|
|💻 Pomocnik kodowaniaWbudowana recenzja kodu, debugowanie i generowanie|
|🌐 Kontrola przeglądarkiOtwieranie URL-i, nawigacja po kartach i interakcja z przeglądarką głosem|
|📨 Wysyłanie wiadomościTworzenie i wysyłanie wiadomości przez zintegrowane aplikacje komunikacyjne|
|🎬 Kontrola YouTubeWyszukiwanie, odtwarzanie i sterowanie YouTube głosem|
|🖱️ Kontrola pulpituPasek zadań, zarządzanie oknami i operacje na poziomie pulpitu|
|🧑‍💻 Pamięć języka w tleWykrywa mówiony język przy pierwszym użyciu i zapisuje go bezszmerowo — wszystkie przyszłe sesje i briefingi automatycznie się dostosowują|

---

## Więcej w Mark I

✋ Natychmiastowe przerwanie — ESC lub przycisk
Naciśnij Escape lub kliknij przycisk INTERRUPT, aby przerwać JARVIS-owi w połowie zdania i wrócić do nasłuchiwania. Wcześniej anulowanie odpowiedzi wymagało czekania na opróżnienie całego bufora audio — czasem cztery sekundy. W Mark I audio jest dzielone na fragmenty ~50 ms (2400 bajtów każdy), więc przerwanie następuje w ramach jednego fragmentu. Przerwanie opróżnia kolejkę audio, ustawia flagę i czyści turę — nasłuchiwanie wznawia się w czasie poniżej 100 ms.
👁️ Natychmiastowe potwierdzenie wizji
Gdy poprosisz JARVIS-a o spojrzenie na ekran lub kamerę, nie zapada już cisza podczas przetwarzania. Narzędzie instruuje Gemini, aby od razu powiedział naturalne zdanie („Sprawdzam Twój ekran, sir”), podczas gdy trwa przechwytywanie obrazu. Właściwa analiza pojawia się jako druga odpowiedź. Koniec z niezręczną ciszą.
📰 Równoległe wyszukiwanie wiadomości — wygrywa pierwszy wynik
Zapytania o wiadomości uruchamiają Gemini Grounded Search i DuckDuckGo news jednocześnie w dwóch wątkach daemon. Który backend dostarczy ważny wynik jako pierwszy — ten wygrywa; drugi jest dyskretnie odrzucany. Wcześniej błąd 503 Gemini blokował wyszukiwanie na kilka sekund przed fallbackiem na DDG. Teraz fallback działa równolegle — całkowity czas pobierania wiadomości to czas najszybszego backendu w danej chwili.
🗞️ Prawdziwe artykuły newsowe (nie strony główne)
Wyszukiwanie wiadomości przez DDG wcześniej korzystało z ddgs.text(), co zwracało adresy stron głównych witryn. Mark I przełącza się na ddgs.news(), które zwraca rzeczywiste adresy URL artykułów, tytuły, fragmenty i nazwy źródeł — dokładnie to, czego chcesz w briefingu.
🌅 Dwufazowe briefingi startowe — działają współbieżnie
Briefing startowy teraz wysyła Fazę 2 (pobieranie wiadomości) podczas gdy Faza 1 (powitanie audio) nadal się odtwarza. Wcześniej Faza 2 czekała na pełne zakończenie Fazy 1. Nakładanie się o 1,5 sekundy oznacza, że nagłówek wiadomości jest gotowy w momencie, gdy JARVIS kończy mówić „Dzień dobry”.
🔁 Inteligentniejsze ponowne łączenie — wykładnicze opóźnienie
Timeouty sieci używają teraz wykładniczego backoffu: 3s → 6s → 12s → 60s (z limitem). Każda ponowna próba pokazuje komunikat statusu po turecku w interfejsie („Bağlantı kurulamadı — Xs sonra tekrar deneniyor”). Wcześniej zerwane połączenie powodowało ciasną pętlę bez przydatnych informacji.
🛡️ Cooldown wizji i ochrona przed echem
Przechwytywanie ekranu jest chronione przed pętlami echa. Jeśli JARVIS mówi o ekranie, a mikrofon złapie jego własny głos, mogło dojść do podwójnego wywołania screen_process. Mark I blokuje duplikaty 4-sekundowym cooldownem i flagą _vision_busy. Obie są całkowicie resetowane przy nowej sesji — naprawiono błąd, w którym cooldown przenosił się między połączeniami i blokował poprawne żądania.
🌐 Adresowanie zależne od języka — bez mieszania
System prompt teraz wymusza: zawsze „sir", bez innych form. W Mark I prompt mówił „Always call sir to user", co powodowało, że JARVIS mówił "sir" w środku tureckiego zdania. Naprawiono.
🪟 Zero okien terminala
Monkey-patch subprocess na starcie ustawia CREATE_NO_WINDOW dla każdego procesu potomnego uruchamianego przez aplikację. Żadnego PowerShell, CMD, żadnego migania terminala — nigdy. Dotyczy wszystkich akcji, w tym przypomnień, komend systemowych i wywołań harmonogramu.
🔄 Izolacja stanu sesji
Wszystkie przejściowe flagi wizji i przerwania (_pending_vision, _vision_busy, _vision_cam_active, _vision_close_pending, _interrupted) są całkowicie resetowane przy każdym nowym połączeniu sesji Gemini. Wcześniej stan z crashed sesji mógł się przenosić i zostawiać JARVIS-a w uszkodzonym stanie aż do restartu.

---

## ⚡ Szybki Start

1. Otwórz Visual Studio Code
2. Otwórz folder Projekt Mark I w VSC
3. Otwórz plik setup.py po czym kliknij F5 i debuguj przez Python
4. Otwórz plik main.py po czym kliknij F5 i debuguj przez Python
5. Pogadaj z Jarvisem :) 

> ⚠️ Uwaga dotycząca instalacji: Niektóre zależności specyficzne dla systemu nie są dołączone do requirements.txt, aby repozytorium pozostało lekkie. Jeśli pojawi się ModuleNotFoundError, zainstaluj brakujący pakiet poleceniem pip install <module_name>.

---

## 📋 Wymagania

System operacyjny: Windows 10/11, macOS lub Linux 
Python3.11 lub 3.12
Mikrofon Wymagany do interakcji głosowej
Klucz APIDarmowy klucz Gemini API (config/api_keys.json)

---

## 🗂️ Struktura projektu

```
Mark I/
├── main.py                  # Core loop — Gemini Live session, audio I/O, tool dispatch
├── ui.py                    # PyQt6 HUD — waveform, log panel, interrupt button, camera feed
├── setup.py                 # First-run configuration wizard
├── actions/
│   ├── web_search.py        # Gemini + DDG parallel search (news, research, price, compare)
│   ├── screen_processor.py  # Screen capture & webcam vision via Gemini Live
│   ├── reminder.py          # OS-native scheduled notifications
│   ├── system_monitor.py    # CPU / RAM / GPU / temperature telemetry
│   ├── computer_settings.py # Volume, brightness, WiFi, power
│   ├── computer_control.py  # Keyboard shortcuts, mouse, window management
│   ├── open_app.py          # Application launcher
│   ├── browser_control.py   # Web browser control
│   ├── file_controller.py   # File system operations
│   ├── file_processor.py    # Document reading and summarization
│   ├── send_message.py      # Messaging integration
│   ├── weather_report.py    # Live weather data
│   ├── flight_finder.py     # Flight search
│   ├── youtube_video.py     # YouTube playback control
│   ├── game_updater.py      # Game update management
│   ├── code_helper.py       # Code review and generation
│   ├── dev_agent.py         # Developer task agent
│   ├── desktop.py           # Desktop and taskbar control
│   └── proactive.py        # Proactive silence-break suggestions
├── memory/                  # Persistent key-value memory store
├── core/
│   └── prompt.txt           # JARVIS personality and tool-routing rules
└── config/
    └── api_keys.json        # API key and system configuration
```

---

## 👤 Kontakt do mnie


| Platforma | Link |
| --- | --- |
| TikTok | [@ogdartgoblin](https://www.tiktok.com/@ogdartgoblin) |
| Instagram | [@bedrunek](https://www.instagram.com/bedrunek) |
