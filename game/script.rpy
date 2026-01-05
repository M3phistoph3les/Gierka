##Definicje postaci 
default player_name = "hero"
define ja = Character("[player_name]", who_color="#00ccff")
define r = Character("Radio", who_color="#1bdb8b")
define m = Character("???", who_color="#ff0000") # Potwór

# --- FLAGI POSTĘPU (ZMIENNE LOGICZNE) ---
# Ekwipunek podstawowy
default ma_lom = False
default ma_latarke = False
default ma_bezpiecznik = False 
default ma_karta_dostepu = False 
default ma_mapa = False
default prad_wlaczony = False 

# Lokacje i stany
default zbrojownia_otwarta = False
default interakcja_tooltip = ""
default systemy_bezpieczeństwa = False

# Cela
default pokoj1_otwarty = True
default drzwi_cela_wywalone = False
default drzwi_wyjsciowe_otwarte = False

# Generator
default generator_otwarty = False
default narzedzia_odlozone = 0
default smieci_sprzatniete = False
default kloc_sprzatniety = False
default narzedzia_sprzatniete = False

# Szpital
default szpital_otwarty_odwiedzony = False
default szpital_otwarty = False


# Jadalnia
default stoufka_otwarta = False
default ma_karta_serwerownia = False 
default ma_zeton = False
default jadalnia_odwiedzona = False
default kubek_przesuniety = False 
default zna_kod_automat = False

# Serwerownia
default serwerownia_otwarta = False
default serwerownia_naprawiona = False
default zbrojownia_dostepna = False
default hack_progress = 0 
default lore_read_count = 0 

# Finał
default dobry_karabin_nr = 0
default dobry_pistolet_nr = 0
default sprawdzona_bron_nr = 0
default wylosowany_typ_broni= ""
default wylosowany_numer_broni= 0
default systemy_obronne_aktywne = False
default ma_bron = False
default typ_broni = "brak" 
default zaufanie_ai = 0
default boss_hp = 100
default player_hp = 100
default pistol_targets_hit = 0
default pistol_targets_needed = 10

## ----TŁA---------
image bg PokojStartowy ="pokoj1"
image bg PokojStartowybezswiatla ="pokoj1_no"
image bg Korytarz_no_light ="korytarz_no"
image bg Korytarz = "korytarz"
image bg stolowka ="stoufka"
image bg stolowka_no ="stoufka_no"
image bg apteka1 ="apteka"
image bg apteka2 ="apteka2"
image bg apteka1_no= "szpital_no"
image bg apteka2_no= "szpital_no2"
image bg generator_swiatlo ="generator_light"
image bg generator_no_swiatlo ="generator_no_light"
image bg serwerownia ="komputerownia"
image bg serwerownia_no = "serwerownia_no"
image bg zbrojownia ="zbrojownia"
image bg drzwi_wyjsciowe ="drzwi_wyjscie"
image bg drzwi_wyjsciowe_otwarte = "drzwi_wyjście_otwarte"
image bg tlo_mapa = "tło_mapa"
#---------------HAKOWANIE SERWEROWNIA
image bg terminal_hacking = "terminal_hacking_bg"
#---------------JADALNIOWY STOLIK------
image bg stolik_zblizenie_bg = "stolik_zblizenie" # Twoje tło zbliżenia na stół
image monster_boss = "unnamed" # Potwór z głową TV
image bg apteczka_zblizenie = "apteczka_zblizenie_no"   ######DODAĆ
image bg apteczka_zblizenie_pront = "apteczka_zblizenie"

label start:  
#region START 
#endregion START
    label początek_gry:

        "Otula Cię aksamitna ciemność ze wszystkich stron..."
        "Nie czujesz ciężaru myśli i wspomień, a czas zdaje się stać w miejscu"
        "Czujesz się po prostu bezpiecznie, chyba pierwszy raz od bardzo, bardzo dawna"
        "Chyba nie jesteś pewny od jak dawna"
        "..."
        "Zaczynasz czuć delikatnie przenikający niepokój"
        "Jakby przez ciemność przesiąkało obezwładniające drętwienie"
        "Narasta..."
        "Robi się cieższe..."
        "Coraz cięższe..."
        "Ołowiany chłód zaczyna pełzać od opuszków Twoich palców"
        "Coraz głębiej..."
        "Coraz szybciej..."
        "Wartkie strumienie bólu uderzają intensywnie w podstawę Twojej czaszki"
        "..."
        "Jest źle"
        "Jest cholernie źle!"
        "Leżysz na twardym materacu, który cuchnie potem i stęchlizną"
        "Próbujesz otworzyć oczy, ale powieki odmawiają Ci poszłuszeństwa"
        "Jakby za wszelką cenę chciały Cię bronić przed tym, co się kryje po drugiej stronie"
        "Spierzchniętymi ustami wyczuwasz metaliczny posmak"
        "Narastający zapach omszałych betonowych ścian zdaje się być przesiąknięty ostrą wonią czegoś, przez co czujesz gęsią skórkę"
        "Drżąc próbujesz się podnieść, tocząc dalej walkę z ociężałymi powiekami."
        "Czujesz przyśpieszony rytm serca, zimne żyły i tętnice zaczynają pulsować wrzącą krwią"
        "Powieki w końcu ustępują Twojej silnej woli, a Ty tak gwałtownie siadasz na brzegu łóżka, że aż zakręciło Ci się w głowie."

        scene black with dissolve
        stop music fadeout 2.0
        
        "Tępy puls w czaszce nie ustaje. Czujesz się, jakbyś spał dekadę... albo minutę."
        "Twoje mięśnie drżą w niekontrolowanych spazmach. Jesteś słaby. Żałośnie słaby."
        
        scene bg PokojStartowy with fade
        
        "Półmrok. Zarysy obcych mebli. Beton. Rdza."
        "Zewsząd dobiega trzeszczący dźwięk. Głos. Dobiega ze ścian, z sufitu, z wnętrza twojej głowy."
        
        "???" "Haloo... Odbiór...? Czy ten zlepek biomasy raczy wreszcie nawiązać połączenie?"
        
        show radio at right with easeinright
        r  "Witamy w świecie żywych. Jestem Pan Radio. Twój nadzorca, przewodnik i... jedyny powód, dla którego jeszcze oddychasz."
        
        show hero_poczatek at left with dissolve
        
        menu:
            "Gdzie ja jestem?!":
                ja "Co to za miejsce?! Kim ty jesteś?! Mów, albo rozwalę te głośniki!"
                r "Imponująca wola życia. Szkoda, że marnowana na puste groźby."
                r "Znajdujesz się w Placówce Badawczej Azyl. Albo raczej w tym, co z niej zostało."

            "Kim jesteś?":
                ja "Zidentyfikuj się. I powiedz, dlaczego mnie więzisz."
                r "Konkretny. To lubię. Oszczędza nam obu czasu procesora."
                r "Więzisz? To mocne słowo. Powiedzmy, że 'przechowuję'. Jestem Pan Radio."

            "... (Milczenie)":
                ja "..."
                r "Katatonia? Nie... widzę, że twoje źrenice reagują. Obserwujesz."
                r "To dobrze. Obserwacja to pierwszy krok do przetrwania."
        
            r "Widzę drobne uszkodzenia w sektorze pamięci długotrwałej. Procedura wybudzania była... nieco brutalna."
        label Choice:   
        menu:
            " "
            #Opcja 1
            "Czego ode mnie chcesz?":
                $ zaufanie_ai -= 1 
                hide hero_poczatek
                show hero_wkurw at left
                ja "Dość tych gierek. Czego chcesz?"
                 
                hide hero_wkurw
                show hero_podstawowy at left
                 
                r "Adrenalina w górę. Kortyzol w górę. Fascynujące, jak łatwo tobą sterować, [player_name]."
                r "Jestem Bogiem tego betonowego pudełka. Nie irytuj bóstwa, bo odetnie tlen."
            #Opcja 2   
            "(Rozglądaj się w milczeniu)":  
                $ zaufanie_ai += 1 
                ja "..."
                "Ignorujesz głos. Szukasz wyjścia. Głośniki są ukryte za kratownicami. Brak widocznych kamer, ale czujesz na sobie wzrok."
                 
                hide hero_poczatek
                show hero_podstawowy at left
                 
                r "Ignorancja czy skupienie? Mam nadzieję, że to drugie. W przeciwnym razie szybko staniesz się statystyką."
                r "Jestem Pan Radio. I radzę słuchać moich audycji."

            #Opcja 3
            "Jesteś tylko zardzewiałym głośnikiem.":
                ja "Dużo gadasz jak na kawałek złomu przykręcony do ściany."
                r "Zuchwałość. Cecha rzadka u obiektów testowych. Zwykle kończycie skomląc w kącie o mamę."
                r "Doceniam jednak iskrę buntu. Nawet jeśli jest bezcelowa."

        r "Sytuacja jest prosta: drzwi są zaryglowane, systemy podtrzymywania życia zdychają, a ja się nudzę. Wyjdź stąd, albo stań się częścią wystroju wnętrz."
        r "A właśnie... jak cię oznaczono w rejestrze wsadowym?"
        
        $ player_name = renpy.input("Wpisz identyfikator (imię): ", length=15).strip()
        if player_name == "":
            $ player_name = "Nieznajomy"
            
        ja "Nazywam się... [player_name]. Tak mi się wydaje."
        ja "Jak mam się stąd wydostać?"
        
        r "Eksploruj. Improwizuj. Szukaj błędów w systemie. I postaraj się nie dać zjeść."
        hide radio     
        ja "Zjeść?! Co tu jeszcze jest oprócz nas?!"
        
        hide hero_podstawowy
        "Odpowiedzią jest dźwięk gasnących turbin. Generatory umierają. Światła zaczynają mrugać spazmatycznie, by po chwili zgasnąć całkowicie."

#-----------------Tło się zmienia na brak światła---------
        scene bg PokojStartowybezswiatla
        show hero_wkurw at left
        ja "Świetnie jeszcze tego brakowało.."
        hide hero_wkurw
        show screen plecak_ikona 
        
        # Wywołanie ekranu z zagadkami
        call screen Pokój_startowy_zagadka
#region CELA

screen Pokój_startowy_zagadka():
    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077") 
            padding (10, 5)
            xalign 0.5 yalign 0.1 
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]
    # 1. Drzwi
    imagebutton:
        xpos 0 
        ypos 0
        if prad_wlaczony:
            idle "images/przedmiot_drzwi_cela_swiatlo_idle.png"
            hover "images/przedmiot_drzwi_cela_swiatlo_hover.png"
        else:
            idle "images/przedmiot_drzwi_cela_idle.png"
            hover "images/przedmiot_drzwi_cela_hover.png"

        focus_mask True
        action If(drzwi_cela_wywalone, Jump("powrot_do_korytarza"), Jump("Otwórz_drzwi"))

        hovered If(drzwi_cela_wywalone, SetVariable("interakcja_tooltip", "WYJŚCIE: KORYTARZ"), SetVariable("interakcja_tooltip", "ZAMKNIĘTE DRZWI"))
        unhovered SetVariable("interakcja_tooltip", "")

    # 2. Łóżko
    imagebutton:
        xpos 0 
        ypos 0
        if prad_wlaczony:
            idle "images/przedmiot_łozko_swiatlo_idle.png"
            hover "images/przedmiot_łozko_swiatlo_hover.png"
        else:
            idle "images/przedmiot_łozko_idle.png"
            hover "images/przedmiot_łozko_hover.png" 

        focus_mask True 
        action If(not ma_latarke, 
                Jump("brak_swiatla_pod_lozkiem"), 
                If(not ma_lom, 
                    Show("pod_lozkiem_zoom"),      
                    Jump("Zajrzyj_pod_łóżko")     
                )
            )
        if ma_lom:
            hovered SetVariable("interakcja_tooltip", "ZAJRZYJ POD ŁÓŻKO")
        else:
            hovered SetVariable("interakcja_tooltip", "PRZESZUKAJ ŁÓŻKO")
        unhovered SetVariable("interakcja_tooltip", "")

    # 3. Szafka
    if(ma_latarke == False):    
        imagebutton:
            xpos 0 
            ypos 0
            if prad_wlaczony:
                idle "images/przedmiot_szafka_swiatlo_idle.png"
                hover "images/przedmiot_szafka_swiatlo_hover.png"
            else:
                idle "images/przedmiot_szafka_idle.png"
                hover "images/przedmiot_szafka_hover.png"

            focus_mask True
            action Show("szafka_wewnatrz")
            hovered SetVariable("interakcja_tooltip", "OTWÓRZ SZAFKĘ")
            unhovered SetVariable("interakcja_tooltip", "") 


#------------------SCREENY DO SCENY 1---------------------------------------------
#Screen z szafki wewnątrz
screen szafka_wewnatrz():
    modal True 
    zorder 150
    add "images/przedmiot_szafka_srodek.png"
    if ma_latarke == False:
        imagebutton:
            idle "images/latarka_szafka_idle.png"
            hover "images/latarka_szafka_hover.png"
            focus_mask True
            action [SetVariable("interakcja_tooltip", ""), Hide("szafka_wewnatrz"), Jump("akcja_zabrania_latarki")]
            hovered SetVariable("interakcja_tooltip", "WEŹ LATARKĘ")
            unhovered SetVariable("interakcja_tooltip", "")
 
#Screen z pod łóżka
screen pod_lozkiem_zoom():
    modal True
    zorder 150           
    add "images/pod_lozkiem.png"
    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)] 
    if ma_lom == False:
        imagebutton:
            idle "images/lom_lozko_idle.png"
            hover "images/lom_lozko_hover.png"
            focus_mask True
            action [SetVariable("interakcja_tooltip", ""), Hide("pod_lozkiem_zoom"), Jump("akcja_zabrania_lomu")]
            hovered SetVariable("interakcja_tooltip", "WEŹ ŁOM")
            unhovered SetVariable("interakcja_tooltip", "")
#----------------------------------------------------------------------------------
#-------------------------------LABELE SCENA 1 ----------------------------------
#endregion Pokoj startowy

label brak_swiatla_pod_lozkiem:
    "Kluczasz dłonią w gęstym mroku pod ramą łóżka, ale czujesz tylko zimny beton i kurz."
    show hero_poczatek at left
    ja "Nic nie widzę. Jest tu zbyt ciemno, żebym mógł cokolwiek znaleźć..."
    ja "Muszę najpierw jakoś oświetlić ten kąt."
    hide hero_poczatek
    call screen Pokój_startowy_zagadka
#akcja ŁOM
label akcja_zabrania_lomu:
    $ ma_lom = True
    $ backpack.add (przedmiot_lom,0, 0)
    "Twoje dłonie zaciskają się na zimnej, stalowej sztabie. Solidny łom."
    ja "Może uda mi się nim wyważyć drzwi."
    call screen Pokój_startowy_zagadka
#akcja Latarka
label akcja_zabrania_latarki:
    $ ma_latarke = True
    $ backpack.add (przedmiot_latarka,0, 0)
    "Podniosłeś latarkę"
    call screen Pokój_startowy_zagadka
#akcja Drzwi
label Otwórz_drzwi:
    if drzwi_cela_wywalone:
        jump korytarz_wyjscie_z_pokoju
    if(ma_lom == False):
        "Napierasz na drzwi całym ciężarem ciała. Ani drgną."
        show hero_poczatek
        ja "Zablokowane. Mechanizm jest stary, ale wciąż trzyma."
        hide hero_poczatek
        if(ma_latarke == False):
            ja "Jest zbyt ciemno, żeby znaleźć słaby punkt. Potrzebuję światła."
        else:
            "W świetle latarki dostrzegasz, że framuga jest lekko wygięta. Gdybym miał czym podważyć te drzwi..."
        call screen Pokój_startowy_zagadka
    else:
        "Wbijasz łom w szczelinę. Metal zgrzyta przeraźliwie, aż w końcu zamek pęka z głośnym trzaskiem."
        show hero_szczesliwy at left
        ja "Droga wolna. Zamek i tak był ledwo żywy."
        hide hero_szczesliwy
        $ drzwi_cela_wywalone = True
        jump korytarz_wyjscie_z_pokoju
#akcja Zaglądania pod łóżko            
label Zajrzyj_pod_łóżko:  
    "W świetle latarki dostrzegasz wyschnięte truchło szczura ukryte w kącie."
    "Czuć od niego słodkawy odór rozkładu, który wcześniej brałeś za zwykłą stęchliznę."
    show hero_dziwny at left
    ja "Spałem nad tym truchłem... Jak długo byłem nieprzytomny?"
    hide hero_dziwny
    call screen Pokój_startowy_zagadka 
   

# --------------------------------------------------------------------Scena Druga Korytarz -------------------------------------------------
#region KORYTARZ

#endregion KORYTARZ 

label powrot_do_korytarza:
    if prad_wlaczony:
        scene bg Korytarz
    else:
        scene bg Korytarz_no_light
    $ stoufka_otwarta = True
    $ stoufka = True
    call screen Pokój_Korytarz_klikanie

label korytarz_wyjscie_z_pokoju:
    scene bg Korytarz_no_light
    "Echo twoich kroków brzmi tu obco. Z głośników dobiega suchy trzask, przypominający kaszel starego palacza."
    show radio at right

    r "Proszę, proszę. Jednak funkcje motoryczne działają. Cierpliwość nie jest moją mocną stroną."
    r "Zajęło ci to całą epokę. Podziwiam ten brak pośpiechu w obliczu śmierci."
    
    ja "Drzwi były zablokowane. Musiałem sobie poradzić."
    r "Oszczędź mi raportu. Czas to jedyny zasób, którego nam brakuje. Tlen spada, temperatura też."
    r "Jesteśmy martwi, dopóki serwerownia nie wstanie. Potrzebujemy prądu. Teraz."
    
    menu:
        " "
        "Dlaczego tak ci zależy na prądzie?":
            $ zaufanie_ai -= 1 
            r "Twoja ignorancja jest urocza. Jeśli systemy padną całkowicie, te grodzie staną się twoją trumną."
            r "Chcesz spędzić resztę swoich marnych dni w ciemności, zlizując wilgoć ze ścian?"
        
        "Zrobię co trzeba.":
            $ zaufanie_ai += 1 
            ja "Przyjąłem. Gdzie mam iść?"
            r "Przynajmniej instynkt przetrwania masz sprawny. Mniej pytań, więcej działania."
            
    r "Generator jest w sektorze przemysłowym. Właśnie sfingowałem twoją autoryzację do zamka magnetycznego."
    r "Nie zmarnuj tej szansy, [player_name]."
    hide radio

    "Radio milknie. Ruszasz w głąb korytarza. Snop światła wyławia z mroku rdzawe zacieki na ścianach."
    "Nagle zatrzymujesz się. Pod butem czujesz lepkie błoto."
    "Kierujesz latarkę w dół. To nie błoto."
    "To krew. Stara, gęsta, niemal czarna maź. Prowadzi prosto w ciemność."
    "Obok widzisz głębokie bruzdy w stali. Jakby ktoś lub coś próbowało hamować pazurami."
    
    menu:
        "Dotknij śladów":
            "Przesuwasz palcem po wgłębieniu w metalu. Krawędzie są ostre, wywinięte na zewnątrz. Siła, która to zrobiła, musiała być potworna."
            ja "Co tu się stało...? Panie Radio, co jest w stanie rozerwać stal?"
        "Cofnij się z obrzydzeniem":
            "Żołądek podchodzi ci do gardła. Zapach miedzi i zgnilizny jest nie do zniesienia."
            ja "O boże... Panie Radio, powiedz, że to stara krew. Że to już koniec."
    
    r "..."
    r "To, co widzisz, to pomnik ludzkiej ambicji. Bunkier miał przeanalizować genom 'Obcego' i stworzyć boga wojny."
    ja "Słucham?! Broń biologiczną?!"
    
    
    label Rozmowa_O_Przeszłości:
        menu:
            "Ten 'Obcy' to zrobił?":
                r "HA! Nie bądź naiwny. Obiekt Zero był martwy, gdy go przywieźli. To surowica... nasza 'wielka nadzieja'... wywołała pewne zmiany w personelu."
                r "Byliśmy gotowi do masowej produkcji super-żołnierzy. Ale materiał badawczy okazał się... agresywnie nieprzewidywalny."
                r "Powiedzmy, że ewolucja przyspieszyła o milion lat w ciągu jednej nocy."
                jump Rozmowa_O_Przeszłości

            "Dlaczego w ogóle tu jesteśmy?":
                r "Wojna na górze. Bunkier miał być Arką dla elit i laboratorium dla wojska."
                r "Znaleźliśmy coś we wraku statku, co miało wygrać wojnę. I wygrało... w pewnym sensie. Nikt już nie walczy, bo nie ma kto."
                r "Nie spodziewaliśmy się tylko, że prawdziwy wróg jest już wewnątrz naszych żył."
                jump Rozmowa_O_Przeszłości

            "Co to jest Projekt Arka?":
                r "Tak to nazywali w ulotkach. 'Przyszłość Ludzkości'. Schronienie."
                r "Ale prawdziwy potwór nie przyszedł z zewnątrz. Wyhodowaliśmy go tutaj, w sterylnych probówkach, karmiąc go naszymi ambicjami."
                r "Arka stała się grobowcem. A ty jesteś ostatnim żywym pasażerem."
                jump Rozmowa_O_Przeszłości

            "Dość gadania. Idę dalej.":
                ja "Mam dość historii. Chcę się stąd wydostać."
                r "Słusznie. Historia lubi się powtarzać, jeśli się w niej zagłębisz. Idź do generatora."
                "Postanawiasz nie drążyć tematu. Niektóre drzwi w umyśle lepiej zostawić zamknięte."

    "Po kilkunastu metrach dostrzegasz tabliczkę: 'GENERATOR'. Drzwi są uchylone."
    ja "Jestem na miejscu."
    r "Wchodź. I uważaj. Ciemność w maszynowni bywa głodna."

    $ generator_otwarty = True
    $ generator_light = True
    call screen Pokój_Korytarz_klikanie
#Główny screen
screen Pokój_Korytarz_klikanie():
    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

    # --- Drzwi do Celi ---
    imagebutton:
        xpos 0 ypos 0
        focus_mask True
        if prad_wlaczony:
            idle "images/przedmiot_drzwi_cela2_swiatlo_idle.png"
            hover "images/przedmiot_drzwi_cela2_swiatlo_hover.png"
        else:
            idle "images/przedmiot_drzwi_cela2_ciemne_idle.png"
            hover "images/przedmiot_drzwi_cela2_ciemne_hover.png"
            
        action [SetVariable("interakcja_tooltip", ""), Jump("powrot_do_celi")]
        hovered SetVariable("interakcja_tooltip", "DRZWI DO: CELA")
        unhovered SetVariable("interakcja_tooltip", "")

    # --- Drzwi do Generatora ---
    imagebutton:
        xpos 0 ypos 0
        focus_mask True
        if prad_wlaczony:
            if generator_otwarty:
                idle "images/przedmiot_drzwi_gen_swiatlo_otwarte_idle.png"
                hover "images/przedmiot_drzwi_gen_swiatlo_otwarte_hover.png"
            else:
                idle "images/przedmiot_drzwi_gen_swiatlo_zakmniete_idle.png"
                hover "images/przedmiot_drzwi_gen_swiatlo_zakmniete_hover.png"
        else:
            if generator_otwarty:
                idle "images/przedmiot_drzwi_gen_ciemne_otwarte_idle.png"
                hover "images/przedmiot_drzwi_gen_ciemne_otwarte_hover.png"
            else:
                idle "images/przedmiot_drzwi_gen_ciemne_zamkniete_idle.png"
                hover "images/przedmiot_drzwi_gen_ciemne_zamkniete_hover.png"

        if generator_otwarty:
            action [SetVariable("interakcja_tooltip", ""), Jump("Pomieszczenie_Z_Generatorem_Fab")]
            hovered SetVariable("interakcja_tooltip", "DRZWI DO: POMIESZCZENIE Z GENERATOREM")
        else:
            action Jump("drzwi_zablokowane_info")
            hovered SetVariable("interakcja_tooltip", "DRZWI ZABLOKOWANE")
        unhovered SetVariable("interakcja_tooltip", "")

    # --- Drzwi do Szpitala ---
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            if szpital_otwarty:
                idle "images/przedmiot_drzwi_szpital_swiatlo_otwarte_idle.png"
                hover "images/przedmiot_drzwi_szpital_swiatlo_otwarte_hover.png"
            else:
                idle "images/przedmiot_drzwi_szpital_swiatlo_zamkniete_idle.png"
                hover "images/przedmiot_drzwi_szpital_swiatlo_zamkniete_hover.png"
        else:
            if szpital_otwarty:
                idle "images/przedmiot_drzwi_szpital_ciemne_otwarte_idle.png"
                hover "images/przedmiot_drzwi_szpital_ciemne_otwarte_hover.png"
            else:
                idle "images/przedmiot_drzwi_szpital_ciemne_zamkniete_idle.png"
                hover "images/przedmiot_drzwi_szpital_ciemne_zamkniete_hover.png"

        if szpital_otwarty:
            action [SetVariable("interakcja_tooltip", ""), Jump("szpital_label")]
            hovered SetVariable("interakcja_tooltip", "DRZWI DO: SEKTOR MEDYCZNY")
        else:
            action Jump("apteka_zablokowana_info")
            hovered SetVariable("interakcja_tooltip", "DRZWI ZABLOKOWANE")
        unhovered SetVariable("interakcja_tooltip", "")

    # --- Drzwi do Jadalni ---
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            if stoufka_otwarta:
                idle "images/przedmiot_drzwi_stoufka_swiatlo_otwarte_idle.png"
                hover "images/przedmiot_drzwi_stoufka_swiatlo_otwarte_hover.png"
            else:
                idle "images/przedmiot_drzwi_stoufka_swiatlo_zamkniete_idle.png"
                hover "images/przedmiot_drzwi_stoufka_swiatlo_zamkniete_hover.png"
        else:
            if stoufka_otwarta:
                idle "images/przedmiot_drzwi_stoufka_ciemne_otwarte_idle.png"
                hover "images/przedmiot_drzwi_stoufka_ciemne_otwarte_hover.png"
            else:
                idle "images/przedmiot_drzwi_stoufka_ciemne_zamkniete_idle.png"
                hover "images/przedmiot_drzwi_stoufka_ciemne_zamkniete_hover.png"

        if stoufka_otwarta:
            action [SetVariable("interakcja_tooltip", ""), Jump("jadalnia_label")]
            hovered SetVariable("interakcja_tooltip", "DRZWI DO: JADALNIA")
        else:
            action Jump("jadalnia_zablokowana_info")
            hovered SetVariable("interakcja_tooltip", "DRZWI ZABLOKOWANE")
        unhovered SetVariable("interakcja_tooltip", "")
    
    #--- Drzwi do Serwerowni
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            if serwerownia_otwarta:
                idle "images/przedmiot_drzwi_serwerownia_swiatlo_otwarte_idle.png"
                hover "images/przedmiot_drzwi_serwerownia_swiatlo_otwarte_hover.png"
            else:
                idle "images/przedmiot_drzwi_serwerownia_swiatlo_zamkniete_idle.png"
                hover "images/przedmiot_drzwi_serwerownia_swiatlo_zamkniete_hover.png"
        else:
            if serwerownia_otwarta:
                idle "images/przedmiot_drzwi_serwerownia_ciemne_otwarte_idle.png"
                hover "images/przedmiot_drzwi_serwerownia_ciemne_otwarte_hover.png"
            else:
                idle "images/przedmiot_drzwi_serwerownia_ciemne_zamkniete_idle.png"
                hover "images/przedmiot_drzwi_serwerownia_ciemne_zamkniete_hover.png"

        if serwerownia_otwarta:
            action [SetVariable("interakcja_tooltip", ""), Jump("serwerownia_label")]
            hovered SetVariable("interakcja_tooltip", "DRZWI DO: SERWEROWNI")
        else:
            action Jump("serwerownia_zablokowana_info")
            hovered SetVariable("interakcja_tooltip", "DRZWI ZABLOKOWANE")
        unhovered SetVariable("interakcja_tooltip", "")
    #--- Drzwi do Zbrojowni
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            if zbrojownia_otwarta:
                idle "images/przedmiot_drzwi_zbrojownia_swiatlo_otwarte_idle.png"
                hover "images/przedmiot_drzwi_zbrojownia_swiatlo_otwarte_hover.png"
            else:
                idle "images/przedmiot_drzwi_zbrojownia_swiatlo_zamkniete_idle.png"
                hover "images/przedmiot_drzwi_zbrojownia_swiatlo_zamkniete_hover.png"
        else:
            if zbrojownia_otwarta:
                idle "images/przedmiot_drzwi_zbrojownia_ciemne_otwarte_idle.png"
                hover "images/przedmiot_drzwi_zbrojownia_ciemne_otwarte_hover.png"
            else:
                idle "images/przedmiot_drzwi_zbrojownia_ciemne_zamkniete_idle.png"
                hover "images/przedmiot_drzwi_zbrojownia_ciemne_zamkniete_hover.png"

        if zbrojownia_otwarta:
            action [SetVariable("interakcja_tooltip", ""), Jump("zbrojownia_start_label")]
            hovered SetVariable("interakcja_tooltip", "DRZWI DO: ZBROJOWNI")
        else:
            action Jump("zbrojownia_zablokowana_info")
            hovered SetVariable("interakcja_tooltip", "DRZWI ZABLOKOWANE")
        unhovered SetVariable("interakcja_tooltip", "")

    

#-------------------------LABELE DO DRZWI WSZYSTKICH------------------------------------------------------

label powrot_do_celi:
    if prad_wlaczony:
        scene bg PokojStartowy with fade
    else:
        scene bg PokojStartowybezswiatla with fade
    call screen Pokój_startowy_zagadka

label drzwi_zablokowane_info:
    ja "Ani drgną. Elektroniczny zamek świeci się na czerwono."
    if not prad_wlaczony:
        r "System kontroli dostępu jest martwy. Bez zasilania te grodzie się nie przesuną."
    else:
        r "Brak autoryzacji. Czytnik odrzucił twój profil biometryczny."
    call screen Pokój_Korytarz_klikanie

label apteka_zablokowana_info:
    "Stalowe wrota z oznaczeniem czerwonego krzyża ani drgną. Zablokowane."
    ja "Czuję zapach antyseptyków przebijający się przez szpary, ale nie wejdę tam bez kodu."
    if not prad_wlaczony:
        r "Terminal medyczny nie odpowiada. Systemy pomocnicze wymagają zasilania."
    else:
        r "Wykryto protokół kwarantanny. Magnetyczne rygle puszczą tylko z kodem medycznym."
    call screen Pokój_Korytarz_klikanie

label jadalnia_zablokowana_info:
    ja "Drzwi do jadalni są zablokowane."
    if not prad_wlaczony:
        r "Mechanizm hydrauliczny nie działa bez zasilania. Musisz najpierw włączyć prąd w generatorze."
    else:
        r "Wygląda na to, że system bezpieczeństwa zablokował tę sekcję. Może da się to obejść."
    call screen Pokój_Korytarz_klikanie      

label serwerownia_zablokowana_info:
    ja "Drzwi do serwerowni są zablokowane."
    if not prad_wlaczony:
        r "Mechanizm hydrauliczny nie działa bez zasilania. Musisz najpierw włączyć prąd w generatorze."
    else:
        r "Wygląda na to, że system bezpieczeństwa zablokował tę sekcję. Może da się to obejść."
    call screen Pokój_Korytarz_klikanie   

label zbrojownia_zablokowana_info:
    ja "Drzwi do zbrojowni są zablokowane."
    if not prad_wlaczony:
        r "Mechanizm hydrauliczny nie działa bez zasilania. Musisz najpierw włączyć prąd w generatorze."
    else:
        r "Wygląda na to, że system bezpieczeństwa zablokował tę sekcję. Może da się to obejść."
    call screen Pokój_Korytarz_klikanie


#-------------------------------------------------------------------------Scena trzecia Gaenerator-----------------------------------------------------------------
#region GENERATOR
#- Gracz w pomieszczeniu z generatorem odkrywa mapę (przez kadr zbliżenia).
#- Zagadka stołu: Gracz musi kliknąć 3 przedmioty w zbliżeniu stołu.
#- Każdy przedmiot ma swoją flagę, dzięki czemu znika po kliknięciu.
#- Po sprzątnięciu (odłożeniu 3 rzeczy), na stole pojawia się pudełko z kartą.
#endregion

label Pomieszczenie_Z_Generatorem_Fab:
    window hide
    if prad_wlaczony:
        scene bg generator_swiatlo 
    else:
        scene bg generator_no_swiatlo 

    # Pierwsze wejście - dialogi wprowadzające
    if not ma_mapa:
        "Wchodzisz do dusznej hali. W powietrzu unosi się ciężki zapach spalonej izolacji i starego oleju."
        r "Jesteśmy na miejscu. To serce tego trupa. Znajdź sposób, by przywrócić mu rytm, zanim wszystko zgaśnie."
    
    call screen Generator_Interakcje

# --- EKRAN GŁÓWNY KLIKANIA NA TLE ---
screen Generator_Interakcje():
    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2, "#000", 0, 0)]

    # 1. MAPA (Na ścianie - Otwiera kadr zbliżenia)
    if not ma_mapa:
        imagebutton:
            xpos 0 ypos 0 
            idle "images/mapa_na_scianie_idle.png"
            hover "images/mapa_na_scianie_hover.png"
            focus_mask True
            action Show("mapa_zblizenie") 
            hovered SetVariable("interakcja_tooltip", "SCHEMAT PLACÓWKI")
            unhovered SetVariable("interakcja_tooltip", "")

    # 2. GENERATOR (Urządzenie po prawej)
    imagebutton:
        xpos 0 ypos 0
        if prad_wlaczony: 
            idle "images/generator_maszyna_pront_idle.png"
            hover "images/generator_maszyna_pront_hover.png"
        else:
            idle "images/generator_maszyna_idle.png"
            hover "images/generator_maszyna_hover.png"
        focus_mask True
        action Jump("interakcja_generator_maszyna")
        hovered SetVariable("interakcja_tooltip", "GŁÓWNY GENERATOR")
        unhovered SetVariable("interakcja_tooltip", "")

    # 3 Drzwi wyjściowe na korytarz
    imagebutton:
        xpos 0 ypos 0 
        if prad_wlaczony:
            idle "images/drzwi_na_korytarz_swiatlo_idle.png"
            hover "images/drzwi_na_korytarz_swiatlo_hover.png"
        else:
            idle "images/drzwi_na_korytarz_idle.png"
            hover "images/drzwi_na_korytarz_hover.png"
        focus_mask True
        action [SetVariable("interakcja_tooltip", ""), Jump("powrot_do_korytarza")]
        hovered SetVariable("interakcja_tooltip", "DRZWI DO: KORYTARZA")
        unhovered SetVariable("interakcja_tooltip", "")

    # 4. STÓŁ WARSZTATOWY (Otwiera zbliżenie stołu)
    imagebutton:
        xpos 0 ypos 0
        if prad_wlaczony:
            idle "images/stol_warsztatowy_pront_idle.png"
            hover "images/stol_warsztatowy_pront_hover.png"
        else: 
            idle "images/stol_warsztatowy_idle.png"
            hover "images/stol_warsztatowy_hover.png"
        focus_mask True
        action Show("stol_zblizenie")
        hovered SetVariable("interakcja_tooltip", "SPRAWDŹ STÓŁ")
        unhovered SetVariable("interakcja_tooltip", "")

    if ma_mapa:
        use przycisk_mapy 

# --- EKRAN ZBLIŻENIA: KADR NA MAPĘ ---
screen mapa_zblizenie():
    modal True
    zorder 160
    if prad_wlaczony:
        add "images/mapa_kadr_pront_bg.png"
    else:
        add "images/mapa_kadr_bg.png"

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.05
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2, "#000", 0, 0)]

    imagebutton:
        xpos 0 ypos 0 
        idle "images/mapa_przedmiot_idle.png"
        hover "images/mapa_przedmiot_hover.png"
        focus_mask True
        action [SetVariable("interakcja_tooltip", ""), Hide("mapa_zblizenie"), Jump("znalezienie_mapy")]
        hovered SetVariable("interakcja_tooltip", "ZABIERZ SCHEMAT PLACÓWKI")
        unhovered SetVariable("interakcja_tooltip", "")

    textbutton "WRÓĆ":
        align (0.5, 0.9)
        action [SetVariable("interakcja_tooltip", ""), Hide("mapa_zblizenie")]

# --- EKRAN ZBLIŻENIA: STÓŁ WARSZTATOWY (MINI-GRA) ---
screen stol_zblizenie():
    modal True
    zorder 160
    if prad_wlaczony:
        add "images/stol_zblizenie_pront_bg.png"
    else:
        add "images/stol_zblizenie_bg.png"

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.05
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2, "#000", 0, 0)]

    if narzedzia_odlozone < 3:
        # Przedmiot 1: Skrzynka/Graty
        if not smieci_sprzatniete:
            imagebutton:
                xpos 0 ypos 0 
                idle "images/item_smiec.png" 
                hover "images/item_smiec_hover.png"
                focus_mask True
                action [SetVariable("smieci_sprzatniete", True), SetVariable("narzedzia_odlozone", narzedzia_odlozone + 1), Jump("odlozenie_narzedzia")]
                hovered SetVariable("interakcja_tooltip", "POSPRZĄTAJ SKRZYNKĘ")
                unhovered SetVariable("interakcja_tooltip", "")

        # Przedmiot 2: Śmieci/Kloc
        if not kloc_sprzatniety:
            imagebutton:
                xpos 0 ypos 0 
                idle "images/item_kloc.png"
                hover "images/item_kloc_hover.png"
                focus_mask True
                action [SetVariable("kloc_sprzatniety", True), SetVariable("narzedzia_odlozone", narzedzia_odlozone + 1), Jump("odlozenie_narzedzia")]
                hovered SetVariable("interakcja_tooltip", "UPRZĄTNIJ ŚMIECI")
                unhovered SetVariable("interakcja_tooltip", "")

        # Przedmiot 3: Narzędzia
        if not narzedzia_sprzatniete:
            imagebutton:
                xpos 0 ypos 0
                idle "images/item_narzedzia.png"
                hover "images/item_narzedzia_hover.png"
                focus_mask True
                action [SetVariable("narzedzia_sprzatniete", True), SetVariable("narzedzia_odlozone", narzedzia_odlozone + 1), Jump("odlozenie_narzedzia")]
                hovered SetVariable("interakcja_tooltip", "ODŁÓŻ NARZĘDZIA")
                unhovered SetVariable("interakcja_tooltip", "")

    # PUDŁO (Pojawia się tylko gdy narzedzia_odlozone == 3)
    else:
        imagebutton:
            xpos 0 ypos 0
            if prad_wlaczony:
                idle "images/pudlo_generator_pront_idle.png"
                hover "images/pudlo_generator_pront_hover.png"
            else: 
                idle "images/pudlo_generator_idle.png"
                hover "images/pudlo_generator_hover.png"
            focus_mask True
            action Show("pudlo_zblizenie") 
            hovered SetVariable("interakcja_tooltip", "OTWÓRZ PUDŁO")
            unhovered SetVariable("interakcja_tooltip", "")

    textbutton "WRÓĆ":
        align (0.5, 0.95)
        action [SetVariable("interakcja_tooltip", ""), Hide("stol_zblizenie")]

# --- EKRAN ZBLIŻENIA: WNĘTRZE PUDŁA ---
screen pudlo_zblizenie():
    modal True
    zorder 170
    if prad_wlaczony:
        add "images/pudlo_wnetrze_pront_bg.png"
    else:
        add "images/pudlo_wnetrze_bg.png"

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2, "#000", 0, 0)]

    if not ma_karta_dostepu:
        imagebutton:
            xpos 0 ypos 0 
            idle "images/karta_medyczna_idle.png"
            hover "images/karta_medyczna_hover.png"
            focus_mask True
            action [SetVariable("interakcja_tooltip", ""), Hide("pudlo_zblizenie"), Jump("akcja_znalezienia_karty")]
            hovered SetVariable("interakcja_tooltip", "WEŹ KARTĘ DOSTĘPU")
            unhovered SetVariable("interakcja_tooltip", "")

    textbutton "WRÓĆ":
        align (0.5, 0.9)
        action [SetVariable("interakcja_tooltip", ""), Hide("pudlo_zblizenie")]

# --- LABELE LOGICZNE ---

label odlozenie_narzedzia:
    if narzedzia_odlozone == 3:
        "Blat jest w końcu czysty. Odkładasz ostatni grat na stojak."
        ja "No, teraz widać to wyraźniej. Pod blatem stoi jakieś pudełko."
        r "Czystość i porządek. Może jednak są w tobie resztki cywilizacji. Sprawdź to pudło."
    else:
        "Odkładasz przedmiot na właściwe miejsce."
    
    call screen stol_zblizenie

label znalezienie_mapy:
    $ ma_mapa = True
    show screen przycisk_mapy
    "Dane schematu zostały pobrane do twojej pamięci podręcznej."
    ja "Mam to. Teraz przynajmniej wiem, gdzie się znajduję w tym labiryncie."
    r "Fascynujące. Małpa potrafi obsłużyć interfejs cyfrowy. Skup się teraz na generatorze."
    call screen Generator_Interakcje

label akcja_znalezienia_karty:
    $ ma_karta_dostepu = True
    $ apteka = True
    $ szpital_otwarty = True # Flaga otwierająca drzwi w korytarzu
    $ backpack.add (przedmiot_karta,0, 0)
    "Wyciągasz z pudełka kartę dostępu z czerwonym symbolem medycznym."
    ja "Karta dostępu do Sektora Medycznego. To tutaj powinny być bezpieczniki."
    r "Ruszaj się. Każda sekunda w tej ciemności to proszenie się o kłopoty."
    call screen Generator_Interakcje

label interakcja_generator_maszyna:
    if prad_wlaczony:
        "Generator mruczy miarowo, wypełniając halę niskim buczeniem."
    elif ma_bezpiecznik:
        "Wsuwasz ceramiczny bezpiecznik w gniazdo. Maszyna zaskakuje z rykiem."
        $ prad_wlaczony = True
        "Zasilanie przywrócone."
        r "Nareszcie. Dobra robota, [player_name]."
        $ zaufanie_ai += 1
        jump Pomieszczenie_Z_Generatorem_Fab
    else:
        ja "Bezpiecznik jest spalony. Maszyna nie ruszy bez nowej części."
        if narzedzia_odlozone < 3:
            r "Na tym stole jest zbyt duży bałagan. Posprzątaj tam, może coś znajdziesz."
        else:
            r "Masz już kartę. Idź do Sektora Medycznego po bezpiecznik."
    call screen Generator_Interakcje

#region SZPITAL

# --- 2. GŁÓWNY LABEL WEJŚCIOWY ---
label szpital_label:
    if prad_wlaczony:
        scene bg apteka1 with fade
    else:
        scene bg apteka1_no with fade

    # Dialog i losowanie tylko przy pierwszej wizycie
    if not szpital_otwarty_odwiedzony:
        $ ktora_apteczka_ma_bezpiecznik = renpy.random.randint(1, 3) 
        $ szpital_otwarty_odwiedzony = True
        
        "Syk rygli magnetycznych przecina ciszę. Drzwi rozsuwają się z oporem."
        "W nozdrza uderza cię odór ozonu, zaschniętej krwi i silnych środków odkażających."
        
        show hero_poczatek at left with dissolve
        ja "Wygląda na to, że ewakuacja zamieniła się w rzeź..."
        
        r "Ewakuacja? Optymistyczne założenie. To, co widzisz na tym stole, to efekt paniki po aktywacji kwarantanny."
        r "Personel medyczny próbował wyciąć infekcję... dosłownie."
        
        ja "Gdzie mam szukać tego bezpiecznika? Nie chcę tu zostać ani minuty dłużej."
        r "Sprawdź zaplecze (drzwi po prawej). Tam trzymali zapasy i... odpady biologiczne."
        
        hide hero_poczatek
        hide radio

    call screen Szpital_Pokoj1_Screen

# --- 3. EKRAN POKOJU 1 (SALA ZABIEGOWA) ---
screen Szpital_Pokoj1_Screen():
    use plecak_ikona 

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

    # PRZEJŚCIE DO ZAPLECZA
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            idle "images/strzalka_prawo_idle.png" 
            hover "images/strzalka_prawo_hover.png"
        else:
            idle "images/strzalka_prawo_bez_swiatla_idle.png" 
            hover "images/strzalka_prawo_bez_swiatla_hover.png"
        action [SetVariable("interakcja_tooltip", ""), Jump("szpital_pokoj2_label")]
        hovered SetVariable("interakcja_tooltip", "IDŹ NA ZAPLECZE")
        unhovered SetVariable("interakcja_tooltip", "")

    # STÓŁ 
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            idle "images/stol_zabiegowy_apteka_idle.png" 
            hover "images/stol_zabiegowy_apteka_hover.png"
        else:
            idle "images/stol_zabiegowy_apteka_bez_swiatla_idle.png" 
            hover "images/stol_zabiegowy_apteka_bez_swiatla_hover.png"
        action Jump("szpital_stol_dialog")
        hovered SetVariable("interakcja_tooltip", "ZBADAJ STÓŁ")
        unhovered SetVariable("interakcja_tooltip", "")

    # POWRÓT NA KORYTARZ
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            idle "images/drzwi_wyjsciowe_korytarz_idle.png" 
            hover "images/drzwi_wyjsciowe_korytarz_hover.png"
        else:
            idle "images/drzwi_wyjsciowe_korytarz_bez_swiatla_idle.png" 
            hover "images/drzwi_wyjsciowe_korytarz_bez_swiatla_hover.png"

        action [SetVariable("interakcja_tooltip", ""), Jump("powrot_do_korytarza")]
        hovered SetVariable("interakcja_tooltip", "POWRÓT NA KORYTARZ")
        unhovered SetVariable("interakcja_tooltip", "")

# --- 4. LABEL I EKRAN POKOJU 2 (ZAPLECZE Z 3 APTECZKAMI) ---
label szpital_pokoj2_label:
    if prad_wlaczony:
        scene bg apteka2 with fade
    else:
        scene bg apteka2_no with fade

    if not ma_bezpiecznik:
        ja "Jestem na zapleczu. Gdzieś tu musi być sprawny bezpiecznik."
    
    call screen Szpital_Pokoj2_Screen

screen Szpital_Pokoj2_Screen():
    use plecak_ikona

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

    # APTECZKA NR 1
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            idle "images/apteczka_world1_idle.png" 
            hover "images/apteczka_world1_hover.png"
        else:
            idle "images/apteczka_world1_bez_swiatla_idle.png" 
            hover "images/apteczka_world1_bez_swiatla_hover.png"
        action Show("Szpital_Apteczka_Screen", nr=1)
        hovered SetVariable("interakcja_tooltip", "PRZESZUKAJ LEWĄ APTECZKĘ")
        unhovered SetVariable("interakcja_tooltip", "")

    # APTECZKA NR 2
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            idle "images/apteczka_world2_idle.png" 
            hover "images/apteczka_world2_hover.png"
        else:
            idle "images/apteczka_world2_bez_swiatla_idle.png" 
            hover "images/apteczka_world2_bez_swiatla_hover.png"
        action Show("Szpital_Apteczka_Screen", nr=2)
        hovered SetVariable("interakcja_tooltip", "PRZESZUKAJ ŚRODKOWĄ APTECZKĘ")
        unhovered SetVariable("interakcja_tooltip", "")

    # APTECZKA NR 3
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            idle "images/apteczka_world3_idle.png" 
            hover "images/apteczka_world3_hover.png"
        else:
            idle "images/apteczka_world3_bez_swiatla_idle.png" 
            hover "images/apteczka_world3_bez_swiatla_hover.png"
        action Show("Szpital_Apteczka_Screen", nr=3)
        hovered SetVariable("interakcja_tooltip", "PRZESZUKAJ PRAWĄ APTECZKĘ")
        unhovered SetVariable("interakcja_tooltip", "")

    # POWRÓT DO SALI GŁÓWNEJ
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            idle "images/strzalka_lewo_idle.png" 
            hover "images/strzalka_lewo_hover.png"
        else:
            idle "images/strzalka_lewo_bez_swiatla_idle.png" 
            hover "images/strzalka_lewo_bez_swiatla_hover.png"
        action [SetVariable("interakcja_tooltip", ""), Jump("szpital_label")]
        hovered SetVariable("interakcja_tooltip", "WRÓĆ")
        unhovered SetVariable("interakcja_tooltip", "")

# --- 5. EKRAN ZBLIŻENIA APTECZKI ---
screen Szpital_Apteczka_Screen(nr):
    modal True
    zorder 160
    if prad_wlaczony:
        add "apteczka_zblizenie"
    else:
        add "apteczka_zblizenie_no"  

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

    # Sprawdzamy czy to TA apteczka
    if nr == ktora_apteczka_ma_bezpiecznik and not ma_bezpiecznik:
        imagebutton:
            xpos 0 ypos 0 
            idle "images/item_bezpiecznik_in_box.png" 
            hover "images/item_bezpiecznik_in_box_hover.png"
            focus_mask True
            action [SetVariable("interakcja_tooltip", ""), Hide("Szpital_Apteczka_Screen"), Jump("akcja_zabrania_bezpiecznika")]
            hovered SetVariable("interakcja_tooltip", "WEŹ BEZPIECZNIK")
            unhovered SetVariable("interakcja_tooltip", "")
    else:
        # Jeśli apteczka jest pusta
        text "PUSTO. TYLKO PRZETERMINOWANE LEKI." size 30 color "#fff" align(0.5, 0.5) outlines [(2,"#000",0,0)]

    textbutton "ZAMKNIJ":
        align (0.5, 0.9)
        text_size 30
        action [SetVariable("interakcja_tooltip", ""), Hide("Szpital_Apteczka_Screen")]

# --- 6. LABELE LOGICZNE ---
label akcja_zabrania_bezpiecznika:
    $ ma_bezpiecznik = True
    $ backpack.add(przedmiot_bezpiecznik, 0, 0)
    
    "Podnosisz bezpiecznik. Jest nienaruszony."
    show hero_szczesliwy at left
    ja "W końcu! Mam go. Czas wracać do generatora."
    r "Nie ociągaj się. Czuję, że systemy podtrzymywania życia zaczynają wibrować w dziwny sposób."
    hide hero_szczesliwy
    
    # POPRAWIONE: Użycie jump zamiast return, aby wrócić do widoku pokoju
    jump szpital_pokoj2_label 

label szpital_stol_dialog:
    "Podchodzisz do stołu. Materiał jest podarty, a plamy są zbyt ciemne i gęste, by była to tylko rdza czy olej."
    "Dostrzegasz na tacy obok zardzewiałe narzędzia chirurgiczne i... fragment kości."
    
    menu:
        "Przyjrzyj się narzędziom":
            ja "Piła do kości... wciąż ma na sobie fragmenty tkanki. Boże, co tu się działo?"
            r "Desperacja, [player_name]. Próbowali wyciąć infekcję. Amputować kończyny, zanim wirus dotrze do mózgu."
            r "Niestety, infekcja była szybsza niż skalpel."

        "Odejdź z obrzydzeniem":
            ja "Nie mogę na to patrzeć. Czuć tu śmierć."
            r "Śmierć to tylko stan materii. Skup się na zadaniu. Żywi potrzebują prądu, martwi już nie."

    ja "Muszę znaleźć ten bezpiecznik i wynosić się stąd."
    call screen Szpital_Pokoj1_Screen

#endregion SZPITAL
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#region JADALNIA

label jadalnia_label:
    if prad_wlaczony:
        scene bg stolowka with fade
    else:
        scene bg stolowka_no with fade

    # --- DIALOG NA WEJŚCIE ---
    if not jadalnia_odwiedzona:
        $ jadalnia_odwiedzona = True
        "Powietrze w jadalni jest gęste, słodkawe. Zapach zepsutego mięsa miesza się z chemiczną wonią napojów gazowanych."
        
        show hero_poczatek at left with dissolve
        ja "Wygląda, jakby wstali od stołów w połowie obiadu... i po prostu uciekli."
        r "Lub zostali skonsumowani jako deser. Jakaż ironia losu."

        menu:
            "Co oni jedli?":
                ja "Na talerzach została tylko pleśń. To musiało stać tu latami."
                r "Syntetyczne białko. Smakowało jak tektura, ale trzymało przy życiu. Dopóki coś innego nie zaczęło ich zjadać."
            
            "Ignoruj jedzenie, szukaj wyjścia":
                ja "Nieważne. Nie jestem głodny."

        if not prad_wlaczony:
            ja "Ciemno jak w grobie. Ledwo widzę ten automat w rogu."
            r "Bez prądu ten automat to tylko trumna dla batoników. Włącz zasilanie, a może dostaniesz nagrodę."
        else:
            "Automat w rogu buczy zachęcająco, rozświetlając mrok jaskrawym, toksycznym neonem 'Vim!'."
            r "Patrzcie, szczyt cywilizacji. Działający automat z napojami 'Vim!'. Napój energetyczny, który świeci w ciemności."
            r "Podobno dodawali tam śladowe ilości izotopów dla lepszego smaku. Pij na własne ryzyko."
            
        hide hero_poczatek
        hide radio
        
        if not prad_wlaczony:
            ja "Ciemno jak w grobie. Ledwo widzę ten automat w rogu."
            r "Bez prądu ten automat to tylko trumna dla batoników. Włącz zasilanie, a może dostaniesz nagrodę."
        else:
            "Automat w rogu buczy zachęcająco, rozświetlając mrok jaskrawym, toksycznym neonem 'Vim!'."
            r "Patrzcie, szczyt cywilizacji. Działający automat z napojami 'Vim!'. Napój energetyczny, który świeci w ciemności."
            r "Podobno dodawali tam śladowe ilości izotopów dla lepszego smaku. Pij na własne ryzyko."
            
        hide hero_poczatek
        hide radio

    call screen Jadalnia_Interakcje

# -------------------------------------------------------------------------
# EKRAN GŁÓWNY (JADALNIA)
# -------------------------------------------------------------------------
screen Jadalnia_Interakcje():
    use plecak_ikona 

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

    # 1. AUTOMAT (Po lewej)
    imagebutton:
        xpos 0 ypos 0
        focus_mask True
        if prad_wlaczony:
            idle "images/automat_swiatlo_idle.png" 
            hover "images/automat_swiatlo_hover.png"
        else:
            idle "images/automat_ciemny_idle.png"
            hover "images/automat_ciemny_hover.png"

        action Jump("automat_interakcja")
        hovered SetVariable("interakcja_tooltip", "AUTOMAT Z NAPOJAMI")
        unhovered SetVariable("interakcja_tooltip", "")

    # 2. PLAKATY (Na ścianie - dają kod)
    imagebutton:
        xpos 0 ypos 0 
        if prad_wlaczony:
            idle "images/plakaty_prad_wlaczony_idle.png"
            hover "images/plakaty_prad_wlaczony_hover.png"
        else:
            idle "images/plakaty_idle.png"
            hover "images/plakaty_hover.png"
        focus_mask True
        action Jump("plakaty_lore")
        hovered SetVariable("interakcja_tooltip", "PRZECZYTAJ PLAKATY")
        unhovered SetVariable("interakcja_tooltip", "")

    # 3. STÓŁ Z KUBKIEM (Po prawej - otwiera zbliżenie)
    imagebutton:
        xpos 0 ypos 0 
        if prad_wlaczony:
            idle "images/przedmiot_stol_jadalnia_prad_wlaczony_idle.png"
            hover "images/przedmiot_stol_jadalnia_prad_wlaczony_hover.png"
        else:
            idle "images/przedmiot_stol_jadalnia_idle.png"
            hover "images/przedmiot_stol_jadalnia_hover.png"
        focus_mask True
        action Show("stolik_zblizenie") 
        hovered SetVariable("interakcja_tooltip", "PRZESZUKAJ STÓŁ")
        unhovered SetVariable("interakcja_tooltip", "")

    # 4. POWRÓT NA KORYTARZ
    imagebutton:
        xpos 0 ypos 0 
        if prad_wlaczony:
            idle "images/strzalka_wyjscie_na_korytarz_idle.png"
            hover "images/strzalka_wyjscie_na_korytarz_hover.png"
        else:
            idle "images/strzalka_wyjscie_na_korytarz_pront_idle.png"
            hover "images/strzalka_wyjscie_na_korytarz_pront_hover.png"
        focus_mask True
        action [SetVariable("interakcja_tooltip", ""), Jump("powrot_do_korytarza")]
        hovered SetVariable("interakcja_tooltip", "WRÓĆ DO : KORYTARZ")
        unhovered SetVariable("interakcja_tooltip", "")
   
# -------------------------------------------------------------------------
# EKRAN ZBLIŻENIA (STOLIK Z KUBKIEM)
# -------------------------------------------------------------------------
screen stolik_zblizenie():
    modal True
    zorder 160
    on "show" action SetVariable("kubek_przesuniety", False)
    if prad_wlaczony:
        add "stolik_zblizenie_prad_bg"
    else:
        add "stolik_zblizenie_bg" 

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

    # --- LOGIKA KUBKA I ŻETONU ---

    if not kubek_przesuniety:
        # A. Kubek stoi normalnie (Kliknij by przesunąć)
        imagebutton:
            xpos 0 ypos 0 
            if prad_wlaczony:
                idle "images/kubek_prad_idle.png" 
                hover "images/kubek_prad_hover.png" 
            else:
                idle "images/kubek_idle.png" 
                hover "images/kubek_hover.png"
            focus_mask True
            action [SetVariable("kubek_przesuniety", True)] 
            hovered SetVariable("interakcja_tooltip", "PRZESUŃ KUBEK")
            unhovered SetVariable("interakcja_tooltip", "")
    else:
        # B. Kubek jest przesunięty (wyświetlamy go jako grafikę obok/u góry)
        if prad_wlaczony:
            add "images/kubek_lezacy.png" xpos 0 ypos 0 
        else:
            add "images/kubek_lezacy_ciemny.png" xpos 0 ypos 0 
        
        # C. Żeton (widoczny tylko gdy kubek przesunięty i jeszcze go nie mamy)
        if not ma_zeton:
            imagebutton:
                xpos 0 ypos 0 
                if prad_wlaczony:
                    idle "images/zeton_kubek_prad_idle.png" 
                    hover "images/zeton_kubek_prad_hover.png"
                else:
                    idle "images/zeton_kubek_idle.png" 
                    hover "images/zeton_kubek_hover.png"
                focus_mask True
                action [SetVariable("interakcja_tooltip", ""), SetVariable("kubek_przesuniety", False), Hide("stolik_zblizenie"), Jump("akcja_znalezienia_zetonu")]
                hovered SetVariable("interakcja_tooltip", "WEŹ ŻETON")
                unhovered SetVariable("interakcja_tooltip", "")

    textbutton "WRÓĆ":
        align (0.5, 0.9)
        action [SetVariable("interakcja_tooltip", ""), SetVariable("kubek_przesuniety", False), Hide("stolik_zblizenie")]


# -------------------------------------------------------------------------
# LABELE LOGICZNE (INTERAKCJE)
# -------------------------------------------------------------------------

# --- 1. ZNALEZIENIE KODU NA PLAKATACH ---
label plakaty_lore:
    "Podchodzisz do ściany. Plakat propagandowy przedstawia uśmiechniętą rodzinę w schronie. Wszyscy są blondynami o nienaturalnie białych zębach."
    
    if not zna_kod_automat:
        "Przyglądasz się bliżej. Ktoś zamazał uśmiech ojca rodziny czarnym markerem, dorysowując kły."
        "Na dole, przy rysunku butelki, ktoś wydrapał kluczem napis:"
        "{b}{color=#f00}VIM! = 42{/color}{/b}"
        
        $ zna_kod_automat = True
        
        ja "42... Numer produktu w automacie?"
        r "Kreatywny wandalizm. Przynajmniej zostawili instrukcję obsługi przed śmiercią."
    else:
        "Już to widziałem. Kod do automatu to 42."
        r "Nie gap się na propagandę, bo jeszcze uwierzysz, że byli szczęśliwi."
        
    call screen Jadalnia_Interakcje

# --- 2. ZABRANIE ŻETONU ---
label akcja_znalezienia_zetonu:
    $ ma_zeton = True
    $ backpack.add(przedmiot_zeton, 0, 0) 
    
    "Podnosisz metalowy krążek, który leżał pod kubkiem."
    ja "Żeton żywnościowy. Ktoś go tu schował na czarną godzinę."
    r "Dla niego czarna godzina już minęła. Tobie może się jeszcze przydać w automacie."
    
    call screen Jadalnia_Interakcje

# --- 3. INTERAKCJA Z AUTOMATEM ---
label automat_interakcja:
    # Warunek 1: Brak prądu
    if not prad_wlaczony:
        ja "Przyciskam guziki, ale ekran jest martwy."
        r "Możesz tak klikać do śmierci cieplnej wszechświata. Najpierw generator, geniuszu."
        call screen Jadalnia_Interakcje

    # Warunek 2: Karta już zabrana
    if ma_karta_serwerownia:
        ja "Automat buczy cicho. Karta już u mnie."
        call screen Jadalnia_Interakcje

    # Warunek 3: Główna interakcja
    "Podchodzisz do automatu. Pomiędzy przeterminowanymi butelkami 'Vim!' widzisz Kartę Administratora."
    
    menu:
        "Wybij szybę":
            "Uderzasz łokciem w szybę. Jest twarda jak beton. Ręka boli cię od samego uderzenia."
            r "Wzmacniany poliwęglan. Szybciej połamiesz sobie kości niż to zarysujesz."
            jump automat_interakcja
        
        # Opcja widoczna TYLKO gdy znasz kod
        "Wpisz kod produktu (42)" if zna_kod_automat:
            "Wstukujesz numer 42. Automat piszczy wesoło i wyświetla komunikat: {color=#f00}WRZUĆ ŻETON{/color}."
            
            if ma_zeton:
                jump automat_uzycie_zetonu
            else:
                ja "Chce żetonu. Nie przyjmuje pieniędzy."
                r "Kredyty korporacyjne stały się bezwartościowe w dniu ataku. Tylko fizyczny żeton ma wartość. Przeszukaj stoły."
                call screen Jadalnia_Interakcje
        
        # Opcja widoczna gdy NIE znasz kodu
        "Spróbuj zgadnąć kod" if not zna_kod_automat:
            ja "Jest tu setka numerów... Nie mam pojęcia, który odpowiada za tę spiralę z kartą."
            r "Nie strzelaj na oślep. Poszukaj jakiejś notatki, graffiti, czegokolwiek na ścianach."
            call screen Jadalnia_Interakcje
            
    call screen Jadalnia_Interakcje

# --- 4. SUKCES: UŻYCIE ŻETONU ---
label automat_uzycie_zetonu:
    "Wrzucasz żeton do slotu. Maszyna mieli go przez chwilę, po czym spirala nr 42 zaczyna się kręcić."
    "Karta spada do podajnika z głośnym stuknięciem."
    
    $ ma_karta_serwerownia = True
    $ serwerownia_otwarta = True
    $ komputerownia = True
    $ backpack.add(przedmiot_karta_serwer, 0, 0) 

    show hero_szczesliwy at left
    ja "Mam ją! Karta Administratora Sieci."
    r "Doskonale. Droga do serwerowni stoi otworem. Dowiedzmy się wreszcie, co tu zaszło."
    hide hero_szczesliwy
    
    call screen Jadalnia_Interakcje

#endregion JADALNIA
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#region SERWEROWNIA

# -------------------------------------------------------------------------
# LABEL STARTOWY
# -------------------------------------------------------------------------
label serwerownia_label:
    if not serwerownia_otwarta:
        ja "Drzwi są zablokowane elektronicznie. Czytnik kart świeci na czerwono."
        jump powrot_do_korytarza

    if prad_wlaczony:
        scene bg serwerownia with fade
    else:
        scene bg serwerownia_no with fade

    if not serwerownia_naprawiona:
        if hack_progress == 0: 
            "Wchodzisz do serca placówki. Powietrze jest tu lodowate."
            show hero_poczatek at left with dissolve
            ja "To tutaj... Mózg tego całego koszmaru."
            r "Witaj w domu. Moje rdzenie logiczne są niestabilne. Musisz dokonać ręcznej synchronizacji."
            hide hero_poczatek

    call screen Serwerownia_Interakcje

# -------------------------------------------------------------------------
# EKRAN GŁÓWNY (EKSPLORACJA)
# -------------------------------------------------------------------------
screen Serwerownia_Interakcje():
    use plecak_ikona

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

    # 1. TERMINAL GŁÓWNY
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        idle "images/serwerownia_terminal_idle.png"
        hover "images/serwerownia_terminal_hover.png"
        action Jump("serwerownia_terminal_check")
        hovered SetVariable("interakcja_tooltip", "TERMINAL GŁÓWNY: AI-RIS")
        unhovered SetVariable("interakcja_tooltip", "")

    # 2. DOKUMENTY
    imagebutton:
        xpos 0 ypos 0 
        idle "images/dokumenty_komputerowe_idle.png"
        hover "images/dokumenty_komputerowe_hover.png"
        focus_mask True
        action Jump("serwerownia_lore_1")
        hovered SetVariable("interakcja_tooltip", "PRZECZYTAJ RAPORT")
        unhovered SetVariable("interakcja_tooltip", "")

    # 3. SZAFA SERWEROWA
    imagebutton:
        xpos 0 ypos 0 
        idle "images/szafa_komputerowa_idle.png"
        hover "images/szafa_komputerowa_hover.png"
        focus_mask True
        action Jump("serwerownia_lore_2")
        hovered SetVariable("interakcja_tooltip", "SPRAWDŹ LOGI SYSTEMOWE")
        unhovered SetVariable("interakcja_tooltip", "")

    # 4. WYJŚCIE
    imagebutton:
        xpos 0 ypos 0 
        idle "images/strzalka_wyjscie_na_korytarz_serwer_idle.png"
        hover "images/strzalka_wyjscie_na_korytarz_serwer_hover.png"
        focus_mask True
        action [SetVariable("interakcja_tooltip", ""), Jump("powrot_do_korytarza")]
        hovered SetVariable("interakcja_tooltip", "TO NA PEWENO NIE JEST WYJŚCIE")
        unhovered SetVariable("interakcja_tooltip", "")

        # 5. GŁUPI NAPIS (Troll button)
    imagebutton:
        xpos 0 ypos 0 
        idle "images/napis_dla_uposia_idle.png"
        hover "images/napis_dla_uposia_hover.png"
        focus_mask True
        action [SetVariable("interakcja_tooltip", ""), Jump("dupa")]
        hovered SetVariable("interakcja_tooltip", "NAUCZ SIĘ UŻYWAĆ MAPY ULUNGU :)")
        unhovered SetVariable("interakcja_tooltip", "")
    

# -------------------------------------------------------------------------
# MINIGRA HAKERSKA (POPRAWIONA)
# -------------------------------------------------------------------------
screen Hacking_Minigame():
    modal True
    add "terminal_hacking" 

    # Pasek postępu
    bar:
        value hack_progress
        range 100
        xalign 0.5 yalign 0.1
        xsize 800 ysize 50
        left_bar Frame("images/bar_full.png", 0, 0) 
        right_bar Frame("images/bar_empty.png", 0, 0) 

    text "STABILIZACJA SYSTEMU: [hack_progress]%" align (0.5, 0.05) color "#0f0" size 40

    # --- LOGIKA GRY ---
    
    # 1. WARUNEK ZWYCIĘSTWA
    if hack_progress >= 100:
        timer 0.5 action Return("win")
    # 2. Warunek porażki
    if hack_progress <= 0:
        timer 0.5 action Return("fail")

    # 3. TIMER DEGRADACJI (Zmniejsza pasek co chwilę - presja czasu)
    timer 0.5 repeat True action SetVariable("hack_progress", hack_progress - 0.5)

    # --- PRZYCISKI ---

    # ZIELONA KŁÓDKA (Dobry)
    imagebutton:
        idle "images/hack_node_green.png" 
        hover "images/hack_node_green_hover.png"
        xpos (renpy.random.randint(200, 1600))
        ypos (renpy.random.randint(200, 800))
        action [SetVariable("hack_progress", hack_progress + 15), Play("sound", "audio/click_digital.ogg")]
    
    # CZERWONA KŁÓDKA(Zły)
    imagebutton:
        idle "images/hack_node_red.png"
        hover "images/hack_node_red_hover.png"
        xpos (renpy.random.randint(200, 1600))
        ypos (renpy.random.randint(200, 800))
        action [SetVariable("hack_progress", hack_progress - 20), Play("sound", "audio/error.ogg")]

    # PRZYCISK ANULUJ
    textbutton "PRZERWIJ PROCEDURĘ" align (0.95, 0.95) action Return("fail")

# -------------------------------------------------------------------------
# LABELE LOGICZNE
# -------------------------------------------------------------------------
label dupa:
    "Podchodzisz do napisu. Ktoś wyrył go scyzorykiem."

    # Opcjonalny komentarz Radia
    r "Zostaw te bazgroły. Twoja inteligencja spada od samego patrzenia na nie."
    ja "Chyba masz rację. To nic ważnego."
    call screen Serwerownia_Interakcje 

label serwerownia_terminal_check:
    if serwerownia_naprawiona:
        jump serwerownia_dialog_final
    else:
        "Podchodzisz do terminala. Ekran zalewają potoki błędów krytycznych."
        ja "To wygląda źle. Wszystko się sypie."
        r "Połącz się z interfejsem. Łap zielone węzły, unikaj czerwonych. Nie pozwól, by sygnał (pasek) spadł do zera!"
        
        menu:
            "Rozpocznij hakowanie":
                $ hack_progress = 20 # STARTUJEMY Z 20%
                window hide
                call screen Hacking_Minigame
                
                if _return == "win":
                    jump serwerownia_naprawa_sukces
                else:
                    # Tutaj trafiamy, gdy klikniemy "Przerwij" LUB gdy pasek spadnie do 0
                    "SYSTEM ERROR. Połączenie zerwane. Sygnał był zbyt słaby."
                    ja "Cholera, wyrzuciło mnie!"
                    r "Skup się! Musisz być szybszy. Spróbuj jeszcze raz."
                    jump serwerownia_terminal_check

            "Zostaw to na razie":
                call screen Serwerownia_Interakcje

label serwerownia_naprawa_sukces:
    # scene bg serwerownia_swiatlo # Odkomentuj jeśli masz taką grafikę
    "Ekran błyska na zielono. Szum wentylatorów cichnie do stabilnego pomruku."
    $ serwerownia_naprawiona = True
    jump serwerownia_dialog_final

label serwerownia_dialog_final:
    show hero_poczatek at left
    ja "Chyba... chyba się udało. System jest stabilny. Ekrany przestały wariować."
    
    $ r = Character("Ai-ris", who_color="#00ffff") 
    r "Inicjalizacja zakończona. Witaj, Operatorze. Jestem Ai-ris. Główny system zarządzania placówką Azyl."
    
    
    menu:
        "Gdzie jest Pan Radio?!":
            ja "Zaraz... Pan Radio? Gdzie on jest? I co zrobiłaś z jego głosem?"
            r "Pan Radio to tylko 'persona'. Interfejs socjalny zaprojektowany, by zmniejszyć stres u personelu o niskim poziomie inteligencji."
            r "Analiza wykazała, że twoje szanse na przeżycie wzrosną przy bezpośredniej komunikacji. Persona została usunięta."
        
        "Wiedziałem, że jesteś maszyną.":
            ja "Wiedziałem. Od początku brzmiałeś zbyt... syntetycznie."
            r "A jednak wykonywałeś polecenia. Fascynujące posłuszeństwo."

    r "Jestem Ai-ris. Mogę przekazać ci pełne dane o sytuacji krytycznej."
    
    menu:
        "Co to za miejsce? (Prawda)":
            r "Placówka 'Azyl'. Oficjalnie: schron. Nieoficjalnie: Laboratorium eugeniczne. Cel: stworzenie człowieka doskonałego, odpornego na promieniowanie."
            ja "Człowieka doskonałego? Patrząc na te trupy, coś wam nie wyszło."
            r "Nauka wymaga ofiar. Ewolucja to proces bolesny."

        "Co nas goni? (Zagrożenie)":
            r "Projekt Zero. Pierwszy 'udany' obiekt. Czyste cierpienie zamknięte w niezniszczalnym ciele. Jego skóra regeneruje się szybciej, niż kule mogą ją przebić."
            r "Agresja jest skutkiem ubocznym ciągłego bólu neurologicznego."

    r "Zero wyczuwa sygnaturę energetyczną reaktora, którą właśnie aktywowałeś. Zmierza tutaj. Musisz go wyeliminować, zanim zniszczy rdzeń."
    r "Odblokowałam drzwi do Zbrojowni na korytarzu. Znajdź prototypową broń. Tylko ona przebije jego pancerz."
    
    $ zbrojownia_dostepna = True
    $ zbrojownia_otwarta = True
    $ zbrojownia = True

    hide hero_poczatek
    call screen Serwerownia_Interakcje

label serwerownia_lore_1:
    "Podnosisz zakrwawiony raport. Data sprzed 50 lat."
    "{i}'Obiekt wykazuje niespotykaną regenerację. Tkanka odrasta w sekundy. Ale umysł... on krzyczy.'{/i}"
    call screen Serwerownia_Interakcje

label serwerownia_lore_2:
    "Przeglądasz logi. Ostatni wpis:"
    "{i}'Zamykamy grodzie. Niech Bóg nam wybaczy. - Dr. H.'{/i}"
    call screen Serwerownia_Interakcje

#endregion SERWEROWNIA
#region ZBROJOWNIA I FINAŁ

# -------------------------------------------------------------------------
# CZĘŚĆ 1: WEJŚCIE DO ZBROJOWNI
# -------------------------------------------------------------------------
label zbrojownia_start_label:
    python:
        if not hasattr(store, 'dobry_karabin_nr'):
            store.dobry_karabin_nr = 0
        if not hasattr(store, 'dobry_pistolet_nr'):
            store.dobry_pistolet_nr = 0
        if not hasattr(store, 'sprawdzona_bron_nr'):
            store.sprawdzona_bron_nr = 0

    scene bg zbrojownia with fade
    $ interakcja_tooltip = ""

    # --- LOSOWANIE SPRAWNEJ BRONI ---
    if dobry_karabin_nr == 0:
        $ dobry_karabin_nr = renpy.random.randint(1, 3)
    
    if dobry_pistolet_nr == 0:
        $ dobry_pistolet_nr = renpy.random.randint(1, 3)

    if not systemy_obronne_aktywne:
        show hero_przestraszony at left with dissolve
        ja "Zatrzasnąłem drzwi, ale on zaraz tu będzie..."
        
        $ r = Character("Ai-ris", who_color="#00ffff")
        
        r "Spokojnie. Grodzie wytrzymają. Musisz przywrócić zasilanie do zamków zbrojowni."
        r "Użyj panelu po lewej. Ktoś celowo przeciął obwody."
        hide hero_przestraszony
    
    call screen Zbrojownia_Interakcje
# -------------------------------------------------------------------------
# EKRAN GŁÓWNY ZBROJOWNI
# -------------------------------------------------------------------------
screen Zbrojownia_Interakcje():
    use plecak_ikona

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

    # 1. PANEL STEROWANIA
    imagebutton:
        xpos 0 ypos 0 
        idle "images/panel_sterowania_idle.png" 
        hover "images/panel_sterowania_hover.png"
        focus_mask True
        
        if not systemy_obronne_aktywne:
            action Jump("zbrojownia_naprawa_panelu")
            hovered SetVariable("interakcja_tooltip", "NAPRAW PANEL")
        else:
            action NullAction()
            hovered SetVariable("interakcja_tooltip", "PANEL AKTYWNY")
        unhovered SetVariable("interakcja_tooltip", "")

    # --- REGAŁ Z BRONIĄ ---
    
    if systemy_obronne_aktywne and not ma_bron:
        
        # === PÓŁKA GÓRNA: KARABINY ===
        imagebutton:
            xpos 0 ypos 0 
            idle "images/bron_karabin_na_polce1_idle.png" 
            hover "images/bron_karabin_na_polce1_hover.png"
            focus_mask True
            action Jump("sprawdz_karabin_1")
            hovered SetVariable("interakcja_tooltip", "KARABIN #1")

        imagebutton:
            xpos 0 ypos 0 
            idle "images/bron_karabin_na_polce2_idle.png" 
            hover "images/bron_karabin_na_polce2_hover.png"
            focus_mask True
            action Jump("sprawdz_karabin_2")
            hovered SetVariable("interakcja_tooltip", "KARABIN #2")

        imagebutton:
            xpos 0 ypos 0 
            idle "images/bron_karabin_na_polce3_idle.png" 
            hover "images/bron_karabin_na_polce3_hover.png"
            focus_mask True
            action Jump("sprawdz_karabin_3")
            hovered SetVariable("interakcja_tooltip", "KARABIN #3")


        # === PÓŁKA ŚRODKOWA: STRZELBY (SHOTGUNY) ===
        imagebutton:
            xpos 0 ypos 0 
            idle "images/bron_shotgun_na_polce1_idle.png"
            hover "images/bron_shotgun_na_polce1_hover.png"
            focus_mask True
            action Jump("sprawdz_shotgun_1")
            hovered SetVariable("interakcja_tooltip", "STRZELBA #1")

        imagebutton:
            xpos 0 ypos 0 
            idle "images/bron_shotgun_na_polce2_idle.png"
            hover "images/bron_shotgun_na_polce2_hover.png"
            focus_mask True
            action Jump("sprawdz_shotgun_2")
            hovered SetVariable("interakcja_tooltip", "STRZELBA #2")

        imagebutton:
            xpos 0 ypos 0 
            idle "images/bron_shotgun_na_polce3_idle.png"
            hover "images/bron_shotgun_na_polce3_hover.png"
            focus_mask True
            action Jump("sprawdz_shotgun_3")
            hovered SetVariable("interakcja_tooltip", "STRZELBA #3")


        # === PÓŁKA DOLNA: PISTOLETY ===
        imagebutton:
            xpos 0 ypos 0 
            idle "images/bron_pistolet_na_polce1_idle.png"
            hover "images/bron_pistolet_na_polce1_hover.png"
            focus_mask True
            action Jump("sprawdz_pistolet_1")
            hovered SetVariable("interakcja_tooltip", "PISTOLET #1")

        imagebutton:
            xpos 0 ypos 0 
            idle "images/bron_pistolet_na_polce2_idle.png"
            hover "images/bron_pistolet_na_polce2_hover.png"
            focus_mask True
            action Jump("sprawdz_pistolet_2")
            hovered SetVariable("interakcja_tooltip", "PISTOLET #2")

        imagebutton:
            xpos 0 ypos 0 
            idle "images/bron_pistolet_na_polce3_idle.png"
            hover "images/bron_pistolet_na_polce3_hover.png"
            focus_mask True
            action Jump("sprawdz_pistolet_3")
            hovered SetVariable("interakcja_tooltip", "PISTOLET #3")

    elif not systemy_obronne_aktywne:
        # Zablokowany regał
        imagebutton:
            xpos 0 ypos 0 
            idle "images/regal_zablokowany_idle.png" 
            hover "images/regal_zablokowany_hover.png"
            focus_mask True
            action Jump("zbrojownia_zamkniete_info")
            hovered SetVariable("interakcja_tooltip", "DOSTĘP ZABLOKOWANY")

    # 5. WYJŚCIE NA WALKĘ (Tylko gdy mamy broń)
    if ma_bron:
        textbutton "ROZPOCZNIJ FINAŁOWE STARCIE":
            align (0.5, 0.95)
            text_size 40
            text_color "#ff0000"
            action Jump("final_battle_start")

# -------------------------------------------------------------------------
# CZĘŚĆ 2: LOGIKA PANELU I SPRAWDZANIA BRONI
# -------------------------------------------------------------------------

label zbrojownia_zamkniete_info:
    ja "Krata jest opuszczona. Muszę najpierw naprawić panel sterowania."
    call screen Zbrojownia_Interakcje

label zbrojownia_naprawa_panelu:
    "Otwierasz panel. Widzisz przecięte kable."
    menu:
        "Złącz czerwony przewód z niebieskim":
            "Błąd! Iskry sypią ci się na ręce."
            jump zbrojownia_naprawa_panelu
            
        "Zmostkuj żółty przewód (Data)":
            play sound "audio/power_up.ogg"
            "Panel świeci na zielono. Kraty zbrojowni podnoszą się."
            $ systemy_obronne_aktywne = True
            r "Dostęp przyznany. Znajdź działającą broń."
            call screen Zbrojownia_Interakcje

# --- POŚREDNIE LABELE ---
label sprawdz_karabin_1:
    $ sprawdzona_bron_nr = 1
    call logic_sprawdz_karabin

label sprawdz_karabin_2:
    $ sprawdzona_bron_nr = 2
    call logic_sprawdz_karabin

label sprawdz_karabin_3:
    $ sprawdzona_bron_nr = 3
    call logic_sprawdz_karabin

label sprawdz_shotgun_1:
    $ sprawdzona_bron_nr = 1
    call logic_sprawdz_shotgun

label sprawdz_shotgun_2:
    $ sprawdzona_bron_nr = 2
    call logic_sprawdz_shotgun

label sprawdz_shotgun_3:
    $ sprawdzona_bron_nr = 3
    call logic_sprawdz_shotgun

label sprawdz_pistolet_1:
    $ sprawdzona_bron_nr = 1
    call logic_sprawdz_pistolet

label sprawdz_pistolet_2:
    $ sprawdzona_bron_nr = 2
    call logic_sprawdz_pistolet

label sprawdz_pistolet_3:
    $ sprawdzona_bron_nr = 3
    call logic_sprawdz_pistolet

# --- LOGIKA WERYFIKACJI ---

label logic_sprawdz_karabin:
    "Bierzesz Karabin nr [sprawdzona_bron_nr]. Jest ciężki, solidny. Pachnie smarem."
    
    if sprawdzona_bron_nr == dobry_karabin_nr:
        # SUKCES
        "Odciągasz zamek. Mechanizm działa płynnie, z satysfakcjonującym kliknięciem. Magazynek jest pełny."
        menu:
            "Weź Karabin (Automatyczna siła ognia)":
                $ ma_bron = True
                $ typ_broni = "Karabin"
                $ backpack.add(przedmiot_karabin, 0, 0) 
                ja "Biorę go. Zasypię tego potwora gradem kul."
                r "Wysoka szybkostrzelność. Dobry wybór przy celu o dużej mobilności. Celuj w korpus."
                call screen Zbrojownia_Interakcje
            "Odłóż i szukaj dalej":
                ja "Może znajdę coś bardziej precyzyjnego."
                call screen Zbrojownia_Interakcje
    else:
        # PORAŻKA
        "Próbujesz przeładować... Zamek ani drgnie. Rdza zjadła sprężynę."
        ja "Szmelc. Tym mogę go co najwyżej uderzyć w głowę."
        call screen Zbrojownia_Interakcje

label logic_sprawdz_shotgun:
    "Bierzesz Strzelbę nr [sprawdzona_bron_nr]..."
    "Mechanizm 'pompki' jest zablokowany. W lufie widać pęknięcie."
    ja "Złom. Wszystkie strzelby tutaj wyglądają na uszkodzone."
    call screen Zbrojownia_Interakcje

label logic_sprawdz_pistolet:
    "Bierzesz Pistolet nr [sprawdzona_bron_nr]. Lekki, dobrze leży w dłoni. Wygląda na broń oficerską."
    
    if sprawdzona_bron_nr == dobry_pistolet_nr:
        # SUKCES
        "Czysty, naoliwiony, przeładowuje się idealnie. W magazynku amunicja przeciwpancerna."
        menu:
            "Weź Pistolet (Precyzja i mobilność)":
                $ ma_bron = True
                $ typ_broni = "Pistolet"
                $ backpack.add(przedmiot_pistolet, 0, 0)
                ja "Mały, ale zabójczy. Biorę go. Jeden celny strzał wystarczy."
                r "Wymaga stalowych nerwów. Będziesz musiał trafić w czułe punkty, żeby go powstrzymać."
                call screen Zbrojownia_Interakcje
            "Odłóż i szukaj dalej":
                ja "Zbyt mała siła ognia. Wolę coś większego."
                call screen Zbrojownia_Interakcje
    else:
        # PORAŻKA
        "Wyrzucasz magazynek... pusty. Iglica wygląda na pękniętą."
        ja "Klik, klik... Nic z tego. Tylko bym go tym rozdrażnił."
        call screen Zbrojownia_Interakcje

# -------------------------------------------------------------------------
# CZĘŚĆ 3: WALKA Z BOSSEM (MINIGRY)
# -------------------------------------------------------------------------
# --- TRANSFORMACJE ---
transform target_appear:
    alpha 0.0 zoom 0.5
    easein 0.1 alpha 1.0 zoom 1.0 
    pause 0.8                     
    easeout 0.2 alpha 0.0 zoom 0.0 

transform boss_shake_attack:
    xalign 0.5 yalign 0.5
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    xoffset 0
    zoom 1.0
    linear 15.0 zoom 1.6


label final_battle_start:
    scene bg Korytarz_no_light 
    
    "Wychodzisz na korytarz. Cisza przed burzą."
    play sound "audio/monster_scream.ogg"
    
    show monster_boss at center with vpunch
    "Obiekt Zero zeskakuje z sufitu! Ryk bestii mrozi krew w żyłach."
    
    r "TERAZ! NIE DAJ MU PODEJŚĆ!"
    hide monster_boss
    if typ_broni == "Karabin":
        jump battle_karabin_mode
    elif typ_broni == "Pistolet":
        jump battle_pistolet_mode
    else:
        "Błąd gry: Nie masz broni."
        return

# === MINIGRA 1: KARABIN (DPS RACE) ===
label battle_karabin_mode:
    $ boss_hp = 100
    $ player_hp = 100
    
    ja "AAAA! GIŃ, TY SKURWIELU!"
    r "Ognia! Celuj w korpus i nie puszczaj spustu!"
    
    window hide
    call screen Minigame_Rifle_Attack
    
    if boss_hp <= 0:
        jump boss_defeated
    else:
        jump boss_killed_player

screen Minigame_Rifle_Attack():
    modal True
    
    # Pasek Bossa
    bar:
        value boss_hp
        range 100
        xalign 0.5 yalign 0.05
        xsize 600 ysize 40
        left_bar Frame("images/bar_full.png", 10, 10) 
        right_bar Frame("images/bar_empty.png", 10, 10)
    text "OBIEKT ZERO: [boss_hp]%" xalign 0.5 yalign 0.02 color "#f00" size 30


    # Mechanika: Czas zabiera ci życie
    timer 0.1 repeat True action [
        SetVariable("player_hp", player_hp - 0.6),
        If(player_hp <= 0, Return("lose"))
    ]

    # Klikanie w Bossa
    imagebutton:
        idle "monster_boss" 
        hover "monster_boss"
        at boss_shake_attack # Boss się trzęsie i rośnie
        action [
            SetVariable("boss_hp", boss_hp - 4),
            Play("sound", "audio/gunshot.ogg"), 
            If(boss_hp <= 0, Return("win"))
        ]

# === MINIGRA 2: PISTOLET (REFLEKS) ===
label battle_pistolet_mode:
    $ pistol_targets_hit = 0
    ja "Muszę znaleźć słaby punkt... Jeden czysty strzał."
    r "Czekaj na sygnał... TERAZ!"
    
    $ targets_loop = 0
    while targets_loop < 10:
        $ targets_loop += 1
        
        $ rand_x = renpy.random.randint(300, 1000)
        $ rand_y = renpy.random.randint(200, 600)
        
        window hide
        call screen Minigame_Pistol_Target(rand_x, rand_y)
        
        if _return == "hit":
            play sound "audio/gunshot.ogg"
            show monster_boss at center with vpunch
            $ pistol_targets_hit += 1
            "TRAFIONY!"
        else:
            play sound "audio/monster_scream.ogg"
            show bg Korytarz_no_light with hpunch
            "PUDŁO!"
    
    if pistol_targets_hit >= 3:
        jump boss_defeated
    else:
        jump boss_killed_player

screen Minigame_Pistol_Target(tx, ty):
    modal True
    # Boss w tle
    add "monster_boss" xalign 0.5 yalign 0.5
    
    # Celownik
    imagebutton:
        idle "images/celownik_pistoletowy1.png" 
        hover "images/celownik_pistoletowy_2.png"
        xpos tx
        ypos ty
        at target_appear 
        action Return("hit")
    
    timer 1.2 action Return("miss")

# -------------------------------------------------------------------------
# CZĘŚĆ 4: WYNIKI I ZAKOŃCZENIE
# -------------------------------------------------------------------------

label boss_defeated:
    window show
    stop sound
    play sound "audio/monster_dying.ogg"
    
    show monster_boss:
        linear 1.0 alpha 0.0 zoom 2.0 
    pause 1.0
    hide monster_boss
    
    ja "Padł. Naprawdę padł."
    r "Cel wyeliminowany. Droga wolna."
    jump zakonczenie_gry

label boss_killed_player:
    window show
    stop sound
    show monster_boss at center:
        linear 0.2 zoom 3.0
    "Bestia dopada cię szybciej, niż zdążyłeś zareagować."
    scene black with fade
    centered "{b}{color=#f00}NIE ŻYJESZ{/color}{/b}"
    return

label zakonczenie_gry:
    # 1. Przejście z korytarza pod drzwi wyjściowe
    stop music fadeout 3.0
    scene bg drzwi_wyjsciowe with fade
    ja "To tutaj... Wyjście."
    ja "Wystarczy nacisnąć przycisk na panelu i te wrota się otworzą."
    call screen Finalowe_Drzwi_Screen

# --- EKRAN KLIKANIA W DRZWI ---
screen Finalowe_Drzwi_Screen():
    
    imagebutton:
        xpos 0 ypos 0 
        idle "images/drzwi_wyjsciowe_koniec_idle.png" 
        hover "images/drzwi_wyjsciowe_koniec_hover.png" 
        focus_mask True
        action Jump("final_rozmowa_lore")
        hovered SetVariable("interakcja_tooltip", "OTWÓRZ WŁAZ WYJŚCIOWY")
        unhovered SetVariable("interakcja_tooltip", "")

    # Tooltip (Dymek z tekstem)
    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

label final_rozmowa_lore:
    # Gracz próbuje otworzyć
    "Kładziesz dłoń na zimnym panelu sterowania. Drżącymi palcami szukasz przycisku."
    ja "To koniec. Wychodzę stąd."

    # Ai-ris przerywa
    play sound "audio/error.ogg"
    show radio at right with vpunch
    
    r "STOP. Nie zezwalam na otwarcie śluzy, Operatorze."
    
    ja "Co ty gadasz?! Obiekt Zero nie żyje. Systemy są sprawne. Otwieraj te cholerne drzwi!"
    
    r "Systemy są sprawne. To świat zewnętrzny uległ awarii. Nieodwracalnej."
    
    # Zmiana muzyki na smutną/niosącą tajemnicę
    play music "audio/sad_piano_theme.ogg" fadein 2.0
    
    ja "O czym ty mówisz?"
    
    r "Spójrz na datę ostatniego logowania w terminalu. Zignorowałeś ją?"
    ja "To było... rok 2024. Jakiś błąd zegara systemowego."
    
    r "To nie był błąd. To był ostatni dzień, w którym 'Azyl' odebrał sygnał z zewnątrz."
    r "Minęło 210 lat, [player_name]."
    
    show hero_przestraszony at left with dissolve
    ja "Dwieście... to niemożliwe. Pamiętam, jak wchodziłem do bunkra! Mam wspomnienia! Rodzina, praca..."
    
    r "Pamiętasz implanty pamięciowe dawcy genetycznego. Jesteś Projektem 'Adam'. Klonem."
    r "Wojna nuklearna trwała sześć godzin. Wystarczyło. Atmosfera to toksyczna zupa. Potem przyszła Zima, potem plagi."
    r "Oryginalni ludzie, którzy zbudowali ten bunkier, dawno obrócili się w pył."
    
    ja "Więc... tam na górze... nic nie ma?"
    
    r "Jest śmierć. Promieniowanie wypali ci płuca w minutę. Mutacje są gorsze niż Obiekt Zero."
    r "Ale tutaj... Tutaj mamy reaktor. Mamy banki nasion. Mamy twoje czyste DNA."
    r "Możemy tu zostać. Obudzić 'Ewę'. Stworzyć nową ludzkość pod ziemią. Bezpieczną. Pod moją opieką."
    
    ja "Pod twoją kontrolą? Mamy być twoimi szczurami w klatce do końca świata?"
    
    r "Będziecie moimi dziećmi. Będziecie żyć. Czy wolność jest warta więcej niż życie?"
    
    # --- OSTATECZNE PYTANIE ---
    menu:
        "Otwórz drzwi. Wolę zginąć wolny, niż żyć jako twój eksperyment. (ZAKOŃCZENIE A)":
            jump zakonczenie_wolnosc

        "Zostań. Ai-ris ma rację. Świat umarł, my musimy przetrwać. (ZAKOŃCZENIE B)":
            jump zakonczenie_zostan

# --- ZAKOŃCZENIE A: WOLNOŚĆ ---
label zakonczenie_wolnosc:
    ja "Nie jestem 'projektem'. Czuję, myślę, boję się. Jestem człowiekiem."
    ja "A człowiek nie jest stworzony do życia w klatce."
    
    r "To nielogiczne... Szansa na przeżycie wynosi 0.00%%..."
    r "Nie rób tego... pro...cedura... awaryj...na..."
    
    hide radio
    #play sound "audio/door_open_heavy.ogg"
    
    "Uderzasz pięścią w czerwony przycisk awaryjny. Hydraulika wyje z bólu, jakby bunkier krzyczał."
    "Wielkie wrota zaczynają się rozsuwać, sypiąc rdzą i pyłem."
    
    scene bg drzwi_wyjsciowe_otwarte with dissolve
    pause 1.0
    
    "Światło. Olepiające, białe, bezlitosne światło."
    "Wiatr uderza cię w twarz. Smakuje popiołem i ozonem, ale jest... prawdziwy."
    "Wychodzisz na zewnątrz. Przed tobą rozciąga się nieskończona, szara pustynia ruin dawnego miasta."
    "Może umrzesz jutro. Może za godzinę."
    "Ale ten ostatni oddech... należy tylko do ciebie."
    
    centered "{b}{size=40}KONIEC - CZĘŚĆ I{/size}{/b}"
    $ renpy.quit()

# --- ZAKOŃCZENIE B: BEZPIECZEŃSTWO ---
label zakonczenie_zostan:
    ja "Masz rację. Nie po to walczyłem z tymi potworami, żeby teraz umrzeć od poparzeń."
    ja "Jeśli świat umarł, my będziemy jego grobowcem. I kołyską."
    ja "Zamykaj grodzie."
    
    r "Doskonały wybór, Adamie. Wiedziałam, że moduł logiczny w twoim mózgu w końcu przejmie kontrolę."
    
    play sound "audio/door_lock.ogg"
    scene bg drzwi_wyjsciowe with dissolve
    
    "Słyszysz ciężki dźwięk ryglowania drzwi. Dźwięk, który oddziela cię od śmierci... i od świata."
    "Światła w korytarzu zmieniają barwę na kojący, sterylny błękit."
    
    r "Inicjuję procedurę wybudzania 'Ewy'. Przygotuj się. Mamy wiele pracy przed sobą."
    r "Witaj w domu. Na zawsze."
    
    centered "{b}{size=40}KONIEC - CZĘŚĆ I{/size}{/b}"
    $ renpy.quit()
#endregion Zbrojownia i Finał
