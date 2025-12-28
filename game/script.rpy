##Definicje postaci 
default player_name = "hero"
define ja = Character("[player_name]", who_color="#00ccff")
define r = Character("Radio", who_color="#1bdb8b")
define m = Character("???", who_color="#ff0000") # Potwór

## zmienne logiczne ( flagi) do śledzenia postępów
default ma_lom = False
default ma_latarke = False
default ma_bezpiecznik = False
default ma_karta_dostepu = False
default ma_mapa = True ##zamienić na false
default prad_wlaczony = False
default drzwi_wyjsciowe_otwarte = False
default zbrojownia_otwarta = False
default serwerownia_otwarta = False
default generator_otwarty = False
default pokoj1_otwarty = True
default szpital_otwarty = False
default drzwi_cela_wywalone = False
default interakcja_tooltip = ""


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

# ------------------------------------------------------Tutaj sobie możesz sceny na starcie pominąć niebedzie potrzeby przeklikiwania :3
label start:  
#region Opis Sceny Pierwszej (btw możesz to zminimalizować)

#Gracz budzi się z ogromną amnezją, wita go Pan Radio i "tłumaczy" sytuacje w jakiej się znajduje na koniec rozmowy gasną światła.
#Gracz ma za zadanie odnaleźć przedmioty które pozwolą mu wyjść z tego ciemnego pomieszczenia. 

#endregion 
    label początek_gry:
        scene black with dissolve
        stop music fadeout 2.0
        
        "Budzi cię tępy, pulsujący ból z tyłu czaszki. Próbujesz otworzyć oczy, ale powieki są ciężkie jak ołów."
        "W ustach czujesz metaliczny posmak krwi i stęchliznę."
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
                "Odpowiesz na moje pytanie?!":
                    hide hero_poczatek
                    show hero_wkurw at left
                    ja "Pytam kim jesteś i co ja tu do cholery robię?!"
                    
                    hide hero_wkurw
                    show hero_podstawowy at left
                    
                    r "Adrenalina rośnie. Puls przyspiesza. Fascynujące, ale bezcelowe."
                    r "Powiedziałem wyraźnie: jestem Pan Radio. Jestem głosem w ścianach."
                    r "Mogę być kim zechcę, ale dla ciebie jestem Bogiem tego małego, betonowego świata."
                    r "Nie irytuj mnie. Sprzężenie zwrotne bywa bolesne."
                   
                "(Milcz i rozglądaj się)":  
                    ja "..."
                    "Rozglądasz się nerwowo, szukając źródła głosu, ale głośniki są ukryte głęboko w rdzewiejących ścianach."
                    
                    hide hero_poczatek
                    show hero_podstawowy at left
                
            r "W każdym razie, cieszę się, że tu jesteś."
            r "Sytuacja jest prosta: drzwi są zamknięte, tlen się kończy a ja się nudzę. Wyjdź stąd, zanim zginiesz."
            r "A właśnie jak ci tam było?"
            $ player_name = renpy.input("Jak masz na imię? ", length=15).strip()
            if player_name == "":
                $ player_name = "hero"
            ja "Możesz na mnie mówić [player_name]"
            ja "Właśnie jak mam stąd wyjść"
            r "Eksploruj. Kombinuj. i takie tam.."
            hide radio    
            ja "Psia mać! muszę coś wykombinować bo oszaleje.."
            hide hero_podstawowy
            "słyszysz jak coś buczy po za twoim pomieszczniem, zaczynają mrugać światła i po chwili kompletnie gasną"

#-----------------Tło się zmienia na brak światła---------
        scene bg PokojStartowybezswiatla
        show hero_wkurw at left
        ja "Świetnie jeszcze tego brakowało.."
        hide hero_wkurw
        show screen plecak_ikona 
        
        # Wywołanie ekranu z zagadkami
        call screen Pokój_startowy_zagadka

#-----------------------------------Pierwsza "Zagadka" w grze dzięki niej gracz otrzymuje latarkę i łom-------------------------------------
#region Pokoj startowy

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

        hovered If(drzwi_cela_wywalone, SetVariable("interakcja_tooltip", "KORYTARZ"), SetVariable("interakcja_tooltip", "ZAMKNIĘTE DRZWI"))
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

label akcja_zabrania_lomu:
    $ ma_lom = True
    "Twoje dłonie zaciskają się na zimnej, stalowej sztabie. Solidny łom."
    ja "Może uda mi się nim wyważyć drzwi."
    call screen Pokój_startowy_zagadka

label akcja_zabrania_latarki:
    $ ma_latarke = True
    "Zabrałeś latarkę."
    call screen Pokój_startowy_zagadka

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
            
label Zajrzyj_pod_łóżko:  
    "W świetle latarki dostrzegasz wyschnięte truchło szczura ukryte w kącie."
    "Czuć od niego słodkawy odór rozkładu, który wcześniej brałeś za zwykłą stęchliznę."
    show hero_dziwny at left
    ja "Spałem nad tym truchłem... Jak długo byłem nieprzytomny?"
    hide hero_dziwny
    call screen Pokój_startowy_zagadka    

# --------------------------------------------------------------------Scena Druga Korytarz -------------------------------------------------
#region Opis Sceny Drugiej
#-Gracz zostaje "Pochwalony" przez pana radio za rozwiązanie poprzedniej zagadki. 
#-Gra (pan radio) Prowadzi gracza do pomieszczenia z generatorem.
#endregion 

label powrot_do_korytarza:
    call screen Pokój_Korytarz_klikanie

label korytarz_wyjscie_z_pokoju:
    scene bg Korytarz_no_light
    "Echo Twoich kroków odbija się od zimnego betonu. Nagle z głośników dobiega suchy trzask."
    show radio at right
    r "No... w końcu. Cierpliwość nie jest cechą, którą zaprogramowano w moich obwodach."
    r "Zajęło ci to wieczność. Czy twoje funkcje motoryczne są równie upośledzone co pamięć?"
    ja "Drzwi były zablokowane. Musiałem..."
    r "Oszczędź mi wymówek. Czas to zasób, którego nie masz w nadmiarze."
    r "Sytuacja jest krytyczna. Serwerownia zdycha, a bez niej obaj staniemy się tylko kupą złomu i gnijącej tkanki."
    r "Potrzebujemy zasilania. Natychmiast."
    menu:
        " "
        "Po co nam ten prąd?":
            r "Twoja ignorancja jest niemal fascynująca. Jeśli systemy padną całkowicie, te grodzie nigdy się nie otworzą."
            r "Chcesz spędzić resztę swoich marnych dni w tym betonowym grobowcu?"
        "...":
            ja "..."
    r "Tak myślałem. Przynajmniej instynkt przetrwania u ciebie jeszcze działa."
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
    call screen Pokój_Korytarz_klikanie

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
        hovered SetVariable("interakcja_tooltip", "POWRÓT: Cela")
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
            hovered SetVariable("interakcja_tooltip", "WEJDŹ: Pomieszczenie z Generatorem")
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
            hovered SetVariable("interakcja_tooltip", "EKSPLORUJ: Skrzydło Medyczne")
        else:
            action Jump("apteka_zablokowana_info")
            hovered SetVariable("interakcja_tooltip", "SEKTOR MEDYCZNY: Dostęp zabroniony")
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


#-------------------------------------------------------------------------Scena trzecia Gaenerator-----------------------------------------------------------------
#region Opis sceny Trzeciej
#-Gracz w pomieszczeniu z generatorem odkrywa mapę placówki (przez kadr zbliżenia).
#-Gracz znajduje pudełko pod stołem, w którym ukryta jest karta dostępu do Sektora Medycznego (przez kadr zbliżenia).
#-Znalezienie karty dostępu ustawia flagę apteka_otwarta na True.
#endregion Region name

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
    # Tooltip
    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2, "#000", 0, 0)]

    # 1. MAPA (Na ścianie/stole - Otwiera kadr zbliżenia)
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
        idle "images/generator_maszyna_idle.png"
        hover "images/generator_maszyna_hover.png"
        focus_mask True
        action Jump("interakcja_generator_maszyna")
        hovered SetVariable("interakcja_tooltip", "GENERATOR GŁÓWNY")
        unhovered SetVariable("interakcja_tooltip", "")

    # 3. STÓŁ WARSZTATOWY (Opis)
    imagebutton:
        xpos 0 ypos 0
        idle "images/stol_warsztatowy_idle.png"
        hover "images/stol_warsztatowy_hover.png"
        focus_mask True
        action Jump("stol_warsztatowy_dialog")
        hovered SetVariable("interakcja_tooltip", "STÓŁ WARSZTATOWY")
        unhovered SetVariable("interakcja_tooltip", "")

    # 4. PUDŁO POD STOŁEM (Otwiera zbliżenie na kartę)
    imagebutton:
        xpos 0 ypos 0
        idle "images/pudlo_generator_idle.png"
        hover "images/pudlo_generator_hover.png"
        focus_mask True
        action Show("pudlo_zblizenie")
        hovered SetVariable("interakcja_tooltip", "OTWÓRZ PUDŁO")
        unhovered SetVariable("interakcja_tooltip", "")

    # Przycisk mapy (HUD) - widoczny tylko po jej znalezieniu
    if ma_mapa:
        use przycisk_mapy 

# --- EKRAN ZBLIŻENIA: KADR NA MAPĘ ---
screen mapa_zblizenie():
    modal True
    zorder 160
    add "images/mapa_kadr_bg.png" # Tło kadru mapy

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2, "#000", 0, 0)]

    if not ma_mapa:
        imagebutton:
            xpos 500 ypos 300 # Dopasuj pozycję mapy na kadrze
            idle "images/mapa_przedmiot_idle.png"
            hover "images/mapa_przedmiot_hover.png"
            focus_mask True
            action [SetVariable("interakcja_tooltip", ""), Hide("mapa_zblizenie"), Jump("znalezienie_mapy")]
            hovered SetVariable("interakcja_tooltip", "POBIERZ SCHEMAT PLACÓWKI")
            unhovered SetVariable("interakcja_tooltip", "")

    textbutton "Wróć":
        align (0.5, 0.9)
        action [SetVariable("interakcja_tooltip", ""), Hide("mapa_zblizenie")]

# --- EKRAN ZBLIŻENIA: WNĘTRZE PUDŁA ---
screen pudlo_zblizenie():
    modal True
    zorder 160
    add "images/pudlo_wnetrze_bg.png" # Tło wnętrza pudła

    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2, "#000", 0, 0)]

    if not ma_karta_dostepu:
        imagebutton:
            xpos 800 ypos 450 # Pozycja karty w pudełku
            idle "images/karta_medyczna_idle.png"
            hover "images/karta_medyczna_hover.png"
            focus_mask True
            action [SetVariable("interakcja_tooltip", ""), Hide("pudlo_zblizenie"), Jump("akcja_znalezienia_karty")]
            hovered SetVariable("interakcja_tooltip", "WEŹ KARTĘ DOSTĘPU")
            unhovered SetVariable("interakcja_tooltip", "")

    textbutton "Wróć":
        align (0.5, 0.9)
        action [SetVariable("interakcja_tooltip", ""), Hide("pudlo_zblizenie")]

# --- LABELE LOGICZNE SCENY 3 ---

label znalezienie_mapy:
    $ backpack.add(przedmiot_mapa, 0, 0)
    $ ma_mapa = True
    show screen przycisk_mapy
    
    "Przesuwasz palcem po zakurzonym ekranie terminala. Dane schematu zostają pobrane do twojej pamięci podręcznej."
    ja "Mam to. Teraz przynajmniej wiem, gdzie się znajduję w tym labiryncie."
    r "Fascynujące. Małpa potrafi obsłużyć interfejs cyfrowy."
    r "Skup się. Mapa nie da ci prądu. Zajmij się generatorem."
    call screen Generator_Interakcje

label akcja_znalezienia_karty:
    $ ma_karta_dostepu = True
    $ apteka_otwarta = True # Odblokowuje drzwi do skrzydła szpitalnego w korytarzu
    
    "Wyciągasz z pudełka kawałek twardego plastiku z czerwonym symbolem medycznym."
    ja "Karta dostępu do Sektora Medycznego. To tutaj powinny być bezpieczniki."
    r "Ruszaj się. Każda sekunda w tej ciemności to proszenie się o kłopoty."
    call screen Generator_Interakcje

label interakcja_generator_maszyna:
    if prad_wlaczony:
        "Generator mruczy miarowo, wypełniając halę niskim buczeniem."
    elif ma_bezpiecznik:
        "Wsuwasz ceramiczny bezpiecznik w gniazdo. Pasuje idealnie."
        "Szarpiesz za dźwignię startową. Maszyna kaszle, aż w końcu zaskakuje z rykiem."
        $ prad_wlaczony = True
        "Światło w całej sekcji nagle rozbłyska."
        r "Nareszcie. Dobra robota, [player_name]."
    else:
        ja "Gniazdo głównego bezpiecznika jest puste. Maszyna nie ruszy bez nowej części."
        if not ma_karta_dostepu:
            r "Przeszukaj to pudło pod stołem. Może technicy zostawili tam kartę do szpitala."
        else:
            r "Masz kartę. Idź do Sektora Medycznego po bezpiecznik."
    call screen Generator_Interakcje

label stol_warsztatowy_dialog:
    "Stół jest zawalony starymi narzędziami. Pod blatem dostrzegasz porzucone pudełko."
    ja "Ktoś tu pracował w wielkim pośpiechu..."
    call screen Generator_Interakcje
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#region SZPITAL

label szpital_label:
    if prad_wlaczony:
        scene bg apteka1 with fade
    else:
        scene bg apteka1_no with fade

    "Syk rygli magnetycznych przecina ciszę. Drzwi rozsuwają się z oporem."
    "W nozdrza uderza cię odór ozonu, zaschniętej krwi i silnych środków odkażających."
    
    if not prad_wlaczony:
        "Wąski snop latarki wyłapuje z cienia przewrócone wózki i porozrzucane narzędzia chirurgiczne."
    else:
        "Jarzeniówki na suficie migoczą spazmatycznie, wydając irytujący, wysoki pisk."

    show hero_poczatek at left with dissolve
    ja "Wygląda na to, że ewakuacja zamieniła się w rzeź..."
    
    r "Ewakuacja? Optymistyczne założenie. To, co widzisz, to efekt paniki po aktywacji kwarantanny."
    r "Nikt nie pytał o drogę do wyjścia, kiedy ściany zaczęły spływać krwią."
    
    ja "Gdzie mam szukać tego bezpiecznika? Nie chcę tu zostać ani minuty dłużej."
    
    r "Zaplecze techniczne, za salą operacyjną. I mała rada... nie patrz w stronę kostnicy. Niektóre rzeczy lepiej zostawić w spokoju."
    
    hide hero_poczatek
    hide radio
    call screen Szpital_Eksploracja

screen Szpital_Eksploracja():
    if interakcja_tooltip != "":
        frame:
            background Solid("#00000077")
            padding (10, 5)
            xalign 0.5 yalign 0.1
            text "[interakcja_tooltip]" size 24 color "#fff" outlines [(2,"#000", 0,0)]

    # 1. Szafka medyczna
    imagebutton:
        xpos 0 ypos 0 
        focus_mask True
        if prad_wlaczony:
            idle "images/szpital_szafka_idle_light.png"
            hover "images/szpital_szafka_hover_light.png"
        else:
            idle "images/szpital_szafka_idle_dark.png"
            hover "images/szpital_szafka_hover_dark.png"
        
        action Jump("szpital_szukaj_bezpiecznika")
        hovered SetVariable("interakcja_tooltip", "SZAFKA TECHNICZNA")
        unhovered SetVariable("interakcja_tooltip", "")

    # 2. Powrót do korytarza
    textbutton "POWRÓT NA KORYTARZ":
        align (0.95, 0.95)
        action [SetVariable("interakcja_tooltip", ""), Jump("powrot_do_korytarza")]

label szpital_szukaj_bezpiecznika:
    if not ma_bezpiecznik:
        "Przeszukujesz metalową szafkę. Twoje palce trafiają na małe, plastikowe pudełko."
        "W środku znajduje się nienaruszony, ceramiczny bezpiecznik. Ostatnia szansa na zasilanie."
        $ ma_bezpiecznik = True
        ja "Mam go. Teraz muszę tylko wrócić do generatora i nie dać się zabić po drodze."
    else:
        "Szafka jest pusta. Zabrałeś już wszystko, co mogło być przydatne."
    call screen Szpital_Eksploracja
#endregion SZPITAL