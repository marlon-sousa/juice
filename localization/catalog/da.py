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

    ##_________________________________________________________

    add("str_copy_location", "Kopiplacering")
    add("str_set_file_types", "Sæt filtyper")
    add("str_set_file_types_warn", \
        "%s er ikke sat til at håndtere visse filtyper. \n" \
        "Vil du slå dem til nu?" % PRODUCT_NAME)
    add("str_subscription_options", "Et-kliks-abonnementsindstillinger:")
    add("str_enforce_settings", "Gennemtving disse indstillinger ved opstart")
    add("str_file_types", "Filtyper")
    add("str_play_button_enqueues", "Afspil-knappen sætter det valgte spor i kø")
    add("str_authentication", "Autentifikation")
    add("str_dl_state_skipped", "Oversprunget")
    add("str_dl_state_removed", "Fjernet")
    
    add("str_username", "Brugernavn")
    add("str_password", "Adgangskode")
    add("str_missing_proxy_password", "Der er angivet et proxy-brugernavn, men ingen proxy-adgangskode. \n" \
        "Slet enten brugernavnet eller angiv en adgangskode.")

    add("str_goto_background_on_close_title", "Indstil nedlukningsopførsel")
    add("str_goto_background_on_close_warn", \
        "%s kan fortsætte med at køre i baggrunden efter hovedvinduet \n" \
        "er lukket. Eller %s kan afslutte.  Vil du have at %s skal \n" \
        "fortsætte med at køre?" % (PRODUCT_NAME,PRODUCT_NAME,PRODUCT_NAME))
    add("str_goto_background_on_close_pref", "Fortsæt med at køre i baggrunden, når jeg lukker hovedvinduet")
    add("str_yes", "Ja")
    add("str_no", "Nej")
    add("str_dont_ask", "Spørg mig ikke igen")
    add("str_ok", "O.k.")
    add("str_hide_window", "Skjul vindue")
    add("str_show_window", "Vis vindue")

    add("str_catchup_pref", "Indhentning springer ældre episoder over permanent")
    add("str_set_catchup_title", "Indstil indhentningsopførsel")
    add("str_set_catchup_description", \
        "Når der tjekkes i indhentningstilstand, vil %s springe alle andre \n" \
        "punkter end det øverste i hver kanal over. Angiv hvordan %s skal behandle \n" \
        "de oversprungne punkter." % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_skip_permanently", "Spring over permanent")
    add("str_skip_temporarily", "Spring kun over denne gang")
    
    add("str_set_oneclick_handler", "Sæt et-kliks-håndtering")
    add("str_set_oneclick_handler_warn",\
        "%s er ikke p.t. din et-kliks-håndtering for podcasts. \n" \
        "Skal vi indstille %s til at starte ved klik på en abonnements-henvisning?" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_ensure_oneclick_handler", "Benyt altid %s til et-kliks-abonnement" % PRODUCT_NAME)
    
    add("str_txt_feedmanager", "Kompatible kanalhåndteringer:")
    add("str_feedmanager_btn_podnova", "www.PodNova.com - Søg eller gennemse podcasts, et-kliks-abonnementer")

    add("str_open_downloads_folder", "Åbn hentemappe")
    add("str_chkupdate_on_startup", "Tjek for nye versioner af programmet under opstarten")
    add("str_bad_feedmanager_url", "Angiv en gyldig URL til kanalhåndteringen.")
    add("str_feed_manager", "Kanalhåndtering")
    add("str_feedmanager_enable", "Synkronisér mine abonnementer med en fjernservice")
    add("str_opml_url", "OPML URL")
    add("str_set_track_genre", "Sæt episodegenre til")
    add("str_auto_delete", "Slet automatisk episoder, der er mere end")
    add("str_days_old", "dage gamle")
    
    add("str_show_notes", "Vis noter")
    add("str_close", "Luk")

    add("str_critical_error_minspace_exceeded", \
        "Stoppede hentning; Den fri plads er %dMB mindre " \
        "end de minimale %dMB.  Frigør noget plads på din disk " \
        "med Oprydning eller justér lagerindstillingerne")
    add("str_critical_error_unknown", "Ukendt kritisk fejl under hentningen.")
    
    add("str_error_checking_new_version", "Der var desværre et problem med at tjekke for en ny version. Prøv igen senere.")
    add("str_hours", "timer")
    add("str_minutes", "minutter")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Skanner")
    add("str_scanned", "Skannede")
    add("str_feed", "kanal")
    add("str_feeds", "kanaler")
    
    add("str_downloading_new_episodes", "Henter nye episoder")
    add("str_sched_specific", "Tjek på bestemte tidspunkter")
    add("str_sched_reg", "Tjek med jævne mellemrum")
    add("str_repeat_every", "Tjek hver")
    add("str_next_run_label", "Næste kørsel:")
    
    add("str_license", "Dette program er fri software. Du kan redistribuere det og/eller ændre det ifølge betingelserne i GNU General Public License fra Free Software Foundation. Enten version 2 af licensen, eller (efter dit eget valg) enhver senere version. Dette program distribueres i håbet om at det vil være nyttigt, men helt uden garanti, selv ikke en underforstået garanti for brugbarhed til noget som helst formål. \n\nSe detaljerne i GNU General Public License.")

    add("str_donate", "Donér til %s" % PRODUCT_NAME)
    add("str_donate_expl", "Det er vigtigt at beholde almenhedens %s-programmer på nettet og bevare denne friheden for denne nye måde at bruge medier på. Ethvert pengebeløb vil glæde udviklerne og tilskynde dem til at arbejde på nye funktioner og services!" % PRODUCT_NAME)
    add("str_donate_yes", "Ja, send mig til donationssiden nu!")
    add("str_donate_two_weeks", "Jeg skal stadig kigge lidt mere på det. Vis mig dette igen om to uger")
    add("str_donate_already", "Jeg har allerede doneret, vis mig ikke dette vindue igen")
    add("str_donate_no", "Nej, jeg vil ikke donere. Vis mig aldrig dette vindue igen")
    add("str_donate_one_day", "Ikke nu, giv mig en påmindelse om en dag")
    add("str_donate_proceed", "Fortsæt")

    add("str_scheduler_dialog", "Tidsstyring")
    add("str_scheduler_tab", "Indstillinger")

    add("str_select_import_file", "Vælg importfil")    
    add("str_add_feed_dialog", "Tilføj kanal")
    add("str_edit_feed", "Kanalegenskaber")

    add("str_really_delete", "Vil du virkelig slette")

    add("str_license_caption", "Licens")

    add("str_ep_downloaded", "Hentet")
    add("str_ep_skipped_removed_other", "Oversprunget/Fjernet/AndenKanal")
    add("str_dl_state_to_download", "Skal hentes")

    add("str_select_none_cleanup", "Vælg ingen")
    add("str_submit_lang", "Indsend et sprog")
    
    add("str_dltab_live", "Hentes i øjeblikket: ")
    add("str_dltab_ul_speed", "Sendehastighed: ")
    add("str_dltab_dl_speed", "Hentehastighed: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Fil")
    add("str_import_opml", "Importér kanaler fra opml...")
    add("str_export_opml", "Eksportér kanaler som opml...")
    add("str_preferences_menubar", "Indstillinger...")
    add("str_close_window", "Skjul vindue")
    add("str_quit", "Afslut")

    add("str_edit", "Redigér")
    add("str_select_all", "Vælg alle")

    add("str_tools", "Værktøjer")
    add("str_check_all", "Tjek alle")
    add("str_catch_up", "Indhent")
    add("str_check_selected", "Tjek valgte")
    add("str_add_feed", "Tilføj kanal...")
    add("str_remove_selected", "Fjern kanal")
    add("str_feed_properties", "Kanalegenskaber...")
    add("str_scheduler_menubar", "Tidsstyring...")
    
    add("str_select_language", "Vælg sprog")

    ## these are also used for the tabs
    add("str_view", "Vis")
    add("str_downloads", "Hentede filer")
    add("str_subscriptions", "Abonnementer")
    add("str_podcast_directory", "Podcast-fortegnelser")
    add("str_cleanup", "Oprydning")

    add("str_help", "Hjælp")
    add("str_online_help", "Hjælp på nettet")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Tjek for opdatering...")
    add("str_report_a_problem", "Indrapportér et problem")
    add("str_goto_website", "Gå til hjemmesiden")
    add("str_make_donation", "Donér")
    add("str_menu_license", "Licens...")
    add("str_about", "Om...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Fjern valgte punkter")
    add("str_cancel_selected_download", "Afbryd valgte hentning")
    add("str_pause_selected", "Sæt valgte i bero")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Ny")
    add("str_dl_state_queued", "Sat i kø")
    add("str_dl_state_downloading", "Henter")
    add("str_dl_state_downloaded", "Hentet")
    add("str_dl_state_cancelled", "Afbrudt")
    add("str_dl_state_finished", "Afsluttet")
    add("str_dl_state_partial", "Delvist hentet")
    add("str_dl_state_clearing", "Fjerner")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Tjek for nye podcasts")
    add("str_catch_up_mode", "Indhent - Hent kun de nyeste abonnementer")

    add("str_add_new_feed", "Tilføj ny kanal");
    add("str_remove_selected_feed", "Fjern valgte kanal")
    add("str_properties", "Egenskaber")
    add("str_check_selected_feed", "Tjek valgte kanal")

    add("str_scheduler_on", "Tidsstyring - Aktiv")
    add("str_scheduler_off", "Tidsstyring - Inaktiv")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Næste kørsel:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Henter episode-oplysninger...")
    add("str_no_episodes_found", "Fandt ingen episoder.")


    ## Directorytab Toolbar
    add("str_refresh", "Genindlæs")
    add("str_open_all_folders", "Åbn alle mapper")
    add("str_close_all_folders", "Luk alle mapper")
    add("str_add", "Tilføj")

    ## Directorytab Other items
    add("str_directory_description", "Klik på en kanal i træet eller skriv eller indsæt i feltet ovenfor og klik tilføj.")




    ## Cleanuptab items
    add("str_select_a_feed", "Vælg en kanal")
    add("str_refresh_cleanup", "Genindlæs")
    
    add("str_look_in", "Se efter episoder i")        
    add("str_player_library", "Afspillerbibliotek")
    add("str_downloads_folder", "Hentemappe")
    add("str_delete_library_entries", "Slet biblioteksposter")
    add("str_delete_files", "Slet filer")
    add("str_select_all_cleanup", "Vælg alle")
    add("str_delete", "Slet")




    ## Logtab items
    add("str_log", "Log")
    add("str_clear", "Slet")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Navn")
    add("str_lst_date", "Dato")        
    add("str_lst_progress", "Fremgang")
    add("str_lst_state", "Tilstand")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Placering")
    add("str_lst_episode", "Episode")
    add("str_lst_playlist", "Spilleliste")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Abonnerer")
    add("str_disabled", "Deaktiveret")
    add("str_newly-subscribed", "Nyt abonnement")
    add("str_unsubscribed", "Afbrudt abonnement")
    add("str_preview", "Forhåndsvisning")
    add("str_force", "Tving")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Vælg et navn til eksportfilen")
    add("str_subs_exported", "Eksporterede abonnementerne.")
    
    ## Preferences Dialog
    add("str_preferences", "Indstillinger")
    
    add("str_save", "Gem")
    add("str_cancel", "Afbryd")
    
    # General
    add("str_general", "Generelt")
    add("str_gen_options_expl", "Sæt %s-programmets generelle indstillinger" % PRODUCT_NAME)
    add("str_hide_on_startup", "Vis kun %s i systempanelet ved opstart" % PRODUCT_NAME)

    add("str_run_check_startup", "Tjek for nye podcasts, når programmet startes")
    add("str_play_after_download", "Afspil filer, så snart de er hentet")
    add("str_location_and_storage", "Placering og lagerhåndtering")
    add("str_stop_downloading", "Stop hentning, hvis harddisken når under")
    add("str_bad_megabyte_limit_1", "Megabyte-grænsen ligner desværre ikke et heltal")
    add("str_bad_megabyte_limit_2", "Prøv igen.")

    add("str_download_folder", "Hent podcasts til denne mappe")
    add("str_browse", "Gennemse")
    add("str_bad_directory_pref_1", "Vi kunne desværre ikke finde den mappe, du angav")
    add("str_bad_directory_pref_2", "Opret den og prøv igen.")

    
    # Threading
    add("str_threads", "Samtidighed")
    add("str_multiple_download", "Indstillinger for samtidig hentning")
    add("str_max_feedscans", "samtidige kanalskanninger")
    add("str_max_downloads", "filer kan hentes samtidig")
   
    # Network settings
    add("str_networking", "Netværksindstillinger")
    add("str_coralize_urls", "Coralize URL'er (eksperimentelt)")
    add("str_proxy_server", "Brug en proxyserver")
    add("str_proxy_address", "Adresse")
    add("str_proxy_port", "Port")
    add("str_proxy_username", "Brugernavn")
    add("str_proxy_password", "Adgangskode")
    add("str_bad_proxy_pref", "Du har aktiveret proxyunderstøttelse, men har ikke angivet en proxyserver og -port. Gå tilbage til fanebladet netværksindstillinger og angiv proxyserver og -port.")

    # Player
    add("str_player", "Afspiller")
    add("str_choose_a_player", "Vælg en afspiller")
    add("str_no_player", "Ingen afspiller")
    
    # Advanced
    add("str_advanced", "Avanceret")
    add("str_options_power_users", "Disse indstillinger kan bruges af superbrugere")
    add("str_run_command_download", "Udfør denne kommando, hver gang en fil er hentet")
    add("str_rcmd_full_path", "%f = Fuld sti til hentet fil")
    add("str_rcmd_podcast_name", "%n = Podcast-navn")
    add("str_other_advanced_options", "Andre avancerede indstillinger")
    add("str_show_log", "Vis log-faneblad i programmet")



    ## Feed Dialog (add/properties)
    add("str_title", "Titel")
    add("str_url", "URL")
    add("str_goto_subs", "Gå til abonnements-fanebladet for at se denne kanals episoder")
    add("str_feed_save", "Gem")
    add("str_feed_cancel", "Afbryd")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Aktivér tidsstyring")
    add("str_sched_select_type", "Vælg mellem tjek på faste tidspunkter eller med faste mellemrum:")
    add("str_check_at_specific_times", "Tjek på disse faste tidspunkter")
    add("str_check_at_regular_intervals", "Tjek med jævne mellemrum")
    add("str_repeat_every:", "Gentag hver:")
    add("str_latest_run", "Seneste kørsel:")
    add("str_next_run", "Næste kørsel:")
    add("str_not_yet", "Ikke endnu")
    #--- Cancel
    add("str_save_and_close", "Gem og luk")
    #--- Save

    add("str_time_error", "En af de valgte tidspunkter ser forkert ud. Gyldige tidspunkter ser således ud: 16:43, 10:02am.")


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
    add("str_check_for_new_podcast_button", "Tjek for nye podcasts ved at trykke på den grønne tjekknap")
    add("str_last_check", "Sidste tjek blev afsluttet")
    add("str_of", ", u")
    add("str_item", "punkt")
    add("str_items", "punkter")
    add("str_downloading", "henter")
    add("str_downloaded", "hentet")
    add("str_enclosure", "episode")
    add("str_enclosures", "episoder")
    add("str_fetched", "hentet")
    add("str_loading_mediaplayer", "Indlæser din medieafspiller...")
    add("str_loaded_mediaplayer", "Din medieafspiller blev indlæst...")        
    add("str_initialized", "%s klar" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast-modtager v" + __version__)
    add("str_localization_restart", "For at oversætte alle %s knapper, skal %s genstartes. Tryk O.k. for at lukke ned, eller afbryd for at fortsætte." % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_really_quit", "Der hentes stadig. Vil du virkelig afslutte?");
    add("str_double_check", "Det ser ud til at der stadig hentes filer.");
    
    # check for update
    add("str_new_version_ipodder", "Der er kommet en ny version af %s. Tryk O.k. for at gå til den side, hvorfra den kan hentes." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "Denne version af %s behøver ingen opdatering" % PRODUCT_NAME)
    add("str_other_copy_running", "Der kører en anden kopi af %s. Hent den frem, vent til den er afsluttet, eller dræb den." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Tjek nu")        
    add("str_open_ipodder", "Åbn %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Skanner kanaler")

    # Feed right-click menu
    add("str_remove", "Fjern")        
    add("str_open_in_browser", "Åbn i browser")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Afspil episode i medieafspiller")
    add("str_clear_selected", "Fjern valgte episoder")
    







