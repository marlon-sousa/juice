#! python
# -*- coding: utf-8 -*-

g_strtable = -1
language_code = __name__.split('.')[-1]

from ipodder.configuration import __version__
from gui.skin import PRODUCT_NAME

def add(label, txt):
    global g_strtable
    g_strtable.AddText(language_code, label, txt)

def AddStrings(strtable):
    global g_strtable
    g_strtable = strtable

    #############################################
    ## MV: 11:25 PM 2/20/2005
    ## READ THIS BEFORE EDITING/ADDING!!
    ## If you add new items, add them in the 'New strings' part.
    ## We can easily send them to the translators that way.
    #############################################

    ##_________________________________________________________
    ##
    ##     New strings
    ##_________________________________________________________

    add("str_txt_feedmanager", "Kompatybilne feed managery :")
    add("str_feedmanager_btn_podnova", "www.PodNova.com - Szukanie podcastów, subskrypcja jednym kliknięciem.")

    add("str_open_downloads_folder", "Otwórz folder Ściągnięte")
    add("str_chkupdate_on_startup", "Prze starcie sprawdzaj czy sa dostępne nowe wersje aplikacji.")
    add("str_bad_feedmanager_url", "Wprowadz poprawny URL dla feed managera.")
    add("str_feed_manager", "Feed manager")
    add("str_feedmanager_enable", "Zsynchronizuj moje subskrypcje ze zdalną usługą")
    add("str_opml_url", "OPML URL")
    add("str_set_track_genre", "Ustaw rodzaj utworu na")
    add("str_auto_delete", "Automatycznie kasuj epizody starsze niż")
    add("str_days_old", "dni")
    
    add("str_show_notes", "Pokaż Notes")
    add("str_close", "Zamknij")
    
    add("str_critical_error_minspace_exceeded", \
        "Ściąganie wstrzymane; Na twardym dysku zostało %dMB wolnego " \
        "miejsca. Minimum określiłeś na %dMB.  Zwolnij miejsce na " \
        "dysku używając opcji Czyszczenie " \
        "lub zmień ustawienia")
    add("str_critical_error_unknown", "Nieznany bład krytyczny przy ściąganiu.")
    
    add("str_error_checking_new_version", "Przepraszamy, ale wystąpił problem ze sprawdzeniem czy sa dostępne nowe wersje. Prosimy spróbować później.")
    add("str_hours", "godzin")
    add("str_minutes", "minut")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Skanowanie")
    add("str_scanned", "Przeskanowane")
    add("str_feed", "feed")
    add("str_feeds", "feed'y")
    
    add("str_downloading_new_episodes", "Sciaganie nowych epizodów")
    add("str_sched_specific", "Sprawdzaj w określonym czasie")
    add("str_sched_reg", "Sprawdzaj w regularnych odstępach")
    add("str_repeat_every", "Powtarzaj co")
    add("str_next_run_label", "Następny raz:")
    
    add("str_license", "Ten program jest darmowy; możesz go redystrybuować i/lub modyfikować na zasadach Licencji GNU General Public jako publikacje Free Software Foundation; na podstawie drugiej wersji Licencji, lub (jeśli wolisz) jakiejkolwiek późniejszej wersji. Ten program jest dystrybuowany z przekonaniem, że będzie pomocny, ale niestety nie możemy udzielać na niego jakiejkolwiek gwarancji. \n\nZobacz Licencje GNU General Public by dowiedzieć się szczegółów.")

    add("str_donate", "Wspomórz %s" % PRODUCT_NAME)
    add("str_donate_expl", "Jest ważnym, by utrzymać program %s przy życiu i tymsamym popierać wolność słowa w Internecie. Jakakolwiek kwota pieniędzy sprawi, że twórcy programu będa szczęśliwi i zdopingowani do pracy nad nowymi funkcjami programu!" % PRODUCT_NAME)
    add("str_donate_yes", "Tak, skieruj mnie do strony gdzie będę mógł finansowo wesprzeć ten projekt!")
    add("str_donate_two_weeks", "Potrzebuje więcej czasu na sprawdzenie programu, pokaż ten komunikat za 2 tygodnie")
    add("str_donate_already", "Już wsparłem finansowo ten projekt, więcej nie pokazuj tego okna")
    add("str_donate_no", "Nie chce wam pomagać, więcej nie pokazuj tego okna")
    add("str_donate_one_day", "Nie teraz, przypomnij mi jutro")
    add("str_donate_proceed", "Dalej")

    add("str_scheduler_dialog", "Planner")
    add("str_scheduler_tab", "Ustawienia")

    add("str_select_import_file", "Wybierz plik do importu")    
    add("str_add_feed_dialog", "Dodaj Feed")
    add("str_edit_feed", "Właściwości Feed")

    add("str_really_delete", "Naprawdę skasuj")

    add("str_license_caption", "Licencja")

    add("str_ep_downloaded", "Ściągnięte")
    add("str_ep_skipped_removed_other", "Pominięty/Skasowany/InnyFeed")
    add("str_dl_state_to_download", "Do ściągnięcia")

    add("str_select_none_cleanup", "Odznacz")
    add("str_submit_lang", "Wyślij plik językowy")
    
    add("str_dltab_live", "Obecne ściągnięcia: ")
    add("str_dltab_ul_speed", "Szybkość wysyłania: ")
    add("str_dltab_dl_speed", "Szybkość ściągania: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Plik")
    add("str_import_opml", "Importuj feed z opml...")
    add("str_export_opml", "Exportuj feed jako opml...")
    add("str_preferences_menubar", "Ustawienia...")
    add("str_close_window", "Zamknij okno")
    add("str_quit", "Wyjdź")

    add("str_edit", "Edytuj")
    add("str_select_all", "Wybierz wszystko")

    add("str_tools", "Narzędzia")
    add("str_check_all", "Zaznacz wszystko")
    add("str_catch_up", "Catch-up")
    add("str_check_selected", "Zaznacz wybrane")
    add("str_add_feed", "Dodaj Feed...")
    add("str_remove_selected", "Usuń Feed")
    add("str_feed_properties", "Właściwości feed...")
    add("str_scheduler_menubar", "Planner...")
    
    add("str_select_language", "Wybierz język")

    ## these are also used for the tabs
    add("str_view", "Zobacz")
    add("str_downloads", "Ściągnięte")
    add("str_subscriptions", "Subskrypcje")
    add("str_podcast_directory", "Katalog podcastów")
    add("str_cleanup", "Czyszczenie")

    add("str_help", "Pomoc")
    add("str_online_help", "Pomoc Online")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Sprawdź uaktualnienie...")
    add("str_report_a_problem", "Zgłoś problem")
    add("str_goto_website", "Idź do strony WWW")
    add("str_make_donation", "Wspomóż projekt")
    add("str_menu_license", "Licencja...")
    add("str_about", "O programie...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Skasuj wybrane")
    add("str_cancel_selected_download", "Anuluj wybrane")
    add("str_pause_selected", "Wstrzymaj wybrane")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Nowy")
    add("str_dl_state_queued", "Oczekuje")
    add("str_dl_state_downloading", "Ściągam")
    add("str_dl_state_downloaded", "Ściągnięte")
    add("str_dl_state_cancelled", "Skasowane")
    add("str_dl_state_finished", "Skończone")
    add("str_dl_state_partial", "Częściowo ściągnięte")
    add("str_dl_state_clearing", "Czyszcze")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Sprawdź czy sa dostępne nowe podcasty")
    add("str_catch_up_mode", "Catch-up - Ściągnij tylko ostatnie nowe epizody")

    add("str_add_new_feed", "Dodaj nowy feed");
    add("str_remove_selected_feed", "Skasuj wybrany feed")
    add("str_properties", "Właściwości")
    add("str_check_selected_feed", "Sprawdź wybrany feed")

    add("str_scheduler_on", "Planner - Właczony")
    add("str_scheduler_off", "Planner - Wyłaczony")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Następny:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Ściągam listę dostępnych plików...")
    add("str_no_episodes_found", "Nic nie znaleziono.")


    ## Directorytab Toolbar
    add("str_refresh", "Odśwież")
    add("str_open_all_folders", "Otwórz wszystkie foldery")
    add("str_close_all_folders", "Zamknij wszystkie foldery")
    add("str_add", "Dodaj")

    ## Directorytab Other items
    add("str_directory_description", "Kliknij na feed na liśie lub wpisz/wklej powyżej i naciśnij przycisk Dodaj.")




    ## Cleanuptab items
    add("str_select_a_feed", "Wybierz feed")
    add("str_refresh_cleanup", "Odśwież")
    
    add("str_look_in", "Szukaj epizodów w")        
    add("str_player_library", "Bibliotece odtwarzacza")
    add("str_downloads_folder", "Folderze Ściągnięte")
    add("str_delete_library_entries", "Wykasuj wpisy w Bibliotece")
    add("str_delete_files", "Skasuj pliki")
    add("str_select_all_cleanup", "Wybierz wszystko")
    add("str_delete", "Skasuj")




    ## Logtab items
    add("str_log", "Log")
    add("str_clear", "Wyczyść")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Nazwa")
    add("str_lst_date", "Data")        
    add("str_lst_progress", "Postęp")
    add("str_lst_state", "Stan")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Ścieżka")
    add("str_lst_episode", "Epizod")
    add("str_lst_playlist", "Playlista")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Subskrybuowane")
    add("str_disabled", "Zablokowane")
    add("str_newly-subscribed", "Nowe subskrybcje")
    add("str_unsubscribed", "Już niesubskrybuowane")
    add("str_preview", "Zajawka")
    add("str_force", "Na siłę")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Wybierz nazwę dla pliku do exportu")
    add("str_subs_exported", "Subskrybcja wyeksportowana.")
    
    ## Preferences Dialog
    add("str_preferences", "Ustawienia")
    
    add("str_save", "Zapisz")
    add("str_cancel", "Anuluj")
    
    # General
    add("str_general", "Ogólne")
    add("str_gen_options_expl", "Ustaw ogólne opcje dla aplikacji %s" % PRODUCT_NAME)
    add("str_hide_on_startup", "Przy starcie pokazuj aplikacje %s w pasku" % PRODUCT_NAME)

    add("str_run_check_startup", "Sprawdź czy nie ma nowych podcastów przy starcie aplikacji")
    add("str_play_after_download", "Odtwarzaj pliki zaraz po ich ściągnięciu")
    add("str_location_and_storage", "Zarządzanie dyskiem")
    add("str_stop_downloading", "Nie ściągaj gdy dostępna powierzchnia twardego dysku osiągnie mniej niż")
    add("str_bad_megabyte_limit_1", "Przepraszam, ale limit megabajtów nie wyglada na liczbę całkowitą")
    add("str_bad_megabyte_limit_2", "Spróbuj ponownie.")

    add("str_download_folder", "Ściągaj podcasty do tego folderu")
    add("str_browse", "Przejrzyj")
    add("str_bad_directory_pref_1", "Przepraszam, nie mogę znaleść folderu który określiłeś")
    add("str_bad_directory_pref_2", "Stwórz folder i spróbuj ponownie.")

    
    # Threading
    add("str_threads", "Wątki")
    add("str_multiple_download", "Ustawienia multi ściągania")
    add("str_max_feedscans", "maksymalna liczba skanowanych wątków na sesje")
    add("str_max_downloads", "maksymalna liczba ściągnięć na sesje")
   
    # Network settings
    add("str_networking", "Ustawiena sieci")
    add("str_coralize_urls", "Koralizuj URL (w fazie testów)")
    add("str_proxy_server", "Użyj serwera proxy")
    add("str_proxy_address", "Adres")
    add("str_proxy_port", "Port")
    add("str_proxy_username", "Nazwa użytkownika")
    add("str_proxy_password", "Hasło")
    add("str_bad_proxy_pref", "Wybrałeś wspomaganie przez serwer proxy, lecz nie podałeś nazwy hosta i numeru portu. Wróć do zakładki Ustawienia sieci, ustaw nazwę hosta proxy oraz jego port.")

    # Player
    add("str_player", "Odtwarzacz")
    add("str_choose_a_player", "Wybierz odtwarzacz")
    add("str_no_player", "Brak odtwarzacza")
    
    # Advanced
    add("str_advanced", "Zaawansowane")
    add("str_options_power_users", "Te opcje mogą być używane tylko przez zaawansowanych użytkowników")
    add("str_run_command_download", "Wykonaj tą komendę po każdym ściągnięciu")
    add("str_rcmd_full_path", "%f = Pełna ścieżka do ściągniętego pliku")
    add("str_rcmd_podcast_name", "%n = Nazwa podcastu")
    add("str_other_advanced_options", "Inne zaawansowane opcje")
    add("str_show_log", "Pokaż zakładkę Log w aplikacji")



    ## Feed Dialog (add/properties)
    add("str_title", "Tytuł")
    add("str_url", "URL")
    add("str_goto_subs", "Idź do zakładki Subskrybcje, by zobaczyć epizody z tego feed'a")
    add("str_feed_save", "Zapisz")
    add("str_feed_cancel", "Anuluj")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Aktywuj planner")
    add("str_sched_select_type", "Zaznacz okienka, by sprawdzać o określonych porach i w regularnych odstępach:")
    add("str_check_at_specific_times", "Sprawdź o tych godzinach")
    add("str_check_at_regular_intervals", "Sprawdź w regularnych odstępach")
    add("str_repeat_every:", "Powtórz co:")
    add("str_latest_run", "Ostatnio:")
    add("str_next_run", "Następne:")
    add("str_not_yet", "Jeszcze nie wykonywano")
    #--- Cancel
    add("str_save_and_close", "Zapisz i zamknij")
    #--- Save

    add("str_time_error", "Jeden z zaplanowanych czasów jest nieprawidłowy. Prawidłowy zapis czasu powinien wygladać tak: 10:02am, 16:43.")


    ## Donations Dialog
    #--- Donate to iPodder
    #--- It's important to keep non-commercial iPodder applications online and keep this new way of consuming media free. Any amount of money will make the team happy and encourage them to work on new features!
    #--- Yes, take me to the donations page now!
    #--- I still have to check it a bit more, show this again in two weeks
    #--- I allready made a donation, don't show this dialog again
    #--- No, I don't want to donate, never show this dialog again
    #--- Not now, notify me again in 1 day
    #--- OK




    ## About Dialog
    #--- Version:
    #--- Programming: Erik de Jonge, Andrew Grumet, Garth Kidd, Perica Zivkovic\nDesign: Martijn Venrooy\nContent strategist: Mark Alexander Posth\nConcept: Adam Curry, Dave Winer\nThanks to all translators for their commitments!\n\nBased on Feedparser and BitTorrent technology.\nThis program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of  merchantability or fitness for a particular purpose. \n\nSee the GNU General Public License for more details.




    ## Statusbar items
    add("str_check_for_new_podcast_button", "Sprawdź czy są dostępne nowe podcasty naciskając zieloną ikonkę z dwiema strzałkami")
    add("str_last_check", "Ostatnio sprawdzano")
    add("str_of", "z")
    add("str_item", "plik")
    add("str_items", "plików")
    add("str_downloading", "ściąganie")
    add("str_downloaded", "ściągnięto")
    add("str_enclosure", "załącznik")
    add("str_enclosures", "załączniki")
    add("str_fetched", "wyodrębnione")
    add("str_loading_mediaplayer", "Uruchamianie twojego odtwarzacza...")
    add("str_loaded_mediaplayer", "Twój odtwarzacz uruchomiony...")        
    add("str_initialized", "%s gotowy" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast receiver v" + __version__)
    add("str_localization_restart", "By dostosować wszystkie opcje w programie %s, wymagany jest restart aplikacji. Naciśnij Ok by zakończyć pracę aplikacji, lub Anuluj by kontynuować." % PRODUCT_NAME)
    add("str_really_quit", "Jestem w trakcie ściągania.  Naprawdę wyjść z programu?");
    add("str_double_check", "Wyglada na to, że ściąganie jest już w trakcie.");
    
    # check for update
    add("str_new_version_ipodder", "Nowa wersja programu %s jest dostępna, naciśnij Ok by przejść do strony producenta." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "Ta wersja aplikacji %s jest najnowsza" % PRODUCT_NAME)
    add("str_other_copy_running", "Inna sesja aplikacji %s jest już uruchomiona. Przywołaj ją, poczekaj aż wykona wszystkie zadania, lub zamknij." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Sprawdź teraz")        
    add("str_open_ipodder", "Otwórz %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Skanowanie feed")

    # Feed right-click menu
    add("str_remove", "Usuń")        
    add("str_open_in_browser", "Otwórz w przegladarce")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Sprawdź ten epizod w Odtwarzaczu")
    add("str_clear_selected", "Wyczyść wybrane pliki")
    



