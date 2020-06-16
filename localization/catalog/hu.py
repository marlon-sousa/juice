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

   add("str_critical_error_minspace_exceeded", \
       "A letöltés megszakítva: a szabad terület %dMB, " \
       "kevesebb, mint %dMB.  Kérlek szabadíts fel területet Please free up space on " \
       "törléssel vagy módosítsd a tárolókezelést" \
       "a Beállítások menüpontban")
   add("str_critical_error_unknown", "Ismeretlen hiba a letöltéskor.")

   add("str_error_checking_new_version", "Sajnálom, hibát találtam az új verzió keresése során. Kérem, próbálja újra késõbb!")
   add("str_hours", "órák")
   add("str_minutes", "percek")

   # The next 4 are for the status bar updates during the initial scan.
   add("str_scanning", "Keresés")
   add("str_scanned", "Keresett")
   add("str_feed", "csatorna")
   add("str_feeds", "csatornák")

   add("str_downloading_new_episodes", "Új adás letöltése")
   add("str_sched_specific", "Ellenõrzés konkrét idõponttól")
   add("str_sched_reg", "Idõszak ellenõrzése")
   add("str_repeat_every", "Ismételje minden")
   add("str_next_run_label", "Következõ futás:")

   add("str_license", "Ez egy szabad program; A dokumentum a Free Software Foundation által kiadott GNU Free Documentation License 2-es vagy újabb verziójában foglalt feltételek keretein belül másolható, terjeszthetõ és/vagy módosítható." \
        "A programot annak reményében készítettük, hogy hasznos lesz, de garanciát nem vállalunk;  \n\nNézdd át a GNU General Public License -t a részletekért.")

   add("str_donate", "%s támogatása" % PRODUCT_NAME)
   add("str_donate_expl", "It's important to keep community-owned %s applications online and keep this new way of consuming media free as in speech. A fejlesztõ csapat minden pénzt szívesen fogad, ami ösztönöz minket arra, hogy új funciókkal és szolgáltatásokkal bõvítsük a programot!" % PRODUCT_NAME)
   add("str_donate_yes", "Igen, menjünk a támogatói oldalra!")
   add("str_donate_two_weeks", "Még egy kicsit gondolkodok rajta, figyelmeztess két hét múlva.")
   add("str_donate_already", "Én már támogattam, ne jelenjen meg legközelebb ez az ablak.")
   add("str_donate_no", "Nem, én nem akarom támogatni a programot,  ne jelenjen meg legközelebb ez az ablak")
   add("str_donate_one_day", "Most nem, értesíts 1 nap múlva")
   add("str_donate_proceed", "Tovább")

   add("str_scheduler_dialog", "Idõzítés")
   add("str_scheduler_tab", "Beállítások")

   add("str_select_import_file", "Fájlok kiválasztása importáláshoz")
   add("str_add_feed_dialog", "Csatorna hozzáadása")
   add("str_edit_feed", "Csatorna tulajdonságok")

   add("str_really_delete", "Tényleg törlöm")

   add("str_license_caption", "Liszensz")

   add("str_ep_downloaded", "Letöltve")
   add("str_ep_skipped_removed_other", "Átugorva/Törölve/Másik csatorna")
   add("str_dl_state_to_download", "Letöltésre")

   add("str_select_none_cleanup", "Válassz egyet")
   add("str_submit_lang", "Nyelv keresése")

   add("str_dltab_live", "Futó letöltések: ")
   add("str_dltab_ul_speed", "Feltöltés sebessége: ")
   add("str_dltab_dl_speed", "Letöltés sebessége: ")

   ##_________________________________________________________
   ##
   ##     Main window (iPodder.xrc)
   ##_________________________________________________________

   ## File menu
   add("str_file", "File")
   add("str_import_opml", "Csatornák importálása opml-bõl...")
   add("str_export_opml", "Csatornák exportálása opml-be...")
   add("str_preferences_menubar", "Beállítások...")
   add("str_close_window", "Ablak bezárása")
   add("str_quit", "Kilépés")

   add("str_edit", "Módosítás")
   add("str_select_all", "Mindent kiválaszt")

   add("str_tools", "Eszközök")
   add("str_check_all", "Összes átvizsgálása")
   add("str_catch_up", "Félbeszakít")
   add("str_check_selected", "Kiválasztottak átvizsgálása")
   add("str_add_feed", "Csatorna hozzáadása...")
   add("str_remove_selected", "Csatorna törlése")
   add("str_feed_properties", "Csatorna tulajdonságok...")
   add("str_scheduler_menubar", "Idõzítés...")

   add("str_select_language", "Nyelv kiválasztása")

   ## these are also used for the tabs
   add("str_view", "Nézet")
   add("str_downloads", "Letöltés")
   add("str_subscriptions", "Elõfizetés")
   add("str_podcast_directory", "Az adások könyvtára")
   add("str_cleanup", "Takarítás")

   add("str_help", "Segítség")
   add("str_online_help", "Online segítség")
   add("str_faq", "FAQ")
   add("str_check_for_update", "Új verzió keresése...")
   add("str_report_a_problem", "Hiba elküldése")
   add("str_goto_website", "Ugrás a weboldalra")
   add("str_make_donation", "Támogatás")
   add("str_menu_license", "Liszensz...")
   add("str_about", "Névjegy...")

   ## Downloadstab Toolbar
   add("str_remove_selected_items", "Kiválasztott elemek törlése")
   add("str_cancel_selected_download", "Kiválasztott letöltések megszakítása")
   add("str_pause_selected", "Szünet kiválasztása")

   ## Downloadstab States (in columns)
   ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
   ## other strings, e.g. str_downloading above which isn't capitalized.
   add("str_dl_state_new", "Új")
   add("str_dl_state_queued", "Várakozás")
   add("str_dl_state_downloading", "Letöltés")
   add("str_dl_state_downloaded", "Letöltve")
   add("str_dl_state_cancelled", "Megszakítva")
   add("str_dl_state_finished", "Befejezve")
   add("str_dl_state_partial", "Részben letöltve")
   add("str_dl_state_clearing", "Takarítás")

   ## Subscriptionstab Toolbar
   add("str_check_for_new_podcasts", "Új adás kijelölése")
   add("str_catch_up_mode", "Félbeszakítás - CSak az új elõfizetések töltsd le!")

   add("str_add_new_feed", "Új csatorna hozzáadása");
   add("str_remove_selected_feed", "Kiválasztott csatorna törlése")
   add("str_properties", "Tulajdonságok")
   add("str_check_selected_feed", "Kiválasztott csatornák ellenõrzése")

   add("str_scheduler_on", "Idõzítés - Be")
   add("str_scheduler_off", "Idõzítés - Ki")

   ## Subscriptionstab Scheduler information
   add("str_next_run:", "Következõ futás:")

   ## Subscriptionstab episode frame
   add("str_downloading_episode_info", "Adás információk letöltése...")
   add("str_no_episodes_found", "Nincs új adás.")

   ## Directorytab Toolbar
   add("str_refresh", "Frissítés")
   add("str_open_all_folders", "Összes könyvtár megnyitása")
   add("str_close_all_folders", "Összes könyvtár bezárása")
   add("str_add", "Add")

   ## Directorytab Other items
   add("str_directory_description", "Kattints a csatornára a kibontásban vagy írd be / másold be a fenti területre és kattints a Hozzáadás gombra.")

   ## Cleanuptab items
   add("str_select_a_feed", "Válassz csatornát")
   add("str_refresh_cleanup", "Frissítés")

   add("str_look_in", "Adás keresése")
   add("str_player_library", "Lejátszó könyvtára")
   add("str_downloads_folder", "Letöltések könyvtára")
   add("str_delete_library_entries", "Könyvtár bejegyzések törlése")
   add("str_delete_files", "Fájlok törlése")
   add("str_select_all_cleanup", "Összes kiválasztása")
   add("str_delete", "Törlés")

   ## Logtab items
   add("str_log", "Log")
   add("str_clear", "Takarítás")

   ## Columns (in downloads- and subscriptionstab)
   add("str_lst_name", "Név")
   add("str_lst_date", "Dátum")
   add("str_lst_progress", "Folyamat")
   add("str_lst_state", "Állapot")
   add("str_lst_mb", "MB")
   add("str_lst_location", "Hely")
   add("str_lst_episode", "Adás")
   add("str_lst_playlist", "Lejátszási lista")

   ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
   add("str_subscribed", "Elõfizetve")
   add("str_disabled", "Letiltva")
   add("str_newly-subscribed", "Új hozzáadás")
   add("str_unsubscribed", "Lemondva")
   add("str_preview", "Elõnézet")
   add("str_force", "Érvényes")

   ##_________________________________________________________
   ##
   ##   Dialog Windows
   ##_________________________________________________________

   ## OPML Import Dialog
   #--- Select import file

   ## OPML Export Dialog
   add("str_choose_name_export_file", "Válassz nevet az export fájlhoz")
   add("str_subs_exported", "Elõfizetés exportálva.")

   ## Preferences Dialog
   add("str_preferences", "Beállítások")

   add("str_save", "Mentés")
   add("str_cancel", "Mégsem")

   # General
   add("str_general", "Általános")
   add("str_gen_options_expl", "Végrehajtja az %s általános beállításait" % PRODUCT_NAME)
   add("str_hide_on_startup", "Indításkor csak a Tálcán jelenik meg.")

   add("str_run_check_startup", "Új adások keresése a program indulásakor")
   add("str_play_after_download", "Letöltés után azonnal játsza le.")
   add("str_location_and_storage", "Hely- és tárolás kezelés")
   add("str_stop_downloading", "Letöltés megállítása, ha a lemezkapacitás kevesebb, mint")
   add("str_bad_megabyte_limit_1", "Bocs, de a határérték nem egész szám")
   add("str_bad_megabyte_limit_2", "Kérlek, próbáld újra.")

   add("str_download_folder", "Adások letöltése ebbe a könyvtárba")
   add("str_browse", "Browse")
   add("str_bad_directory_pref_1", "Bocs, de nem találom a megadott könyvtárat")
   add("str_bad_directory_pref_2", "Kérlek, csináld meg és próbáld újra.")

   # Threading
   add("str_threads", "Párhuzamos munkavégzés")
   add("str_multiple_download", "Párhuzamos letöltések beállítása")
   add("str_max_feedscans", "maximális folyamatok száma a csatornakeresés során")
   add("str_max_downloads", "maximális letöltések száma a letöltések során")

   # Network settings
   add("str_networking", "Hálózati beállítások")
   add("str_coralize_urls", "Coralize URLs (kísérlet)")
   add("str_proxy_server", "Proxy szerver használata")
   add("str_proxy_address", "Cím")
   add("str_proxy_port", "Port")
   add("str_proxy_username", "Felhasználónév")
   add("str_proxy_password", "Jelszó")
   add("str_bad_proxy_pref", "Engedélyezted a proxy használatot, de nem adtál meg szervert és portot. Kérlek, menj vissza a Hálózati beállításokba és állítsd be a hiányzó értékeket.")

   # Player
   add("str_player", "Lejátszó")
   add("str_choose_a_player", "Válassz lejátszót!")
   add("str_no_player", "Nincs lejátszó")

   # Advanced
   add("str_advanced", "Haladó")
   add("str_options_power_users", "Ezeket az opciókat csak haladó felhasználók használják!")
   add("str_run_command_download", "Program futtatása minden letöltés után")
   add("str_rcmd_full_path", "%f = A letöltött fájlok teljes elérési útvonala.")
   add("str_rcmd_podcast_name", "%n = Adás neve")
   add("str_other_advanced_options", "További haladó beállítások")
   add("str_show_log", "Log fül megjelenítése az alkalmazásban")

   ## Feed Dialog (add/properties)
   add("str_title", "Cím")
   add("str_url", "URL")
   add("str_goto_subs", "Menj az elõfizetések fülre, a csatorna adásainak megtekintéséhez!")
   add("str_feed_save", "Mentés")
   add("str_feed_cancel", "Mégsem")

   ## Scheduler Dialog
   add("str_enable_scheduler", "Idõzítés engedélyezése")
   add("str_sched_select_type", "Válaszd a lenti rádiógombokat az idõpont vagy a letöltések ismétlõdésének beállításához:")
   add("str_check_at_specific_times", "Ellenõrzés ebben az idõpontban")
   add("str_check_at_regular_intervals", "Ellenõrzés meghatározott ismétlõdéssel:")
   add("str_repeat_every:", "Ismétlés minden:")
   add("str_latest_run", "Utolsó futás:")
   add("str_next_run", "Következõ futás:")
   add("str_not_yet", "Még nem")
   #--- Cancel
   add("str_save_and_close", "Mentés és bezárás")
   #--- Save

   add("str_time_error", "A beállított idõpont nem megfelelõ. A helyes formátum: 10:02am, 16:43.")

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
   add("str_check_for_new_podcast_button", "Új adások kereséséhez nyomd meg a zöld gombot!")
   add("str_last_check", "Az utolsó ellenõrzések")
   add("str_of", "of")
   add("str_item", "adás")
   add("str_items", "adások")
   add("str_downloading", "letöltés")
   add("str_downloaded", "letöltve")
   add("str_enclosure", "melléklet")
   add("str_enclosures", "mellékletek")
   add("str_fetched", "elhozva")
   add("str_loading_mediaplayer", "Média lejátszó betöltése ...")
   add("str_loaded_mediaplayer", "Média lejátszó betöltve ...")
   add("str_initialized", "%s kész" % PRODUCT_NAME)

   ## Other application strings
   add("str_ipodder_title", PRODUCT_NAME + " - Podcast receiver v" + __version__)
   add("str_localization_restart", "A nyelvváltás után az %st újra kell indítani. Kattints az OK gombra, ha leálítod, Mégsemre ha folytatni akarod az %s használatát." % (PRODUCT_NAME,PRODUCT_NAME))
   add("str_really_quit", "Letöltés folyamatban. Biztos, hogy kilépsz?");
   add("str_double_check", "Úgy tûnik, hogy letöltés van folyamtban.");

   # check for update
   add("str_new_version_ipodder", "Az %s új verziója letölthetõ, kattints az OK gombra a letöltéshez." % PRODUCT_NAME)
   add("str_no_new_version_ipodder", "Nincs frissebb %s verzió" % PRODUCT_NAME)
   add("str_other_copy_running", "Az %s már fut. Another copy of %s is running. Várdd meg amíg befejezi vagy lõdd le!" % (PRODUCT_NAME,PRODUCT_NAME))

   # Windows taskbar right-click menu
   add("str_check_now", "Adások keresése")
   add("str_open_ipodder", "%s megnyitása" % PRODUCT_NAME)
   #--- Downloading
   add("str_scanning_feeds", "Csatornák keresése")

   # Feed right-click menu
   add("str_remove", "Eltávolítás")
   add("str_open_in_browser", "Megnyitás böngészõben")

   # Downloads right-click menu
   add("str_play_episode", "Adás lejátszása médiaplayerben.")
   add("str_clear_selected", "Kiválasztott eleme törlése")
