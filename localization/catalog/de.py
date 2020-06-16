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
    ## We can easily throw them to the translators that way.
    #############################################


    ##_________________________________________________________
    ##
    ##     New strings
    ##_________________________________________________________



    add("str_error_checking_new_version", "Es tut uns leid, aber es gab ein Problem beim Überprüfen auf eine neue Version. Bitte versuchen Sie es später noch einmal.")
    add("str_hours", "Stunden")
    add("str_minutes", "Minuten")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Durchsuchen")
    add("str_scanned", "Durchsucht")
    add("str_feed", "Feed")
    add("str_feeds", "Feeds")
    
    add("str_downloading_new_episodes", "Download neuer Episoden")
    add("str_sched_specific", "Zu bestimmten Zeiten checken")
    add("str_sched_reg", "In regelmäßigen Intervallen checken")
    add("str_repeat_every", "Wiederholen alle")
    add("str_next_run_label", "Nächster Lauf:")
    
    add("str_license", "This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of  merchantability or fitness for a particular purpose. \n\nSee the GNU General Public License for more details.")

    add("str_donate", "Für %s spenden" % PRODUCT_NAME)
    add("str_donate_expl", "Es ist wichtig, diese der Allgemeinheit gehörenden, auf %s basierenden Programme frei für alle zur Verfügung stellen zu können, denn jeder soll die Möglichkeit haben, auf diese neue Art Audio, Video und mehr nutzen zu können. Jeder Betrag macht das Team glücklich und motiviert die Teilnehmer, für Sie an neuen Features und Diensten zu arbeiten!" % PRODUCT_NAME)
    add("str_donate_yes", "Ja, ich möchte jetzt die Spenden-Seite besuchen!")
    add("str_donate_two_weeks", "Ich möchte die Software noch weiter testen, bitte erinnere mich in 2 Wochen wieder")
    add("str_donate_already", "Ich habe bereits gespendet, zeige diesen Dialog nicht wieder an.")
    add("str_donate_no", "No, Ich will nicht spenden, zeige diesen Dialog nicht wieder an.")
    add("str_donate_one_day", "Nicht jetzt, aber erinnere mich in einem Tag")
    add("str_donate_proceed", "Fortfahren")

    add("str_scheduler_dialog", "Terminplaner")
    add("str_scheduler_tab", "Einstellungen")

    add("str_select_import_file", "Import-Datei auswählen")    
    add("str_add_feed_dialog", "Feed hinzufügen")
    add("str_edit_feed", "Feed-Eigenschaften")

    add("str_really_delete", "Wirklich löschen")

    add("str_menu_license", "Lizenz...")
    add("str_license_caption", "Lizenz")

    add("str_ep_downloaded", "Heruntergeladen")
    add("str_ep_skipped_removed_other", "Übersprungen/Entfernt/AndererFeed")
    add("str_dl_state_to_download", "Noch herunterzuladen")

    add("str_select_none_cleanup", "Nichts auswählen")
    add("str_submit_lang", "Eine weitere Sprache hinzufügen")
    
    add("str_dltab_live", "Aktive Downloads: ")
    add("str_dltab_ul_speed", "Upload-Geschwindigkeit: ")
    add("str_dltab_dl_speed", "Download-Geschwindigkeit: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________



    ## File menu
    add("str_file", "Datei")
    add("str_import_opml", "Feeds aus OPML importieren")
    add("str_export_opml", "Feeds als OPML exportieren")
    add("str_preferences_menubar", "Einstellungen...")
    add("str_close_window", "Fenster schließen")
    add("str_quit", "Beenden")

    add("str_edit", "Bearbeiten")
    add("str_select_all", "Alles auswählen")

    add("str_tools", "Werkzeuge")
    add("str_check_all", "Alle Feeds überprüfen")
    add("str_catch_up", "Nur letzten Eintrag laden (Catch-Up)")
    add("str_check_selected", "Ausgewählte Feeds überprüfen")
    add("str_add_feed", "Hinzufügen Feed ...")
    add("str_remove_selected", "Feed entfernen")
    add("str_feed_properties", "Feed-Eigenschaften")
    add("str_scheduler_menubar", "Terminplaner...")

    add("str_select_language", "Sprache auswählen")

    ## these are also used for the tabs
    add("str_view", "Fenster")
    add("str_downloads", "Downloads")
    add("str_subscriptions", "Abonnierte Feeds")
    add("str_podcast_directory", "Podcast-Verzeichnis")
    add("str_cleanup", "Aufräumen")

    add("str_help", "Hilfe")
    add("str_online_help", "Online-Hilfe")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Auf Aktualisierung prüfen")
    add("str_report_a_problem", "Problem melden")
    add("str_goto_website", "Gehe zur Webseite")
    add("str_make_donation", "%s unterstützen" % PRODUCT_NAME)
    add("str_about", "Info/Über")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Selektierte Einträge entfernen")
    add("str_cancel_selected_download", "Selektierte Downloads abbrechen")
    add("str_pause_selected", "Selektierte Downloads anhalten")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Neu")
    add("str_dl_state_queued", "Queue")
    add("str_dl_state_downloading", "Lädt")
    add("str_dl_state_downloaded", "Heruntergeladen")
    add("str_dl_state_cancelled", "Abgebrochen")
    add("str_dl_state_finished", "Fertig")
    add("str_dl_state_partial", "Teilweise heruntergeladen")
    add("str_dl_state_clearing", "Säubern")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Auf neue Podcasts prüfen")
    add("str_catch_up_mode", "Catch-up - nur den jeweils neuesten Eintrag herunterladen")

    add("str_add_new_feed", "Feed hinzufügen")
    add("str_remove_selected_feed", "Feed entfernen")
    add("str_properties", "Feed-Eigenschaften")
    add("str_check_selected_feed", "Feed überprüfen")

    add("str_scheduler_on", "Terminplaner - An")
    add("str_scheduler_off", "Terminplaner - Aus")

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Nächster Lauf:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Lädt Episoden-Information")
    add("str_no_episodes_found", "Keine Episoden gefunden.")


    ## Directorytab Toolbar
    add("str_refresh", "Aktualisieren")
    add("str_open_all_folders", "Alle Ordner öffnen")
    add("str_close_all_folders", "Schließen aller Ordner")
    add("str_add", "Hinzufügen")

    ## Directorytab Other items
    add("str_directory_description", "Klicken Sie auf einen Feed in dem Baum, oder geben Sie ihn ein in das obige Feld. Wählen Sie dann hinzufügen.")




    ## Cleanuptab items
    add("str_select_a_feed", "Einen Feed auswählen")
    add("str_refresh_cleanup", "Aktualisieren")

    add("str_look_in", "Nach Episoden schauen in ")
    add("str_player_library", "Medienbibliothek des Players")
    add("str_downloads_folder", "Ordner für Downloads")
    add("str_delete_library_entries", "Lösche Medienbibliothek-Einträge")
    add("str_delete_files", "Lösche Dateien")
    add("str_select_all_cleanup", "Alles auswählen")
    add("str_delete", "Löschen")




    ## Logtab items
    add("str_log", "Log")
    add("str_clear", "Log löschen")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Name")
    add("str_lst_date", "Datum")
    add("str_lst_progress", "Fortschritt")
    add("str_lst_state", "Status")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Pfad")
    add("str_lst_episode", "Episode")
    add("str_lst_playlist", "Playlist")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Abonniert")
    add("str_disabled", "inaktiv")
    add("str_newly-subscribed", "Neu abonniert")
    add("str_unsubscribed", "Abbestellt")
    add("str_preview", "Vorschau")
    add("str_force", "Erzwingen")


    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________


    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Namen für Export-Datei auswählen")
    add("str_subs_exported", "Feed-Liste exportiert.")

    ## Preferences Dialog
    add("str_preferences", "Einstellungen")
    add("str_save", "Speichern")
    add("str_cancel", "Abbrechen")

    # General
    add("str_general", "Allgemein")
    add("str_gen_options_expl", "Generelle Einstellungen für %s" % PRODUCT_NAME)
    add("str_hide_on_startup", "Nach dem Start in Systemtray minimieren")

    add("str_run_check_startup", "Beim Start auf neue Episoden überprüfen")
    add("str_play_after_download", "Spiele Downloads ab, sobald sie fertig geladen sind")
    add("str_location_and_storage", "Ablagepfad-Verwaltung")
    add("str_stop_downloading", "Herunterladen abbrechen, wenn freier Platz auf der Festplatte folgenden Wert unterschreitet")
    add("str_bad_megabyte_limit_1", "Leider keine gültige ganze Zahl")
    add("str_bad_megabyte_limit_2", "Bitte noch einmal versuchen.")

    add("str_download_folder", "Podcasts in diesem Ordner speichern")
    add("str_browse", "Durchsuchen")
    add("str_bad_directory_pref_1", "Leider konnten das angegebene Verzeichnis nicht gefunden werden.")
    add("str_bad_directory_pref_2", "Bitte anlegen und es danach noch einmal versuchen.")


    # Threading
    add("str_threads", "Threading")
    add("str_multiple_download", "Einstellungen für gleichzeitige Downloads")
    add("str_max_feedscans", "maximale Anzahl gleichzeitiger Zugriffe für Feed lesen")
    add("str_max_downloads", "maximale Anzahl gleichzeitiger Downloads pro Session")

    # Network settings
    add("str_networking", "Netzwerk-Einstellungen")
    add("str_coralize_urls", "Coralize URLs (experimental)")
    add("str_proxy_server", "Proxyserver verwenden")
    add("str_proxy_address", "Adresse")
    add("str_proxy_port", "Port")
    add("str_proxy_username", "Username")
    add("str_proxy_password", "Passwort")
    add("str_bad_proxy_pref", "Sie haben den Proxy-Support aktiviert, aber leider keinen Proxy-Server bzw. Port angegeben. Bitte gehen Sie zurück zu den Netzwerk-Einstellungen und füllen Sie diese Felder.")

    # Player
    add("str_player", "Medien-Player")
    add("str_choose_a_player", "Medien-Player auswählen")
    add("str_no_player", "Kein Player")

    # Advanced
    add("str_advanced", "Erweitert")
    add("str_options_power_users", "Diese Optionen können von Power-Usern verwendet werden")
    add("str_run_command_download", "Diesen Befehl nach jedem Download starten")
    add("str_rcmd_full_path", "%f = kompletter Pfad zur heruntergeladenen Datei")
    add("str_rcmd_podcast_name", "%n = Name des Podcasts")
    add("str_other_advanced_options", "Mehr erweiterte Einstellungen")
    add("str_show_log", "Eigenes Tab für Log anzeigen")



    ## Feed Dialog (add/properties)
    add("str_title", "Titel")
    add("str_url", "URL")
    add("str_goto_subs", "Gehe zu Abonnements um die Eigenschaften dieses Feeds zu sehen")
    add("str_feed_save", "Speichern")
    add("str_feed_cancel", "Abbrechen")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Aktiviere Terminplaner")
    add("str_sched_select_type", "Wann soll der Terminplaner auf Aktualisirungen prüfen:")
    add("str_check_at_specific_times", "Zu festen Uhrzeiten")
    add("str_check_at_regular_intervals", "in regelmäßigen Intervallen")
    add("str_repeat_every:", "Wiederholen alle")
    add("str_latest_run", "Letzter Lauf:")
    add("str_next_run", "Nächster Lauf:")
    add("str_not_yet", "Noch nicht")
    #--- Cancel
    add("str_save_and_close", "Speichern und Schließen")
    #--- Save

    add("str_time_error", "Eine der angegebenen Zeiten ist falsch, gültige Zeiten sehen so aus 16:43, 10:02am.")

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
    #--- Programming: Erik de Jonge, Andrew Grumet, Garth Kidd, Perica Zivkovic\nDesign: Martijn Venrooy\nContent strategist: Mark Alexander Posth\nConcept: Adam Curry, Dave Winer\nThanks to all translators for their commitments!\n\nBased on Feedparser and BitTorrent technology.\nThis program is free software you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of  merchantability or fitness for a particular purpose. \n\nSee the GNU General Public License for more details.




    ## Statusbar items
    add("str_check_for_new_podcast_button", "Drücken Sie auf den grünen Button, um auf neue Podcast zu überprüfen")
    add("str_last_check", "Letze Überprüfung beendet am")
    add("str_of", "von")
    add("str_item", "Einträgen")
    add("str_items", "Einträgen")
    add("str_downloading", "herunterladen")
    add("str_downloaded", "heruntergeladen")
    add("str_enclosure", "Enclosure")
    add("str_enclosures", "Enclosures")
    add("str_fetched", "fetched")
    add("str_loading_mediaplayer", "Media-Player laden ...")
    add("str_loaded_mediaplayer", "Media-Player geladen ...")
    add("str_initialized", "%s ist bereit" % PRODUCT_NAME)


    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast-Lader v" + __version__)
    add("str_localization_restart", "Um alle Einstellungen zu lokalisieren, ist ein Neustart von %s notwendig. Klicken Sie OK um %s zu beenden, Abbrechen um weiterzuarbeiten." % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_really_quit", "Mindestens ein Download ist aktiv.  Wirklich beenden?");
    add("str_double_check", "Ein Download findet bereits statt.");

    # check for update
    add("str_new_version_ipodder", "Es ist eine neue Version von %s verfügbar, drücken Sie OK, um auf die Webseite zu wechseln." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "Ihre %s-Version ist die aktuelleste!" % PRODUCT_NAME)
    add("str_other_copy_running", "Eine andere Instanz von %s ist bereits gestartet. Bitte verwenden Sie diese, warten Sie darauf daß es erscheint oder beenden Sie den Prozeß." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Jetzt überprüfen")
    add("str_open_ipodder", "%s öffnen" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Feeds überprüfen")

    # Feed right-click menu
    add("str_remove", "Entfernen")
    add("str_open_in_browser", "In Browser öffnen")

    # Downloads right-click menu
    add("str_play_episode", "Episode abspielen")
    add("str_clear_selected", "Selektierte Einträge löschen")




