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
        "Закачка прекращена; Свободного места на диске " \
        "менее %dMB. Обеспечьте место под подкаст.")
    add("str_critical_error_unknown", "Неизвестная ошибка при закачке.")
    
    add("str_error_checking_new_version", "Возникла ошибка при проверки программы на новую версию")
    add("str_hours", "час.")
    add("str_minutes", "мин.")

    # The next 4 are for the status bar updates during the initial scan.
    add("str_scanning", "Проверка")
    add("str_scanned", "Проверка завершена")
    add("str_feed", "подкаст-директория")
    add("str_feeds", "подкаст-директорий")
    
    add("str_downloading_new_episodes", "Закачка новых подкастов")
    add("str_sched_specific", "Проверка в определённое время")
    add("str_sched_reg", "Проверка в определённые интервалы")
    add("str_repeat_every", "Повторять каждые")
    add("str_next_run_label", "Следующая проверка:")
    
    add("str_license", "Эта программа свободно распространяется; Вы можете пересобирать и/или модифицировать её под условиями лицензии GNU General Public License, опубликованной Free Software Foundation. Эта программа распространяется с надеждой, что может быть полезна, но без всяких гарантий. \n\nСмотрите GNU General Public License для большей информации.")

    add("str_donate", "Внести пожертвование %s" % PRODUCT_NAME)
    add("str_donate_expl", "Очень важно сохранить ПО %s-сообщества и поддерживать его дальнейшее развитие. Небольшое денежное пожертвование сможет сделать разработчиков счастливыми и дать стимул для дальнейшей разработки и введению новых сервисов!" % PRODUCT_NAME)
    add("str_donate_yes", "Да, открыть страницу пожертвований сейчас!")
    add("str_donate_two_weeks", "Я ещё потестирую программу. Напомнить через 2 недели")
    add("str_donate_already", "Я уже сделал пожертвование. Не показывать больше окно")
    add("str_donate_no", "Нет, я не сделал пожертвование. Не показывать больше окно")
    add("str_donate_one_day", "Не сейчас. Напомнить завтра")
    add("str_donate_proceed", "Продолжить")

    add("str_scheduler_dialog", "Планировщик")
    add("str_scheduler_tab", "Параметры")

    add("str_select_import_file", "Выберите импортируемый файл")    
    add("str_add_feed_dialog", "Добавить подкаст-директорию")
    add("str_edit_feed", "Установки подкаст-директории")

    add("str_really_delete", "Действительно удалить")

    add("str_license_caption", "Лицензия")

    add("str_ep_downloaded", "Закачано")
    add("str_ep_skipped_removed_other", "Пропущено/Удалено/Другое")
    add("str_dl_state_to_download", "Закачать")

    add("str_select_none_cleanup", "Выделение снято")
    add("str_submit_lang", "Найти языки")
    
    add("str_dltab_live", "Закачивается: ")
    add("str_dltab_ul_speed", "Скорость закачки: ")
    add("str_dltab_dl_speed", "Скорость скачивания: ")


    ##_________________________________________________________
    ##
    ##     Main window (iPodder.xrc)
    ##_________________________________________________________


    
    ## File menu
    add("str_file", "Файл")
    add("str_import_opml", "Импортировать подкаст-директории из opml...")
    add("str_export_opml", "Экспортировать подкаст-директории в opml...")
    add("str_preferences_menubar", "Установки...")
    add("str_close_window", "Закрыть окно")
    add("str_quit", "Выход")

    add("str_edit", "Редактировать")
    add("str_select_all", "Выбрать всё")

    add("str_tools", "Инструменты")
    add("str_check_all", "Проверить всё")
    add("str_catch_up", "Скачать новое")
    add("str_check_selected", "Проверить выбранное")
    add("str_add_feed", "Добавить подкаст-директорию...")
    add("str_remove_selected", "Удалить подкаст-директорию")
    add("str_feed_properties", "Свойства подкаст-директории...")
    add("str_scheduler_menubar", "Планировщик...")
    
    add("str_select_language", "Выбрать язык")

    ## these are also used for the tabs
    add("str_view", "Вид")
    add("str_downloads", "Закачки")
    add("str_subscriptions", "Описания")
    add("str_podcast_directory", "База Подкаст-директорий")
    add("str_cleanup", "Очистить")

    add("str_help", "Помощь")
    add("str_online_help", "Online помощь")
    add("str_faq", "FAQ")
    add("str_check_for_update", "Проверить обновления...")
    add("str_report_a_problem", "Послать отчёт об ошибке")
    add("str_goto_website", "Посетить WEB-страницу")
    add("str_make_donation", "Сделать пожертвование")
    add("str_menu_license", "Лицензия...")
    add("str_about", "О программе...")


    ## Downloadstab Toolbar
    add("str_remove_selected_items", "Удалить выбранное")
    add("str_cancel_selected_download", "Отменить выбранные закачки")
    add("str_pause_selected", "Пауза")

    ## Downloadstab States (in columns)
    ## Enclosure states. Use str_dl_state_ prefix to avoid collisions with
    ## other strings, e.g. str_downloading above which isn't capitalized.
    add("str_dl_state_new", "Новое")
    add("str_dl_state_queued", "Очередь")
    add("str_dl_state_downloading", "Скачивается")
    add("str_dl_state_downloaded", "Скачано")
    add("str_dl_state_cancelled", "Отменено")
    add("str_dl_state_finished", "Закончено")
    add("str_dl_state_partial", "Частично закачано")
    add("str_dl_state_clearing", "Очистка")


    ## Subscriptionstab Toolbar
    add("str_check_for_new_podcasts", "Проверить на новые подкасты")
    add("str_catch_up_mode", "Скачать новое - Только скачать новые описания")

    add("str_add_new_feed", "Добавить подкаст-директорию");
    add("str_remove_selected_feed", "Удалить выбранные подкаст-директории")
    add("str_properties", "Установки")
    add("str_check_selected_feed", "Проверить выбранные подкаст-директории")

    add("str_scheduler_on", "Планировщик - Вкл")
    add("str_scheduler_off", "Планировщик - Выкл")        

    ## Subscriptionstab Scheduler information
    add("str_next_run:", "Следующая проверка:")

    ## Subscriptionstab episode frame
    add("str_downloading_episode_info", "Скачивание информации об эпизоде...")
    add("str_no_episodes_found", "Эпизодов не найдено.")


    ## Directorytab Toolbar
    add("str_refresh", "Refresh")
    add("str_open_all_folders", "Открыть все папки")
    add("str_close_all_folders", "Закрыть все папки")
    add("str_add", "Add")

    ## Directorytab Other items
    add("str_directory_description", "Выберите подкаст-директорию в списке или введине название в поле выше.")




    ## Cleanuptab items
    add("str_select_a_feed", "Выберите подкаст-директорию")
    add("str_refresh_cleanup", "Обновить")
    
    add("str_look_in", "Искать эпизоды")        
    add("str_player_library", "Библиотека")
    add("str_downloads_folder", "Директории закачки")
    add("str_delete_library_entries", "Удалить содержимое библиотеки")
    add("str_delete_files", "Удалить файлы")
    add("str_select_all_cleanup", "Выбрать всё")
    add("str_delete", "Удалить")




    ## Logtab items
    add("str_log", "Лог")
    add("str_clear", "Очистить")


    ## Columns (in downloads- and subscriptionstab)
    add("str_lst_name", "Название")
    add("str_lst_date", "Дата")        
    add("str_lst_progress", "Прогресс")
    add("str_lst_state", "Состояние")
    add("str_lst_mb", "Мб")
    add("str_lst_location", "Местоположение")
    add("str_lst_episode", "Эпизод")
    add("str_lst_playlist", "Список воспроизведения")

    ## Feed subscription states -- see ipodder/feeds.py SUB_STATES variable
    add("str_subscribed", "Подписано")
    add("str_disabled", "Отключено")
    add("str_newly-subscribed", "Вновь подписано")
    add("str_unsubscribed", "Отписано")
    add("str_preview", "Предпросмотр")
    add("str_force", "Заставлять")
    





    ##_________________________________________________________
    ##
    ##   Dialog Windows
    ##_________________________________________________________



    ## OPML Import Dialog
    #--- Select import file

    ## OPML Export Dialog
    add("str_choose_name_export_file", "Выберите имя экспортируемого файла")
    add("str_subs_exported", "Описания экспортированы.")
    
    ## Preferences Dialog
    add("str_preferences", "Установки")
    
    add("str_save", "Сохранить")
    add("str_cancel", "Отмена")
    
    # General
    add("str_general", "Главные")
    add("str_gen_options_expl", "Установите главные настройки %s'а" % PRODUCT_NAME)
    add("str_hide_on_startup", "Прятать %s в трей при старте" % PRODUCT_NAME)

    add("str_run_check_startup", "Запускать проверку на новые версии при старте")
    add("str_play_after_download", "Проигрывать скачанное")
    add("str_location_and_storage", "Управление хранилищем")
    add("str_stop_downloading", "Остановить закачку, если на диске места меньше, чем ")
    add("str_bad_megabyte_limit_1", "Извините, но число не корректно")
    add("str_bad_megabyte_limit_2", "Попробуйте ещё.")

    add("str_download_folder", "Закачивать подкасты в папку")
    add("str_browse", "Обзор")
    add("str_bad_directory_pref_1", "Извините, директория не найдена")
    add("str_bad_directory_pref_2", "Пожалуйста, создайте директорию и выберите её.")

    
    # Threading
    add("str_threads", "Потоки")
    add("str_multiple_download", "Установки многопотоковой закачки")
    add("str_max_feedscans", "максимальное количество потоков при проверке")
    add("str_max_downloads", "максимальное количество потоков при скачке")
   
    # Network settings
    add("str_networking", "Установки сети")
    add("str_coralize_urls", "Подсвечивать URL'ы (экспериментально)")
    add("str_proxy_server", "Использовать proxy")
    add("str_proxy_address", "Адрес")
    add("str_proxy_port", "Порт")
    add("str_proxy_username", "Логин")
    add("str_proxy_password", "Пароль")
    add("str_bad_proxy_pref", "Вы определили работу через прокси, но не определили адрес и порт.  Пожалуйста, вернитесь к этим настройкам и заполните их.")

    # Player
    add("str_player", "Проигрыватель")
    add("str_choose_a_player", "Выберите проигрыватель")
    add("str_no_player", "Нет проигрывателя")
    
    # Advanced
    add("str_advanced", "Расширенные")
    add("str_options_power_users", "Эти настройки могут быть изменены продвинутыми пользователями")
    add("str_run_command_download", "Запускать эту команду после каждой закачки")
    add("str_rcmd_full_path", "%f = Полный путь к закачанному файлу")
    add("str_rcmd_podcast_name", "%n = Название подкаста")
    add("str_other_advanced_options", "Другие расширенные настройки")
    add("str_show_log", "Показывать лог в отдельной вкладке")



    ## Feed Dialog (add/properties)
    add("str_title", "Заголовок")
    add("str_url", "URL")
    add("str_goto_subs", "Перейти на вкладку описаний, чтобы поглядеть эпизоды")
    add("str_feed_save", "Сохранить")
    add("str_feed_cancel", "Отмена")




    ## Scheduler Dialog
    add("str_enable_scheduler", "Включить Планировщик")
    add("str_sched_select_type", "Выберите переключатели ниже. чтобы определить режим проверки:")
    add("str_check_at_specific_times", "Проверка в определённое время")
    add("str_check_at_regular_intervals", "Проверка через интервалы")
    add("str_repeat_every:", "Повторять каждые:")
    add("str_latest_run", "Последняя проверка:")
    add("str_next_run", "Следующая проверка:")
    add("str_not_yet", "Не сейчас")
    #--- Cancel
    add("str_save_and_close", "Сохранить и выйти")
    #--- Save

    add("str_time_error", "Одно из запланированных событий некорретно составлено. Правильный синтаксис: 10:02am, 16:43.")


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
    add("str_check_for_new_podcast_button", "Проверить на новые подкасты путём нажатия зелёной кнопки")
    add("str_last_check", "Последняя проверка завершена в ")
    add("str_of", "из")
    add("str_item", "элем.")
    add("str_items", "элем.")
    add("str_downloading", "скачивается")
    add("str_downloaded", "скачано")
    add("str_enclosure", "вложить")
    add("str_enclosures", "вложено")
    add("str_fetched", "выбрано")
    add("str_loading_mediaplayer", "Загружается Ваш медиапроигрыватель...")
    add("str_loaded_mediaplayer", "Загружен Ваш медиапроигрыватель...")        
    add("str_initialized", "%s готов" % PRODUCT_NAME)




    ## Other application strings
    add("str_ipodder_title", PRODUCT_NAME + " - Подкаст-менеджер v" + __version__)
    add("str_localization_restart", "Чтобы применить установки, необходимо перегрузить программу. Нажмите Ok, чтобы завершить работу, Cancel Для продолжения работы.")
    add("str_really_quit", "Закачка в процессе.  Прекратить и выйти?");
    add("str_double_check", "Скачка уже в процессе.");
    
    # check for update
    add("str_new_version_ipodder", "Доступна новая версия %s, нажмите Ok для перехода на сайт." % PRODUCT_NAME)
    add("str_no_new_version_ipodder", "Эта версия %s - последняя" % PRODUCT_NAME)
    add("str_other_copy_running", "Другая копия %s уже запущена. Пожалуйста, дождитесь её закрытия или прервите её выполнение." % PRODUCT_NAME)

    # Windows taskbar right-click menu
    add("str_check_now", "Проверить сейчас")        
    add("str_open_ipodder", "Открыть %s" % PRODUCT_NAME)
    #--- Downloading
    add("str_scanning_feeds", "Проверка подкаст-директорий")

    # Feed right-click menu
    add("str_remove", "Удалить")        
    add("str_open_in_browser", "Открыть в браузере")
    
    

    # Downloads right-click menu
    add("str_play_episode", "Проиграть эпизод в медиапроигрывателе")
    add("str_clear_selected", "Очистить выбранные элементы")
