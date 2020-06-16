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
        "Descarga cancelada; espacio libre %dMB menos " \
        "que el minimo de %dMB.  Por favor, libere espacio en" \
        "su disco usando la herramienta limpieza o ajustando los parámetros de administrador" \
        "de almacenamiento en Preferencias")
    add("str_critical_error_unknown", "Error critico desconocido en la descarga")
    
    add("str_error_checking_new_version", "Error comprobando nueva versión.  Por favor, intentelo más tarde.")
    add("str_hours", "horas")
    add("str_minutes", "minutos")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Revisando")
    add("str_scanned", "Revisado")
    add("str_feed", "fuente")
    add("str_feeds", "fuentes")
    
    add("str_downloading_new_episodes", "Descargando nuevos episodios")
    add("str_sched_specific", "Comprobar en instantes determinados")
    add("str_sched_reg", "Comprobar en intervalos regulares")
    add("str_repeat_every", "Repetir cada")
    add("str_next_run_label", "Próxima ejecución:")
    
    add("str_license", "Este programa es de codigo libre; puedes distribuirlo y/o modificarlo bajo los términos de la licencia GNU General Public License publicada por la Free Software Foundation, tanto en la versión 2 de la Licencia como en cualquier version posterior. Este programa se distribuye con la finalidad de ser útil, pero sin ninguna garantía; incluso sin la garantia implicita en la comercialidad o el proposito particular de un programa. \n\nMira la GNU General Public License para más detalles.")

	

    add("str_donate", "Donar a %s" % PRODUCT_NAME)
    add("str_donate_expl", "Es importante mantener las aplicaciones de la comunidad %s online y mantener esta nueva forma de transmitir contenidos multimedia. Cualquier aporte de dinero sera bien recibido por el equipo y los animara a trabajar en nuevas características y servicios!" % PRODUCT_NAME)


    add("str_donate_yes", "Si, llevame a la pagina de donaciones ahora!")
    add("str_donate_two_weeks", "Todavia me lo tengo que pensar un poco más, vuelve a consultarme en dos semanas")
    add("str_donate_already", "Ya he hecho una donación, no vuelvas a consultarme")
    add("str_donate_no", "No, no quiero hacer ninguna donación, no vuelvas a consultarme")
    add("str_donate_one_day", "Ahora no, consultame otra vez mañana")
    add("str_donate_proceed", "Procede")

    add("str_scheduler_dialog", "Planificador")
    add("str_scheduler_tab", "Opciones")

    add("str_select_import_file", "Selecciona el fichero a importar")    
    add("str_add_feed_dialog", "Añadir una fuente")
    add("str_edit_feed", "Propiedades de la fuente")

    add("str_really_delete", "Definitivamente borralo")

    add("str_license_caption", "Licencia")

    add("str_ep_downloaded", "Descargado")
    add("str_ep_skipped_removed_other", "Omitido/Eliminado/Otra fuente")
    add("str_dl_state_to_download", "Para descargar")

    add("str_select_none_cleanup", "No seleccionar ninguno")
    add("str_submit_lang", "Enviar un idioma")
    
    add("str_dltab_live", "Descargas actuales:")
    add("str_dltab_ul_speed", "Velocidad de subida: ")
    add("str_dltab_dl_speed", "Velocidad de descarga: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Archivo")
    add("str_import_opml", "Importar fuentes de ompl...")
    add("str_export_opml", "Exportar fuentes a opml...")
    add("str_preferences_menubar", "Preferencias...")
    add("str_close_window", "Cerrar ventana")
    add("str_quit", "Salir")

    add("str_edit", "Editar")
    add("str_select_all", "Seleccionar todo")

    add("str_tools", "Herramientas")
    add("str_check_all", "Comprobar todos")
    add("str_catch_up", "Ponerse al dia")
    add("str_check_selected", "Comprobar seleccionados")
    add("str_add_feed", "Añadir una fuente...")
    add("str_remove_selected", "Eliminar fuente")
    add("str_feed_properties", "Propiedades de la fuente...")
    add("str_scheduler_menubar", "Planificador...")
    
    add("str_select_language", "Seleccionar idioma")

    ## these are also used for the tabs
    add("str_view", "Ver")
    add("str_downloads", "Descargas")
    add("str_subscriptions", "Suscripciones")
    add("str_podcast_directory", "Directorio de Podcast")
    add("str_cleanup", "Limpiar")

    add("str_help", "Ayuda")
    add("str_online_help", "Ayuda online")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Comprobar actualizaciones...")
    add("str_report_a_problem", "Notificar un problema")
    add("str_goto_website", "Ir al sitio web")
    add("str_make_donation", "Hacer una donación")
    add("str_menu_license", "Licencia...")
    add("str_about", "Sobre...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Eliminar elementos seleccionados")
    add("str_cancel_selected_download", "Cancelar la descarga seleccionada")
    add("str_pause_selected", "Interrumpir los elementos seleccionados")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Nuevo")
    add("str_dl_state_queued", "En cola")
    add("str_dl_state_downloading", "Descargando")
    add("str_dl_state_downloaded", "Descargado")
    add("str_dl_state_cancelled", "Cancelado")
    add("str_dl_state_finished", "Terminado")
    add("str_dl_state_partial", "Descargado parcialmente")
    add("str_dl_state_clearing", "Limpiando")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Comprobar nuevos podcasts")
    add("str_catch_up_mode", "Ponerse al dia - Descargar solo las ultimas suscripciones")

    add("str_add_new_feed", "Añadir nueva fuente");
    add("str_remove_selected_feed", "Eliminar fuente seleccionada")
    add("str_properties", "Propiedades")
    add("str_check_selected_feed", "Comprobar fuente seleccionada")

    add("str_scheduler_on", "Planificador - Activado")
    add("str_scheduler_off", "Planificador - Desactivado")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Proxima tarea planificada:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Descargando información del episodio...")
    add("str_no_episodes_found", "Ningun episodio encontrado.")


    ## Directorytab Toolbar
    add("str_refresh", "Actualizar")
    add("str_open_all_folders", "Abrir todoas las carpetas")
    add("str_close_all_folders", "Cerrar todas las carpetas")
    add("str_add", "Añadir")

    ## Directorytab Other items
    add("str_directory_description", "Haz click en una fuente o escribe/pega en el espacio disponible y haz click en añadir")




    ## Cleanuptab items
    add("str_select_a_feed", "Selecciona una fuente")
    add("str_refresh_cleanup", "Actualizar")
    
    add("str_look_in", "Buscar episodios en")        
    add("str_player_library", "Libreria de reproducción")
    add("str_downloads_folder", "Directorio de descargas")
    add("str_delete_library_entries", "Eliminar entradas de la biblioteca")
    add("str_delete_files", "Eliminar ficheros")
    add("str_select_all_cleanup", "Seleccionar todo")
    add("str_delete", "Eliminar")




    ## Logtab items
    add("str_log", "Log")
    add("str_clear", "Limpiar")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Nombre")
    add("str_lst_date", "Fecha")        
    add("str_lst_progress", "Progreso")
    add("str_lst_state", "Estado")
    add("str_lst_mb", "MB")
    add("str_lst_location", "Localización")
    add("str_lst_episode", "Episodio")
    add("str_lst_playlist", "Lista de reproducción")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Suscrito")
    add("str_disabled", "Desactivado")
    add("str_newly-subscribed", "Nueva suscripción")
    add("str_unsubscribed", "No suscrito")
    add("str_preview", "Previsualizar")
    add("str_force", "Forzar")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Escoge un nombre para el archivo a exportar")
    add("str_subs_exported", "Suscripciones exportadas.")
    
    ## Preferences Dialog
    add("str_preferences", "Preferencias")
    
    add("str_save", "Guardar")
    add("str_cancel", "Cancelar")
    
    # General
    add("str_general", "General")
    add("str_gen_options_expl", "Establecer las opciones generales para la aplicacion %s" % PRODUCT_NAME)
    add("str_hide_on_startup", "Mostrar %s en la barra de herramientas al inicio" % PRODUCT_NAME)

    add("str_run_check_startup", "Comprobar nuevos podcasts al iniciar la aplicación ")
    add("str_play_after_download", "Reproducir las descargas al terminar de bajarse")
    add("str_location_and_storage", "Administración de localización y almacenamiento")
    add("str_stop_downloading", "Parar de descargar si el disco duro alcanza un minimo de ")
    add("str_bad_megabyte_limit_1", "El límite de megabytes no es un numero entero")
    add("str_bad_megabyte_limit_2", "Prueba otra vez.")

    add("str_download_folder", "Descargar podcasts en este directorio")
    add("str_browse", "Navegar")
    add("str_bad_directory_pref_1", "No se ha podido encontrar el directorio solicitado")
    add("str_bad_directory_pref_2", "Por favor, vuelve a crearlo y prueba otra vez.")

    
    # Threading
    add("str_threads", "Hilos concurrentes")
    add("str_multiple_download", "Opciones de descarga múltiple")
    add("str_max_feedscans", "Máximos hilos concurrentes de revisión de fuentes por sesión")
    add("str_max_downloads", "Máximas descargas por sesión")
   
    # Network settings
    add("str_networking", "Opciones de red")
    add("str_coralize_urls", "Coralize URLs (experimental)")
    add("str_proxy_server", "Utilizar servidor proxy")
    add("str_proxy_address", "Dirección")
    add("str_proxy_port", "Puerto")
    add("str_proxy_username", "Nombre de usuario")
    add("str_proxy_password", "Contraseña")
    add("str_bad_proxy_pref", "Has activado el soporte para servidor proxy pero no has introducido el servidor proxy y el puerto. Vuelve a la pestaña de opciones de red e introduce un servidor proxy y un puerto válidos.")



    # Player
    add("str_player", "Reproductor")
    add("str_choose_a_player", "Elegir un reproductor")
    add("str_no_player", "Ningun reproductor")
    
    # Advanced
    add("str_advanced", "Avanzado")
    add("str_options_power_users", "Estas opciones pueden ser usadas por usuarios avanzados")
    add("str_run_command_download", "Ejecuta este comando después de cada descarga")
    add("str_rcmd_full_path", "%f = Ruta entera al archivo descargado")
    add("str_rcmd_podcast_name", "%n = nombre del Podcast")
    add("str_other_advanced_options", "Otras opciones avanzadas")
    add("str_show_log", "Mostrar pestaña de log en la aplicación")



    ## Feed Dialog (add/properties)
    add("str_title", "Titulo")
    add("str_url", "Dirección URL")
    add("str_goto_subs", "Ir a la pestaña de suscripciones para ver los episodios de esta fuente")
    add("str_feed_save", "Guardar")
    add("str_feed_cancel", "Cancelar")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Activar planificador")
    add("str_sched_select_type", "Selecciona los botones debajo para comprobar en instantes especificos o en intervalos regulares:")
    add("str_check_at_specific_times", "Comprobar en instantes determinados")
    add("str_check_at_regular_intervals", "Comprobar en intervalos regulares")
    add("str_repeat_every:", "Repetir cada:")
    add("str_latest_run", "Última ejecución:")
    add("str_next_run", "Próxima ejecución:")
    add("str_not_yet", "Todavia no")
    #--- Cancel
    add("str_save_and_close", "Guardar y cerrar")
    #--- Save

    add("str_time_error", "Alguna de las horas planificadas no parece ser correcta. Valores válidos son de la forma:  10:02am, 16:43.")


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
    add("str_check_for_new_podcast_button", "Comprobar nuevos podcasts pulsando el boton verde de comprobar")
    add("str_last_check", "Ultima comprobación llevada a cabo a las")
    add("str_of", "de")
    add("str_item", "elemento")
    add("str_items", "elementos")
    add("str_downloading", "descargando")
    add("str_downloaded", "descargado")
    add("str_enclosure", "enclosure")
    add("str_enclosures", "enclosures")
    add("str_fetched", "fetched")
    add("str_loading_mediaplayer", "Cargando tu reproductor multimedia...")
    add("str_loaded_mediaplayer", "Reproductor multimedia cargado...")        
    add("str_initialized", "%s listo" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Podcast receiver v" + __version__)
    add("str_localization_restart", "Para localizar todos los controles de %s es necesario reiniciar. Haz click en ok para reiniciar, o en cancelar para continuar." % PRODUCT_NAME)
    add("str_really_quit", "Hay descargas en curso, seguro que deseas salir?");
    add("str_double_check", "Parece que algun archivo esta descargandose");
    
    # check for update
    add("str_new_version_ipodder", "Existe una nueva version de %s disponible, haz click en Ok para ir a la pagina de descargas." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "This version of %s is up to date" % PRODUCT_NAME)
    add("str_other_copy_running", "%s ya esta ejecutandose. Por favor, apagalo o espera a que acabe." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Comprobar ahora")        
    add("str_open_ipodder", "Abrir %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Escanear fuentes")

    # Feed right-click menu
    add("str_remove", "Eliminar")        
    add("str_open_in_browser", "Abrir en el navegador")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Reproducir episodio en el reproductor multimedia.")
    add("str_clear_selected", "Eliminar elementos seleccionados")
    



