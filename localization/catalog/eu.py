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

    add("str_goto_background_on_close_title", "Ezarri ateratzeko jarrera")
    add("str_goto_background_on_close_warn", \
        "%s atzeko planoan lan egiten jarraitu dezake, nahiz eta leiho nagusia itxi . \n" \
        " Edo %sretik atera zaitezke.  %s martxan jarraitzea  \n" \
        "nahi duzu?" % (PRODUCT_NAME,PRODUCT_NAME,PRODUCT_NAME))
    add("str_goto_background_on_close_pref", "Atzeko planoan lan egiten mantendu leiho nagusia itxi arren")
    add("str_yes", "Bai")
    add("str_no", "Ez")
    add("str_dont_ask", "Ez galdetu berriro")
    add("str_ok", "Ados")
    add("str_hide_window", "Leihoa itxi")
    add("str_show_window", "Leihoa erakutsi")

    add("str_catchup_pref", "Catchup funtzioak ez ditu programa zaharrak kontutan hartuko")
    add("str_set_catchup_title", "Catchup funtzioaren jarrera ezarri")
    add("str_set_catchup_description", \
        "Bilaketa Catchup funtzioaren bitartez egiten denean, kontutan hartuko diren programa bakarrak \n" \
        "jario bakoitzan goian dauenak dira.  Mesedez, zehaztu ezazu %srek nola kudeatu behar dituen\n" \
        "kontutan hartu ez diren elementuak." % PRODUCT_NAME)
    add("str_skip_permanently", "Ez hartu kontutan betirako")
    add("str_skip_temporarily", "Ez hartu kontutan orain")
    
    add("str_set_oneclick_handler", "Ezarri klik-bakarreko maneiatzailea")
    add("str_set_oneclick_handler_warn",\
        "%s ez da klik-bakarreko podcast harpidetze maneiatzailea. \n" \
        "Klik-bakarreko harpidetza loturak kudeatzeko %s erabili nahi duzu??" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_ensure_oneclick_handler", "Always use %s for one-click subscription" % PRODUCT_NAME)
    
    add("str_txt_feedmanager", "Jario irakurgailu bateragarriak:")
    add("str_feedmanager_btn_podnova", "www.PodNova.com - Bilatu edo ikusi podcastak, klik-bakarreko harpidetzarekin")

    add("str_open_downloads_folder", "Ireki jaitsieren katalogoa")
    add("str_chkupdate_on_startup", "Begiratu aplikazioaren bertsio berriak hasieratzean.")
    add("str_bad_feedmanager_url", "Mesedez, jario irakurgailuarentzat URL baliogarri bat sartu.")
    add("str_feed_manager", "Jario irakurtzailea")
    add("str_feedmanager_enable", "Sinkronizatu harpidetzak urruneko zerbitzu batekin")
    add("str_opml_url", "OPML URL")
    add("str_set_track_genre", "Ezarri abesti/programaren mota")
    add("str_auto_delete", "Ezabatu automatikoki baldintza hau betetzen duten programak")
    add("str_days_old", "egun zahar")
    
    add("str_show_notes", "Oharrak erakutsi")
    add("str_close", "Itxi")

    add("str_critical_error_minspace_exceeded", \
        "Jaitsiera etenda; %dMB libre dituzu " \
        "%dMBeko minimoa baino gutxiago.  Mesedez ustu " \
        "zure diska edo aldatu biltegiratze ezaugarriak " \
        "Lehentasun ataleko kudeatze ezaugarrietan")
    add("str_critical_error_unknown", "Ezezaguna den errore kritikoa fitxategia jaistean.")
    
    add("str_error_checking_new_version", "Barkatu, baina errore bat gertatu da bertsio berria bilatzen.  Mesedez saiatu beranduago.")
    add("str_hours", "orduak")
    add("str_minutes", "minutuak")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Eskaneatzen")
    add("str_scanned", "Eskaneatuta")
    add("str_feed", "Jarioa")
    add("str_feeds", "jarioak")
    
    add("str_downloading_new_episodes", "Programa berriak jaisten")
    add("str_sched_specific", "Begiratu denbora konkretu batean")
    add("str_sched_reg", "Begirtatu denbora tarte konkretuetan")
    add("str_repeat_every", "Errepikatze maiztasuna:")
    add("str_next_run_label", "Hurrengo martxan jartzea:")
    
    add("str_license", "This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of  merchantability or fitness for a particular purpose. \n\nSee the GNU General Public License for more details.")

    add("str_donate", "%s-i dohaintza bat egin" % PRODUCT_NAME)
    add("str_donate_expl", "It's important to keep community-owned %s applications online and keep this new way of consuming media free as in speech. Any amount of money will make the team happy and encourage them to work on new features and services!" % PRODUCT_NAME)
    add("str_donate_yes", "Bai, eraman nazazu dohaintza egiteko orrira orain")
    add("str_donate_two_weeks", "Pixkat gehiago begiratu behar dut, erakutsi berriro bi astetan")
    add("str_donate_already", "Jadanik dohaintza bat egin dut, ez erakutsi hau berriro")
    add("str_donate_no", "Ez, ez dut dohaintza bat egin nahi, ez erakutsi hau berriro")
    add("str_donate_one_day", "Ez orain, erakutsi hau berriro egun batean")
    add("str_donate_proceed", "Jarraitu")

    add("str_scheduler_dialog", "Planifikatzailea")
    add("str_scheduler_tab", "Konfigurazioa")

    add("str_select_import_file", "Aukeratu inportatzeko fitxategia")    
    add("str_add_feed_dialog", "Jario bat gehitu")
    add("str_edit_feed", "Jarioaren ezaugarriak")

    add("str_really_delete", "Benetan ezabatu")

    add("str_license_caption", "Lizentzia")

    add("str_ep_downloaded", "Jaitsia")
    add("str_ep_skipped_removed_other", "Pasatakoa/Ezabatua/BesteIturriBatetik")
    add("str_dl_state_to_download", "Jaisteko")

    add("str_select_none_cleanup", "Ezer ez aukeratu")
    add("str_submit_lang", "Hizkuntza bat bidali")
    
    add("str_dltab_live", "Orain jaisten: ")
    add("str_dltab_ul_speed", "Igotze abiadura: ")
    add("str_dltab_dl_speed", "Jaiste abiadura: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Fitxategia")
    add("str_import_opml", "Opml fitxategi batetik jaitsi jarioak...")
    add("str_export_opml", "Jarioak opml fitxategi batean esportatu..")
    add("str_preferences_menubar", "Ezaugarriak...")
    add("str_close_window", "Lehioa ezkutatu")
    add("str_quit", "Atera")

    add("str_edit", "Editatu")
    add("str_select_all", "Denak hautatu")

    add("str_tools", "Tresnak")
    add("str_check_all", "Denak markatu")
    add("str_catch_up", "Catch-up")
    add("str_check_selected", "Markatu aukeratuak")
    add("str_add_feed", "Jario bat gehitu...")
    add("str_remove_selected", "Jario bat ezabatu...")
    add("str_feed_properties", "Jarioaren ezaugarriak...")
    add("str_scheduler_menubar", "Planifikatzailea...")
    
    add("str_select_language", "Hizkuntza aukeratu")

    ## these are also used for the tabs
    add("str_view", "Ikusi")
    add("str_downloads", "Jaitsierak")
    add("str_subscriptions", "Harpidetzak")
    add("str_podcast_directory", "Podcast katalogoa")
    add("str_cleanup", "Garbitu")

    add("str_help", "Laguntza")
    add("str_online_help", "Online Laguntza")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Begiratu berrikuntzarik dagoen...")
    add("str_report_a_problem", "Arazo bat igorri")
    add("str_goto_website", "Webgunera joan")
    add("str_make_donation", "Dohaintza bat egin")
    add("str_menu_license", "Lizentzia...")
    add("str_about", "Honi buruz...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Ezabatutako hautatutako elementuak")
    add("str_cancel_selected_download", "Hautatutako jaitsiera eten")
    add("str_pause_selected", "Gelditu hautatutakoa")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Berria")
    add("str_dl_state_queued", "Ilaran")
    add("str_dl_state_downloading", "Jaisten")
    add("str_dl_state_downloaded", "Jaitsita")
    add("str_dl_state_cancelled", "Ezeztatua")
    add("str_dl_state_finished", "Amaitua")
    add("str_dl_state_partial", "Erdizka jaitsia")
    add("str_dl_state_clearing", "Garbitzen")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Podcast berriak aurkitu")
    add("str_catch_up_mode", "Catch-up - Only download the last new subscriptions")

    add("str_add_new_feed", "Jario berria gehitu");
    add("str_remove_selected_feed", "Hautatutako jarioa ezabatu")
    add("str_properties", "Ezaugarriak")
    add("str_check_selected_feed", "Markatu hautatutako jarioak")

    add("str_scheduler_on", "Planifikatzailea - Gaitua")
    add("str_scheduler_off", "Planifikatzailea - Ezgaitua")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Hurrengo martxan jartzea:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Programari buruzko informazioa jaisten...")
    add("str_no_episodes_found", "Ez dira programak aurkitu.")


    ## Directorytab Toolbar
    add("str_refresh", "Berritu")
    add("str_open_all_folders", "Katalogo guztiak ireki")
    add("str_close_all_folders", "Katalogo guztiak hautatu")
    add("str_add", "Gehitu")

    ## Directorytab Other items
    add("str_directory_description", "Zuhaitzeko jario batean klik egin edo ondoan dagoen zuriunean idatzi/itsatsi jarioaren helbidea eta ondoren Gehitu klikatu.")




    ## Cleanuptab items
    add("str_select_a_feed", "Jario bat aukeratu")
    add("str_refresh_cleanup", "Berritu")
    
    add("str_look_in", "Programak bilatu hemen,")        
    add("str_player_library", "Erreproduzigailuaren liburutegia")
    add("str_downloads_folder", "Jaitsitakoen katalogoa")
    add("str_delete_library_entries", "Ezabatu liburutegiko sarrerak")
    add("str_delete_files", "Ezabatu fitxategiak")
    add("str_select_all_cleanup", "Denak hautatu")
    add("str_delete", "Ezabatu")




    ## Logtab items
    add("str_log", "Loga")
    add("str_clear", "Garbitu")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Izena")
    add("str_lst_date", "Data")        
    add("str_lst_progress", "Progresua")
    add("str_lst_state", "Egoera")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Kokalekua")
    add("str_lst_episode", "Programa")
    add("str_lst_playlist", "Lista")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Harpidetua")
    add("str_disabled", "Ezgaitua")
    add("str_newly-subscribed", "Berriki harpidetua")
    add("str_unsubscribed", "Harpidetza ezeztatua")
    add("str_preview", "Aurrikusi")
    add("str_force", "Behartu")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Esportatzeko fitxategiarentzat izen bat aukeratu")
    add("str_subs_exported", "Harpidetzak esportatuak.")
    
    ## Preferences Dialog
    add("str_preferences", "Ezaugarriak")
    
    add("str_save", "Gorde")
    add("str_cancel", "Ezeztatu")
    
    # General
    add("str_general", "Orokor")
    add("str_gen_options_expl", "%s aplikazioarentzat aukera orokorrak" % PRODUCT_NAME)
    add("str_hide_on_startup", "Hasieran %s system tray-ean bakarrik erakutsi" % PRODUCT_NAME)

    add("str_run_check_startup", "Begiratu ea podcast berriak dauden programa hasieratzean")
    add("str_play_after_download", "Entzun jaitsitako programak jaitsi eta berehala")
    add("str_location_and_storage", "Kokaleku eta biltegiratze kudeaketa")
    add("str_stop_downloading", "Gelditu jaisten disko gogorra minimo honetara iristen bada: ")
    add("str_bad_megabyte_limit_1", "Barkatu, megabyte muga ez dirudi osoko balio bat")
    add("str_bad_megabyte_limit_2", "Mesedez saiatu berriro.")

    add("str_download_folder", "Jaitsi podcast hau katalogo honetan")
    add("str_browse", "Arakatu")
    add("str_bad_directory_pref_1", "Barkatu, ezin izan dugu sartutako katalogoa aurkitu")
    add("str_bad_directory_pref_2", "Mesedez sortu ezazu eta saiatu berriro.")

    
    # Threading
    add("str_threads", "Threading")
    add("str_multiple_download", "Hainbat jaitsierentzat ezaugarriak")
    add("str_max_feedscans", "maximal threads for feedscanning per session")
    add("str_max_downloads", "Jaitsiera muga sesio bakoitzeko")
   
    # Network settings
    add("str_networking", "Sare konfigurazioa")
    add("str_coralize_urls", "URLak Coralizatu (experimentala)")
    add("str_proxy_server", "Proxy zerbitzari bat erabili")
    add("str_proxy_address", "Helbidea")
    add("str_proxy_port", "Portua")
    add("str_proxy_username", "Erabiltzailea")
    add("str_proxy_password", "Pasahitza")
    add("str_bad_proxy_pref", "Proxy zerbitzaria erabiltzeko eskatu duzu baina ez dituzu proxyaren helbidea eta portua zehaztu. Mesedez Sare konfigurazio fitxara eta proxyaren helbidea eta portua zehaztu")

    # Player
    add("str_player", "Erreproduzigailua")
    add("str_choose_a_player", "Erreproduzigailu bat aukeratu")
    add("str_no_player", "Erreproduzigailurik ez")
    
    # Advanced
    add("str_advanced", "Aurreratua")
    add("str_options_power_users", "Aukera hauek Erabiltzaile Jakintsuek (Power Users) erabiltzeko dira")
    add("str_run_command_download", "Exekutatu komando hau jaitsi eta gero")
    add("str_rcmd_full_path", "%f = Jaitsitako fitxategiaren helbide osoa")
    add("str_rcmd_podcast_name", "%n = Podcastaren izena")
    add("str_other_advanced_options", "Beste aukera aurreratu batzuk")
    add("str_show_log", "Erakutsi log fitxa aplikazioan")



    ## Feed Dialog (add/properties)
    add("str_title", "Izenburua")
    add("str_url", "URL")
    add("str_goto_subs", "Joan harpidetza fitxara podcast honi buruzko programa ezberdinak ikusteko")
    add("str_feed_save", "Gorde")
    add("str_feed_cancel", "Ezeztatu")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Planifikatzailea gaitu")
    add("str_sched_select_type", "Markatu ondoko radio botoi hauek momentu konkretu batean edo denbora tarte konkretu batzuetan podcasta ikuskatzeko:")
    add("str_check_at_specific_times", "Momentu konkretu batean ikuskatu")
    add("str_check_at_regular_intervals", "Denbora tarte konkretu batzuetan ikuskatu")
    add("str_repeat_every:", "Errepikatze maiztasuna:")
    add("str_latest_run", "Azken martxan jartzea:")
    add("str_next_run", "Hurrengo martxan jartzea:")
    add("str_not_yet", "Ez oraindik")
    #--- Cancel
    add("str_save_and_close", "Gorde eta itxi")
    #--- Save

    add("str_time_error", "Hauetako planifikazio denbora batek ez dirudi ondo dagoela. Horrela izan beharko luke: 10:02am, 16:43.")


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
    add("str_check_for_new_podcast_button", "Ikuskatu podcast berriak dauden botoi berria sakatuz")
    add("str_last_check", "Azkeneko ikuskaketa:")
    add("str_of", "nongoa:")
    add("str_item", "elementu")
    add("str_items", "elementuak")
    add("str_downloading", "jaisten")
    add("str_downloaded", "jaitsita")
    add("str_enclosure", "enclosure")
    add("str_enclosures", "enclosures")
    add("str_fetched", "fetched")
    add("str_loading_mediaplayer", "Zure musika errepoduzigailua abiarazten...")
    add("str_loaded_mediaplayer", "Zure musika errepoduzigailua abiarazita...")        
    add("str_initialized", "%s prest" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast irakurgailua v" + __version__)
    add("str_localization_restart", "%sren kontrol guztiak lokalizatzeko berabiatzea beharrezkoa da. OK sakatu ondo ixteko, edo ezeztatu jarraitzeko." % PRODUCT_NAME)
    add("str_really_quit", "Jaitsiera bidean, benetan atera nahi duzu?");
    add("str_double_check", "Badirudi jadanik programa hau jaisten ari zarela");
    
    # check for update
    add("str_new_version_ipodder", "%s bertsio berri bat dagoela dirudi, jaisteko gunera joan OK zapalduz" % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "%s bertsio hau eguneraturik dago" % PRODUCT_NAME)
    add("str_other_copy_running", "%s beste bertsio bat martxan dago. Esnatu ezazu, itxaron amaitzea, edo hil ezazu." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Egiaztatu orain")        
    add("str_open_ipodder", "%s ireki" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Jarioak eskaneatzen")

    # Feed right-click menu
    add("str_remove", "Ezabatu")        
    add("str_open_in_browser", "Ireki nabigatzailean")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Programak ireki musika erreproduzigailuan")
    add("str_clear_selected", "Garbitu aukeratutakoak")
    




