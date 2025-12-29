# ---------------------- 1. KOD PYTHON (KLASY) ----------------------
init python:
    # Definicja samego przedmiotu (statystyki + wygląd)
    class Item:
        def __init__(self, name, idle_img, hover_img):
            self.name = name
            self.idle_img = idle_img   # Obrazek normalny
            self.hover_img = hover_img # Obrazek po najechaniu myszką

    # Pomocnicza klasa dla przedmiotu leżącego w plecaku (Przedmiot + Pozycja)
    class InventorySlot:
        def __init__(self, item, x, y):
            self.item = item
            self.x = x
            self.y = y

    # Zarządzanie ekwipunkiem
    class Inventory:
        def __init__(self):
            self.slots = [] # Lista przedmiotów wraz z ich pozycjami

        # Metoda dodawania wymaga podania pozycji X i Y
        def add(self, item, x, y):
            new_slot = InventorySlot(item, x, y)
            self.slots.append(new_slot)
            renpy.notify(f"Znaleziono: {item.name}")

        def remove(self, slot):
            if slot in self.slots:
                self.slots.remove(slot)

# ---------------------- 2. EKRAN PLECAKA (SCREEN) ----------------------
screen plecak_screen():
    modal True   # Blokuje klikanie w grę pod spodem
    zorder 100   # Wyświetla się nad wszystkim innym
    
    # Używamy fixed zamiast frame, żeby mieć pełną kontrolę nad pozycjami
    fixed:
        # 1. TŁO (Musi być pierwsze, żeby było na spodzie)
        add "plecak.png":
            align (0.5, 0.5) 
            # xsize 1920 # Odkomentuj, jeśli chcesz wymusić rozmiar
            # ysize 1080

        # 2. PRZEDMIOTY (Rysowane NA tle)
        # UWAGA: Używamy nazwy 'backpack', żeby zgadzała się z Twoim script.rpy!
        for slot in backpack.slots:
            imagebutton:
                idle slot.item.idle_img
                hover slot.item.hover_img
                
                # --- NAPRAWA PROBLEMU Z ZASŁANIANIEM ---
                focus_mask True  ### <--- TO SPRAWIA, ŻE KLIKASZ TYLKO W KSZTAŁT, A NIE W PRZEZROCZYSTOŚĆ
                # ---------------------------------------

                # Pozycja (liczona od lewego górnego rogu ekranu)
                pos (slot.x, slot.y)
                
                action Notify("To jest: " + slot.item.name)
                tooltip slot.item.name

        # 3. PRZYCISK ZAMKNIJ (Na samym wierzchu)
        textbutton "Zamknij":
            align (0.95, 0.05) # Prawy górny róg
            text_size 40       # Większy tekst
            text_color "#ffffff" 
            action Hide("plecak_screen")

    # Obsługa dymków (tooltip) - wyświetla nazwę przedmiotu
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            align (0.5, 0.9) # Wyświetl nazwę na dole ekranu
            size 40
            color "#fff"
            outlines [(2, "#000", 0, 0)]

# ---------------------- 3. EKRAN IKONKI (HUD) ----------------------
screen plecak_ikona():
    zorder 90 # Warstwa poniżej otwartego plecaka
    
    imagebutton:
        # Ustawiamy w prawym górnym rogu z małym odstępem
        align (0.95, 0.05) 
        
        # Grafiki ikony
        idle "ikona_plecaka.png" 
        hover "ikona_plecaka_hover.png" # Jeśli nie masz hovera, usuń tę linię
        
        # focus_mask sprawia, że klikasz tylko w narysowaną torbę, a nie w przezroczyste tło
        focus_mask True 
        
        # Akcja po kliknięciu
        action Show("plecak_screen")

# ---------------------- 4. ZMIENNE GRY (DEFINICJE) ----------------------

# WAŻNE: Nazwa zmiennej to 'backpack', żeby pasowała do kodu w script.rpy ($ backpack.add)
default backpack = Inventory()

# Definiujemy przedmioty
define przedmiot_lom = Item("ŁOM", "lom.png", "lom_hover.png")
define przedmiot_latarka = Item("LATARKA", "latarka.png", "latarka_hover.png")
#-------- PRZEDMIOT Z GENERATORA
define przedmiot_karta = Item("KARTA DOSTĘPU", "karta.png", "karta_hover.png")
#-------- PRZEDMIOT Z APTEKI
define przedmiot_bezpiecznik = Item("BEZPIECZNIK", "bezpiecznik.png", "bezpiecznik_hover.png")
#---------NOWE JADALNIOWE PRZEDMIOTY
define przedmiot_zeton = Item("ŻETON PRACOWNICZY", "zeton.png", "zeton_hover.png")
define przedmiot_karta_serwer = Item("KARTA ADMINISTRATORA", "karta_serwer.png", "karta_serwer_hover.png")
#---------NOWE PRZEDMIOTY ZBROJOWNIA
define przedmiot_strzelba = Item("PISTOLET BOJOWY", "pistolet.png", "pistolet_hover.png")
define przedmiot_karabin = Item("KARABIN SZTURMOWY", "karabin.png", "karabin_hover.png")