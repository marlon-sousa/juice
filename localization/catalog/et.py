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

    add("str_goto_background_on_close_title", "Sea sulgemise käitumine")
    add("str_goto_background_on_close_warn", \
        "%s võib jätkata tegevust tagaplaanil pärast peaakna \n" \
        "sulgemist.  Või võib %s lõpetada tegevuse.  Kas sa sooviksid et %s jätkaks \n" \
        "tegevust?" % (PRODUCT_NAME,PRODUCT_NAME,PRODUCT_NAME))
    add("str_goto_background_on_close_pref", "Jätka tegevust tagaplaanil kui ma sulgen peaakna")
    add("str_yes", "Jah")
    add("str_no", "Ei")
    add("str_dont_ask", "Ära küsi seda uuesti")
    add("str_ok", "Olgu")
    add("str_hide_window", "Peida aken")
    add("str_show_window", "Näita akent")

    add("str_catchup_pref", "Catchup skips older episodes permanently")
    add("str_set_catchup_title", "Set catchup behavior")
    add("str_set_catchup_description", \
        "When checking in Catchup mode, %s will skip all but the top \n" \
        "item in each feed.  Please specify how %s should treat the \n" \
        "skipped items." % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_skip_permanently", "Skip permanently")
    add("str_skip_temporarily", "Skip this time only")
    
    add("str_set_oneclick_handler", "Set one-click handler")
    add("str_set_oneclick_handler_warn",\
        "%s is not currently your one-click subscription handler for podcasts. \n" \
        "Should we set %s to launch from one-click subscription links?" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_ensure_oneclick_handler", "Always use %s for one-click subscription" % PRODUCT_NAME)
    
    add("str_txt_feedmanager", "Compatible feedmanagers:")
    add("str_feedmanager_btn_podnova", "www.PodNova.com - Search or browse podcasts, single click subscribing")

    add("str_open_downloads_folder", "Ava allalaadimiste kataloog")
    add("str_chkupdate_on_startup", "Check for new versions of the application at startup.")
    add("str_bad_feedmanager_url", "Please enter a valid URL for the feed manager.")
    add("str_feed_manager", "Feed manager")
    add("str_feedmanager_enable", "Synchronize my subscriptions to a remote service")
    add("str_opml_url", "OPML URL")
    add("str_set_track_genre", "Set track genre to")
    add("str_auto_delete", "Kustuta automaatselt episoodid, mis on rohkem kui")
    add("str_days_old", "päeva vanad")
    
    add("str_show_notes", "Näita märkmeid")
    add("str_close", "Sulge")
    
    add("str_critical_error_minspace_exceeded", \
        "Download skipped; free space %dMB less " \
        "than min %dMB.  Please free up space on " \
        "your disk using Cleanup or adjust the storage " \
        "management settings in Preferences")
    add("str_critical_error_unknown", "Unknown critical error while downloading.")
    
    add("str_error_checking_new_version", "We're sorry, but there was an error checking for a new version.  Please try again later.")
    add("str_hours", "hours")
    add("str_minutes", "minutes")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Scanning")
    add("str_scanned", "Scanned")
    add("str_feed", "feed")
    add("str_feeds", "feeds")
    
    add("str_downloading_new_episodes", "Downloading new episodes")
    add("str_sched_specific", "Check at specific times")
    add("str_sched_reg", "Check at regular intervals")
    add("str_repeat_every", "Repeat every")
    add("str_next_run_label", "Järgmine kontroll:")
    
    add("str_license", "This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of  merchantability or fitness for a particular purpose. \n\nSee the GNU General Public License for more details.")

    add("str_donate", "Donate to %s" % PRODUCT_NAME)
    add("str_donate_expl", "It's important to keep community-owned %s applications online and keep this new way of consuming media free as in speech. Any amount of money will make the team happy and encourage them to work on new features and services!" % PRODUCT_NAME)
    add("str_donate_yes", "Yes, take me to the donations page now!")
    add("str_donate_two_weeks", "I still have to check it a bit more, show this again in two weeks")
    add("str_donate_already", "I allready made a donation, don't show this dialog again")
    add("str_donate_no", "No, I don't want to donate, never show this dialog again")
    add("str_donate_one_day", "Not now, notify me again in 1 day")
    add("str_donate_proceed", "Proceed")

    add("str_scheduler_dialog", "Scheduler")
    add("str_scheduler_tab", "Settings")

    add("str_select_import_file", "Select import file")    
    add("str_add_feed_dialog", "Add a Feed")
    add("str_edit_feed", "Feed properties")

    add("str_really_delete", "Kas tahad tõesti kustutada")

    add("str_license_caption", "Litsents")

    add("str_ep_downloaded", "Allalaetud")
    add("str_ep_skipped_removed_other", "Vahele jäätud/eemaldatud/teine allikas")
    add("str_ep_to_download", "Laeb alla")

    add("str_select_none_cleanup", "Ära vali ühtegi")
    add("str_submit_lang", "Esita keel")
    
    add("str_dltab_live", "Otseülekandeid: ")
    add("str_dltab_ul_speed", "Saatmise kiirus: ")
    add("str_dltab_dl_speed", "Allalaadimise kiirus: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Fail")
    add("str_import_opml", "Impordi allikad opml-st...")
    add("str_export_opml", "Ekspordi allikad opml-na...")
    add("str_preferences_menubar", "Eelistused...")
    add("str_close_window", "Sulge aken")
    add("str_quit", "Välju")

    add("str_edit", "Redigeeri")
    add("str_select_all", "Vali kõik")

    add("str_tools", "Tööriistad")
    add("str_check_all", "Kontrolli kõiki allikaid")
    add("str_catch_up", "Tõmba uued")
    add("str_check_selected", "Kontrolli valituid")
    add("str_add_feed", "Lisa allikas...")
    add("str_remove_selected", "Eemalda allikas")
    add("str_feed_properties", "Allika omadused...")
    add("str_scheduler_menubar", "Ajakava...")
    
    add("str_select_language", "Vali keel")

    ## these are also used for the tabs
    add("str_view", "Vaade")
    add("str_downloads", "Allalaadimised")
    add("str_subscriptions", "Tellimused")
    add("str_podcast_directory", "Podcastide nimekiri")
    add("str_cleanup", "Suurpuhastus")

    add("str_help", "Abi")
    add("str_online_help", "Abi internetis")
    add("str_faq", "KKK")
    add("str_check_for_update", "Kontrolli kas on uuendusi...")
    add("str_report_a_problem", "Teata probleemist")
    add("str_goto_website", "Mine kodulehele")
    add("str_make_donation", "Tee annetus")
    add("str_menu_license", "Litsents...")
    add("str_about", "Teave...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Eemalda valitud ühikud")
    add("str_cancel_selected_download", "Tühista valitud allalaadimised")
    add("str_pause_selected", "Peata valitud")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Uus")
    add("str_dl_state_queued", "Järjekorras")
    add("str_dl_state_downloading", "Laeb alla")
    add("str_dl_state_downloaded", "Allalaetud")
    add("str_dl_state_cancelled", "Tühistatud")
    add("str_dl_state_finished", "Lõpetatud")
    add("str_dl_state_partial", "Osaliselt alla laetud")
    add("str_dl_state_clearing", "Puhastab")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Vaata ega uusi podcaste pole saabunud")
    add("str_catch_up_mode", "Tõmba uued - lae alla ainult viimased uued tellimused")

    add("str_add_new_feed", "Lisa uus allikas");
    add("str_remove_selected_feed", "Eemalda valitud allikas")
    add("str_properties", "Omadused")
    add("str_check_selected_feed", "Kontrolli valitud allikat")

    add("str_scheduler_on", "Ajakava - sees")
    add("str_scheduler_off", "Ajakava - väljas")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Järgmine kontroll:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Laen alla episoodi infot...")
    add("str_no_episodes_found", "Ühtegi episoodi ei leitud.")


    ## Directorytab Toolbar
    add("str_refresh", "Värskenda")
    add("str_open_all_folders", "Ava kõik kataloogid")
    add("str_close_all_folders", "Sulge kõik kataloogid")
    add("str_add", "Lisa")

    ## Directorytab Other items
    add("str_directory_description", "Kliki allikal nimistus või kirjuta/kleebi üleval olevasse kasti ning vajuta Lisa .")




    ## Cleanuptab items
    add("str_select_a_feed", "Vali allikas")
    add("str_refresh_cleanup", "Värskenda")
    
    add("str_look_in", "Otsi episoode mis on")        
    add("str_player_library", "mängija hoiuses")
    add("str_downloads_folder", "allalaadimiste kataloogis")
    add("str_delete_library_entries", "Kustuta hoiuse sissekanded")
    add("str_delete_files", "Kustuta failid")
    add("str_select_all_cleanup", "Vali kõik")
    add("str_delete", "Kustuta")




    ## Logtab items
    add("str_log", "Logi")
    add("str_clear", "Tühjenda")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Nimi")
    add("str_lst_date", "Kuupäev")        
    add("str_lst_progress", "Progress")
    add("str_lst_state", "Seisund")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Asukoht")
    add("str_lst_episode", "Episood")
    add("str_lst_playlist", "Allikas")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Tellitud")
    add("str_disabled", "Keelatud")
    add("str_newly-subscribed", "Värskelt tellitud")
    add("str_unsubscribed", "Tellimus tühistatud")
    add("str_preview", "Eelvaade")
    add("str_force", "Sunni")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Choose a name for the export file")
    add("str_subs_exported", "Subscriptions exported.")
    
    ## Preferences Dialog
    add("str_preferences", "Preferences")
    
    add("str_save", "Salvesta")
    add("str_cancel", "Tühista")
    
    # General
    add("str_general", "General")
    add("str_gen_options_expl", "Set the general options for the %s application" % PRODUCT_NAME)
    add("str_hide_on_startup", "At startup only show %s in the system tray" % PRODUCT_NAME)

    add("str_run_check_startup", "Run a check for new podcasts when the application is started")
    add("str_play_after_download", "Play downloads right after they're downloaded")
    add("str_location_and_storage", "Location and storage management")
    add("str_stop_downloading", "Stop downloading if harddisc reaches a minimal of")
    add("str_bad_megabyte_limit_1", "Sorry, the megabyte limit doesn't look like an integer")
    add("str_bad_megabyte_limit_2", "Please try again.")

    add("str_download_folder", "Download podcasts into this folder")
    add("str_browse", "Browse")
    add("str_bad_directory_pref_1", "Sorry, we couldn't find the directory you entered")
    add("str_bad_directory_pref_2", "Please create it and try again.")

    
    # Threading
    add("str_threads", "Threading")
    add("str_multiple_download", "Multiple download settings")
    add("str_max_feedscans", "maximal threads for feedscanning per session")
    add("str_max_downloads", "maximal downloads per session")
   
    # Network settings
    add("str_networking", "Network settings")
    add("str_coralize_urls", "Coralize URLs (experimental)")
    add("str_proxy_server", "Use a proxyserver")
    add("str_proxy_address", "Address")
    add("str_proxy_port", "Port")
    add("str_proxy_username", "Username")
    add("str_proxy_password", "Password")
    add("str_bad_proxy_pref", "You enabled proxy support but didn't provide a proxy host and port.  Please return to the Network settings tab and set the proxy host and port.")

    # Player
    add("str_player", "Player")
    add("str_choose_a_player", "Choose a player")
    add("str_no_player", "No player")
    
    # Advanced
    add("str_advanced", "Advanced")
    add("str_options_power_users", "These options can be used by Power Users")
    add("str_run_command_download", "Run this command after each download")
    add("str_rcmd_full_path", "%f = Full path to downloaded file")
    add("str_rcmd_podcast_name", "%n = Podcast name")
    add("str_other_advanced_options", "Other advanced options")
    add("str_show_log", "Show log tab in application")



    ## Feed Dialog (add/properties)
    add("str_title", "Pealkiri")
    add("str_url", "Aadress")
    add("str_goto_subs", "Mine tellimuste ribale, et näha selle allika episoode")
    add("str_feed_save", "Salvesta")
    add("str_feed_cancel", "Tühista")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Enable scheduler")
    add("str_sched_select_type", "Select radio buttons below to check at specific times or at regular intervals:")
    add("str_check_at_specific_times", "Check at these specific times")
    add("str_check_at_regular_intervals", "Check at regular intervals")
    add("str_repeat_every:", "Repeat every:")
    add("str_latest_run", "Latest run:")
    add("str_next_run", "Järgmine kontroll:")
    add("str_not_yet", "Not yet")
    #--- Cancel
    add("str_save_and_close", "Salvesta ja sulge")
    #--- Save

    add("str_time_error", "One of the scheduled times doesn't look right. Valid times look like this: 10:02am, 16:43.")


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
    add("str_check_for_new_podcast_button", "Check for new podcasts by pressing the button green check button")
    add("str_last_check", "Last check completed at")
    add("str_of", "of")
    add("str_item", "item")
    add("str_items", "items")
    add("str_downloading", "downloading")
    add("str_downloaded", "downloaded")
    add("str_enclosure", "enclosure")
    add("str_enclosures", "enclosures")
    add("str_fetched", "fetched")
    add("str_loading_mediaplayer", "Loading your media player...")
    add("str_loaded_mediaplayer", "Loaded your media player...")        
    add("str_initialized", "%s on töökorras" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast receiver v" + __version__)
    add("str_localization_restart", "Et uut keelt kasutada, sulgeb %s ennast ning sa pead selle uuesti avama. Kliki OK et sulgeda, cancel et jätkata praegust keelt kasutades." % PRODUCT_NAME)
    add("str_really_quit", "A download is in progress.  Really quit?");
    add("str_double_check", "It looks like a download is already in progress.");
    
    # check for update
    add("str_new_version_ipodder", "A new version of %s is available, press Ok to go to the download site." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "This version of %s is up to date" % PRODUCT_NAME)
    add("str_other_copy_running", "Another copy of %s is running. Please raise it, wait for it to complete, or kill it." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Kontrolli allikaid")        
    add("str_open_ipodder", "Ava %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Scanning feeds")

    # Feed right-click menu
    add("str_remove", "Eemalda")        
    add("str_open_in_browser", "Ava brauseris")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Mängi episoodi meediaesitajas")
    add("str_clear_selected", "Eemalda valitud ühikud")
    




