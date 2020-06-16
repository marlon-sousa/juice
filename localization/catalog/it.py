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

    add("str_username", "Username")
    add("str_password", "Password")
    add("str_missing_proxy_password", "E' stato impostato un username per il proxy ma non una password. \n" \
        "Resettare entrambi i valori o inserire una password.")

    add("str_goto_background_on_close_title", "Set close behavior")
    add("str_goto_background_on_close_warn", \
        "%s può continuare a lavorare in background dopo la chiusura \n" \
        "della finestra principale. In alternativa %s può essere chiuso. \n" \
        "Desideri mantenere attivo %s?" % (PRODUCT_NAME,PRODUCT_NAME,PRODUCT_NAME))
    add("str_goto_background_on_close_pref", "Continua l'esecuzione in background alla chiusura della finestra principale")
    add("str_yes", "Si")
    add("str_no", "No")
    add("str_dont_ask", "Non chiedere nuovamente")
    add("str_ok", "OK")
    add("str_hide_window", "Nascondi finestra")
    add("str_hide_tray_icon", "Nascondi icona nella System Tray")
    add("str_show_window", "Mostra finestra")

    add("str_catchup_pref", "Catchup skips older episodes permanently")
    add("str_set_catchup_title", "Set catchup behavior")
    add("str_set_catchup_description", \
        "When checking in Catchup mode, %s will skip all but the top \n" \
        "item in each feed. Please specify how %s should treat the \n" \
        "skipped items." % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_skip_permanently", "Salta permanentemente")
    add("str_skip_temporarily", "Salta solo questa volta")
    
    add("str_set_oneclick_handler", "Set one-click handler")
    add("str_set_oneclick_handler_warn",\
        "%s is not currently your one-click subscription handler for podcasts. \n" \
        "Should we set %s to launch from one-click subscription links?" % (PRODUCT_NAME,PRODUCT_NAME))
    add("str_ensure_oneclick_handler", "Always use %s for one-click subscription" % PRODUCT_NAME)
    
    add("str_txt_feedmanager", "Gestori di feed compatibili:")
    add("str_feedmanager_btn_podnova", "www.PodNova.com - Cerca o visualizza i podcast, iscrizione mediante un solo click")

    add("str_open_downloads_folder", "Apri la cartella dei download")
    add("str_chkupdate_on_startup", "Controlla nuove versioni all'avvio del programma.")
    add("str_bad_feedmanager_url", "Impostare un URL valido per il gestore dei feed.")
    add("str_feed_manager", "Gestore dei Feed")
    add("str_feedmanager_enable", "Sincronizza le sottoscrizioni con un servizio remoto")
    add("str_opml_url", "URL OPML")
    add("str_set_track_genre", "Imposta il genere della traccia a")
    add("str_auto_delete", "Cancella automaticamente episodi più vecchi di")
    add("str_days_old", "giorni")
    
    add("str_show_notes", "Mostra note")
    add("str_close", "Chiudi")
    
    add("str_critical_error_minspace_exceeded", \
        "Download saltato; spazio libero %dMB minore " \
        "dei %dMB richiesti. Liberare spazio " \
        "sul computer utilizzando il comando Pulizia o cambiare le impostazioni " \
        "di salvataggio nelle Preferenze")
    add("str_critical_error_unknown", "Errore critico sconosciuto durante il download.")
    
    add("str_error_checking_new_version", "Si è verificato un errore durante il controllo delle nuove versioni. Riprovare più tardi.")
    add("str_hours", "ore")
    add("str_minutes", "minuti")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Scansione in corso")
    add("str_scanned", "Scansione completata")
    add("str_feed", "feed")
    add("str_feeds", "feed")
    
    add("str_downloading_new_episodes", "Scaricamento di nuovi episodi in corso")
    add("str_sched_specific", "Controlla ad orari specifici")
    add("str_sched_reg", "Controlla ad intervalli regolari")
    add("str_repeat_every", "Ripeti ogni")
    add("str_next_run_label", "Prossimo avvio:")
    
    add("str_license", "Questo è un programma gratuito; è possibile ridistribuire e/o modificare il programma secondo i termini della  General Public License come pubblicato dalla Free Software Foundation; è possibile utilizzare la versione 2 della Licenza, o (a propria discrezione) una qualsiasi versione successiva. Il programma è distribuito nella speranza che possa essere utile, ma senza alcuna garanzia; in particolare, ma non esclusivamente, nessuna garanzia implicita sulla commerciabilità o l'idoneità a uno scopo particolare. \n\nPer maggiori informazioni consultare la GNU General Public License.")

    add("str_donate", "Fai una donazione a %s" % PRODUCT_NAME)
    add("str_donate_expl", "E' importante mantenere in vita la comunità di %s e continuare a fornire questo nuovo modo di consumare file multimediali libero. Qualsiasi somma di denaro è ben gradita dal team di sviluppo ed incoraggerà la realizzazione di nuove funzioni e servizi!" % PRODUCT_NAME)
    add("str_donate_yes", "Sì, apri ora la pagina per eseguire la donazione!")
    add("str_donate_two_weeks", "Devo ancora pensarci su, mostra questa finestra tra due settimane")
    add("str_donate_already", "Ho già eseguito una donazione, non mostrare nuovamente questa finestra")
    add("str_donate_no", "No, non desidero eseguire una donazione, non mostrare nuovamente questa finestra")
    add("str_donate_one_day", "Non ora, mostra questa notifica tra 1 giorno")
    add("str_donate_proceed", "Procedi")

    add("str_scheduler_dialog", "Scheduler")
    add("str_scheduler_tab", "Impostazioni")

    add("str_select_import_file", "Seleziona file da importare")    
    add("str_add_feed_dialog", "Aggiungi Feed")
    add("str_edit_feed", "Proprietà Feed")

    add("str_really_delete", "Confermi eliminazione?")

    add("str_license_caption", "Licenza")

    add("str_ep_downloaded", "Scaricati")
    add("str_ep_skipped_removed_other", "Saltati/Rimossi/Altri Feed")
    add("str_dl_state_to_download", "Da scaricare")

    add("str_select_none_cleanup", "Nessuna selezione")
    add("str_submit_lang", "Invia una traduzione")
    
    add("str_dltab_live", "Download live: ")
    add("str_dltab_ul_speed", "Velocità upload: ")
    add("str_dltab_dl_speed", "Velocità download: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "File")
    add("str_import_opml", "Importa feed da file opml...")
    add("str_export_opml", "Esporta feed in un file opml...")
    add("str_preferences_menubar", "Preferenze...")
    add("str_close_window", "Chiudi finestra")
    add("str_quit", "Esci")

    add("str_edit", "Modifica")
    add("str_select_all", "Seleziona tutto")

    add("str_tools", "Strumenti")
    add("str_check_all", "Controlla tutti")
    add("str_catch_up", "Catch-up")
    add("str_check_selected", "Controlla selezionati")
    add("str_add_feed", "Aggiungi feed...")
    add("str_remove_selected", "Rimuovi feed")
    add("str_feed_properties", "Proprietà feed...")
    add("str_scheduler_menubar", "Scheduler...")
    
    add("str_select_language", "Scegli lingua")

    ## these are also used for the tabs
    add("str_view", "Visualizza")
    add("str_downloads", "Download")
    add("str_subscriptions", "Sottoscrizioni")
    add("str_podcast_directory", "Directory podcast")
    add("str_cleanup", "Pulizia")

    add("str_help", "Help")
    add("str_online_help", "Help Online")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Controlla aggiornamenti...")
    add("str_report_a_problem", "Segnala un problema")
    add("str_goto_website", "Vai al sito")
    add("str_make_donation", "Fai una donazione")
    add("str_menu_license", "Licenza...")
    add("str_about", "Informazioni...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Rimuovi elementi selezionati")
    add("str_cancel_selected_download", "Cancella download selezionati")
    add("str_pause_selected", "Metti in pausa")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Nuovo")
    add("str_dl_state_queued", "In coda")
    add("str_dl_state_downloading", "Scaricamento in corso")
    add("str_dl_state_downloaded", "Scaricamento completato")
    add("str_dl_state_cancelled", "Cancellato")
    add("str_dl_state_finished", "Completato")
    add("str_dl_state_partial", "Parzialmente completato")
    add("str_dl_state_clearing", "Cancellazione in corso")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Controlla nuovi podcast")
    add("str_catch_up_mode", "Catch-up - Scarica solo l'ultima sottoscrizione")

    add("str_add_new_feed", "Aggiungi feed");
    add("str_remove_selected_feed", "Rimuovi feed selezionati")
    add("str_properties", "Proprietà feed")
    add("str_check_selected_feed", "Controlla/Scarica feed selezionati")

    add("str_scheduler_on", "Scheduler - Attivato")
    add("str_scheduler_off", "Scheduler - Disattivato")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Prossimo avvio:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Scaricamento informazioni episodio in corso...")
    add("str_no_episodes_found", "Nessun episodio trovato.")


    ## Directorytab Toolbar
    add("str_refresh", "Aggiorna")
    add("str_open_all_folders", "Apri tutte le cartelle")
    add("str_close_all_folders", "Chiudi tutte le cartelle")
    add("str_add", "Aggiungi")

    ## Directorytab Other items
    add("str_directory_description", "Seleziona un feed nell'elenco o digita/incolla l'indirizzo nello spazio sottostante e scegli aggiungi.")




    ## Cleanuptab items
    add("str_select_a_feed", "Seleziona feed")
    add("str_refresh_cleanup", "Aggiorna")
    
    add("str_look_in", "Cerca episodi in")        
    add("str_player_library", "Libreria di esecuzione")
    add("str_downloads_folder", "Cartella di scaricamento")
    add("str_delete_library_entries", "Elimina elementi nella libreria")
    add("str_delete_files", "Elimina file scaricati")
    add("str_select_all_cleanup", "Seleziona tutto")
    add("str_delete", "Elimina")




    ## Logtab items
    add("str_log", "Log")
    add("str_clear", "Cancella")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Nome")
    add("str_lst_date", "Data")        
    add("str_lst_progress", "Progresso")
    add("str_lst_state", "Stato")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Collocazione")
    add("str_lst_episode", "Episodio")
    add("str_lst_playlist", "Playlist")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Sottoscritto")
    add("str_disabled", "Disabilitato")
    add("str_newly-subscribed", "Nuova sottoscrizione")
    add("str_unsubscribed", "Non sottoscritto")
    add("str_preview", "Anteprima")
    add("str_force", "Force")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Scegliere un nome per il file")
    add("str_subs_exported", "Sottoscrizioni esportate.")
    
    ## Preferences Dialog
    add("str_preferences", "Preferenze")
    
    add("str_save", "Salva")
    add("str_cancel", "Cancella")
    
    # General
    add("str_general", "Generale")
    add("str_gen_options_expl", "Imposta le opzioni generali per il programma %s" % PRODUCT_NAME)
    add("str_hide_on_startup", "Mostra %s nella system tray all'avvio" % PRODUCT_NAME)

    add("str_run_check_startup", "Esegui un controllo per nuovi podcast all'avvio del programma")
    add("str_play_after_download", "Riproduci immediatamente i file a scaricamento completato")
    add("str_location_and_storage", "Gestione collocazione e salvataggio contenuti")
    add("str_stop_downloading", "Interrompi lo scaricamento se l'harddisk raggiunge lo spazio di")
    add("str_bad_megabyte_limit_1", "Il limite di megabyte impostato non sembra essere un valore intero")
    add("str_bad_megabyte_limit_2", "Si prega di riprovare.")

    add("str_download_folder", "Scarica i podcast in questa cartella")
    add("str_browse", "Seleziona")
    add("str_bad_directory_pref_1", "Impossibile trovare la cartella specificata.")
    add("str_bad_directory_pref_2", "Creare la cartella e riprovare.")

    
    # Threading
    add("str_threads", "Processi")
    add("str_multiple_download", "Impostazioni di scaricamento multiplo")
    add("str_max_feedscans", "numero massimo di processi di scansione feed per sessione")
    add("str_max_downloads", "numero massimo di download per sessione")
   
    # Network settings
    add("str_networking", "Impostazioni di rete")
    add("str_coralize_urls", "Coralize URLs (experimental)")
    add("str_proxy_server", "Usa server proxy")
    add("str_proxy_address", "Indirizzo")
    add("str_proxy_port", "Porta")
    add("str_proxy_username", "Username")
    add("str_proxy_password", "Password")
    add("str_bad_proxy_pref", "E' stato abilitato il supporto proxy senza specificare un host o una porta. Ritornare alle impostazioni di rete ed impostare l'host e la porta per il proxy.")

    # Player
    add("str_player", "Player")
    add("str_choose_a_player", "Scegli un player")
    add("str_no_player", "Nessun player")
    
    # Advanced
    add("str_advanced", "Avanzate")
    add("str_options_power_users", "L'utilizzo di queste opzioni è consigliato ad Utenti Esperti")
    add("str_run_command_download", "Esegui questo comando dopo ogni download")
    add("str_rcmd_full_path", "%f = Percorso completo al file scaricato")
    add("str_rcmd_podcast_name", "%n = Nome podcast")
    add("str_other_advanced_options", "Altre opzioni avanzate")
    add("str_show_log", "Mostra la tab dei log nel programma")



    ## Feed Dialog (add/properties)
    add("str_title", "Titolo")
    add("str_url", "URL")
    add("str_goto_subs", "Vai alla tab delle sottoscrizioni per visualizzare questo episodio")
    add("str_feed_save", "Salva")
    add("str_feed_cancel", "Cancella")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Abilita scheduler")
    add("str_sched_select_type", "Seleziona i bottoni sottostanti per controllare ad un orario specifico o ad intervalli regolari:")
    add("str_check_at_specific_times", "Controlla ad orari specifici")
    add("str_check_at_regular_intervals", "Controlla ad intervalli regolari")
    add("str_repeat_every:", "Ripeti ogni:")
    add("str_latest_run", "Ultimo avvio:")
    add("str_next_run", "Prossimo avvio:")
    add("str_not_yet", "Non ancora")
    #--- Cancel
    add("str_save_and_close", "Salva e chiudi")
    #--- Save

    add("str_time_error", "Uno degli orari pianificati non risulta corretto. esempio di formato corretto: 10:02am, 16:43.")


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
    add("str_check_for_new_podcast_button", "Controlla nuovi podcast premendo il bottone verde")
    add("str_last_check", "Ultimo controllo completato il")
    add("str_of", "di")
    add("str_item", "elemento")
    add("str_items", "elementi")
    add("str_downloading", "in fase di scaricamento")
    add("str_downloaded", "scaricati")
    add("str_enclosure", "enclosure")
    add("str_enclosures", "enclosure")
    add("str_fetched", "letto")
    add("str_loading_mediaplayer", "Caricamento media player in corso...")
    add("str_loaded_mediaplayer", "Caricamento media player completato...")        
    add("str_initialized", "%s pronto" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast receiver v" + __version__)
    add("str_localization_restart", "E' necessario riavviare il programma per aggiornare la localizzazione. Clicca OK per procedere, cancella per continuare.")
    add("str_really_quit", "Scaricamento in corso. Confermi l'uscita?");
    add("str_double_check", "Sembra che uno scaricamento sia in corso.");
    
    # check for update
    add("str_new_version_ipodder", "E' disponibile una nuova versione di %s, premi Ok per aprire la pagina di download." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "La versione di %s in uso è la più recente" % PRODUCT_NAME)
    add("str_other_copy_running", "Un'altra istanza di %s è in esecuzione. Attendere il completamento o chiudere l'istanza." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Controlla Ora")        
    add("str_open_ipodder", "Apri %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Scansione feed in corso")

    # Feed right-click menu
    add("str_remove", "Rimuovi")        
    add("str_open_in_browser", "Apri nel browser")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Riproduci episodio in mediaplayer")
    add("str_clear_selected", "Rimuovi elementi selezionati")
    




