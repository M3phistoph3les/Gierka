screen początek_gry():
    # To sprawia, że gra "czeka" na kliknięcie i nie idzie dalej sama
    modal True 

    # 1. RADIO (Rozmowa)
    imagebutton:
        xpos 1200 ypos 400 # Współrzędne (musisz dopasować do swojej grafiki!)
        idle "radio.png" # Obrazek radia (lub przezroczysty, jeśli radio jest na tle)
        hover "radio_hover.png" # Obrazek podświetlony (opcjonalnie)
        focus_mask True # Klikasz tylko w kształt, nie w tło obrazka
        action Jump("interakcja_radio") # Skok do etykiety rozmowy

    # 2. ŁÓŻKO (Szukanie pod łóżkiem)
    imagebutton:
        xpos 100 ypos 600
        # Jeśli łóżko jest namalowane na tle (bg PokojStartowy), używamy "Null()" jako idle, 
        # żeby przycisk był niewidzialny, ale klikalny w danym obszarze.
        # Wymaga zdefiniowania rozmiaru (xsize, ysize).
        idle Solid("#00000000") # Całkowicie przezroczysty prostokąt
        hover Solid("#ffffff20") # Lekko biały prostokąt po najechaniu (dla testu)
        xsize 600 ysize 300 # Wielkość obszaru kliknięcia
        
        action Jump("interakcja_lozko")

    # 3. DRZWI (Wyjście)
    imagebutton:
        xpos 800 ypos 300
        idle Solid("#00000000") 
        hover Solid("#ffffff20") 
        xsize 400 ysize 600
        
        action Jump("interakcja_drzwi")

    # 4. SZAFKA (Latarka)
    imagebutton:
        xpos 1500 ypos 700
        idle Solid("#00000000")
        hover Solid("#ffffff20")
        xsize 200 ysize 200
        
        action Jump("interakcja_szafka")

screen pod_lozkiem():
    modal True
    if ma_lom == False:        
    # 1. ŁOM (pod łóżkiem)
        imagebutton:
            xpos 400 ypos 300 
            idle "przedmiot_lom_lezy.png" 
            hover "przedmiot_lom_lezy_hover.png" 
            focus_mask True
            action [
                Function(backpack.add, przedmiot_lom, 0, 0), 
                SetVariable("ma_lom", True),
                Notify("Zabrałeś łom!")
            ]

    textbutton "Wróć":
        align (0.9, 0.9)
        text_size 50
        action Return()

screen w_szafie():
    modal True

    # 1. Latarka (w szafie)
    imagebutton:
        # Ustaw go tam, gdzie leży na grafice
        xpos 400 ypos 300 
        # Grafika latarki (bez tła, przezroczyste PNG)
        idle "przedmiot_lom_lezy.png" 
        hover "przedmiot_lom_lezy_hover.png" # Opcjonalne podświetlenie
        # Co się dzieje po kliknięciu?
        action [
        # 1. Dodaj do plecaka (Twoja funkcja)
        Function(backpack.add, przedmiot_latarka, 0, 0), 
                
        # 2. Zmień flagę, że już go mamy (żeby zniknął z ekranu)
        SetVariable("ma_latarke", True),
                
        # 3. Wyświetl komunikat
        Notify("Zabrałeś Latarkę!")
        ]
            
        focus_mask True

    

        
    # Ikona plecaka (HUD) - żeby zawsze można było go otworzyć
    use plecak_ikona