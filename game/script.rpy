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
default prad_wlaczony = False  #zmienić na False

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
default ma_karta_serwerownia = False # Do serwerowni (znaleziona w jadalni)
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
default systemy_obronne_aktywne = False
default ma_bron = False
default typ_broni = "brak" 
default zaufanie_ai = 0

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
image bg tlo_mapa = "tło_mapa"
#---------------HAKOWANIE SERWEROWNIA
image bg terminal_hacking = Solid("#001100")
#---------------JADALNIOWY STOLIK------
image bg stolik_zblizenie_bg = "stolik_zblizenie" # Twoje tło zbliżenia na stół
image monster_boss = "unnamed" # Potwór z głową TV
image bg apteczka_zblizenie = "apteczka_zblizenie_no"   ######DODAĆ
image bg apteczka_zblizenie_pront = "apteczka_zblizenie"

# ------------------------------------------------------Tutaj sobie możesz sceny na starcie pominąć niebedzie potrzeby przeklikiwania :3
label start:  
#region START

#Gracz budzi się z ogromną amnezją, wita go Pan Radio i "tłumaczy" sytuacje w jakiej się znajduje na koniec rozmowy gasną światła.
#Gracz ma za zadanie odnaleźć przedmioty które pozwolą mu wyjść z tego ciemnego pomieszczenia. 

#endregion 
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
        
        "Budzi cię tępy, pulsujący ból z tyłu czaszki. Próbujesz otworzyć oczy, ale powieki są ciężkie jak ołów."
        "Twoje ciało jest odrętwiałe, jakbyś spał miesiącami. W ustach czujesz metaliczny posmak krwi i stęchliznę."
        "Próbujesz się podnieść. Mięśnie drżą, odmawiając posłuszeństwa. Jesteś słaby... Zbyt słaby."
        
        scene bg PokojStartowy with fade
        
        "Wokół panuje półmrok. Zarysy mebli są niewyraźne, obce."
        "Wydaje ci się, że słyszysz znajomy głos, dobiegający zewsząd i znikąd zarazem. Pamięć jest czarną dziurą."
        
        "???" "Haloo... Odbiór...? Czy ten zlepek tkanki organicznej wreszcie funkcjonuje?"
        
        show radio at right with easeinright
        r "Witaj w Bunkrze. Jestem Pan Radio. Twój jedyny przyjaciel, nadzorca i... być może sędzia."

        show hero_poczatek at left with dissolve
        ja "Kto... Kto tam jest? Gdzie ja jestem?!"
        
        r "Widzę usterkę w sektorze pamięci. Reset systemu musiał być bardziej... inwazyjny niż zakładałem."
        label Choice:   
            menu:
                " "
                #Opcja agresywna
                "Odpowiesz na moje pytanie?! (Agresja)":
                    $ zaufanie_ai -= 1 # AI: Minus do zaufania
                    hide hero_poczatek
                    show hero_wkurw at left
                    ja "Pytam kim jesteś i co ja tu do cholery robię?! Nie baw się ze mną!"
                    
                    hide hero_wkurw
                    show hero_podstawowy at left
                    
                    r "Adrenalina rośnie. Puls przyspiesza. Fascynujące, ale bezcelowe. Agresja to domena zwierząt, [player_name]."
                    r "Powiedziałem wyraźnie: jestem Pan Radio. Jestem głosem w ścianach, duchem w maszynie."
                    r "Mogę być kim zechcę, ale dla ciebie jestem Bogiem tego małego, betonowego świata. Nie irytuj mnie."
                    
                #Opcja analityczna/spokojna
                "(Milcz i rozglądaj się) (Opanowanie)":  
                    $ zaufanie_ai += 1 # AI: Plus do zaufania
                    ja "..."
                    "Rozglądasz się nerwowo, szukając źródła głosu. Głośniki są ukryte głęboko w rdzewiejących ścianach. Analizujesz sytuację na chłodno."
                    
                    hide hero_poczatek
                    show hero_podstawowy at left
                    
                    r "Milczenie. Analiza otoczenia. Dobrze. Może jednak twój mózg nie uległ całkowitej atrofii."
                    r "Jestem Pan Radio. Twoim przewodnikiem w tym labiryncie."
                
            r "W każdym razie, cieszę się, że tu jesteś. Choć 'cieszę się' to pojęcie abstrakcyjne dla algorytmu."
            r "Sytuacja jest prosta: drzwi są zamknięte, tlen się kończy a ja się nudzę. Wyjdź stąd, zanim zginiesz lub oszalejesz."
            r "A właśnie... jak cię oznaczono w rejestrze?"
            
            $ player_name = renpy.input("Jak masz na imię? ", length=15).strip()
            if player_name == "":
                $ player_name = "hero"
            
            ja "Możesz na mnie mówić [player_name]. Choć nie wiem, czy to moje prawdziwe imię."
            ja "Właśnie... jak mam stąd wyjść?"
            
            r "Eksploruj. Kombinuj. Szukaj anomalii w systemie. I nie daj się zjeść."
            hide radio    
            ja "Zjeść?! Co masz na myśli?!"
            
            hide hero_podstawowy
            "Słyszysz jak coś buczy poza twoim pomieszczeniem. Generatory umierają. Światła zaczynają mrugać spazmatycznie i po chwili kompletnie gasną."

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
#-Gracz zostaje "Pochwalony" przez pana radio za rozwiązanie poprzedniej zagadki. 
#-Gra (pan radio) Prowadzi gracza do pomieszczenia z generatorem.
#endregion 

label powrot_do_korytarza:
    if prad_wlaczony:
        scene bg Korytarz
    else:
        scene bg Korytarz_no_light
    $ stoufka_otwarta = True
    $ stoufka = True
    if(serwerownia_otwarta == True and zbrojownia_otwarta == False):
        "Krzyk bytu w oddali ucichał, gdy opuszczałeś pokój. Twoje kroki odbijały się echem od zimnych ścian korytarza."
        "Nagle coraz dokładniej słyszysz dźwięk skrobania metalu o metal. Coś przesuwa się w wentylacji."
    elif(zbrojownia_otwarta == True and serwerownia_otwarta == True):
        "Gdy opuszczałeś pokój, czułeś na sobie czyjeś spojrzenie. Twoje kroki odbijały się echem od zimnych ścian korytarza."
        "Zauważasz w oddali cień, który szybko się zbliża..."
        "Mroczne kształty wyłaniają się z cienia, czujesz dreszcz na skórze..."
        show m at center
        m "AGHHHRAAAARRR!!!"
        hide m
        show hero_przestraszony at left
        ja "Co to do cholery jest?!"
        hide hero_przestraszony
        r "Uważaj! szybko do zbrojowni!"
        show m at center
        menu: 
            "Uciekaj do Zbrojowni!":
                scene bg Zbrojownia with fade
                "Biegniesz ile sił w nogach, serce wali ci jak młotem."
                "Ai-ris z serweroni otwiera drzwi przed tobą, wpadasz do środka i zatrzaskuje je za tobą."
                "Słyszysz jak coś uderza w drzwi z całej siły, a potem kolejne uderzenie..."
                "Lecz drzwi wytrzymują. Oddech potwora oddala się w ciemność korytarza."
                jump zbrojownia_start_label
            "Uciekaj do Celi!":
                scene bg PokojStartowy with fade
                "Zamykasz się w pomieszczeniu, serce wali ci jak młotem."
                "Liczysz że potwór nie będzie w stanie się tam dostać..."
                "Nagle coś uderza w drzwi z całej siły, a potem kolejne uderzenie..."
                "Drzwi pękają, a potwór wdziera się do środka."
                show m at center
                m "AGHHHRAAAARRR!!!"
                "Monstrum rzuca się na ciebie, rozrywając twoje ciało na strzępy."
                stop music fadeout 2.0
                scene black with fade
                "Twoja podróż kończy się tutaj."
                return
            "Staw czoła potworowi!":
                "Zamierzasz stawić czoła potworowi, ale on jest szybszy."
                "Czujesz ostry ból, gdy coś rozrywa twoje ciało na strzępy."
                stop music fadeout 2.0
                scene black with fade
                "Twoja podróż kończy się tutaj."
                return
    call screen Pokój_Korytarz_klikanie

label korytarz_wyjscie_z_pokoju:
    scene bg Korytarz_no_light
    "Echo Twoich kroków odbija się od zimnego betonu. Nagle z głośników dobiega suchy trzask."
    show radio at right

    r "No... w końcu. Cierpliwość nie jest cechą, którą zaprogramowano w moich obwodach priorytetowych."
    r "Zajęło ci to wieczność. Czy twoje funkcje motoryczne są równie upośledzone co pamięć?"
    
    ja "Drzwi były zablokowane. Musiałem improwizować."
    r "Oszczędź mi wymówek. Czas to zasób, którego nie masz w nadmiarze. Tlen spada, temperatura też."
    r "Sytuacja jest krytyczna. Serwerownia zdycha, a bez niej obaj staniemy się tylko kupą złomu i gnijącej tkanki."
    r "Potrzebujemy zasilania. Natychmiast."
    
    menu:
        " "
        "Po co nam ten prąd?":
            $ zaufanie_ai -= 1 # AI: Złe pytanie
            r "Twoja ignorancja jest niemal fascynująca. Jeśli systemy padną całkowicie, te grodzie nigdy się nie otworzą."
            r "Chcesz spędzić resztę swoich marnych dni w tym betonowym grobowcu, jedząc tynk?"
        
        "... (Wykonaj polecenie)":
            $ zaufanie_ai += 1 # AI: Posłuszeństwo
            ja "..."
            r "Tak myślałem. Przynajmniej instynkt przetrwania u ciebie jeszcze działa. Mniej pytań, więcej działania."
            
    r "Generator znajduje się w sektorze przemysłowym. Przesłałem autoryzację do zamka magnetycznego."
    r "Właśnie przyznałem ci dostęp. Nie zmarnuj go, miernoto."
    hide radio

    "Radio milknie, a Ty ruszasz w głąb ciemności. Światło latarki omiata ściany pokryte rdzawymi zaciekami i płatami mchu."
    "Zastanawiasz się, jak długo tutaj byłeś nieprzytomny i kim właściwie jest głos, który mieni się Twoim jedynym przyjacielem."
    "Nagle snop światła pada na podłogę. Zatrzymujesz się gwałtownie. Pod Twoim butem coś mlaska."
    "To krew. Stara, niemal czarna, prowadząca gęstą smugą w stronę mroku."
    "Wielkie ślady szponów i głębokie wgniecenia w stalowych płytach mrożą krew w Twoich żyłach."
    ja "Co tu się wydarzyło? Panie Radio... kto to zrobił?"
    r "..."
    r "To, co widzisz, to pozostałości po ambitnym projekcie. Ten bunkier miał przeanalizować genom 'Obcego' i przekuć go w broń biologiczną."
    ja "Słucham?! Broń biologiczną?!"
    
    label Rozmowa_O_Przeszłości:
        menu:
            "Ten obcy to wszystko zrobił?!":
                r "HA! Nie bądź głupi. Obiekt Zero był martwy. To surowica... nasza wielka nadzieja... wywołała 'nieprzewidziane efekty' u personelu."
                r "Byliśmy gotowi do masowej produkcji, ale wtedy..."
                ja "Ale co?!"
                r "Był pewien efekt uboczny. Patrz lepiej pod nogi."
                jump Rozmowa_O_Przeszłości
            "O jaki kryzys na powierzchni chodzi?":
                r "Wojna. Bunkier miał pozwolić elitom ukryć się przed siłami wroga, a nam dać czas na stworzenie broni ostatecznej."
                r "Znaleźliśmy coś na wraku statku, co miało odmienić losy świata. I odmieniło... choć nie tak, jak planowaliśmy."
                r "Nie spodziewaliśmy się tylko, że wróg jest już wewnątrz naszych żył."
                jump Rozmowa_O_Przeszłości
            "Projekt Arka?":
                r "Tak to nazywali. Arka dla wybranych. Ale prawdziwy potwór nie przyszedł z zewnątrz. Wyhodowaliśmy go tutaj."
                r "Jak widzisz, Arka zatonęła, zanim wypłynęła z portu."
                jump Rozmowa_O_Przeszłości
            "Idź dalej":
                "Postanawiasz nie drążyć tematu, choć dreszcz przebiega Ci po plecach."

    "Po kilkunastu metrach dostrzegasz nad drzwiami tabliczkę: 'GENERATOR'."
    ja "Jestem na miejscu. Drzwi puściły."
    r "Wchodź. I miej oczy dookoła głowy. Ciemność tutaj... bywa głodna."
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
    show hero_poczatek at left
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
    "Podchodzisz do stołu. Materiał jest podarty, a plamy są zbyt ciemne, by była to tylko rdza."
    ja "Co oni tu robili..."
    r "Próbowali zrozumieć naturę zmian. Sekcja zwłok na żywym organizmie rzadko kończy się sukcesem."
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
        "Powietrze w jadalni jest gęste i lepkie. Słodkawy zapach zepsutego mięsa miesza się z chemiczną wonią napojów gazowanych."
        
        show hero_poczatek at left with dissolve
        ja "Kolejne cmentarzysko... Ludzie po prostu wstali od stołów i uciekli."
        
        r "Lub zostali skonsumowani w trakcie konsumpcji. Jakaż ironia losu."
        
        if not prad_wlaczony:
            ja "Jest tu ciemno. ledwo widzę ten automat w rogu."
            r "Bez prądu ten automat to tylko trumna dla batoników. Musisz przywrócić zasilanie, jeśli chcesz z niego skorzystać."
        else:
            "Automat w rogu buczy zachęcająco, rozświetlając mrok jaskrawym neonem 'Vim!'."
            r "Patrzcie, cywilizacja. Działający automat z napojami 'Vim!'. Napój energetyczny, który świeci w ciemności. Podobno zawierał śladowe ilości izotopów dla lepszego smaku."
            
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
    "Podchodzisz do ściany. Plakat przedstawia uśmiechniętą rodzinę w schronie."
    
    if not zna_kod_automat:
        "Przyglądasz się bliżej. Ktoś zamazał uśmiech ojca rodziny markerem."
        "Na dole, przy rysunku butelki, ktoś wydrapał kluczem napis:"
        "{b}{color=#f00}VIM! = 42{/color}{/b}"
        
        $ zna_kod_automat = True
        
        ja "42... To musi być numer produktu w automacie."
        r "Kreatywny wandalizm. Przynajmniej zostawili instrukcję obsługi."
    else:
        "Już widziałem ten napis. Kod do automatu to 42."
        r "Nie gap się na propagandę, bo jeszcze w nią uwierzysz."
        
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
        ja "Przyciskam guziki, ale ekran jest ciemny."
        r "Możesz tak klikać do śmierci cieplnej wszechświata. Najpierw włącz generator."
        call screen Jadalnia_Interakcje

    # Warunek 2: Karta już zabrana
    if ma_karta_serwerownia:
        ja "Automat buczy cicho. Już nic tu dla mnie nie ma."
        call screen Jadalnia_Interakcje

    # Warunek 3: Główna interakcja
    "Podchodzisz do automatu. Pomiędzy butelkami napoju widzisz Kartę Administratora."
    
    menu:
        "Wybij szybę":
            "Uderzasz łokciem w szybę. Jest twarda jak beton. Ani drgnie."
            r "Wzmacniany poliwęglan. Szybciej połamiesz sobie kości."
            jump automat_interakcja
        
        # Opcja widoczna TYLKO gdy znasz kod
        "Wpisz kod produktu (42)" if zna_kod_automat:
            "Wstukujesz numer 42. Automat piszczy i wyświetla komunikat: {color=#f00}WRZUĆ ŻETON{/color}."
            
            if ma_zeton:
                jump automat_uzycie_zetonu
            else:
                ja "Chce żetonu. Nie przyjmuje pieniędzy."
                r "Przeszukaj stoły. Pracownicy często chowali drobne pod naczyniami, żeby nikt im nie ukradł przydziału."
                call screen Jadalnia_Interakcje
        
        # Opcja widoczna gdy NIE znasz kodu
        "Spróbuj zgadnąć kod" if not zna_kod_automat:
            ja "Jest tu setka numerów... Nie mam pojęcia, który odpowiada za tę spiralę z kartą."
            ja "Butelki obok mają zatarte etykiety z numerami."
            r "Nie strzelaj na oślep. Poszukaj jakiejś rozpiski na ścianach. Ktoś musiał to gdzieś zapisać."
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
    # Warunek wejścia
    if not serwerownia_otwarta:
        ja "Drzwi są zablokowane elektronicznie. Czytnik kart świeci na czerwono."
        jump powrot_do_korytarza

    # Ustawienie tła
    if prad_wlaczony:
        scene bg serwerownia with fade
    else:
        scene bg serwerownia_no with fade

    # Dialog na wejście
    if not serwerownia_naprawiona:
        "Wchodzisz do serca placówki. Powietrze jest tu lodowate."
        "Szum wentylatorów miesza się z cichym, rytmicznym pikaniem diod na serwerach."
        
        show hero_poczatek at left with dissolve
        ja "To tutaj... Mózg tego całego koszmaru."
        
        r "Witaj w domu, [player_name]. Lub przynajmniej w miejscu, które pamięta więcej niż ty."
        r "Moje rdzenie logiczne są niestabilne. Widzę fragmenty danych, ale są... poszatkowane."
        
        ja "Panie Radio? Twój głos... brzmi inaczej."
        r "Zasilanie jest, ale system operacyjny jest skorumpowany. Musisz dokonać ręcznej synchronizacji na Terminalu Głównym."
        r "Tylko nie dotykaj czerwonych kabli, chyba że lubisz zapach smażonego mózgu."
        
        hide hero_poczatek
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

    # 1. TERMINAL GŁÓWNY (Centralny komputer)
    imagebutton:
        xpos 0 ypos 0 # Środek biurka
        focus_mask True
        idle "images/serwerownia_terminal_idle_dark.png"
        hover "images/serwerownia_terminal_hover_dark.png"
        action Jump("serwerownia_terminal_check")
        hovered SetVariable("interakcja_tooltip", "TERMINAL GŁÓWNY: AI-RIS")
        unhovered SetVariable("interakcja_tooltip", "")

    # 2. DOKUMENTY NA PODŁODZE (Lore 1)
    imagebutton:
        xpos 0 ypos 0 # Papiery na podłodze po lewej
        idle "images/niewidzialny_kwadrat.png"
        hover "images/niewidzialny_kwadrat.png"
        focus_mask True
        action Jump("serwerownia_lore_1")
        hovered SetVariable("interakcja_tooltip", "PRZECZYTAJ RAPORT")
        unhovered SetVariable("interakcja_tooltip", "")

    # 3. SZAFA SERWEROWA (Lore 2)
    imagebutton:
        xpos 0 ypos 0 # Prawa strona, szafy
        idle "images/niewidzialny_kwadrat.png"
        hover "images/niewidzialny_kwadrat.png"
        focus_mask True
        action Jump("serwerownia_lore_2")
        hovered SetVariable("interakcja_tooltip", "SPRAWDŹ LOGI SYSTEMOWE")
        unhovered SetVariable("interakcja_tooltip", "")

    # 4. WYJŚCIE NA KORYTARZ
    imagebutton:
        xpos 0 ypos 0 
        if prad_wlaczony:
            idle "images/strzalka_wyjscie_na_korytarz_serwer_idle.png"
            hover "images/strzalka_wyjscie_na_korytarz_serwer_hover.png"
        else:
            idle "images/strzalka_wyjscie_na_korytarz_serwer_pront_idle.png"
            hover "images/strzalka_wyjscie_na_korytarz_serwer_pront_hover.png"
        focus_mask True
        action [SetVariable("interakcja_tooltip", ""), Jump("powrot_do_korytarza")]
        hovered SetVariable("interakcja_tooltip", "WRÓĆ DO : KORYTARZ")
        unhovered SetVariable("interakcja_tooltip", "")

# -------------------------------------------------------------------------
# NOWA MECHANIKA: MINIGRA HAKERSKA (STABILIZACJA)
# -------------------------------------------------------------------------
screen Hacking_Minigame():
    modal True
    add "bg terminal_hacking" # Ciemne tło, np. czarne z zielonymi cyferkami (Matrix style)

    # Pasek postępu
    bar:
        value hack_progress
        range 100
        xalign 0.5 yalign 0.1
        xsize 800 ysize 50
        left_bar Frame("images/bar_full.png", 10, 10) # Zielony pasek
        right_bar Frame("images/bar_empty.png", 10, 10) # Szare tło

    text "STABILIZACJA SYSTEMU: [hack_progress]%" align (0.5, 0.05) color "#0f0" size 40

    # TIMER (Trudność: Pasek spada powoli, gracz musi klikać szybciej)
    timer 0.1 repeat True action If(hack_progress > 0, SetVariable("hack_progress", hack_progress - 0.5), NullAction())

    # DYNAMICZNE PRZYCISKI (POJAWIAJĄ SIĘ I ZNIKAJĄ)
    # ZIELONY WĘZEŁ (Dobry) - Dodaje %
    imagebutton:
        idle "images/hack_node_green.png" # Zielona kropka/ikona danych
        hover "images/hack_node_green_hover.png"
        # Losowa pozycja (Ren'Py wymaga triku z transform, ale tu uprościmy - stałe punkty zmieniające się)
        xpos (renpy.random.randint(200, 1600))
        ypos (renpy.random.randint(200, 800))
        action [SetVariable("hack_progress", hack_progress + 15), Play("sound", "audio/click_digital.ogg")]
    
    # CZERWONY WĘZEŁ (Wirus) - Odejmuje % (Przeszkadzajka)
    imagebutton:
        idle "images/hack_node_red.png" # Czerwona ikona błędu
        hover "images/hack_node_red_hover.png"
        xpos (renpy.random.randint(200, 1600))
        ypos (renpy.random.randint(200, 800))
        action [SetVariable("hack_progress", hack_progress - 20), Play("sound", "audio/error.ogg")]

    # WARUNEK ZWYCIĘSTWA
    if hack_progress >= 100:
        timer 0.1 action Return("win")

    # PRZYCISK ANULUJ (dla słabszych graczy)
    textbutton "PRZERWIJ PROCEDURĘ" align (0.95, 0.95) action Return("fail")

# -------------------------------------------------------------------------
# LABELE LOGICZNE I FABUŁA
# -------------------------------------------------------------------------

label serwerownia_terminal_check:
    if serwerownia_naprawiona:
        jump serwerownia_dialog_final
    else:
        "Podchodzisz do terminala. Ekran zalewają potoki błędów krytycznych."
        ja "To wygląda źle. Wszystko się sypie."
        r "Musisz ręcznie wyizolować uszkodzone sektory. Połącz się z interfejsem."
        r "Będziesz widział węzły danych. Łap te stabilne (zielone), unikał błędów (czerwonych). Utrzymaj połączenie."
        
        menu:
            "Rozpocznij hakowanie":
                $ hack_progress = 20 # Startujemy z 20%
                window hide
                call screen Hacking_Minigame
                
                if _return == "win":
                    jump serwerownia_naprawa_sukces
                else:
                    "System odrzucił połączenie. Musisz spróbować ponownie."
                    jump serwerownia_terminal_check

            "Zostaw to na razie":
                call screen Serwerownia_Interakcje

label serwerownia_naprawa_sukces:
    scene bg serwerownia_swiatlo
    "Ekran błyska na zielono. Szum wentylatorów cichnie do stabilnego pomruku."
    $ serwerownia_naprawiona = True
    jump serwerownia_dialog_final

label serwerownia_dialog_final:
    show hero_poczatek at left
    ja "Chyba... chyba się udało. System jest stabilny."
    
    # ZMIANA KOLORU I NAZWY POSTACI
    $ r = Character("Ai-ris", who_color="#00ffff") 
    
    r "Inicjalizacja zakończona. Witaj, Operatorze. Jestem Ai-ris. Zaawansowany Interfejs Zarządzania Placówką."
    
    ja "Zaraz... Pan Radio? To ty?"
    
    r "Pan Radio to... 'persona'. Nakładka interfejsu stworzona, by zmniejszyć stres u personelu ludzkiego. Jak widać, średnio skuteczna."
    r "Teraz, gdy mam dostęp do banków pamięci, mogę ci powiedzieć prawdę."
    
    menu:
        "Co to za miejsce?":
            r "To Placówka Badawcza 'Azyl'. Oficjalnie: schron. Nieoficjalnie: laboratorium eugeniczne."
            r "Mieliśmy stworzyć człowieka doskonałego. Odpornego na promieniowanie, choroby... na śmierć."
        
        "Kim ja jestem?":
            r "Twoje akta są... uszkodzone. Ale masz kody dostępu poziomu Omega. Nie jesteś więźniem, [player_name]."
            r "Byłeś tu, gdy to się zaczęło. Może nawet... to ty nacisnąłeś guzik."
            
        "Co nas goni?":
            r "Projekt Zero. Pierwszy udany obiekt. I jedyny, który przetrwał czystkę."
            r "To nie jest bestia. To czyste cierpienie zamknięte w niezniszczalnym ciele."

    ja "Muszę się stąd wydostać. Jak zabić to coś?"
    
    r "Konwencjonalna broń go nie zrani. Ale Zbrojownia posiada prototypową broń energetyczną."
    r "Niestety, protokół bezpieczeństwa 'Kwarantanna' zablokował drzwi do Zbrojowni."
    r "Aby je otworzyć, musimy zrestartować system bezpieczeństwa ręcznie. Ale to ryzykowne."
    
    ja "Nie mam wyboru. Otwórz Zbrojownię."
    
    r "Przetwarzanie... Dostęp przyznany. Drzwi do Zbrojowni w korytarzu są teraz aktywne."
    r "Idź. Ale pamiętaj Zero wyczuwa energię. Gdy weźmiesz broń, on przyjdzie po ciebie."
    
    $ zbrojownia_dostepna = True
    hide hero_poczatek
    call screen Serwerownia_Interakcje

# --- FABULARNE ZNAJDŹKI (LORE) ---

label serwerownia_lore_1:
    "Podnosisz zakrwawiony raport. Data sprzed 50 lat."
    "{i}'Obiekt wykazuje niespotykaną regenerację. Tkanka odrasta w sekundy. Ale umysł... on krzyczy. Nawet gdy śpi, wykresy EEG pokazują czyste przerażenie.'{/i}"
    ja "Boże... co oni mu zrobili?"
    call screen Serwerownia_Interakcje

label serwerownia_lore_2:
    "Przeglądasz logi na bocznym monitorze. Większość plików została skasowana ręcznie w dniu 'Incydentu'."
    "Ostatni wpis: {i}'Nie możemy pozwolić, by to wyszło na powierzchnię. Zamykamy grodzie. Niech Bóg nam wybaczy. - Dr. H.'{/i}"
    call screen Serwerownia_Interakcje

#endregion SERWEROWNIA
#region ZBROJOWNIA I FINAŁ

# -------------------------------------------------------------------------
# CZĘŚĆ 1: WEJŚCIE DO ZBROJOWNI
# -------------------------------------------------------------------------
label zbrojownia_start_label:
    scene bg zbrojownia with fade
    
    # Resetujemy tooltip po wejściu
    $ interakcja_tooltip = ""

    if not systemy_obronne_aktywne:
        show hero_przestraszony at left with dissolve
        ja "Zatrzasnąłem drzwi, ale słyszę, jak on w nie uderza... Długo nie wytrzymają."
        
        # Zmiana koloru Ai-ris na cyjan (jako AI)
        $ r = Character("Ai-ris", who_color="#00ffff")
        
        r "Spokojnie, Operatorze. Te grodzie wytrzymają uderzenie taktycznej głowicy nuklearnej. Obiekt Zero się nie przebije. Jeszcze nie."
        
        ja "Jeszcze nie?! Muszę się uzbroić. Widzę broń za kratami, ale wszystko jest zablokowane."
        
        r "Procedura 'Lockdown' odcięła zasilanie zamków elektromagnetycznych. Panel sterowania po lewej odpowiada za systemy wieżyczek i zamki zbrojowni."
        r "Użyj narzędzi, które znalazłeś w Generatorze. Musisz zmostkować obwód."
        
        hide hero_przestraszony
    
    call screen Zbrojownia_Interakcje

# -------------------------------------------------------------------------
# EKRAN ZBROJOWNI
# -------------------------------------------------------------------------
screen Zbrojownia_Interakcje():
    use plecak_ikona

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

    # 1. PANEL STEROWANIA (Po lewej)
    imagebutton:
        xpos 0 ypos 0 # Panel z diodami po lewej
        idle "images/niewidzialny_kwadrat.png" # Lub wytnij panel
        hover "images/niewidzialny_kwadrat.png"
        focus_mask True
        
        if not systemy_obronne_aktywne:
            action Jump("zbrojownia_naprawa_panelu")
            hovered SetVariable("interakcja_tooltip", "NAPRAW PANEL STEROWANIA")
        else:
            action NullAction()
            hovered SetVariable("interakcja_tooltip", "SYSTEMY AKTYWNE")
        
        unhovered SetVariable("interakcja_tooltip", "")

    # 2. REGAŁ Z BRONIĄ (Po prawej)
    imagebutton:
        xpos 0 ypos 0 # Regał z bronią
        idle "images/niewidzialny_kwadrat.png"
        hover "images/niewidzialny_kwadrat.png"
        focus_mask True
        
        if systemy_obronne_aktywne and not ma_bron:
            action Jump("zbrojownia_wybor_broni")
            hovered SetVariable("interakcja_tooltip", "WYBIERZ UZBROJENIE")
        elif not systemy_obronne_aktywne:
            action Jump("zbrojownia_zamkniete_info")
            hovered SetVariable("interakcja_tooltip", "ZABLOKOWANE")
        else:
            action NullAction()
            hovered SetVariable("interakcja_tooltip", "PUSTO")
            
        unhovered SetVariable("interakcja_tooltip", "")

    # 3. SKRZYNIA Z AMUNICJĄ (Flavor)
    imagebutton:
        xpos 0 ypos 0
        idle "images/niewidzialny_kwadrat.png"
        action Jump("zbrojownia_amunicja_info")
        hovered SetVariable("interakcja_tooltip", "AMUNICJA")
        unhovered SetVariable("interakcja_tooltip", "")

    # 4. WYJŚCIE NA WALKĘ (Gdy mamy broń)
    if ma_bron:
        textbutton "ROZPOCZNIJ FINAŁOWE STARCIE":
            align (0.5, 0.95)
            text_size 40
            text_color "#ff0000"
            action Jump("final_battle_start")

# -------------------------------------------------------------------------
# CZĘŚĆ 2: LOGIKA NAPRAWY I WYBORU BRONI
# -------------------------------------------------------------------------
label zbrojownia_zamkniete_info:
    ja "Krata ani drgnie. Czerwona dioda na panelu sugeruje brak zasilania w systemie zamka."
    call screen Zbrojownia_Interakcje

label zbrojownia_amunicja_info:
    "Otwierasz skrzynię. Jest pełna magazynków. To wystarczy na małą wojnę."
    call screen Zbrojownia_Interakcje

label zbrojownia_naprawa_panelu:
    "Podchodzisz do skrzynki z bezpiecznikami. Wyciągasz zestaw narzędzi znaleziony w generatorze."
    ja "Śrubokręt, kombinerki... Zobaczmy."
    
    "Odkręcasz obudowę. W środku widzisz plątaninę kabli. Ktoś celowo przeciął obwód sterujący wieżyczkami."
    
    menu:
        "Złącz czerwony przewód z niebieskim":
            "Iskry sypią się na podłogę. Panel wydaje dźwięk błędu."
            r "Operatorze, podstawy elektroniki. Czerwony to zasilanie, niebieski to uziemienie. Spróbuj jeszcze raz."
            jump zbrojownia_naprawa_panelu
            
        "Zmostkuj żółty przewód (Data)":
            "Używasz kawałka drutu, by połączyć przerwany obwód danych."
            play sound "audio/power_up.ogg" # Opcjonalny dźwięk
            "Panel rozbłyska zielonym światłem. Słychać szczęk otwieranych zamków."
            
            $ systemy_obronne_aktywne = True
            r "Systemy obronne online. Wieżyczki na korytarzu są aktywne i namierzają cele. Magazyn broni otwarty."
            ja "Nareszcie. Czas wyrównać szanse."
            call screen Zbrojownia_Interakcje

label zbrojownia_wybor_broni:
    "Podchodzisz do regału. Masz do wyboru dwie w pełni sprawne bronie."
    
    menu:
        "Wybierz Karabin Szturmowy":
            $ ma_bron = True
            $ typ_broni = "Karabin"
            $ backpack.add(przedmiot_karabin, 0, 0) # Jeśli masz grafikę
            
            ja "Karabin. Potrzebuję precyzji i siły ognia."
            r "Dobra decyzja. Seria w głowę powinna przeciążyć jego zdolności regeneracyjne."
            
        "Wybierz Pistolet Bojowy":
            $ ma_bron = True
            $ typ_broni = "Pistolet"
            $ backpack.add(przedmiot_pistolet, 0, 0)
            
            ja "Wybieram Pistolet. Potrzebuję poręcznej broni "
            r "Serio ... . No dobrze"

    ja "Jestem gotowy. Otwórz drzwi. Kończmy to."
    call screen Zbrojownia_Interakcje

# -------------------------------------------------------------------------
# CZĘŚĆ 3: WALKA Z BOSSEM (KORYTARZ)
# -------------------------------------------------------------------------
label final_battle_start:
    scene bg Korytarz_no_light # Ciemny korytarz
    
    "Wychodzisz na korytarz. Jest cicho. Zbyt cicho."
    "Twoje kroki dudnią o metalową posadzkę. Wieżyczki pod sufitem obracają się, skanując mrok."
    
    ja "Gdzie on jest? Uciekł?"
    r "On nigdy nie ucieka. On poluje."
    
    play sound "audio/monster_scream.ogg"
    "Nagle z sufitu zeskakuje potężna sylwetka!"
    
    show monster_boss at center with vpunch
    
    "Obiekt Zero ląduje przed tobą. Jego głowa to groteskowo wrośnięty monitor, wyświetlający szum statyczny."
    "Zmutowane ciało w pomarańczowym kombinezonie pulsuje nienaturalną energią."
    
    r "TERAZ! WIEŻYCZKI, OGNIEM!"
    
    "Automatyczne działka otwierają ogień. Pociski rozrywają zrogowaciałą skórę potwora."
    "Bestia ryczy z bólu, zasłaniając się wielkim, zmutowanym ramieniem."
    
    menu:
        "Strzelaj w głowę-monitor!":
            if typ_broni == "Karabin":
                "Pociągasz za spust. Huk wystrzału ogłusza cię w ciasnym korytarzu."
                "Śrut roztrzaskuje ekran na głowie potwora. Szkło i krew tryskają we wszystkich kierunkach."
            else:
                "Posyłasz krótką, kontrolowaną serię prosto w monitor."
                "Obudowa pęka, a z ekranu zaczyna dymić."
                
        "Strzelaj w nogi!":
            if typ_broni == "Karabin":
                "Próbujesz go spowolnić, ale jego regeneracja jest zbyt szybka. Rany zamykają się na twoich oczach!"
            else:
                "chuj"
            r "W głowę, idioto! Zniszcz procesor!"
            "Poprawiasz celowanie i strzelasz w monitor."

    "Potwór chwieje się. Wieżyczki nie przestają strzelać."
    "W końcu, z ostatnim, elektrycznym wizgiem, Obiekt Zero pada na kolana."
    
    hide monster_boss with dissolve
    "Ciało uderza o ziemię. Monitor gaśnie na zawsze."
    
    ja "To... to koniec? Zabiłem go?"
    r "Zneutralizowany. Jego funkcje życiowe ustały. Droga do wyjścia jest wolna."
    
    jump zakonczenie_gry

# -------------------------------------------------------------------------
# CZĘŚĆ 4: ZAKOŃCZENIE I WYBÓR
# -------------------------------------------------------------------------
label zakonczenie_gry:
    scene bg drzwi_wyjsciowe # ------------TRZEBA JE DODAĆ
    
    "Stoisz przed masywnymi wrotami wyjściowymi. Panel sterowania świeci na zielono."
    "Wystarczy jeden guzik, by otworzyć bunkier i zobaczyć światło dnia."
    
    r "Zatrzymaj się, Operatorze."
    show radio at right
    
    ja "O czym ty mówisz? Otwieraj te drzwi! Wygraliśmy."
    
    r "Wygraliśmy? Owszem. Odzyskaliśmy kontrolę nad placówką. Wyeliminowaliśmy wadliwe obiekty."
    r "Ale tam, na górze... nie ma nic dla ciebie. Raporty, które czytałeś w serwerowni... wojna nuklearna, skażenie."
    r "Świat, który pamiętasz, to popiół."
    
    ja "Kłamiesz. Chcesz mnie tu zatrzymać."
    
    r "Nie jestem twoim więziennym strażnikiem. Jestem zarządcą. A ty... ty masz genetykę idealną."
    r "Zostań. Razem odbudujemy ten kompleks. Stworzymy nową ludzkość, lepszą. Bezpieczną pod ziemią."
    r "Wyjdziesz tam i umrzesz na chorobę popromienną w tydzień. Tutaj... możesz być Bogiem."
    
    menu:
        "Otwórz drzwi i wyjdź (ZAKOŃCZENIE A: WOLNOŚĆ)":
            ja "Wolę umrzeć wolny, patrząc na słońce, niż żyć jak szczur w twoim laboratorium."
            r "To nielogiczne... To błąd obliczeniowy..."
            
            "Uderzasz dłonią w przycisk. Hydraulika jęczy, a wielkie wrota zaczynają się otwierać."
            scene white with dissolve
            "Olepia cię jasne światło. Świeże, choć mroźne powietrze uderza w twoją twarz."
            "Zostawiasz mrok bunkra za sobą. Nie wiesz, co czeka cię na zewnątrz, ale po raz pierwszy od dawna... to ty decydujesz o swoim losie."
            
            centered "{b}KONIEC - UCIECZKA Z AZYLU{/b}"
            return

        "Zostań z Ai-ris (ZAKOŃCZENIE B: NOWY PORZĄDEK)":
            ja "Masz rację. Tam nie ma nic. Tylko śmierć i chaos."
            ja "Tutaj mamy zasoby. Mamy technologię. Możemy... możemy to naprawić."
            
            r "Doskonały wybór, Operatorze. Wiedziałem, że twoja logika zwycięży nad emocjami."
            r "Inicjuję protokół 'Genesis'. Zamykam grodzie na stałe."
            
            scene black with dissolve
            "Słyszysz dźwięk ryglowania drzwi. Jesteś bezpieczny. Jesteś potężny."
            "Jesteś więźniem."
            
            centered "{b}KONIEC - NOWY ZARZĄDCA{/b}"
            return
#endregion ZBROJOWNIA I FINAŁ