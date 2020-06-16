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

    add("str_set_track_genre", "Sätt genre till:")
    add("str_auto_delete", "Ta automatiskt bort avsnitt äldre än")
    add("str_days_old", "dagar")
    
    add("str_show_notes", "Visa kommentarer")
    add("str_close", "Stäng")
    
    add("str_critical_error_minspace_exceeded", \
        "Nedladdning avbruten: ledigt utrymme (%dMB) mindre " \
        "än minsta tillåtna (%dMB).")
    add("str_critical_error_unknown", "Allvarligt okänt fel vid nedladdning.")
    
    add("str_error_checking_new_version", "Det uppstod tyvärr ett fel vid sökning efter ny version. Var vänlig försök igen senare.")
    add("str_hours", "timmar")
    add("str_minutes", "minuter")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Uppdaterar ...")
    add("str_scanned", "Uppdaterad")
    add("str_feed", "flöde")
    add("str_feeds", "flöden")
    
    add("str_downloading_new_episodes", "Laddar ned nya avsnitt")
    add("str_sched_specific", "Kontrollera vid specifika tider")
    add("str_sched_reg", "Kontrollera regelbundet")
    add("str_repeat_every", "Upprepa varje")
    add("str_next_run_label", "Nästa:")
    
    add("str_license", "Detta är en fri programvara; du får omdistribuera och/eller modifiera under reglerna från GNU General Public License, publicerad av Free Software Foundation;  antingen version 2, eller någon senare version. Detta program är distribuerat i hopp om att det ska vara användbart, men utan garanti;  \n\nVi hänvisar till GNU General Public License för mer information.")

    add("str_donate", "Donera till %s" % PRODUCT_NAME)
    add("str_donate_expl", "Det är viktigt att hålla gemenskapsägda %s-applikationer online och behålla detta nya sätt att konsumera fri media. Donerade pengar håller vårat team glatt och sporrar oss att jobba på nya funktioner och tjänster." % PRODUCT_NAME)
    add("str_donate_yes", "Ja, ta mig till donationssidan nu!")
    add("str_donate_two_weeks", "Jag är inte riktigt säker än; fråga igen om 2 veckor.")
    add("str_donate_already", "Jag har redan donerat; visa inte den här dialogen igen.")
    add("str_donate_no", "Nej, jag vill inte donera. Visa inte den här dialogen igen.")
    add("str_donate_one_day", "Inte nu; fråga om en dag.")
    add("str_donate_proceed", "Fortsätt")

    add("str_scheduler_dialog", "Schemaläggare")
    add("str_scheduler_tab", "Inställningar")

    add("str_select_import_file", "Välj importeringsfil")    
    add("str_add_feed_dialog", "Lägg till flöde")
    add("str_edit_feed", "Flödesegenskaper")

    add("str_really_delete", "Vill du ta bort")

    add("str_license_caption", "Licens")

    add("str_ep_downloaded", "Nedladdad")
    add("str_ep_skipped_removed_other", "Skippad/Borttagen/AnnatFlöde")
    add("str_dl_state_to_download", "Väntar på nedladdning")

    add("str_select_none_cleanup", "Välj ingen")
    add("str_submit_lang", "Bidra med översättning")
    
    add("str_dltab_live", "Livenedladdningar: ")
    add("str_dltab_ul_speed", "Hastighet uppströms: ")
    add("str_dltab_dl_speed", "Hastighet nedströms: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Akriv")
    add("str_import_opml", "Importera flöden från OPML ...")
    add("str_export_opml", "Exportera flöden till OPML...")
    add("str_preferences_menubar", "Egenskaper ...")
    add("str_close_window", "Stäng fönster")
    add("str_quit", "Avsluta")

    add("str_edit", "Redigera")
    add("str_select_all", "Markera alla")

    add("str_tools", "Verktyg")
    add("str_check_all", "Kontrollera alla")
    add("str_catch_up", "Kom-ikapp")
    add("str_check_selected", "Kontrollera markerade")
    add("str_add_feed", "Lägg till flöde ...")
    add("str_remove_selected", "Ta bort flöde")
    add("str_feed_properties", "Flödesegenskaper ...")
    add("str_scheduler_menubar", "Schemaläggare...")
    
    add("str_select_language", "Välj språk")

    ## these are also used for the tabs
    add("str_view", "Visa")
    add("str_downloads", "Nedladdningar")
    add("str_subscriptions", "Prenumerationer")
    add("str_podcast_directory", "Podradiokatalog")
    add("str_cleanup", "Rensa upp")

    add("str_help", "Hjälp")
    add("str_online_help", "Onlinehjälp")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Sök efter nya versioner ...")
    add("str_report_a_problem", "Rapportera problem")
    add("str_goto_website", "Gå till webbplatsen")
    add("str_make_donation", "Donera")
    add("str_menu_license", "Licens...")
    add("str_about", "Om...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Ta bort markerade")
    add("str_cancel_selected_download", "Avbryt markerad nedladdning")
    add("str_pause_selected", "Pausa markerad")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Ny")
    add("str_dl_state_queued", "Köad")
    add("str_dl_state_downloading", "Laddar ned")
    add("str_dl_state_downloaded", "Nedladdad")
    add("str_dl_state_cancelled", "Avbruten")
    add("str_dl_state_finished", "Färdig")
    add("str_dl_state_partial", "Halvt nedladdad")
    add("str_dl_state_clearing", "Rensar")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Uppdatera flöden")
    add("str_catch_up_mode", "Kom-ikapp - Ladda bara ned de senaste avsnitten")

    add("str_add_new_feed", "Lägg till flöde");
    add("str_remove_selected_feed", "Ta bort markerat flöde")
    add("str_properties", "Egenskaper")
    add("str_check_selected_feed", "Kontrollera markerat flöde")

    add("str_scheduler_on", "Schemaläggare - På")
    add("str_scheduler_off", "Schemaläggare - Av")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Nästa:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Söker info ...")
    add("str_no_episodes_found", "Inga nya avsnitt.")


    ## Directorytab Toolbar
    add("str_refresh", "Uppdatera")
    add("str_open_all_folders", "Öppna alla kataloger")
    add("str_close_all_folders", "Stäng alla kataloger")
    add("str_add", "Lägg till")

    ## Directorytab Other items
    add("str_directory_description", "Klicka på ett flöde i trädet eller ange det ovan och klicka på Lägg till.")




    ## Cleanuptab items
    add("str_select_a_feed", "Markera ett flöde")
    add("str_refresh_cleanup", "Uppdatera")
    
    add("str_look_in", "Kontrollera efter avsnitt i")        
    add("str_player_library", "Spelarkatalog")
    add("str_downloads_folder", "Nedladdatkatalogen")
    add("str_delete_library_entries", "Ta bort katalogfiler")
    add("str_delete_files", "Ta bort filer")
    add("str_select_all_cleanup", "Markera alla")
    add("str_delete", "Ta bort")




    ## Logtab items
    add("str_log", "Logg")
    add("str_clear", "Rensa")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Titel")
    add("str_lst_date", "Datum")        
    add("str_lst_progress", "Förlopp")
    add("str_lst_state", "Status")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Plats")
    add("str_lst_episode", "Avsnitt")
    add("str_lst_playlist", "Radio")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Prenumererad")
    add("str_disabled", "Avstängd")
    add("str_newly-subscribed", "Nyligen prenumererad")
    add("str_unsubscribed", "Oprenumererad")
    add("str_preview", "Förhandsvisa")
    add("str_force", "Tvinga")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Välj ett namn för exportfilen")
    add("str_subs_exported", "Prenumerationer exporterade.")
    
    ## Preferences Dialog
    add("str_preferences", "Egenskaper")
    
    add("str_save", "Spara")
    add("str_cancel", "Avbryt")
    
    # General
    add("str_general", "Allmänt")
    add("str_gen_options_expl", "Ändra allmäna inställningar för %sapplikationer." % PRODUCT_NAME)
    add("str_hide_on_startup", "Visa %s endast i meddelandefältet vid uppstart." % PRODUCT_NAME)

    add("str_run_check_startup", "Kontrollera podradiostationer vid start")
    add("str_play_after_download", "Spela avsnitt direkt efter nedladdning")
    add("str_location_and_storage", "Plats- och sparningsinställningar")
    add("str_stop_downloading", "Avbryt nedladdningar om hårddiskutrymmet underskrider")
    add("str_bad_megabyte_limit_1", "Begränsningen måste vara ett heltal.")
    add("str_bad_megabyte_limit_2", "Var vänlig försök igen.")

    add("str_download_folder", "Spara avsnitt till denna katalog")
    add("str_browse", "Bläddra")
    add("str_bad_directory_pref_1", "Kan inte hitta katalog")
    add("str_bad_directory_pref_2", "Var vänlig att skapa den och försök igen.")

    
    # Threading
    add("str_threads", "Aktiviteter")
    add("str_multiple_download", "Akitivtetsinställnigar")
    add("str_max_feedscans", "flödeskontroller åt gången")
    add("str_max_downloads", "nedladdningar åt gången")
   
    # Network settings
    add("str_networking", "Nätverksinställningar")
    add("str_coralize_urls", "Använd proxytjänst för URL (rekommenderas inte)")
    add("str_proxy_server", "Använd proxyserver")
    add("str_proxy_address", "Adress")
    add("str_proxy_port", "Port")
    add("str_proxy_username", "Användarnamn")
    add("str_proxy_password", "Lösenord")
    add("str_bad_proxy_pref", "Du har valt att använda en proxyserver, men glömde att ange en värd och port.  Var vänlig återgå till Nätverksinställningar och ange en värd och port för proxyservern.")

    # Player
    add("str_player", "Spelare")
    add("str_choose_a_player", "Välj en spelare")
    add("str_no_player", "Ingen spelare")
    
    # Advanced
    add("str_advanced", "Avancerat")
    add("str_options_power_users", "Dessa inställningar bör endast ändras av experter")
    add("str_run_command_download", "Kör detta kommando efter varje nedladdning")
    add("str_rcmd_full_path", "%f = Full sökväg till nedladdad fil")
    add("str_rcmd_podcast_name", "%n = Podradions namn")
    add("str_other_advanced_options", "Övrigt")
    add("str_show_log", "Visa logg-flik")



    ## Feed Dialog (add/properties)
    add("str_title", "Titel")
    add("str_url", "URL")
    add("str_goto_subs", "Gå till prenumerationsfliken för att se denna podradios avsnitt")
    add("str_feed_save", "Spara")
    add("str_feed_cancel", "Avbryt")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Använd schemaläggare")
    add("str_sched_select_type", "Justera för att automatiskt kontrollera vid specifika eller regelbundna tider:")
    add("str_check_at_specific_times", "Kontrollera vid specfika tider")
    add("str_check_at_regular_intervals", "Kontrollera regelbundet")
    add("str_repeat_every:", "Upprepa varje:")
    add("str_latest_run", "Senaste:")
    add("str_next_run", "Nästa:")
    add("str_not_yet", "Inte än")
    #--- Cancel
    add("str_save_and_close", "Spara och stäng")
    #--- Save

    add("str_time_error", "En av de schemalagda tiderna verkar vara felaktigt. Kontrollera tiderna och försök igen.")


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
    add("str_check_for_new_podcast_button", "Kontrollera efter nya avsnitt genom att klicka på den gröna kontrollknappen")
    add("str_last_check", "Senaste kontroll")
    add("str_of", "av")
    add("str_item", "fil")
    add("str_items", "filer")
    add("str_downloading", "laddar ned")
    add("str_downloaded", "nedladdad")
    add("str_enclosure", "bifogning")
    add("str_enclosures", "bifogningar")
    add("str_fetched", "mottagen")
    add("str_loading_mediaplayer", "Laddar mediaspelare ...")
    add("str_loaded_mediaplayer", "Mediaspelare laddad...")        
    add("str_initialized", "%s klar" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podradiomottagare v" + __version__)
    add("str_localization_restart", "För att alla inställningar ska uppdateras krävs en omstart. Klicka Ok för att stänga ned eller avbryt för att fortsätta.")
    add("str_really_quit", "Du har en pågående nedladdning.  Vill du verkligen avsluta?");
    add("str_double_check", "Det verkar som att du har en pågående nedladdning.");
    
    # check for update
    add("str_new_version_ipodder", "En ny version av %s finns tillgänglig - tryck Ok för att gå till sajten." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "Du har den senaste versionen")
    add("str_other_copy_running", "En annan instans av %s körs. Var vänlig avsluta den först." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Kontrollera nu")        
    add("str_open_ipodder", "Öppna %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Kontrollerar flöden")

    # Feed right-click menu
    add("str_remove", "Ta bort")        
    add("str_open_in_browser", "Öppna i webbläsaren")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Spela upp")
    add("str_clear_selected", "Rensa markerade avsnitt")
    



