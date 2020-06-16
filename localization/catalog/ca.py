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

    add("str_txt_feedmanager", "Administradors de fonts compatibles:")
    add("str_feedmanager_btn_podnova", "www.PodNova.com - Buscar o veure podcasts, subscripció amb un únic clic.")

    add("str_open_downloads_folder", "Obrir la carpeta de descàrregues")
    add("str_chkupdate_on_startup", "Comprobar si hi han noves versions al arrancar.")
    add("str_bad_feedmanager_url", "Entreu una adreça vàlida per l'administrador de fonts.")
    add("str_feed_manager", "Administrador de fonts")
    add("str_feedmanager_enable", "Sincronitzar les subscripcions amb un servei remot")
    add("str_opml_url", "Adreça OPML")
    add("str_set_track_genre", "Enviar el tipus de pista a")
    add("str_auto_delete", "Esborrar automàticament episodis de mes de")
    add("str_days_old", "dias.")
    
    add("str_show_notes", "Mostrar les notes")
    add("str_close", "Tancar")

    add("str_critical_error_minspace_exceeded", \
        "Descàrrega ignorada; l'espai lliure està %dMB per sota " \
        "del mínim de %dMB. Si us plau allibereu espai en el " \
        "vostre disc utilitzant Neteja o ajusteu les preferencies " \
        "de gestió d'espai")
    add("str_critical_error_unknown", "Error crític desconegut durant la descàrrega.")
    
    add("str_error_checking_new_version", "Ho sentim però hi ha hagut un error en la busqueda de noves versions. Torneu a probar-ho mes endavant.")
    add("str_hours", "hores")
    add("str_minutes", "minuts")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Comprovant")
    add("str_scanned", "Comprovat")
    add("str_feed", "font")
    add("str_feeds", "fonts")
    
    add("str_downloading_new_episodes", "Descarrega de nous episodis")
    add("str_sched_specific", "Comprobar a hores determinades")
    add("str_sched_reg", "Comprovar periòdicament")
    add("str_repeat_every", "Repetir cada")
    add("str_next_run_label", "Propera execució:")
    
    add("str_license", "Aquesta aplicació es programari lliure; el podeu redistribuir i/o modificar sota les condicions de la Llicencia Pública General de GNU tal i com es publicada per la Free Software Foundation; sigui la versió 2 de la llicencia o, sota el vostra criteri, qualsevol versió posterior. Aquesta aplicació es distribueix amb l'esperança de que resulti útil, pero sense cap mena de garantia, ni tan sols la garantia implícita de mercandibilitat ni de adequació per cap propòsit particular. \n\nPer a mes detalls veieu la Llicencia Pública General de GNU.")

    add("str_donate", "Fer una donació a %s" % PRODUCT_NAME)
    add("str_donate_expl", "Es important mantenir en linea les aplicacions %s de la comunitat i mantenir aquest modus de consumir mitjans gratuits. Qualsevol quantitat de diners encoratjarà al equip a treballar en noves prestacions i serveis!" % PRODUCT_NAME)
    add("str_donate_yes", "Si, porta'm a la pàgina de donacions ara mateix!")
    add("str_donate_two_weeks", "Encara vull provar-lo una mica mes, tornam-ho a recordar en dues setmanes")
    add("str_donate_already", "Ja he fet una donació, no em tornis a mostrar aquest dialeg")
    add("str_donate_no", "No, no vull pas donar. No em tornis a mostrar aquest dialeg mai mes")
    add("str_donate_one_day", "Ara no, recordam-ho demà")
    add("str_donate_proceed", "Fer-ho ara")

    add("str_scheduler_dialog", "Programador")
    add("str_scheduler_tab", "Configuració")

    add("str_select_import_file", "Selecció")    
    add("str_add_feed_dialog", "Afegir una font")
    add("str_edit_feed", "Propietats de la font")

    add("str_really_delete", "Esborrar realment")

    add("str_license_caption", "Llicencia")

    add("str_ep_downloaded", "Descarregat")
    add("str_ep_skipped_removed_other", "Ignorat/Eliminat/Altre Font")
    add("str_dl_state_to_download", "A Descarregar")

    add("str_select_none_cleanup", "No seleccionar-ne cap")
    add("str_submit_lang", "Enviar un idioma")
    
    add("str_dltab_live", "Descàrregues en procés: ")
    add("str_dltab_ul_speed", "Velocitat de càrrega: ")
    add("str_dltab_dl_speed", "Velocitat de descàrrega: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Fitxer")
    add("str_import_opml", "Importar fonts des d'un opml...")
    add("str_export_opml", "Exportar fonts com a opml...")
    add("str_preferences_menubar", "Preferencies...")
    add("str_close_window", "Tancar finestra")
    add("str_quit", "Sortir")

    add("str_edit", "Editar")
    add("str_select_all", "Seleccionar-ho tot")

    add("str_tools", "Eines")
    add("str_check_all", "Comprovar-ho tot")
    add("str_catch_up", "Posar-se al dia")
    add("str_check_selected", "Comprovar la selecció")
    add("str_add_feed", "Afegir una font...")
    add("str_remove_selected", "Eliminar la font")
    add("str_feed_properties", "Propietats de la font...")
    add("str_scheduler_menubar", "Programador...")
    
    add("str_select_language", "Seleccionar l'idioma")

    ## these are also used for the tabs
    add("str_view", "Veure")
    add("str_downloads", "Descàrregues")
    add("str_subscriptions", "Subscripcions")
    add("str_podcast_directory", "Directori Podcast")
    add("str_cleanup", "Neteja")

    add("str_help", "Ajuda")
    add("str_online_help", "Ajuda en linea")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Comprobar si hi han actualitzacions...")
    add("str_report_a_problem", "Informar d'un problema")
    add("str_goto_website", "Anar a la pàgina web")
    add("str_make_donation", "Fer una donació")
    add("str_menu_license", "Llicència...")
    add("str_about", "Quan a...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Eliminar els elements seleccionats")
    add("str_cancel_selected_download", "Cancel·lar la descarrega de la selecció")
    add("str_pause_selected", "Pausar la selecció")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Nou")
    add("str_dl_state_queued", "En qua")
    add("str_dl_state_downloading", "Descarregant")
    add("str_dl_state_downloaded", "Descarregat")
    add("str_dl_state_cancelled", "Cancel·lat")
    add("str_dl_state_finished", "Finalitzat")
    add("str_dl_state_partial", "Descarregat parcialment")
    add("str_dl_state_clearing", "Netejant")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Comprovar si hi han nous podcasts")
    add("str_catch_up_mode", "Posar al dia - Descarregar únicament les últimes subscripcions")

    add("str_add_new_feed", "Afegir una font");
    add("str_remove_selected_feed", "Eliminar la font seleccionada")
    add("str_properties", "Propietats")
    add("str_check_selected_feed", "Comprovar la font seleccionada")

    add("str_scheduler_on", "Programador - Activat")
    add("str_scheduler_off", "Programador - Desactivat")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Propera execució:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Descarregant informació d'episodis...")
    add("str_no_episodes_found", "No s'ha trobat cap episodi.")


    ## Directorytab Toolbar
    add("str_refresh", "Actualitzar")
    add("str_open_all_folders", "Obrir totes les carpetes")
    add("str_close_all_folders", "Tancar totes les carpetes")
    add("str_add", "Afegir")

    ## Directorytab Other items
    add("str_directory_description", "Feu clic en una font a l'arbre o copieu/enganxeu en el espai superior i feu clic a Afegir.")




    ## Cleanuptab items
    add("str_select_a_feed", "Seleccioneu una font")
    add("str_refresh_cleanup", "Actualitzar")
    
    add("str_look_in", "Buscar episodis a")        
    add("str_player_library", "Arxiu del reproductor")
    add("str_downloads_folder", "Carpeta de descàrregues")
    add("str_delete_library_entries", "Esborrar entrades de la llibreria")
    add("str_delete_files", "Esborrar fitxers")
    add("str_select_all_cleanup", "Seleccionar-ho tot")
    add("str_delete", "Esborrar")




    ## Logtab items
    add("str_log", "Registre")
    add("str_clear", "Buidar")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Nom")
    add("str_lst_date", "Data")        
    add("str_lst_progress", "Progrés")
    add("str_lst_state", "Estat")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Lloc")
    add("str_lst_episode", "Episodi")
    add("str_lst_playlist", "Llista de reproducció")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Subscrit")
    add("str_disabled", "Desabilitat")
    add("str_newly-subscribed", "Subscripció recent")
    add("str_unsubscribed", "Subscripció anul·lada")
    add("str_preview", "Previsualitzat")
    add("str_force", "Forçat")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Seleccioneu el fitxer a importar

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Esculliu un nom per al fitxer d'exportació")
    add("str_subs_exported", "Subscripcions exportades.")
    
    ## Preferences Dialog
    add("str_preferences", "Preferencies")
    
    add("str_save", "Desa")
    add("str_cancel", "Cancel·la")
    
    # General
    add("str_general", "General")
    add("str_gen_options_expl", "Configuració de les opcions generals del %s" % PRODUCT_NAME)
    add("str_hide_on_startup", "Reduir a la Barra de Sistema al arrancar")

    add("str_run_check_startup", "Comprova si hi han nous podcasts quant s'arranqui l'aplicació")
    add("str_play_after_download", "Reprodueix les descàrregues tant bon punt s'hagin descarregat")
    add("str_location_and_storage", "Configuració de lloc i emmagatzemament")
    add("str_stop_downloading", "Deixa de descarregar si el disc baixa d'un mínim de")
    add("str_bad_megabyte_limit_1", "Ho sento, El límit de megabytes no sembla un nombre sencer.")
    add("str_bad_megabyte_limit_2", "Si us plau, torneu-ho a provar.")

    add("str_download_folder", "Carpeta on es descarregaran els podcasts")
    add("str_browse", "Navega")
    add("str_bad_directory_pref_1", "Ho sento, no trobo la carpeta que heu entrat")
    add("str_bad_directory_pref_2", "Si us plau, torneu-la a crear i torneu-ho a provar.")

    
    # Threading
    add("str_threads", "Descàrregues simultaneas")
    add("str_multiple_download", "Configuració de descàregues múltiples")
    add("str_max_feedscans", "Nombre màxim de comprovacions de font simultaneas")
    add("str_max_downloads", "Nombre màxim de descàrregeus per sessió")
   
    # Network settings
    add("str_networking", "Configuració de Xarxa")
    add("str_coralize_urls", "Coralitza les URLs (experimental)")
    add("str_proxy_server", "Usa un servidor intermediari")
    add("str_proxy_address", "Adreça")
    add("str_proxy_port", "Port")
    add("str_proxy_username", "Nom d'usuari")
    add("str_proxy_password", "Contrasenya")
    add("str_bad_proxy_pref", "Heu habilitat l'us de servidors intermediaris pero no heu proporcinat un servidor intermediari i un port. Si us plau, torneu al panell Configuració de Xarxa i poseu-hi un servidor intermediari i el seu port.")

    # Player
    add("str_player", "Reproductor")
    add("str_choose_a_player", "Esculliu un reproductor")
    add("str_no_player", "No hi ha cap reproductor")
    
    # Advanced
    add("str_advanced", "Avançat")
    add("str_options_power_users", "Aquestes opcions poden esser usades pels usuaris avançats")
    add("str_run_command_download", "Executa aquesta comanda després de cada descàrrega")
    add("str_rcmd_full_path", "%f = Camí complert al fitxer descarregat")
    add("str_rcmd_podcast_name", "%n = Nom del podcast")
    add("str_other_advanced_options", "Altres opcions avançades")
    add("str_show_log", "Mostrar panell de log a l'aplicació")



    ## Feed Dialog (add/properties)
    add("str_title", "Titol")
    add("str_url", "URL")
    add("str_goto_subs", "Per veure els episodis d'aquesta font aneu al panell de subscripcions.")
    add("str_feed_save", "Desa")
    add("str_feed_cancel", "Cancel·la")




    ## scheduler dialog
    add("str_enable_scheduler", "Activar el programador")
    add("str_sched_select_type", "Seleccioneu els següents botons per comprovar a hores específiques o a intervals regulars:")
    add("str_check_at_specific_times", "Comprovar específicament a aquestes hores")
    add("str_check_at_regular_intervals", "Comprovar a intervals regulars")
    add("str_repeat_every:", "Repetir cada:")
    add("str_latest_run", "Última execució:")
    add("str_next_run", "Propera execució:")
    add("str_not_yet", "Encara no")
    #--- cancel
    add("str_save_and_close", "Desa i tanca")
    #--- save

    add("str_time_error", "Un dels horaris programats no sembla correcte. Els horaris correctes segueixen el patró: 10:02am, 16:43.")


    ## Donations Dialog
    #--- Fer una donació a ipodder
    #--- Es important mantenir aplicacions no comercials d'iPodder en linea i mantenir aquesta manera de consumir mitjans gratuits. Qualsevol quantitat de diners farà feliç els membres del equip i els encoratjarà a ampliar-ne les posibilitats!
    #--- Si, porta'm ara mateix a la pàgina de donacions!
    #--- Encara l'haig de provar una mica més, recorda'm-ho dins de dues setmanes
    #--- Ja he fet una donació, no tornis a mostrar aquest dialeg
    #--- No, no vull fer cap donació, no tornis a mostrar aquest dialeg mai mes
    #--- Ara no, recorda'm-ho demà
    #--- D'acord




    ## About Dialog
    #--- Versió:
    #--- Programació: Erik de Jonge, Andrew Grumet, Garth Kidd, Perica Zivkovic\nDiseny: Martijn Venrooy\nEstratega de continguts: Mark Alexander Posth\nConcepte: Adam Curry, Dave Winer\nGracies a tots el traductors per el seu esforç!\n\nBasat en les tecnologies Feedparser i BitTorrent.\nAquest programari es lliure; el podeu distribuir i/o modificar sota els termes de la Llicencia Pública General GNU tal i com és publicada per la Free Software Foundation; tant la versió 2 de la llicencia, com (al seu criteri) qualsevol versió posterior. Aquest programari es distribueix amb l'esperança de que sigui útil però sense cap mena de garantia, ni tan sols la garantia implicita de "mercantabilitat" ni de adequació a cap proposit. \n\nPer a més detalls veure la Llicencia Pública General GNU.




    ## statusbar items
    add("str_check_for_new_podcast_button", "Comproveu si hi ha nous episodis prement el botó vert")
    add("str_last_check", "Última comprovació ")
    add("str_of", "de")
    add("str_item", "element")
    add("str_items", "elements")
    add("str_downloading", "descarregant")
    add("str_downloaded", "descarregat")
    add("str_enclosure", "paquet")
    add("str_enclosures", "paquets")
    add("str_fetched", "obtingut(s)")
    add("str_loading_mediaplayer", "Carregant el reproductor multimèdia...")
    add("str_loaded_mediaplayer", "S'ha carregat el reproductor multimèdia...")        
    add("str_initialized", "%s inicialitzat" % PRODUCT_NAME)




    ## other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Descarregador de Podcasts v" + __version__)
    add("str_localization_restart", "Per traduir tots els controls del %s cal reiniciar. premeu D'acord per apagar correctament o Cancel·lar per continuar." % PRODUCT_NAME)
    add("str_really_quit", "Hi ha una descàrrega en marxa. esteu segur de voler sortir?");
    add("str_double_check", "Sembla que ja hi ha una descàrrega en marxa.");
    
    # check for update
    add("str_new_version_ipodder", "Hi ha disponible una nova versió de %s. Premeu D'acord per anar a la pàgina de descàrregues." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "Aquesta versió de %s està al dia." % PRODUCT_NAME)
    add("str_other_copy_running", "Ja s'està executant un altre copia de %s. Si us plau, porteu-la a primer pla i espereu que acabi o finalitzeu-la." % PRODUCT_NAME)

    # windows taskbar right-click menu
    add("str_check_now", "Comprovar ara")        
    add("str_open_ipodder", "Obrir %s" % PRODUCT_NAME)
    #--- downloading
    add("str_scanning_feeds", "Comprobant les fonts")

    # feed right-click menu
    add("str_remove", "eliminar")        
    add("str_open_in_browser", "Obrir en navegador")
    
    

    # downloads right-click menu
    add("str_play_episode", "Reproduir l'episodi en el reproductor multimèdia")
    add("str_clear_selected", "Esborrar els elements seleccionats")
