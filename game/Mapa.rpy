# ==============================================================================
# 1. ZMIENNE (STATUSY LOKACJI)
# ==============================================================================

# Zmienna tooltipa (dymka z nazwą)
default mapa_tooltip = ""

# Statusy lokacji
default pokoj1 = True
default korytarz = True
default stoufka = False
default apteka = False
default generator_light = False
default komputerownia = False
default zbrojownia = False

# ==============================================================================
# 2. MAŁY PRZYCISK W ROGU (HUD)
# ==============================================================================

screen przycisk_mapy():
    zorder 100 
    imagebutton:
        # Upewnij się, że masz te pliki w folderze game/images/
        idle "images/ikona_mapy_idle.png"
        hover "images/ikona_mapy_hover.png"
        focus_mask True
        action Show("mapa_miasta")

# ==============================================================================
# 3. GŁÓWNA MAPA (SCREEN)
# ==============================================================================

screen mapa_miasta():
    modal True
    zorder 200 # Mapa przykrywa wszystko

    add "images/Mapa_.png"

    # PRZYCISK ZAMKNIJ
    textbutton "X Zamknij":
        xalign 0.95 yalign 0.05
        action Hide("mapa_miasta")
        text_size 40 text_color "#ffffff"

    # --- LOKACJA: CELA (POKÓJ 1) ---
    if pokoj1:
        imagebutton:
            auto "images/lokalizacja_początkowa_%s.png"
            focus_mask True
            action [Hide("mapa_miasta"), Jump("pokoj1_label")]
            hovered SetVariable("mapa_tooltip", "CELA")
            unhovered SetVariable("mapa_tooltip", "")
    else:
        add "images/ikonka_cela_no.png"
        #---LOKACJA: KORYTARZ---
    if korytarz:
        imagebutton:
            
            auto "images/ikona_korytarz_%s.png" 
            focus_mask True 
            action [Hide("mapa_miasta"), Jump("korytarzz_label")]
            hovered SetVariable("mapa_tooltip", "KORYTARZ")
            unhovered SetVariable("mapa_tooltip", "")
    else:
        add "images/ikonka_korytarz_no.png"    
    # ---LOKACJA: GENERATOR---
    if generator_light:
        imagebutton:
            auto "images/ikonka_generator_%s.png" 
            focus_mask True
            action [Hide("mapa_miasta"), Jump("generatorr_label")]  
            hovered SetVariable("mapa_tooltip", "GENERATOR")
            unhovered SetVariable("mapa_tooltip", "")
    else:
        add "images/ikonka_generator_no.png"
    # ---LOKACJA: SZPITAL---
    if apteka:
        imagebutton:
            auto "images/ikonka_apteka_%s.png" 
            focus_mask True
            action [Hide("mapa_miasta"), Jump("szpitall_label")]
            hovered SetVariable("mapa_tooltip", "SZPITAL")
            unhovered SetVariable("mapa_tooltip", "")
    else:
        add "images/ikonka_szpital_no.png" 
    
    # ---LOKACJA: STOŁÓWKA---
    if stoufka:
        imagebutton:
            auto "images/ikona_stoufka_%s.png" 
            focus_mask True
            action [Hide("mapa_miasta"), Jump("stoufkaa_label")]
            hovered SetVariable("mapa_tooltip", "STOŁÓWKA")
            unhovered SetVariable("mapa_tooltip", "")
    else:
        add "images/ikonka_stoufka_no.png"
    #---LOKACJA : SERWEROWNIA---
    if komputerownia:
        imagebutton:
            auto "images/ikonka_komputerownia_%s.png" 
            focus_mask True
            action [Hide("mapa_miasta"), Jump("serwerowniaa_label")]
            hovered SetVariable("mapa_tooltip", "SERWEROWNIA")
            unhovered SetVariable("mapa_tooltip", "")
    else:
        add "images/ikonka_komputerownia_no.png" 
    #---LOKACJA: ZBROJOWNIA---
    if zbrojownia:
        imagebutton:
            auto "images/ikonka_zbrojownia_%s.png" 
            focus_mask True
            action [Hide("mapa_miasta"), Jump("zbrojowniaa_label")]
            hovered SetVariable("mapa_tooltip", "ZBROJOWNIA")
            unhovered SetVariable("mapa_tooltip", "")
    else:
        add "images/ikonka_zbrojownia_no.png" 
    if mapa_tooltip != "":
        frame:
            # Jeśli nie masz gui/frame.png, Ren'Py użyje domyślnego tła
            background Frame("gui/frame.png", 10, 10) 
            xalign 0.5 yalign 0.1 padding (20, 10)
            text mapa_tooltip size 30 color "#ffffff" outlines [(2, "#000000", 0, 0)]

# ==============================================================================
# 4. LABELE (SCENARIUSZ)
# ==============================================================================

label pokoj1_label:
    window hide
    # Sprawdzamy stan prądu przy wejściu do celi
    if prad_wlaczony:
        scene bg PokojStartowy with fade # Jasne tło
    else:
        scene bg PokojStartowybezswiatla with fade # Ciemne tło

    show screen plecak_ikona
    show screen przycisk_mapy
    if prad_wlaczony:
        "Stare jarzeniówki buczą i mrugają, zalewając celę zimnym, trupim światłem." 
    call screen Pokój_startowy_zagadka

label korytarzz_label:
    window hide
    if prad_wlaczony:
        scene bg Korytarz with fade
    else:
        scene bg Korytarz_no_light 
    show screen plecak_ikona    
    show screen przycisk_mapy
    "Wyszedłeś na korytarz"
    call screen Pokój_Korytarz_klikanie

label generatorr_label:
    window hide
    if prad_wlaczony:
        scene bg generator_swiatlo with fade
    else:
        scene bg generator_no_swiatlo 
    show screen przycisk_mapy
    show screen plecak_ikona
    "Dotarłeś do pokoju z generatorem."
    call screen Generator_Interakcje

label szpitall_label:
    window hide
    if prad_wlaczony:
        scene apteka with fade
    else:
        scene szpital_no 
    show screen plecak_ikona    
    show screen przycisk_mapy
    "Wyszedłeś Apteki"
    call screen Szpital_Pokoj1_Screen
    
label stoufkaa_label:
    window hide
    if prad_wlaczony:
        scene bg stolowka with fade
    else:
        scene bg stolowka_no 
    show screen plecak_ikona    
    show screen przycisk_mapy
    "Wyszedłeś do Jadalni"
    call screen Jadalnia_Interakcje 

label serwerowniaa_label:
    window hide
    if prad_wlaczony:
        scene bg serwerownia with fade
    else:
        scene bg serwerownia_no 
    show screen plecak_ikona    
    show screen przycisk_mapy
    "Wyszedłeś do Serwerowni"
    call screen Serwerownia_Interakcje

label zbrojowniaa_label:
    window hide
    if prad_wlaczony:
        scene bg zbrojownia with fade
    else:
        scene bg zbrojownia 
    show screen plecak_ikona    
    show screen przycisk_mapy
    "Wyszedłeś Zbrojowni"
    call screen Zbrojownia_Interakcje