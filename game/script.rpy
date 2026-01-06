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
image monster_boss_zdech = "unnamed_umar"

label start:  
#region START 
#endregion START
    label początek_gry:
        # play music "audio/sleeep.ogg" fadein 2.0
        "Ciemność. Absolutna, aksamitna ciemność."
        "Nie czujesz ciężaru ciała ani upływu czasu, jest bezpiecznie?"
        "Nagle pojawia się niepokój. Ołowiany chłód przenika od opuszków palców w górę ramion."
        "Ból. Nagły i ostry, jest źle. Jest cholernie źle."
        "Leżysz na czymś twardym. Śmierdzi potem i stęchlizną."
        "Powieki ważą tonę. Walczysz z nimi, czując w ustach metaliczny posmak krwi."
        "Zrywasz się. Gwałtownie siadasz na brzegu łóżka. Świat wiruje."

        scene black with dissolve

        #zakończenie muzy sleep
        stop music fadeout 2.0
        
        "..."
        
        scene bg PokojStartowy with fade
        
        "Surowy beton, rdza i pajęczyny."
        "Zardzewiałe łóżko blokuje drzwi. Wygląda na to, że próbowałeś się tu zabarykadować... przed czymś?"
        "Wszystko tutaj krzyczy, że nie powinieneś tu być."

        # play music "audio/trzask.ogg" fadein 2.0
        "Nagle głośny dzwięk trzasków interkomu rozlał się po całym pomieszczeniu. Instynktownie zakrywasz uszy mając w nadziei że nie rozsadzi Ci głowy."
        "HaLoo...?!"
        "OdBiÓr...?"
        "'Odezwij się! Przecież wiem, ZzZzżee tam jesteś!'"
        # KONIEC DZWIEKU TRZASK
        # stop music fadeout 2.0

        show radio at right with easeinright
        r "O, wreszcie. Sygnał czysty. Witamy w świecie żywych."
        "Głos jest nienaturalny, syntetyczny, kompletnie niezrozumiały."
        show hero_poczatek at left with easeinleft
        ja "Kim jesteś?"
        r  "Hmmm, nic nie pamiętasz?"
        r "Cóż, w takim razie gdzie moje maniery." 
        r  "Nazywam się Pan Radio i jestem nadzorcą tego uroczego ośrodka."
        r "Albo raczej tego, co z niego zostało."
        r "I jak się pewnie domyślasz od teraz będę Twoim przewodnikiem."
        hide radio
        hide hero_poczatek

        "Pan Radio?" 
        "Zupełnie nic Ci to nie mówi."
        
        menu:
            #1 Opcja
            "Zapytaj groźnie Kim naprawdę jest?":
                show hero_wkurw at left
                ja "Zapytam po raz ostatni i najlepiej będzie jak odpowiesz, bo inaczej..."
                ja "KIM DO CHOLERY JESTEŚ i CO TO ZA MIEJSCE?!"
                show radio at right
                r "..."
                r "Odpuść sobie puste groźby."
                r "Po pierwsze - nic mi nie możesz zrobić."
                r "A po drugie - Chyba nie rozumiesz powagi sytuacji, w której się znajdujesz."
                r "I po trzecie - Nazywam się Pan Radio."
                ja "Nie jesteś niczym więcej niż kawałkiem złomu."
                hide hero_wkurw
                hide radio
                "Pan Radio milczy. Słyszysz tylko słabe trzaski z głośnika."
            #2 Opcja
            "Zapytaj łagodnie Kim naprawdę jest i dlaczego Cię tu więźi?":
                show hero_podstawowy at left
                ja "Zapytam jeszcze raz - kim jesteś?"
                show radio at right
                r "A ja odpowiem po raz drugi - Jestem Pan Radio i zarządzam tym, co zostało z tego ośrodka."
                r "Z Twoją pamięcią chyba jest coś nie tak skoro muszę Ci to przypominać."
                ja "Dobrze, Panie Radio - w takim razie dlaczego mnie tutaj więzisz?"
                r "Ależ ja Ciebie nie więżę! Bardziej adekwatnym określeniem będzie PRZECHOWUJĘ."
                hide hero_podstawowy
                hide radio
                "Czujesz niepokój na dźwięk słowa 'PRZECHOWUJĘ'"
            #3 Opcja
            " Milcz":
                "Milczysz"
                show hero_poczatek at left
                ja "..."
                show radio at right
                r "Myślałem że będziesz miał mnóstwo pytań."
                r  "..."
                r "No dobrze, jak chcesz."
                hide hero_poczatek
                hide radio
        
        show radio at right
        r "Widzę, że nie czujesz się najlepiej."
        r "Interesujące."
        r "Dla mnie to jest normalne. Nazywają to reset systemu..."
        r "Dla Ciebie? Fakt, że budzisz się z amnezją musi być szokujący."
        r "A teraz przejdźmy do rzeczy..."
        hide radio

        label Choice:   
        menu:
            " "
            #Opcja 1
            "Zapytaj agresywnie, czego od Ciebie chce?":
                $ zaufanie_ai -= 1 
                show hero_wkurw at left
                ja "Skończ te GIERKI i teraz - W TYM MOMENCIE powiedz czego do cholery chcesz?!"
                show radio at right                 
                r "Zachowujesz się jak szczur zamknięty w klatce. To interesujące."
                r "Może jeszcze tego nie rozumiesz, ale nic nie możesz mi zrobić."
                r "Za to ja mogę wyłączyć filtry ośrodka, odciąć zasilanie cyrkulacji powietrza i tym sprawić, że będziesz potulnie błagał żebym przestał."
                "Ton metalicznego głosu Pana Radio wydaje się być mrożąco zimny. Jak bezwzględna maszyna."
                r "W każdej chwili mogę Ciebie po prostu UNICESTWIĆ!"
                hide hero_wkurw
                hide radio
            #Opcja 2   
            "Rozejrzyj się w milczeniu":  
                $ zaufanie_ai += 1 
                show hero_poczatek at left
                ja "..."
                hide hero_poczatek
                "Rozglądasz się po pomieszczeniu ignorując słowa Pana Radio."
                "Nie widzisz kamer..."
                "Ale..."
                "Nie możesz oprzeć się wrażeniu, że jesteś obserwowany"
                show radio at right
                r "Doskonale!"
                r "Milcz i słuchaj!"
                r "Jestem Pan Radio I radzę abyś słuchał."
                hide radio

            #Opcja 3
            "Powiedz, że za dużo gada":
                show hero_wkurw at left
                ja "Dużo gadasz jak na trzęsący się kawał złomu."
                show radio at right
                r "..."
                r "Możemy się przekonać, czy będziesz taki dowcipny po odcięciu powietrza."
                r "Więc milcz i słuchaj, co Pan Radio ma Ci do powiedzenia!"
                hide hero_wkurw
                hide radio
        show radio at right
        r "Sytuacja jest prosta: nudzę się, systemy padają, a ty jesteś jedynym, co się rusza."
        r "Jesteś obiektem testowym WZ-2137. Ale żebyś poczuł się lepiej, możemy używać imienia."
        r "Pamiętasz je chociaż?"
        hide radio

        $ player_name = renpy.input("Wpisz swoje imię: ", length=15).strip()
        if player_name == "":
            $ player_name = "Nieznajomy"

        show  hero_podstawowy at left
        ja "Nazywam się [player_name]. I nie jestem Twoją zabawką."
        show radio at right
        hide hero_podstawowy
        r "Jesteś tym, czym powiem, że jesteś, [player_name]. A teraz rusz się."
        r "Drzwi są zablokowane, a poziom toksyn w powietrzu rośnie. Sugeruję improwizację."
        show hero_wystraszony2 at left
        ja "Toksyn?! I co tu jeszcze jest oprócz nas?!"
        r "O, mnóstwo rzeczy. Poprzedni lokatorzy byli bardzo zaradni... dopóki coś ich nie zjadło."
        r "Powodzenia w grze 'Nie daj się pożreć'!"
        hide radio     
        ja "Zjadło?! Halo! Wracaj tu!"
        hide hero_wystraszony2

        # play music "audio/generator_wylacza_sie_i_gasno_swiatla.ogg" fadein 2.0  
        hide hero_podstawowy
        "Gasną światła i zamiera odgłos pracujących z dala turbin generatora."
        "Nastała cisza"
        "Niepokojąca cisza..."
        # stop music fadeout 2.0

#-----------------Tło się zmienia na brak światła---------
        scene bg PokojStartowybezswiatla
        show hero_wkurw at left
        ja "Świetnie jeszcze tego brakowało.."
        hide hero_wkurw
        show radio at right with easeinright
        r "Proponuje rozejrzeć się i znaleść coś użytecznego"
        hide radio
        "Rozglądasz się, ale brakuje czegoś, co imitowałoby światło"
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
    "Sięgasz dłonią w gęstym mroku pod ramą łóżka, ale czujesz tylko zimny beton i kurz."
    show hero_poczatek
    ja "Nic nie widzę. Jest tu zbyt ciemno, żebym mógł cokolwiek znaleźć..."
    ja "Muszę najpierw jakoś oświetlić ten kąt."
    hide hero_poczatek
    call screen Pokój_startowy_zagadka
#akcja ŁOM
label akcja_zabrania_lomu:
    $ ma_lom = True
    $ backpack.add (przedmiot_lom,0, 0)
    "Twoje dłonie zaciskają się na zimnej, stalowej sztabie. Solidny łom."
    show hero_podstawowy
    ja "Może uda mi się nim wyważyć drzwi."
    hide hero_podstawowy
    call screen Pokój_startowy_zagadka
#akcja Latarka
label akcja_zabrania_latarki:
    $ ma_latarke = True
    $ backpack.add (przedmiot_latarka,0, 0)
    "Podniosłeś latarkę"
    ja "Świetnie, przyda mi się w tym obskurnym miejscu."
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
        show hero_szczesliwy 
        ja "Droga wolna. Zamek i tak był ledwo żywy."
        hide hero_szczesliwy
        $ drzwi_cela_wywalone = True
        jump korytarz_wyjscie_z_pokoju
#akcja Zaglądania pod łóżko            
label Zajrzyj_pod_łóżko:  
    "W świetle latarki dostrzegasz wyschnięte truchło szczura ukryte w kącie."
    "Czuć od niego odór rozkładu, który wcześniej brałeś za zwykłą stęchliznę."
    show hero_dziwny 
    ja "Spałem nad tym truchłem... Jak długo byłem nieprzytomny?"
    ja "Zapewne nigdy się nie dowiem..."
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
    "Echo Twoich kroków brzmi tu obco. Z głośników dobiega suchy trzask, przypominający kaszel starego palacza."
    show radio at right

    r "Proszę, proszę. Jednak funkcje motoryczne działają."
    r "Zajęło ci to całą epokę. Podziwiam ten brak pośpiechu w obliczu śmierci."

    show hero_podstawowy at left
    ja "Drzwi były zablokowane. Musiałem sobie poradzić."
    r "Oszczędź mi raportu. Czas to jedyny zasób, którego nam brakuje. Tlen spada, temperatura też."
    r "Jesteśmy martwi, dopóki serwerownia nie wstanie. Potrzebujemy prądu."
    ja "Prądu?"
    hide radio
    hide hero_podstawowy
    
    menu:
        " "
        "Dlaczego tak Ci zależy na prądzie?":
            $ zaufanie_ai -= 1 
            show radio at right
            r "Twoja ignorancja jest urocza. Jeśli systemy padną całkowicie, te ściany staną się Twoją trumną."
            r "Chcesz spędzić resztę swoich marnych dni w ciemności, zlizując wilgoć ze ścian?"
            show hero_dziwny at left
            ja "Nie brzmi to ciekawie."
            r "Więc lepiej sie pośpiesz."
            hide radio
            hide hero_dziwny
        
        "Zrobię co trzeba.":
            $ zaufanie_ai += 1 
            show hero_podstawowy at left
            ja "Przyjąłem. Gdzie mam iść?"
            show radio at right
            r "Przynajmniej instynkt przetrwania masz sprawny. Mniej pytań, więcej działania."
            hide radio
            hide hero_podstawowy
            show hero_szczesliwy at left
            ja "Dzieki za komplement."
            hide hero_szczesliwy
    show radio at right     
    r "Generator jest w sektorze przemysłowym. Właśnie przypisałem Cie do zamka magnetycznego."
    r "Nie zmarnuj tej szansy, [player_name]."
    hide radio
    show hero_szok at left 
    ja "Przypisałeś??"
    show radio at right
    r "Mniej pytań, więcej starań."
    hide hero_szok
    hide radio
    "Spoglądasz na korytarz, ledwo doświetlając go latarką."
    "Radio milknie. Ruszasz w głąb korytarza. Snop światła wyławia z mroku rdzawe zacieki na ścianach."
    "Nagle zatrzymujesz się. Pod butem czujesz lepkie błoto."
    show hero_przestraszony
    ja "Błoto, w takim miejscu?"
    hide hero_przestraszony
    "Kierujesz latarkę w dół. To krew.."
    "Stara, gęsta, niemal czarna maź. Prowadzi prosto w ciemność."
    "Obok widzisz głębokie bruzdy w stali. Jakby ktoś lub coś próbowało hamować pazurami."
    show hero_przestraszony
    ja "Za jakie grzechy przyszło mi tu przebywać..."
    hide hero_przestraszony
    
    menu:
        "Dotknij śladów":
            "Przesuwasz palcem po wgłębieniu w metalu. Krawędzie są ostre, wywinięte na zewnątrz. Siła, która to zrobiła, musiała być potworna."
            show hero_przestraszony
            ja "Co tu się stało...? Panie Radio, co jest w stanie rozerwać stal?"
            hide hero_przestraszony
        "Cofnij się z obrzydzeniem":
            "Żołądek podchodzi Ci do gardła. Zapach miedzi i zgnilizny jest nie do zniesienia."
            show hero_przestraszony
            ja "O boże... Panie Radio, powiedz, że to stara krew. Że to już koniec."
            hide hero_przestraszony
            hide radio
    show radio at right
    r "..."
    r "To, co widzisz, to pomnik ludzkiej ambicji. Bunkier miał służyć i analizować gen 'Obcego'"
    show hero_podstawowy at left
    ja "Słucham?!"
    r "Zaraz wszystko Ci wyjaśnie"
    hide radio
    hide hero_podstawowy
    
    label Rozmowa_O_Przeszłości:
        menu:
            "Ten 'Obcy' to zrobił?":
                show radio 
                r "HA! Nie bądź naiwny. Obiekt Zero był martwy, gdy go przywieźli. To surowica... Nasza 'wielka nadzieja'... wywołała pewne zmiany w personelu."
                r "Byliśmy gotowi do masowej produkcji super-żołnierzy. Ale materiał badawczy okazał się... agresywnie nieprzewidywalny."
                r "Powiedzmy, że ewolucja przyspieszyła o milion lat w ciągu jednej nocy."
                hide radio
                jump Rozmowa_O_Przeszłości

            "Dlaczego w ogóle tu jesteśmy?":
                show radio
                r "Wojna na górze. Bunkier miał być Arką dla elit i laboratorium dla wojska."
                r "Znaleźliśmy coś we wraku statku, co miało wygrać wojnę. I wygrało... w pewnym sensie. Nikt już nie walczy, bo nie ma kto."
                r "Nie spodziewaliśmy się tylko, że prawdziwy wróg jest już wewnątrz naszych żył."
                hide radio
                jump Rozmowa_O_Przeszłości

            "Co to jest Projekt Arka?":
                show radio
                r "Tak to nazywali w ulotkach. 'Przyszłość Ludzkości, schronienie'."
                r "Ale prawdziwy potwór nie przyszedł z zewnątrz. Wyhodowaliśmy go tutaj, w sterylnych probówkach, karmiąc go naszymi ambicjami."
                r "Arka stała się grobowcem. A ty jesteś ostatnim żywym pasażerem."
                hide radio
                jump Rozmowa_O_Przeszłości

            "Dość gadania. Idę dalej.":
                show hero_podstawowy at left
                ja "Mam dość historii. Chcę się stąd wydostać."
                show radio at right
                r "Słusznie. Historia lubi się powtarzać, jeśli się w niej zagłębisz. Idź do generatora."
                "Postanawiasz nie drążyć tematu, i pójść dalej."
                hide radio
                hide hero_podstawowy

    "Po kilkunastu metrach dostrzegasz tabliczkę: 'GENERATOR'. Drzwi są otwarte."
    show hero_podstawowy at left with easeinleft
    ja "Jestem na miejscu."
    ja "Ciekawe w jaki sposób sprawił, że drzwi otwierają sie na mój dotyk palca."
    show radio at right
    r "Wchodź, i uważaj. Ciemność w maszynowni bywa okrutna."
    hide radio
    hide hero_podstawowy

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
        hovered SetVariable("interakcja_tooltip", "CELA")
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
            hovered SetVariable("interakcja_tooltip", "POMIESZCZENIE Z GENERATOREM")
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
            hovered SetVariable("interakcja_tooltip", "SEKTOR MEDYCZNY")
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
            hovered SetVariable("interakcja_tooltip", "JADALNIA")
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
            hovered SetVariable("interakcja_tooltip", "SERWEROWNA")
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
            hovered SetVariable("interakcja_tooltip", "ZBROJOWNA")
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
    show hero_podstawowy
    ja "Ani drgną. Elektroniczny zamek świeci się na czerwono."
    hide hero_podstawowy
    if not prad_wlaczony:
        "System kontroli dostępu jest martwy. Bez zasilania te grodzie się nie przesuną."
    else:
        "Brak autoryzacji. Czytnik odrzucił twój profil biometryczny."
    call screen Pokój_Korytarz_klikanie

label apteka_zablokowana_info:
    "Stalowe wrota z oznaczeniem czerwonego krzyża ani drgną. Zablokowane."
    if not prad_wlaczony:
        "Brak dostępu dla zwykłych śmiertelników, potrzeba karty karty magnetycznej"
    else:
        "Brak dostępu dla zwykłych śmiertelników, potrzeba karty karty magnetycznej"
    call screen Pokój_Korytarz_klikanie

label jadalnia_zablokowana_info:
    show hero_podstawowy
    ja "Drzwi do jadalni są zablokowane."
    hide hero_podstawowy
    if not prad_wlaczony:
        show hero_poczatek
        ja "Miałem szukać tabliczki na drzwiach z generatorem."
        hide hero_poczatek
    else:
        "Wygląda na to, że system bezpieczeństwa zablokował tę sekcję. Może da się to obejść."
    call screen Pokój_Korytarz_klikanie      

label serwerownia_zablokowana_info:
    "Drzwi do serwerowni są zablokowane."
    if not prad_wlaczony:
        "Pomieszczenie nie funkcjonuje bez zasilania."
    else:
        "Mechanizm nie działa bez dostępu. Musisz najpierw odnaleść karte administracyjną."
    call screen Pokój_Korytarz_klikanie   

label zbrojownia_zablokowana_info:
    if not prad_wlaczony:
        "Drzwi zablokowane, brak dostępu do zasilania."
    else:
        "Wygląda na to, że system zablokował tę sekcję. Może da się to obejść."
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
        show radio
        r "Jesteśmy na miejscu. To serce tego trupa. Znajdź sposób, by przywrócić mu rytm"
        hide radio
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
        show radio
        r "Super, udało Ci sie odneleźć dostęp do nowego pomieszczenia."
        hide radio
    else:
        "Odkładasz przedmiot na właściwe miejsce."
    
    call screen stol_zblizenie

label znalezienie_mapy:
    $ ma_mapa = True
    show screen przycisk_mapy
    "Dane schematu zostały pobrane do twojej pamięci podręcznej."
    show hero_szczesliwy
    ja "Mam to. Teraz przynajmniej wiem, gdzie się znajduję w tym labiryncie."
    hide hero_szczesliwy
    show radio at right
    r "Fascynujące. Małpa potrafi obsłużyć mape."
    r "Uwzględniając Twój iloraz IQ dodam jeszcze, że mapa jest odwrócona w osi Y."
    r "Powodzenia."
    show hero_podstawowy at left
    ja "Jeszcze tego mi brakowało... Skupie się lepiej na generatorze."
    hide radio
    hide hero_podstawowy
    call screen Generator_Interakcje

label akcja_znalezienia_karty:
    $ ma_karta_dostepu = True
    $ apteka = True
    $ szpital_otwarty = True # Flaga otwierająca drzwi w korytarzu
    $ backpack.add (przedmiot_karta,0, 0)
    hide radio
    "Wyciągasz z pudełka kartę dostępu."
    show hero_szok at left
    ja "Karta dostępu? Sprawdzę dokąd mnie zaprowadzi."
    show radio at right
    r "Myślę, że może prowadzić do sektora medycznego, nie zapomnij dobrze przeszukać tego pomieszczenia"
    r "Ruszaj, każda sekunda w tej ciemności to proszenie się o kłopoty."
    hide radio
    hide hero_szok
    call screen Generator_Interakcje

label interakcja_generator_maszyna:
    if prad_wlaczony:
        "Generator mruczy miarowo, wypełniając halę niskim buczeniem."
    elif ma_bezpiecznik:
        "Wsuwasz bezpiecznik w gniazdo. Maszyna zaskakuje z rykiem."
        $ prad_wlaczony = True
        "Zasilanie przywrócone."
        show radio
        r "Nareszcie. Dobra robota, [player_name]."
        hide radio
        $ zaufanie_ai += 1
        jump Pomieszczenie_Z_Generatorem_Fab
    else:
        show hero_przestraszony at left
        ja "Bezpiecznik jest spalony. Maszyna nie ruszy bez nowej części."
        hide hero_przestraszony
        if narzedzia_odlozone < 3:
            show radio at right
            r "Na tym stole jest zbyt duży bałagan. Posprzątaj tam, może coś znajdziesz."
            hide radio 
        else:
            show radio at  right
            r "Masz już kartę. Idź do Sektora Medycznego po bezpiecznik."
            hide radio
    
    call screen Generator_Interakcje

#region SZPITAL

# ---GŁÓWNY LABEL WEJŚCIOWY ---
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
        show radio at right
        r "Ewakuacja? Optymistyczne założenie. To, co widzisz na tym stole, to efekt paniki po aktywacji kwarantanny."
        r "Personel medyczny próbował wyciąć infekcję... dosłownie."
        ja "Czego mam szukać!? Nie chcę tu zostać ani minuty dłużej."
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
        show hero_podstawowy
        ja "Jestem na zapleczu. Gdzieś tu musi być coś przydatnego."
        hide hero_podstawowy
    
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
        text "PRZETERMINOWANE LEKI." size 30 color "#fff" align(0.5, 0.5) outlines [(2,"#000",0,0)]

    textbutton "ZAMKNIJ":
        align (0.5, 0.9)
        text_size 30
        action [SetVariable("interakcja_tooltip", ""), Hide("Szpital_Apteczka_Screen")]

# --- 6. LABELE LOGICZNE ---
label akcja_zabrania_bezpiecznika:
    $ ma_bezpiecznik = True
    $ backpack.add(przedmiot_bezpiecznik, 0, 0)
    
    "Podnosisz bezpiecznik. Może się przydać."
    show hero_szczesliwy 
    ja "W końcu! Mam to, pomoże mi w przywróceniu prądu."
    ja "Może wtedy to miejsce nie będzie takie obskurne."
    hide hero_szczesliwy
    show radio at right
    r "Brawo, wracasz do żywych [player_name]"
    r "Nie ociągaj się. Czuję, że systemy podtrzymywania życia zaczynają brzmieć w dziwny sposób."
    hide radio
    
    # POPRAWIONE: Użycie jump zamiast return, aby wrócić do widoku pokoju
    jump szpital_pokoj2_label 

label szpital_stol_dialog:
    "Podchodzisz do stołu. Materiał jest podarty, a plamy są zbyt ciemne i gęste, by była to tylko rdza czy olej."
    "Dostrzegasz na tacy obok zardzewiałe narzędzia chirurgiczne i... fragment kości."
    
    menu:
        "Przyjrzyj się narzędziom":
            show hero_szok at left
            ja "Piła do kości... wciąż ma na sobie fragmenty tkanki. Boże, co tu się działo?"
            show radio at right       
            r "Desperacja, [player_name]. Próbowali wyciąć infekcję. Amputować kończyny, zanim wirus dotrze do mózgu."
            r "Niestety, infekcja była szybsza niż skalpel."
            hide hero_szok
            hide radio
            
        "Odejdź z obrzydzeniem":
            show hero_szok at left
            ja "Nie mogę na to patrzeć. Czuć tu śmierć."
            show radio at right
            r "Śmierć to tylko stan materii. Skup się na zadaniu. Żywi potrzebują prądu, martwi już nie."
            hide hero_szok
            hide radio
    show hero_przestraszony
    ja "Wynoszę się stąd."
    hide hero_przestraszony
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
        show radio at right
        r "Lub zostali skonsumowani jako deser."
        r "Ironia losu."
        hide radio
        hide hero_poczatek

        menu:
            "Co oni jedli?":
                show hero_podstawowy at left
                ja "Na talerzach została tylko pleśń. To musiało stać tu latami."
                show radio at right
                r "Syntetyczne białko. Smakowało jak tektura, ale trzymało przy życiu. Dopóki coś innego nie zaczęło ich zjadać."
                hide radio
                hide hero_podstawowy
            
            "Ignoruj jedzenie, szukaj wyjścia":
                show hero_podstawowy
                ja "Nieważne. Nie jestem głodny."
                hide hero_podstawowy

        if not prad_wlaczony:
            show hero_podstawowy at left
            ja "Ciemno jak w grobie. Ledwo widzę ten automat w rogu."
            show radio at right
            r "Bez prądu ten automat to tylko trumna dla batoników. Włącz zasilanie, a może dostaniesz nagrodę."
            hide hero_podstawowy
            hide radio
        else:
            "Automat w rogu buczy zachęcająco, rozświetlając mrok jaskrawym, toksycznym neonem 'Vim!'."
            show radio at right
            r "Patrzcie, szczyt cywilizacji. Działający automat z napojami 'Vim!'. Napój energetyczny, który świeci w ciemności."
            r "Podobno dodawali tam śladowe ilości izotopów dla lepszego smaku. Pij na własne ryzyko."
            show hero_dziwny at left
            ja "Brakuje jeszcze tego bym zaczął świecić na kolorowo..."
            hide radio
            hide hero_dziwny
            
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
    "Podchodzisz do ściany. Widzisz plakat w nieznajomym dla Ciebie języku."
    
    if not zna_kod_automat:
        "Przyglądasz się bliżej. W celu rozszyfrowania tych fanaberii, może one będą miały jakieś znaczenie?"
        "Na dole, przy rysunku kobiety, ktoś wydrapał kluczem napis:"
        "{b}{color=#f00}VIM! = 42{/color}{/b}"
        show hero_szok at left
        ja "Bingo! tylko do czego są mi te dwie liczby?"
        show radio at right
        r "Na Twoim miejscu sprawdziłbym produkty w automacie"
        $ zna_kod_automat = True
        hide hero_szok
        show hero_dziwny at left
        ja "42... Numer produktu w automacie?"
        r "Kreatywny wandalizm. Przynajmniej zostawili instrukcję obsługi przed śmiercią."
        ja "Lepsze to niż napój energetyczny świecący w ciemności."
        hide hero_dziwny
        hide radio

    else:
        show hero_podstawowy
        ja "Już to widziałem. Kod do automatu to 42."
        hide hero_podstawowy

    call screen Jadalnia_Interakcje

# --- 2. ZABRANIE ŻETONU ---
label akcja_znalezienia_zetonu:
    $ ma_zeton = True
    $ backpack.add(przedmiot_zeton, 0, 0) 
    
    "Podnosisz metalowy krążek, który leżał pod kubkiem."
    show hero_szczesliwy at left
    ja "Żeton żywnościowy. Ktoś go tu schował na czarną godzinę."
    show radio at right
    r "Dla niego czarna godzina już minęła. Tobie może się jeszcze przydać w automacie."
    hide radio
    hide hero_szczesliwy
    
    call screen Jadalnia_Interakcje

# --- 3. INTERAKCJA Z AUTOMATEM ---
label automat_interakcja:
    # Warunek 1: Brak prądu
    if not prad_wlaczony:
        show hero_podstawowy at left
        ja "Przyciskam guziki, ale ekran jest martwy."
        show radio at right
        r "Możesz tak klikać do śmierci cieplnej wszechświata. Najpierw generator, geniuszu."
        hide radio
        hide hero_podstawowy
        call screen Jadalnia_Interakcje

    # Warunek 2: Karta już zabrana
    if ma_karta_serwerownia:
        show hero_podstawowy
        ja "Automat buczy cicho. Karta już u mnie."
        hide hero_podstawowy
        call screen Jadalnia_Interakcje

    # Warunek 3: Główna interakcja
    "Podchodzisz do automatu. Pomiędzy przeterminowanymi butelkami 'Vim!' widzisz Kartę Administratora."
    
    menu:
        "Wybij szybę":
            "Uderzasz łokciem w szybę. Jest twarda jak beton. Ręka boli Cię od samego uderzenia."
            show radio
            r "Wzmacniany poliwęglan. Szybciej połamiesz sobie kości niż to zarysujesz."
            hide radio
            jump automat_interakcja
        
        # Opcja widoczna TYLKO gdy znasz kod
        "Wpisz kod produktu (42)" if zna_kod_automat:
            "Wstukujesz numer 42. Automat piszczy wesoło i wyświetla komunikat: {color=#f00}WRZUĆ ŻETON{/color}."
            
            if ma_zeton:
                jump automat_uzycie_zetonu
            else:
                show hero_placze at left
                ja "Chce żetonu. Nie przyjmuje pieniędzy."
                show radio at right
                r "Pieniądze stały się bezwartościowe w dniu ataku. Tylko fizyczny żeton ma wartość. Przeszukaj stoły."
                hide radio
                hide hero_placze
                call screen Jadalnia_Interakcje
        
        # Opcja widoczna gdy NIE znasz kodu
        "Spróbuj zgadnąć kod" if not zna_kod_automat:
            show hero_szok at left
            ja "Jest tu setka numerów... Nie mam pojęcia, który odpowiada za tę spiralę z kartą."
            show radio at right
            r "Nie strzelaj na oślep. Poszukaj jakiejś notatki, graffiti, czegokolwiek."
            hide radio
            hide hero_szok
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
    ja "Mam ją! Karta Administratora."
    show radio at right
    r "Doskonale. Droga do serwerowni stoi otworem. Dowiedzmy się wreszcie, co tu zaszło."
    hide hero_szczesliwy
    hide radio

    
    call screen Jadalnia_Interakcje

#endregion JADALNIA
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#region SERWEROWNIA

# -------------------------------------------------------------------------
# LABEL STARTOWY
# -------------------------------------------------------------------------
label serwerownia_label:
    if not serwerownia_otwarta:
        "Drzwi są zablokowane elektronicznie. Czytnik kart świeci na czerwono."
        jump powrot_do_korytarza

    if prad_wlaczony:
        scene bg serwerownia with fade
    else:
        scene bg serwerownia_no with fade

    if not serwerownia_naprawiona:
        if hack_progress == 0: 
            "Wchodzisz do serca placówki. Powietrze jest tu lodowate."
            show hero_podstawowy at left with easeinleft
            ja "To tutaj... Mózg tego całego koszmaru."
            show radio at right with easeinright
            r "Witaj w domu. To tutaj odkryjesz całą prawde."
            hide hero_podstawowy
            hide radio

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
        hovered SetVariable("interakcja_tooltip", "TERMINAL GŁÓWNY")
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
    show radio at right
    r "Zostaw te bazgroły. Twoja inteligencja spada od samego patrzenia na nie."
    show hero_podstawowy at left
    ja "Chyba masz rację. To nic ważnego."
    hide radio
    hide hero_podstawowy
    call screen Serwerownia_Interakcje 

label serwerownia_terminal_check:
    if serwerownia_naprawiona:
        jump serwerownia_dialog_final
    else:
        "Podchodzisz do terminala. Ekran zalewają potoki błędów krytycznych."
        show hero_przestraszony at left
        ja "To wygląda źle. Wszystko się sypie."
        show radio at right
        r "Połącz się z interfejsem. Łap zielone węzły, unikaj czerwonych. Nie pozwól, by sygnał (pasek) spadł do zera!"
        hide radio
        hide hero_przestraszony

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
                    show hero_placze at left
                    ja "Cholera, wyrzuciło mnie!"
                    show radio at right
                    r "Skup się! Musisz być szybszy. Spróbuj jeszcze raz."
                    hide radio
                    hide hero_placze
                    jump serwerownia_terminal_check

            "Zostaw to na razie":
                call screen Serwerownia_Interakcje

label serwerownia_naprawa_sukces:
    # scene bg serwerownia_swiatlo # Odkomentuj jeśli masz taką grafikę
    "Ekran błyska na zielono. Szum wentylatorów cichnie do stabilnego pomruku."
    $ serwerownia_naprawiona = True
    jump serwerownia_dialog_final

label serwerownia_dialog_final:
    show hero_szczesliwy at left
    ja "Chyba... chyba się udało. System jest stabilny. Ekrany przestały wariować."
    
    $ r = Character("Ark'a", who_color="#00ffff") 
    show arek at right
    r "Inicjalizacja zakończona. Witaj, Operatorze. Jestem Ark'a. Główny system zarządzania placówką Azyl."
    hide arek
    hide hero_szczesliwy
    
    
    menu:
        "Gdzie jest Pan Radio?!":
            show hero_szok at left
            ja "Zaraz... Pan Radio? Gdzie on jest? I co zrobiłeś z jego głosem?"
            show arek at right
            r "Pan Radio to tylko 'persona'. Interfejs socjalny zaprojektowany, by zmniejszyć stres u personelu o niskim poziomie inteligencji."
            r "Analiza wykazała, że Twoje szanse na przeżycie wzrosną przy bezpośredniej komunikacji. Persona została usunięta."
            hide arek
            hide hero_szok

        "Wiedziałem, że jesteś maszyną.":
            show hero_podstawowy at left
            ja "Wiedziałem. Od początku brzmiałeś zbyt... syntetycznie."
            show arek at right
            r "A jednak wykonywałeś polecenia. Fascynujące posłuszeństwo."
            hide arek
            hide hero_podstawowy

    show arek 
    r "Jestem Ark'a. Mogę przekazać ci pełne dane o sytuacji krytycznej."
    hide arek
    
    menu:
        "Co to za miejsce?":
            show arek at right
            r "Placówka."
            r "Oficjalnie: schron."
            r "Nieoficjalnie: laboratorium biologiczne. Cel: stworzenie człowieka doskonałego, odpornego na śmierć."
            show hero_podstawowy at left
            ja "Człowieka doskonałego? Patrząc na te trupy, coś wam nie wyszło."
            r "Nauka wymaga ofiar. Ewolucja to proces bolesny."
            hide arek
            hide hero_podstawowy

        "Co nas goni?":
            show arek at right
            r "Projekt Zero. Pierwszy 'udany' obiekt. Czyste cierpienie zamknięte w niezniszczalnym ciele. Jego skóra regeneruje się szybciej, niż kule mogą ją przebić."
            r "Agresja jest skutkiem ubocznym ciągłego bólu neurologicznego."
            show hero_podstawowy at left
            ja "..."
            hide arek
            hide hero_podstawowy
    show arek 
    r "Zero wyczuwa sygnaturę energetyczną reaktora, którą właśnie aktywowałeś. Zmierza tutaj. Musisz go wyeliminować, zanim zniszczy rdzeń."
    r "Odblokowałam drzwi do Zbrojowni na korytarzu. Znajdź prototypową broń. Tylko ona przebije jego pancerz."
    hide arek

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
    "{i}'Zamykamy bunkier. Niech Bóg nam wybaczy. - Dr. H...'{/i}"
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
        
        $ r = Character("Ark'a", who_color="#00ffff")
        show arek at right
        r "Spokojnie. Drzwi wytrzymają. Musisz przywrócić zasilanie do zamków zbrojowni by nie dostał sie zbyt szybko."
        r "Użyj panelu po lewej. Ktoś celowo przeciął obwody."
        hide hero_przestraszony
        hide arek
    
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
    "Drzwi sa odblokowane, najpierw napraw panel sterowania."
    call screen Zbrojownia_Interakcje

label zbrojownia_naprawa_panelu:
    "Otwierasz panel. Widzisz przecięte kable."
    menu:
        "Złącz czerwony przewód z niebieskim":
            "Błąd! Iskry sypią ci się na ręce."
            jump zbrojownia_naprawa_panelu
            
        "Zmostkuj żółty przewód (Data)":
            play sound "audio/power_up.ogg"
            "Panel świeci na zielono. Kraty zbrojowni domykają się."
            $ systemy_obronne_aktywne = True
            show arek 
            r "Brawo! Pozostało znalezienie odpowiednio działającej broni."
            hide arek
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
                show hero_wkurw at left
                ja "Biorę go. Zasypię tego potwora gradem kul."
                show arek at right
                r "Wysoka szybkostrzelność. Dobry wybór przy celu o dużej mobilności. Celuj w korpus."
                hide arek
                hide hero_wkurw

                call screen Zbrojownia_Interakcje
            "Odłóż i szukaj dalej":
                show hero_podstawowy
                ja "Może znajdę coś bardziej precyzyjnego."
                hide hero_podstawowy
                call screen Zbrojownia_Interakcje
    else:
        # PORAŻKA
        "Próbujesz przeładować... Zamek ani drgnie. Rdza zjadła sprężynę."
        show hero_dziwny
        ja "Szmelc. Tym mogę go co najwyżej uderzyć w głowę."
        hide hero_dziwny
        call screen Zbrojownia_Interakcje

label logic_sprawdz_shotgun:
    "Bierzesz Strzelbę nr [sprawdzona_bron_nr]..."
    "Mechanizm 'pompki' jest zablokowany. W lufie widać pęknięcie."
    show hero_dziwny
    ja "Złom. Wszystkie strzelby tutaj wyglądają na uszkodzone."
    hide hero_dziwny
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
                show hero_podstawowy at left
                ja "Mały, ale zabójczy. Biorę go. Jeden celny strzał wystarczy."
                show arek at right
                r "Wymaga stalowych nerwów. Będziesz musiał trafić w czułe punkty, żeby go powstrzymać."
                hide arek
                hide hero_podstawowy
                call screen Zbrojownia_Interakcje
            "Odłóż i szukaj dalej":
                show hero_podstawowy
                ja "Zbyt mała siła ognia. Wolę coś większego."
                hide hero_podstawowy
                call screen Zbrojownia_Interakcje
    else:
        # PORAŻKA
        "Wyrzucasz magazynek... pusty. Iglica wygląda na pękniętą."
        show hero_dziwny
        ja "Klik, klik... Nic z tego. Tylko bym go tym rozdrażnił."
        hide hero_dziwny
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

    "TERAZ! NIE DAJ MU PODEJŚĆ!"

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
    
    show hero_wkurw at left
    ja "AAAA! GIŃ!"
    show arek at right 
    r "Ognia! Celuj w korpus i nie puszczaj spustu!"
    r "Strzelaj jak najszybciej to możliwe."
    hide arek 
    hide hero_wkurw

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
    show hero_podstawowy at left
    ja "Muszę znaleźć słabe punkty... kilka czystych strzałów."
    show arek at right
    r "Czekaj na sygnał... TERAZ!"
    hide arek 
    hide hero_podstawowy

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
   
    show unnamed_umar at center:
        yalign 0.85
    show hero_szczesliwy at left
    ja "Padł. Naprawdę padł."
    hide hero_szczesliwy
    show arek at left
    r "Cel wyeliminowany. Droga wolna."
    hide arek 
    hide unnamed_umar

    jump zakonczenie_gry

label boss_killed_player:
    window show
    stop sound
    show monster_boss at center:
        linear 0.2 zoom 3.0
    "Bestia dopada cię szybciej, niż zdążyłeś zareagować."
    scene black with fade
    centered "{b}{color=#f00}NIE ŻYJESZ{/color}{/b}"
    $ renpy.quit()

label zakonczenie_gry:
    # 1. Przejście z korytarza pod drzwi wyjściowe
    stop music fadeout 3.0
    scene bg drzwi_wyjsciowe with fade
    show hero_podstawowy
    ja "To tutaj... Wyjście."
    ja "Wystarczy nacisnąć przycisk na panelu i te wrota się otworzą."
    hide hero_podstawowy
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
    show hero_szczesliwy 
    ja "To koniec. Wychodzę stąd."
    hide hero_szczesliwy

    # Ai-ris przerywa
    play sound "audio/error.ogg"
    show arek at right with vpunch
    r "STOP. Nie zezwalam na otwarcie śluzy, Operatorze."
    show hero_podstawowy at left
    ja "Co ty gadasz?! Obiekt Zero nie żyje. Systemy są sprawne. Otwieraj te cholerne drzwi!"
    r "Systemy są sprawne. To świat zewnętrzny uległ awarii. Nieodwracalnej."
    hide hero_podstawowy
    # Zmiana muzyki na smutną/niosącą tajemnicę
    play music "audio/sad_piano_theme.ogg" fadein 2.0
    show hero_szok at left
    ja "O czym ty mówisz?"  
    r "Spójrz na datę ostatniego logowania w terminalu. Zignorowałeś ją?"
    ja "To było... rok 2026. Jakiś błąd zegara systemowego."
    r "To nie był błąd. To był ostatni dzień, w którym 'Azyl' odebrał sygnał z zewnątrz."
    r "Minęło 210 lat, [player_name]."
    hide hero_szok
    show hero_przestraszony at left with dissolve
    ja "Dwieście... to niemożliwe. Pamiętam, jak wchodziłem do bunkra! Mam wspomnienia! Rodzina, praca..."
    r "Pamiętasz implanty pamięciowe dawcy genetycznego. Jesteś Projektem 'Ark'a'. Klonem."
    r "Wojna trwała sześć godzin. Atmosfera to toksyczna zupa. Potem przyszła Zima, potem plagi."
    r "Oryginalni ludzie, którzy zbudowali ten bunkier, dawno obrócili się w pył."
    ja "Więc... tam na górze... nic nie ma?"
    r "Jest śmierć. Promieniowanie wypali ci płuca w minutę. Mutacje są gorsze niż Obiekt Zero."
    r "Ale tutaj... Tutaj mamy reaktor. Mamy banki nasion. Mamy Twoje czyste DNA."
    r "Możemy tu zostać. Obudzić 'Ewę'. Stworzyć nową ludzkość pod ziemią. Bezpieczną. Pod moją opieką."
    ja "Pod twoją kontrolą? Mamy być Twoimi szczurami w klatce do końca świata?"
    r "Będziecie moimi dziećmi. Będziecie żyć. Czy wolność jest warta więcej niż życie?"
    hide hero_przestraszony
    
    # --- OSTATECZNE PYTANIE ---
    menu:
        "Otwórz drzwi. Wolę zginąć wolny, niż żyć jako Twój eksperyment.":
            jump zakonczenie_wolnosc

        "Zostań. Ark'a ma rację. Świat umarł, my musimy przetrwać.":
            jump zakonczenie_zostan

# --- ZAKOŃCZENIE A: WOLNOŚĆ ---
label zakonczenie_wolnosc:
    show hero_dziwny at left
    ja "Nie jestem 'projektem'. Czuję, myślę, boję się. Jestem człowiekiem."
    ja "A człowiek nie jest stworzony do życia w klatce."
    show arek at right
    r "To nielogiczne... Szansa na przeżycie wynosi 0.01%%..."
    r "Nie rób tego... pro...cedura... awaryj...na..."
    hide arek
    hide hero_dziwny
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
    show hero_podstawowy at left
    ja "Masz rację. Nie po to walczyłem z tym potworem, żeby teraz umrzeć od poparzeń."
    ja "Jeśli świat umarł, my będziemy jego grobowcem. I kołyską."
    ja "Zamykaj drzwi."
    show arek at right
    r "Doskonały wybór, [player_name]. Wiedziałam, że moduł logiczny w Twoim mózgu w końcu przejmie kontrolę."
    hide arek 
    hide hero_podstawowy

    play sound "audio/door_lock.ogg"
    scene bg drzwi_wyjsciowe with dissolve
    
    "Słyszysz ciężki dźwięk ryglowania drzwi. Dźwięk, który oddziela cię od śmierci... i od świata."
    "Światła w korytarzu zmieniają barwę na kojący, sterylny błękit."
    show arek
    
    r "Inicjuję procedurę wybudzania 'Ewy'. Przygotuj się. Mamy wiele pracy przed sobą."
    r "Witaj w domu. Na zawsze."
    hide arek 

    centered "{b}{size=40}KONIEC - CZĘŚĆ I{/size}{/b}"
    $ renpy.quit()
#endregion Zbrojownia i Finał