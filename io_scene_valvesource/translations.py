#coding=utf-8
_languages = ['ru', 'ja', 'es']

_data = {
'vca_sequence': {
	'ja': "シクウェンスを生成します",
	'en': "Generate Sequence",
	'ru': "Создать анимацию",
	'es': "Generar Secuencía",
},
'controllers_simple_tip': {
	'en': "Generate one flex controller per shape key",
	'ru': "Создавать по контроллеру на каждый ключ формы",
	'es': "Generar un controlador de flexion por llave de forma",
},
'vertmap_group_props': {
	'en': "Vertex Maps",
	'es': "Mapas de Vertices",
},
'action_selection_filter_tip': {
	'en': "All actions that match the armature's filter term and have users",
	'ru': "Все действия, которые подходят под фильтр имён действий и где-либо используются",
	'es': "",
},
'curve_poly_side_fwd': {
	'en': "Forward (outer) side",
	'ru': "Внешняя сторона",
	'es': "",
},
'action_selection_current_tip': {
	'en': "The armature's currently assigned action or NLA tracks",
	'ru': "Текущее действие (или нелинейная анимация) скелета",
	'es': "",
},
'valvesource_cloth_enable': {
	'en': "Cloth Physics Enable",
	'es': "",
},
'subdir_tip': {
	'en': "Optional path relative to scene output folder",
	'ru': "Куда экспортировать? (Необязательно; по умолчанию экспортируется в ту же папку, где находится .blend-файл) ",
	'es': "",
},
'controllers_mode': {
	'ja': "DMXフレックスのコントローラー生成",
	'en': "DMX Flex Controller generation",
	'ru': "Генерация контроллеров лицевой анимации (DMX)",
	'es': "",
},
'scene_export': {
	'ja': "シーンをエクスポート",
	'en': "Scene Export",
	'ru': "Экспорт всей сцены",
	'es': "",
},
'shape_stereo_mode_tip': {
	'en': "How stereo split balance should be defined",
	'ru': "Способ разделения объекта на левую и правую части для стерео-контроллеров",
	'es': "",
},
'bone_rot_legacy': {
	'en': "Legacy rotation",
	'ru': "Обратная совместимость вращения костей",
	'es': "",
},
'controllers_advanced_tip': {
	'en': "Insert the flex controllers of an existing DMX file",
	'ru': "Вставить блок контроллеров лицевой анимации",
	'es': "",
},
'triangulate_tip': {
	'en': "Avoids concave DMX faces, which are not supported by Source",
	'ru': "Избегать вогнутых полигонов в DMX-файлах (не поддерживается studiomdl)",
	'es': "",
},
'action_filter': {
	'ja': "アクションフィルター",
	'en': "Action Filter",
	'ru': "Фильтр действий",
	'es': "",
},
'vca_start_tip': {
	'en': "Scene frame at which to start recording Vertex Animation",
	'ru': "Кадр в сцене, с которого следует начать запись вершинной анимации",
	'es': "",
},
'action_filter_tip': {
	'en': "Actions with names matching this filter pattern and which have users will be exported",
	'ru': "Будут эксортированы только те действия, имена которых подходят под этот фильтр, и которые где-либо используются",
	'es': "",
},
'shape_stereo_sharpness_tip': {
	'en': "How sharply stereo flex shapes should transition from left to right",
	'ru': "Насколько резко будет осуществляться переход между левой и правой частью объекта",
	'es': "",
},
'vca_sequence_tip': {
	'en': "On export, generate an animation sequence that drives this Vertex Animation",
	'ru': "При экспорте автоматически создать sequence, управляющий этой вершинной анимацией",
	'es': "",
},
'shape_stereo_mode': {
	'en': "DMX stereo split mode",
	'ru': "Разделение на левую и правую части для стерео-контрлолеров (DMX)",
	'es': "",
},
'dummy_bone': {
	'en': "Implicit motionless bone",
	'ru': "\"Пустая\" недвижимая кость",
	'es': "",
},
'vca_group_props': {
	'ja': "頂点アニメーション",
	'en': "Vertex Animation",
	'ru': "Вершинная анимация",
	'es': "",
},
'curve_poly_side': {
	'ja': "ポリゴン生成",
	'en': "Polygon Generation",
	'ru': "Генерация геометрии",
	'es': "",
},
'group_merge_mech': {
	'ja': "メカニカルな局部は結合",
	'en': "Merge mechanical parts",
	'ru': "Слить вместе механические части",
	'es': "",
},
'action_selection_mode_tip': {
	'en': "How actions are selected for export",
	'ru': "Какие действия экспортировать?",
	'es': "",
},
'use_scene_export_tip': {
	'en': "Export this item with the scene",
	'ru': "Экспортировать этот объект при экспорте сцены",
	'es': "",
},
'curve_poly_side_back': {
	'en': "Backward (inner) side",
	'ru': "Внутренняя сторона",
	'es': "",
},
'valvesource_vertex_blend': {
	'en': "Blend Params RGB",
	'es': "",
},
'bone_rot_legacy_tip': {
	'en': "Remaps the Y axis of bones in this armature to Z, for backwards compatibility with old imports (SMD only)",
	'ru': "Переназначить Y-ось всех костей в Z-ось для обратной совместимости с старыми импортами",
	'es': "",
},
'controller_source': {
	'ja': "DMXフレックスのコントローラーのソースファイル ",
	'en': "DMX Flex Controller source",
	'ru': "Файл контроллеров лицевой анимации (DMX)",
	'es': "",
},
'group_suppress_tip': {
	'en': "Export this group's objects individually",
	'ru': "Экспортировать объекты этой группы по отдельности",
	'es': "",
},
'action_selection_current': {
	'ja': "現在 / NLA",
	'en': "Current / NLA",
	'ru': "Текущее действие / Нелинейная анимация",
	'es': "",
},
'shape_stereo_sharpness': {
	'en': "DMX stereo split sharpness",
	'ru': "Резкость разделения в стерео-контроллерах",
	'es': "",
},
'group_suppress': {
	'ja': "ミュート",
	'en': "Suppress",
	'ru': "\"Пересиливание\"",
	'es': "",
},
'shape_stereo_vgroup': {
	'en': "DMX stereo split vertex group",
	'ru': "Группа вешин разделения для стерео-контроллеров",
	'es': "",
},
'shape_stereo_vgroup_tip': {
	'en': "The vertex group that defines stereo balance (0=Left, 1=Right)",
	'ru': "Группа вершин для автоматического деления ключей формы на левую и правую часть. 0 = Левая часть, 1 = Правая часть.",
	'es': "",
},
'controllers_source_tip': {
	'en': "A DMX file (or Text datablock) containing flex controllers",
	'ru': "DMX-файл или внутренний текст в Blender, содержащий настройки контроллеров лицевой анимации",
	'es': "",
},
'valvesource_vertex_blend1': {
	'en': "Blend Params Extra (?)",
	'es': "",
},
'curve_poly_side_tip': {
	'en': "Determines which side(s) of this curve will generate polygons when exported",
	'ru': "Указывает, какая сторона (стороны) выделенной кривой будет использоваться для генерации геометрии",
	'es': "",
},
'triangulate': {
	'ja': "三角測量",
	'en': "Triangulate",
	'ru': "Преобразовывать все многоугольники в треугольники",
	'es': "",
},
'curve_poly_side_both': {
	'en': "Both sides",
	'ru': "Обе стороны",
	'es': "",
},
'group_merge_mech_tip': {
	'en': "Optimises DMX export of meshes sharing the same parent bone",
	'ru': "Оптимизиция экспорт объектов, имеющих общих родителей",
	'es': "",
},
'action_selection_mode': {
	'en': "Action Selection",
	'ru': "Выбор действия",
	'es': "",
},
'shape_stereo_mode_vgroup': {
	'en': "Use a vertex group to define stereo balance",
	'ru': "Использовать группу вершин для разделения стерео-контроллеров",
	'es': "",
},
'vca_end_tip': {
	'en': "Scene frame at which to stop recording Vertex Animation",
	'ru': "Кадр в сцене, которым следует закончить запись вершинной анимации",
	'es': "",
},
'valvesource_vertex_paint': {
	'en': "Vertex Paint",
	'es': "",
},
'controllers_mode_tip': {
	'en': "How flex controllers are defined",
	'ru': "Способ задания контроллеров лицевой анимации",
	'es': "",
},
'subdir': {
	'en': "Subfolder",
	'ru': "Подпапка",
	'es': "",
},
'dummy_bone_tip': {
	'en': "Create a dummy bone for vertices which don't move. Emulates Blender's behaviour in Source, but may break compatibility with existing files (SMD only)",
	'ru': "Создать кость и привязать к ней вершины, которые не двигаются. (Только SMD.)",
	'es': "",
},
'exportpanel_steam': {
	'ja': "Steam コミュニティ",
	'en': "Steam Community",
	'ru': "Сообщество Steam",
	'es': "",
},
'exportables_arm_filter_result': {
	'ja': "「{0}」アクション～{1}",
	'en': "\"{0}\" actions ({1})",
	'ru': "Фильтр имён действий \"{0}\" на скелете {1}",
	'es': "",
},
'exportables_flex_count_corrective': {
	'ja': "是正シェイプ：{0}",
	'en': "Corrective Shapes: {0}",
	'ru': "Ключей форм коррекции: {0}",
	'es': "",
},
'exportables_curve_polyside': {
	'ja': "ポリゴン生成：",
	'en': "Polygon Generation:",
	'ru': "Генерация геометрии:",
	'es': "",
},
'exportmenu_title': {
	'ja': "Source Tools エクスポート",
	'en': "Source Tools Export",
	'ru': "Экспорт в Source",
	'es': "",
},
'exportables_flex_help': {
	'ja': "フレックス・コントローラーのヘレプ",
	'en': "Flex Controller Help",
	'ru': "Помощь по контроллерам лицевой анимации",
	'es': "",
},
'exportpanel_title': {
	'ja': "Source Engine エクスポート",
	'en': "Source Engine Export",
	'ru': "Экспорт в Source",
	'es': "",
},
'exportables_flex_src': {
	'ja': "コントローラーのソースファイル ",
	'en': "Controller Source",
	'ru': "Файл настроек контроллеров",
	'es': "",
},
'exportmenu_invalid': {
	'en': "Cannot export selection",
	'ru': "Выделенный объект невозможно экспортировать",
	'es': "",
},
'qc_title': {
	'ja': "Source Engine QCのコンパイル",
	'en': "Source Engine QC Complies",
	'ru': "Компиляция QC",
	'es': "",
},
'exportables_flex_props': {
	'ja': "フレックスのプロパティ",
	'en': "Flex Properties",
	'ru': "Свойства контроллеров лицевой анимации",
	'es': "",
},
'exportables_flex_generate': {
	'ja': "コントローラーを生成します",
	'en': "Generate Controllers",
	'ru': "Сгенерировать контроллеры",
	'es': "",
},
'exportables_flex_split': {
	'ja': "ステレオフルックスの差額：",
	'en': "Stereo Flex Balance:",
	'ru': "Разделение на правую и левую часть:",
	'es': "",
},
'exportables_group_mute_suffix': {
	'ja': "(ミユト)",
	'en': "(suppressed)",
	'ru': "(игнорируется)",
	'es': "",
},
'exportmenu_scene': {
	'ja': "シーンをエクスポート ({0}つファイル)",
	'en': "Scene export ({0} files)",
	'ru': "Экспорт {0} файлов",
	'es': "",
},
'exportpanel_dmxver': {
	'ja': "DMXのバージョン：",
	'en': "DMX Version:",
	'ru': "Версия DMX:",
	'es': "",
},
'exportpanel_update': {
	'ja': "更新アドオンの確認",
	'en': "Check for updates",
	'ru': "Проверить обновления",
	'es': "",
},
'exportables_title': {
	'ja': "Source Engineのエクスポート可能",
	'en': "Source Engine Exportables",
	'ru': "Объекты для Source",
	'es': "",
},
'exportables_armature_props': {
	'ja': "アーマティアのプロパティ",
	'en': "Armature Properties ({0})",
	'ru': "Свойства скелета ({0})",
	'es': "",
},
'qc_bad_enginepath': {
	'ja': "エンジンのパスが無効です",
	'en': "Invalid Engine Path",
	'ru': "Некорректный путь до папки bin",
	'es': "",
},
'qc_invalid_source2': {
	'ja': "Source Engine 2はQCファイルが使いません",
	'en': "QC files do not exist in Source 2",
	'ru': "QC-файлы движком Source 2 не используются",
	'es': "",
},
'exportmenu_selected': {
	'en': "Selected objects ({0} files)",
	'ru': "Выбранные объекты ({0} файлов)",
	'es': "",
},
'exportables_group_props': {
	'ja': "グループのプロパティ",
	'en': "Group Properties",
	'ru': "Свойства групп",
	'es': "",
},
'qc_no_enginepath': {
	'ja': "エンジンのパスはありません",
	'en': "No Engine Path provided",
	'ru': "Не указан путь до папки bin",
	'es': "",
},
'exportables_curve_props': {
	'ja': "カーブのプロパティ",
	'en': "Curve Properties",
	'ru': "Свойства сплайна",
	'es': "",
},
'exportables_flex_count': {
	'ja': "シェイプ：{0}",
	'en': "Shapes: {0}",
	'ru': "Ключей формы: {0}",
	'es': "",
},
'bl_info_author': {
	'ja': "トム・エドワーズ～グリゴリ・レヴジン",
	'en': "Tom Edwards (translators: Grigory Revzin)",
	'ru': "Том Эдвардс (переводили: Григорий Ревзин)",
	'es': "",
},
'activate_dependency_shapes': {
	'en': "Activate dependency shapes",
	'ru': "Активировать зависимые ключи формы",
	'es': "",
},
'settings_prop': {
	'en': "Blender Source Tools settings",
	'ru': "Настройки Blender Source Tools",
	'es': "",
},
'bl_info_description': {
	'en': "Importer and exporter for Valve Software's Source Engine. Supports SMD\\VTA, DMX and QC.",
	'ru': "Экспорт и импорт для движка Source. Поддерживаемые форматы: SMD/VTA, DMX, QC.",
	'es': "",
},
'export_menuitem': {
	'en': "Source Engine (.smd, .vta, .dmx)",
	'ru': "Движок Source (.smd, .vta, .dmx)",
	'es': "",
},
'help': {
	'ja': "ヘレプ",
	'en': "Help",
	'ru': "Помощь",
	'es': "",
},
'bl_info_location': {
	'ja': "ファイル > インポート / エクスポート、シーンのプロパティ",
	'en': "File > Import/Export, Scene properties",
	'ru': "Файл > Импортировать/Экспортировать, свойства сцены",
	'es': "",
},
'import_menuitem': {
	'en': "Source Engine (.smd, .vta, .dmx, .qc)",
	'ru': "Движок Source (.smd, .vta, .dmx, .qc)",
	'es': "",
},
'exporter_err_nogroupitems': {
	'en': "Nothing in Group \"{0}\" is enabled for export",
	'es': "",
},
'exporter_report_qc': {
	'en': "{0} files exported and {2} QCs compiled ({3}/{4}) in {1} seconds",
	'ru': "Экспортировано файлов: {0}. Скомпилировано QC-файлов: {2} (движок {3}, мод {4}). Прошло секунд: {1};",
	'es': "",
},
'exporter_err_relativeunsaved': {
	'en': "Cannot export to a relative path until the blend file has been saved.",
	'ru': "Невозможно экспортировать по относительному пути, пока файл .blend не сохранён.",
	'es': "",
},
'exporter_err_nopolys': {
	'en': "Object {0} has no polygons, skipping",
	'ru': "Пропуск объекта {0}: нет геометрии",
	'es': "",
},
'exporter_err_arm_nonuniform': {
	'en': "Armature \"{0}\" has non-uniform scale. Mesh deformation in Source will differ from Blender.",
	'ru': "Скелет {0} масштабирован непропорционально. В движке Source скелет будет работать неправильно.",
	'es': "",
},
'exporter_err_facesnotex_ormat': {
	'en': "{0} faces on {1} did not have a Material or Texture assigned",
	'ru': "{0} полигонам на {1} не присвоен ни материал, ни текстура",
	'es': "",
},
'exporter_err_arm_noanims': {
	'en': "Couldn't find any animation for Armature \"{0}\"",
	'ru': "Нет анимации для скелета {0}",
	'es': "",
},
'exporter_err_dupeenv_arm': {
	'en': "Armature modifier \"{0}\" found on \"{1}\", which already has a bone parent or constraint. Ignoring.",
	'ru': "Пропуск модификатора \"Скелет\" ({0}) на объекте {1}: он уже имеет кость-родителя или ограничение",
	'es': "",
},
'exporter_err_bonelimit': {
	'en': "Exported {0} bones, but SMD only supports {1}!",
	'ru': "Экспортировано {0} костей, но SMD поддерживает только {1}!",
	'es': "",
},
'exporter_err_unmergable': {
	'en': "Skipping vertex animations on Group \"{0}\", which could not be merged into a single DMX object due to its envelope. To fix this, either ensure that the entire Group has the same bone parent or remove all envelopes.",
	'ru': "Пропуск вершинной анимации для группы «{0}», которую не удаётся слить в DMX-модель из-за огибающих. Проверьте, что у всей группы одна и та же кость-родитель или удалите все огибающие.",
	'es': "",
},
'exporter_warn_source2names': {
	'en': "Consider renaming \"{0}\": in Source 2, model names can contain only lower-case characters, digits, and/or underscores.",
},
'exporter_warn_unicode': {
	'ja': "{0}「{1}」の名前はUnicode文字を含みます。間違ってコンパイルすることが可能です。",
	'en': "Name of {0} \"{1}\" contains Unicode characters. This may not compile correctly!",
	'es': "",
},
'exporter_err_flexctrl_loadfail': {
	'en': "Could not load flex controllers. Python reports: {0}",
	'ru': "Загрузить контроллеры из указанного DMX-файла не удалось. Ошибка Python: {0}",
	'es': "",
},
'qc_compile_err_nofiles': {
	'en': "Cannot compile, no QCs provided. The Blender Source Tools do not generate QCs.",
	'ru': "Нет QC-файлов, нечего компилировать. Blender Source Tools не генерируют QC-файлы.",
	'es': "",
},
'exporter_err_missing_corrective_target': {
	'en': "Found corrective shape key \"{0}\", but not target shape \"{1}\"",
	'es': "",
},
'qc_compile_complete': {
	'ja': "{0}つ「{1}」QCがコンパイルしました",
	'en': "Compiled {0} {1} QCs",
	'ru': "Скомпилировано {0} QC для движка {1}.",
	'es': "",
},
'exporter_err_shapes_decimate': {
	'en': "Cannot export shape keys from \"{0}\" because it has a '{1}' Decimate modifier. Only Un-Subdivide mode is supported.",
	'ru': "Невзможно экспортировать ключи формы для {0}, потому что активен модификатор \"Аппроксимация\" в режиме {1}. Поддерживается только режим \"Снять подразделение\"",
	'es': "",
},
'exporterr_goldsrc_multiweights': {
	'en': "{0} verts on \"{1}\" have multiple weight links. GoldSrc does not support this!",
	'es': "",
},
'exporter_err_splitvgroup_undefined': {
	'en': "Object \"{0}\" uses Vertex Group stereo split, but does not define a Vertex Group to use.",
	'ru': "На объекте {0} задан режим стерео-разделения по группе вершин, но не задана группа вершин.",
	'es': "",
},
'exporter_err_open': {
	'en': "Could not create {0} file. Python reports: {1}.",
	'ru': "Не удалось создать файл {0}. Ошибка Python: {1}",
	'es': "",
},
'qc_compile_title': {
	'ja': "QCコンパイル",
	'en': "Compile QC",
	'ru': "Скомпилировать QC-файл",
	'es': "",
},
'exporter_err_noexportables': {
	'en': "Found no valid objects for export",
	'ru': "Не найдено подходящих для экспорта объектов",
	'es': "",
},
'exporter_warn_sanitised_filename': {
	'en': "Sanitised exportable name \"{0}\" to \"{1}\"",
	'es': "",
},
'exporter_warn_correctiveshape_duplicate': {
	'en': "Corrective shape key \"{0}\" has the same activation conditions ({1}) as \"{2}\". Skipping.",
	'es': "",
},
'exporter_err_flexctrl_missing': {
	'en': "No flex controller defined for shape {0}.",
	'ru': "Для ключа формы {0} не задано ни одного контроллера",
	'es': "",
},
'qc_compile_err_compiler': {
	'en': "Could not execute studiomdl from \"{0}\"",
	'ru': "Не удалось запустить studiomdl, проверьте путь: {1}",
	'es': "",
},
'exporter_err_facesnotex': {
	'en': "{0} faces on {1} did not have a Texture assigned",
	'ru': "Для {0} граней на объекте {1} не задана текстура",
	'es': "",
},
'exporter_err_flexctrl_undefined': {
	'en': "Could not find flex controllers for \"{0}\"",
	'ru': "Не удалось найти контроллеры лицевой анимации для объекта {0}",
	'es': "",
},
'exporter_warn_source2smdsupport': {
	'en': "Source 2 no longer supports SMD.",
	'es': "",
},
'exporter_tip': {
	'en': "Export and compile Source Engine models",
	'ru': "Экспортирует и компилирует модели для движка Source",
	'es': "",
},
'exporter_warn_weightlinks_culled': {
	'en': "{0} excess weight links beneath scene threshold of {1:0.2} culled on \"{2}\".",
	'ru': "На «{2}» удалено {0} излишних привязок к костям: предел веса, заданный для сцены, {1:0.2}",
	'es': "",
},
'exporter_prop_scene_tip': {
	'en': "Export all items selected in the Source Engine Exportables panel",
	'ru': "Экспортировать все объекты, заданные в панели \"Объекты для Source\"",
	'es': "",
},
'exporter_err_dmxenc': {
	'en': "DMX format \"Model {0}\" requires DMX encoding \"Binary 3\" or later",
	'ru': "Формат DMX-файла \"Model {0}\" требует структуру DMX-файла не более старую, чем \"Binary 3\".",
	'es': "",
},
'exporter_prop_group': {
	'ja': "グループの名前",
	'en': "Group Name",
	'ru': "Имя группы",
	'es': "",
},
'qc_compile_tip': {
	'en': "Compile QCs with the Source SDK",
	'ru': "Компилирует QC-файлы с помощью studiomdl",
	'es': "",
},
'exporter_report_suffix': {
	'en': " with {0} Errors and {1} Warnings",
	'ru': " ошибок: {0}, предупреждений: {1}.",
	'es': "",
},
'exporter_err_groupempty': {
	'en': "Group {0} has no active objects",
	'ru': "В группе {0} нет активных объектов",
	'es': "",
},
'exporter_err_dmxother': {
	'en': "Cannot export DMX. Resolve errors with the SOURCE ENGINE EXPORT panel in SCENE PROPERTIES.",
	'ru': "Невозможно экспортировать DMX-файлы. Проверьте панель \"Экспорт в Source\"",
	'es': "",
},
'exporter_prop_group_tip': {
	'ja': "エクスポートにグループの名前",
	'en': "Name of the Group to export",
	'ru': "Имя группы для экспорта",
	'es': "",
},
'exporter_warn_multiarmature': {
	'en': "Multiple armatures detected",
	'es': "",
},
'exporter_err_solidifyinside': {
	'en': "Curve {0} has the Solidify modifier with rim fill, but is still exporting polys on both sides.",
	'ru': "На кривой {0} включён модификатор Объёмность с заполнением обода, однако всё равно экспортируется двусторонняя геометрия",
	'es': "",
},
'exporter_err_dupeenv_con': {
	'en': "Bone constraint \"{0}\" found on \"{1}\", which already has a bone parent. Ignoring.",
	'ru': "Пропук ограничения кости {0}  на объекте {1}: для неё уже задана кость-родитель.",
	'es': "",
},
'exporter_err_unconfigured': {
	'en': "Scene unconfigured. See the SOURCE ENGINE EXPORT panel in SCENE PROPERTIES.",
	'ru': "Требуется скофигурировать сцену для экспорта в Source. Проверьте панель \"Экcпорт в Source\"",
	'es': "",
},
'exporter_err_makedirs': {
	'en': "Could not create export folder. Python reports: {0}",
	'ru': "Не удалось создать папку для экспорта. Ошибка Python: {0}",
	'es': "",
},
'exporter_warn_weightlinks_excess': {
	'en': "{0} verts on \"{1}\" have over {2} weight links. Source does not support this!",
	'ru': "На «{1}» {0} вершин имеют привязку к более {2} костей. Source не поддерживает такое коилчество привязок.",
	'es': "",
},
'exporter_err_noframes': {
	'en': "Armature {0} has no animation frames to export",
	'es': "",
},
'exporter_report_menu': {
	'ja': "レポート：Source Tools エラー",
	'en': "Source Tools Error Report",
	'ru': "Отчёт о ошибках Source Tools",
	'es': "",
},
'exporter_report': {
	'ja': "{0}つファイルは{1}秒エクスポート",
	'en': "{0} files exported in {1} seconds",
	'ru': "Файлов экспортировано: {0}. Прошло секунд: {1};",
	'es': "",
},
'exporter_err_groupmuted': {
	'ja': "ゲルーポ「{0}」はミュートです",
	'en': "Group {0} is suppressed",
	'ru': "Свойства группы {0} \"пересилены\"",
	'es': "",
},
'exporter_title': {
	'ja': "SMD/VTA/DMXをエクスポート",
	'en': "Export SMD/VTA/DMX",
	'ru': "Экспорт SMD/VTA/DMX",
	'es': "",
},
'qc_compile_err_unknown': {
	'en': "Compile of {0} failed. Check the console for details",
	'ru': "Не удалось скомпилировать QC-файл {0}. Ошибка описана в консоли",
	'es': "",
},
'exporter_err_splitvgroup_missing': {
	'en': "Could not find stereo split Vertex Group \"{0}\" on object \"{1}\"",
	'ru': "Не найдена группа веришн {0} для разделения на левую и правую части стерео-контроллеров на объекте {1}",
	'es': "",
},
'importer_complete': {
	'en': "Imported {0} files in {1} seconds",
	'ru': "Импортировано файлов: {0}. Прошло секунд: {1}.",
	'es': "",
},
'importer_bonemode': {
	'ja': "ボーンカスタムシェイプ",
	'en': "Bone shapes",
	'ru': "Отображение костей",
	'es': "",
},
'importer_err_nofile': {
	'ja': "選択ファイルはありません",
	'en': "No file selected",
	'ru': "Файл не выбран",
	'es': "",
},
'importer_err_smd': {
	'en': "Could not open SMD file \"{0}\": {1}",
	'ru': "Невозможно открыть файл {0}. Ошибка Python: {1}",
	'es': "",
},
'importer_qc_macroskip': {
	'en': "Skipping macro in QC {0}",
	'ru': "Пропуск QC-команды в файле {0}",
	'es': "",
},
'importer_bones_validate_desc': {
	'en': "Report new bones as missing without making any changes to the target Armature",
	'es': "",
},
'importer_tip': {
	'en': "Imports uncompiled Source Engine model data",
	'ru': "Импортирует промежуточные файлы Source",
	'es': "",
},
'importer_title': {
	'ja': "インポート SMD/VTA, DMX, QC",
	'en': "Import SMD/VTA, DMX, QC",
	'ru': "Импорт SMD/VTA, DMX, QC",
	'es': "",
},
'importer_makecamera': {
	'ja': "$originにカメラを生成",
	'en': "Make Camera At $origin",
	'ru': "Создать камеру по координатам, указанным в $origin",
	'es': "",
},
'importer_bone_parent_miss': {
	'en': "Parent mismatch for bone \"{0}\": \"{1}\" in Blender, \"{2}\" in {3}.",
	'ru': "Не совпадают родители у кости \"{0}\": \"{1}\" в Blender, \"{2}\" в файле \"{3}\".",
	'es': "",
},
'importer_makecamera_tip': {
	'en': "For use in viewmodel editing; if not set, an Empty will be created instead",
	'ru': "Помогает в редактировании v_model-ов. Если не задано, будет создан пустой объект",
	'es': "",
},
'importer_err_shapetarget': {
	'en': "Could not import shape keys: no valid target object found",
	'ru': "Невозможно импортировать ключи формы: не найден подходящий объект",
	'es': "",
},
'importer_rotmode_tip': {
	'en': "Determines the type of rotation Keyframes created when importing bones or animation",
	'ru': "Задаёт тип создаваемых при экспорте ключевых кадров с вращением",
	'es': "",
},
'importer_skipremdoubles_tip': {
	'en': "Import raw, disconnected polygons from SMD files; these are harder to edit but a closer match to the original mesh",
	'es': "",
},
'importer_balance_group': {
	'en': "DMX Stereo Balance",
	'ru': "Разделение стерео-контроллеров",
	'es': "",
},
'importer_bones_mode_desc': {
	'en': "How to behave when a reference mesh import introduces new bones to the target Armature (ignored for QCs)",
	'es': "",
},
'importer_rotmode': {
	'ja': "回転モード",
	'en': "Rotation mode",
	'ru': "Способ задания вращения",
	'es': "",
},
'importer_skipremdoubles': {
	'ja': "SMDのポリゴンと法線を保持",
	'en': "Preserve SMD Polygons & Normals",
	'es': "",
},
'importer_bonemode_tip': {
	'en': "How bones in new Armatures should be displayed",
	'ru': "Как будут выглядеть кости в импортированном скелете?",
	'es': "",
},
'importer_bones_append': {
	'ja': "対象で追加",
	'en': "Append to Target",
	'es': "",
},
'importer_err_qci': {
	'en': "Could not open QC $include file \"{0}\" - skipping!",
	'ru': "Пропуск файла \"{0}\" из команды $include: не удалсь открыть.",
	'es': "",
},
'importer_up_tip': {
	'en': "Which axis represents 'up' (ignored for QCs)",
	'ru': "Какая из осей соответствует направлению \"вврех\"?",
	'es': "",
},
'importer_err_namelength': {
	'en': "{0} name \"{1}\" is too long to import. Truncating to \"{2}\"",
	'es': "",
},
'importer_bones_append_desc': {
	'en': "Add new bones to the target Armature",
	'es': "",
},
'importer_err_unmatched_mesh': {
	'en': "{0} VTA vertices ({1}%) were not matched to a mesh vertex! An object with a vertex group has been created to show where the VTA file's vertices are.",
	'ru': "{0} вершин ({1}%) не удалось привязать к объекту при импорте VTA. Создан объект с группой вершин, показывающей, где заданные в VTA вершины.",
	'es': "",
},
'importer_bones_validate': {
	'ja': "対象で確認",
	'en': "Validate Against Target",
	'es': "",
},
'importer_name_nomat': {
	'ja': "UndefinedMaterial",
	'en': "UndefinedMaterial",
	'ru': "UndefinedMaterial",
	'es': "",
},
'importer_bones_newarm_desc': {
	'en': "Make a new Armature for this import",
	'es': "",
},
'importer_err_refanim': {
	'en': "Found animation in reference mesh \"{0}\", ignoring!",
	'ru': "Пропуск анимации в файле с позой по умолчанию (\"{0}\")",
	'es': "",
},
'importer_bones_mode': {
	'ja': "ボーンの追加がモード",
	'en': "Bone Append Mode",
	'es': "",
},
'importer_err_badweights': {
	'en': "{0} vertices weighted to invalid bones on {1}",
	'ru': "{0} вершин привязаны к неверным костям на объекте {1}",
	'es': "",
},
'importer_err_bonelimit_smd': {
	'en': "SMD only supports 128 bones!",
	'ru': "Движок SMD не поддерживает больше 128 костей!",
	'es': "",
},
'importer_err_badfile': {
	'en': "Format of {0} not recognised",
	'ru': "Не распознан формат файла \"{0}\"",
	'es': "",
},
'importer_err_smd_ver': {
	'en': "Unrecognised/invalid SMD file. Import will proceed, but may fail!",
	'ru': "Не удалось распознать SMD-файл. Импорт будет продолжен до первой ошибки.",
	'es': "",
},
'importer_doanims': {
	'ja': "アニメーションをインポート",
	'en': "Import Animations",
	'ru': "Импортировать анимации",
	'es': "",
},
'importer_use_collections':{
	'en': "Create Collections",
	'es': "",
},
'importer_use_collections_tip':{
	'en': "Create a Blender collection for each imported mesh file. This retains the original file structure (important for DMX) and makes it easy to switch between LODs etc. with the number keys",
	'es': "",
},
'importer_err_missingbones': {
	'en': "{0} contains {1} bones not present in {2}. Check the console for a list.",
	'ru': "{1} костей из {0} не найдены в {2}.",
	'es': "",
},
'importer_name_unmatchedvta': {
	'en': "Unmatched VTA",
	'ru': "Несопоставленные вершины VTA",
	'es': "",
},
'importer_bones_newarm': {
	'ja': "アーマティアを生成",
	'en': "Make New Armature",
	'es': "",
},
'qc_warn_noarmature': {
	'en': "Skipping {0}; no armature found.",
	'es': "",
},
'exportstate_pattern_tip': {
	'en': "Visible objects with this string in their name will be affected",
	'ru': "Будут обработаны видимые объекты, содержащие в своём названии эту строку",
	'es': "",
},
'exportstate': {
	'en': "Set Source Tools export state",
	'ru': "Задать состояние экспорта Source Tools",
	'es': "",
},
'activate_dep_shapes': {
	'en': "Activate Dependency Shapes",
	'ru': "Активировать зависимые ключи формы",
	'es': "",
},
'gen_block_success': {
	'en': "DMX written to text block \"{0}\"",
	'ru': "Настройки контроллеров лицевой анимации записаны в {0}",
	'es': "",
},
'gen_block': {
	'ja': "DMXフレックスのコントローラーの抜粋を生成します",
	'en': "Generate DMX Flex Controller block",
	'ru': "Сгенерировать настройки контроллеров лицевой анимации",
	'es': "",
},
'vca_add_tip': {
	'en': "Add a Vertex Animation to the active Source Tools exportable",
	'ru': "Добавить к текущему экспортируемому объекту Source Tools вершинную анимацию",
	'es': "",
},
'insert_uuid': {
	'en': "Insert UUID",
	'ru': "Вставить UUID",
	'es': "",
},
'launch_hlmv_tip': {
	'en': "Launches Half-Life Model Viewer",
	'ru': "Запускает просмотощик моделей Source, HLMV",
	'es': "",
},
'vertmap_remove': {
	'en': "Remove Source 2 Vertex Map",
	'es': "",
},
'activate_dep_shapes_tip': {
	'en': "Activates shapes found in the name of the current shape (underscore delimited)",
	'ru': "Активирует зависимые ключи формы  (ключи формы, которые можно найти в названии данного ключа, разделённые подчёркиванием)",
	'es': "",
},
'vca_qcgen_tip': {
	'en': "Copies a QC segment for this object's Vertex Animations to the clipboard",
	'ru': "Создать в буфере обмена фрагмент QC-файла для управления текущей вершинной анимацией",
	'es': "",
},
'vca_remove_tip': {
	'en': "Remove the active Vertex Animation from the active Source Tools exportable",
	'ru': "Удалить текущую вершинную анимацию с экспортируемого объекта Source Tools",
	'es': "",
},
'vca_add': {
	'en': "Add Vertex Animation",
	'ru': "Добавить вершинную анимацию",
	'es': "",
},
'vertmap_select': {
	'en': "Select Source 2 Vertex Map",
	'es': "",
},
'vca_preview': {
	'ja': "頂点アニメーションを再生します",
	'en': "Preview Vertex Animation",
	'ru': "Предпросмотр вершинной анимации",
	'es': "",
},
'activate_dep_shapes_success': {
	'en': "Activated {0} dependency shapes",
	'ru': "Активировано {0} зависимых ключей формы",
	'es': "",
},
'launch_hlmv': {
	'ja': "HLMVを開始",
	'en': "Launch HLMV",
	'ru': "Запустить HLMV",
	'es': "",
},
'exportstate_pattern': {
	'en': "Search pattern",
	'ru': "Маска поиска",
	'es': "",
},
'insert_uuid_tip': {
	'en': "Inserts a random UUID at the current location",
	'ru': "Вставить новый UUID",
	'es': "",
},
'gen_block_tip': {
	'en': "Generate a simple Flex Controller DMX block",
	'ru': "Генерирует простой блок контроллеров лицевой анимации, по контроллеру на один ключ формы",
	'es': "",
},
'gen_drivers': {
	'ja': "是正シェイプキーのドライバーを生成します",
	'en': "Generate Corrective Shape Key Drivers",
	'ru': "Создать драйверы для ключей форм коррекции",
	'es': "",
},
'apply_drivers':{
	'en': "Regenerate Shape Key Names From Drivers",
	'es': "",
},
'apply_drivers_tip':{
	'en': "Renames corrective shape keys so that each their names are a combination of the shape keys that control them (via Blender animation drivers)",
	'es': "",
},
'apply_drivers_success':{
	'en': "{0} shapes renamed.",
	'es': "",
},
'vca_qcgen': {
	'ja': "QCの抜粋を生成します",
	'en': "Generate QC Segment",
	'ru': "Создать фрагмент QC-файла",
	'es': "",
},
'vertmap_create': {
	'en': "Create Source 2 Vertex Map",
	'es': "",
},
'vca_preview_tip': {
	'en': "Plays the active Source Tools Vertex Animation using scene preview settings",
	'ru': "Проигрывает текущую вершинную анимацию для предпросмотра",
	'es': "",
},
'vca_remove': {
	'en': "Remove Vertex Animation",
	'ru': "Удалить текущую вершинную анимацию с экспортируемого объекта Source Tools",
	'es': "",
},
'gen_drivers_tip': {
	'en': "Adds Blender animation drivers to corrective Source engine shapes",
	'ru': "Создаёт драйверы для ключей форм коррекции, использующихся в Source",
	'es': "",
},
'qc_path': {
	'ja': "QCのパス",
	'en': "QC Path",
	'ru': "Путь до QC-файлов",
	'es': "",
},
'engine_path': {
	'ja': "エンジンのパス",
	'en': "Engine Path",
	'ru': "Путь до папки bin движка",
	'es': "",
},
'game_path_tip': {
	'en': "Directory containing gameinfo.txt (if unset, the system VPROJECT will be used)",
	'ru': "Путь до мода (где gameinfo.txt). Если не задано, то будет использована переменная среды VPROJECT",
	'es': "",
},
'visible_only': {
	'ja': "たった可視のレイヤー",
	'en': "Visible layers only",
	'ru': "Только видимые слои",
	'es': "",
},
'dmx_encoding': {
	'ja': "DMXの符号化",
	'en': "DMX encoding",
	'ru': "Способ кодирования DMX-файла",
	'es': "",
},
'game_path': {
	'ja': "ゲームのパス",
	'en': "Game Path",
	'ru': "Путь до мода",
	'es': "",
},
'up_axis': {
	'ja': "対象の上昇軸",
	'en': "Target Up Axis",
	'ru': "Направление \"Вверх\"",
	'es': "",
},
'dmx_format': {
	'ja': "DMXのフォーマット",
	'en': "DMX format",
	'ru': "Формат DMX-файла",
	'es': "",
},
'ignore_materials': {
	'ja': "Blenderのマテリアルを軽視",
	'en': "Ignore Blender Materials",
	'ru': "Игнорировать материалы Blender",
	'es': "",
},
'visible_only_tip': {
	'en': "Ignore objects in hidden layers",
	'ru': "Не экспортировать объекты, расположенные на выключенных слоях",
	'es': "",
},
'active_exportable': {
	'ja': "アクティブ・エクスポート可能",
	'en': "Active exportable",
	'ru': "Активный объект для экспорта",
	'es': "",
},
'exportroot_tip': {
	'en': "The root folder into which SMD and DMX exports from this scene are written",
	'ru': "Папка, куда будут экспортироваться SMD и DMX из текущей сцены",
	'es': "",
},
'qc_compilenow': {
	'ja': "今全てはコンパイル",
	'en': "Compile All Now",
	'ru': "Скомпилировать все QC",
	'es': "",
},
'up_axis_tip': {
	'en': "Use for compatibility with data from other 3D tools",
	'ru': "Используется для совместимости с экспортами из Maya и других 3D-пакетов",
	'es': "",
},
'smd_format': {
	'ja': "対象のエンジン",
	'en': "Target Engine",
	'ru': "мишень движка",
	'es': "",
},
'dmx_mat_path_tip': {
	'en': "Folder relative to game root containing VMTs referenced in this scene (DMX only)",
	'ru': "Путь (относительно мода), содержащий VMT-файлы для этой модели (аналог $cdmaterials; только для DMX-файлов)",
	'es': "",
},
'qc_compileall_tip': {
	'en': "Compile all QC files whenever anything is exported",
	'ru': "Компилировать все указанные QC-файлы сразу после экспорта",
	'es': "",
},
'qc_path_tip': {
	'en': "This scene's QC file(s); Unix wildcards supported",
	'ru': "QC-файлы, связанные с этой сценой; поддерживаются маски для имён файлов",
	'es': "",
},
'qc_nogamepath': {
	'en': "No Game Path and invalid VPROJECT",
	'ru': "Не указан путь до мода; переменная VPROJECT содержит ошибочные данные",
	'es': "",
},
'dmx_mat_path': {
	'ja': "マテリアルのパス",
	'en': "Material Path",
	'ru': "Путь до материалов",
	'es': "",
},
'exportroot': {
	'ja': "エクスポートのパス",
	'en': "Export Path",
	'ru': "Куда экспортировать",
	'es': "",
},
'export_format': {
	'ja': "エクスポートのフォーマット",
	'en': "Export Format",
	'ru': "Формат файла экспорта",
	'es': "",
},
'qc_compileall': {
	'ja': "エクスポートから、みんあがコンパイル",
	'en': "Compile all on export",
	'ru': "Компилировать QC-файлы после экспорта",
	'es': "",
},
'dmx_weightlinkcull': {
	'ja': "ウェイト・リンクの間引きのしきい値",
	'en': "Weight Link Cull Threshold",
	'ru': "Порог веса привязки вершины к кости",
	'es': "",
},
'dmx_weightlinkcull_tip': {
	'en': "The maximum strength at which a weight link can be removed to comply with Source's per-vertex link limit.",
	'ru': "Если вершина связана с некоторой костью, и её вес меньше здесь указанного, то связь с этой костью будет удалена при экспорте, чтобы вписаться в ограничение движка Source. («Source не поддерживает такое количество привязок»)",
	'es': "",
},
'dmx_encoding_tip': {
	'en': "Manual override for binary DMX encoding version",
	'ru': "Версия структуры DMX-файла",
	'es': "",
},
'dmx_format_tip': {
	'en': "Manual override for DMX model format version",
	'ru': "Версия формата модели (DMX-файл)",
	'es': "",
},
'engine_path_tip': {
	'en': "Directory containing studiomdl (Source 1) or resourcecompiler (Source 2)",
	'ru': "Путь до папки с studiomdl (Source 1) или resourcecompiler (Source 2)",
	'es': "",
},
'ignore_materials_tip': {
	'en': "Only export face-assigned image filenames",
	'ru': "Называть материалы в экспортированной модели по именам текстур, а не Blender-материалов",
	'es': "",
},
'updater_title': {
	'ja': "更新Source Toolsの確認",
	'en': "Check for Source Tools updates",
	'ru': "Проверить обновления Source Tools",
	'es': "",
},
'update_err_downloadfailed': {
	'en': "Could not complete download:",
	'ru': "Не удалось завершить загрузку обновления",
	'es': "No se pudo completar la descarga:",
},
'offerchangelog_offer': {
	'en': "Restart Blender to complete the update. Click to view the changelog.",
	'ru': "Перезапустите Blender для завершения обновления. Нажмите для просмотра списка изменений.",
	'es': "Reinicie blender para completar la actualización. Haga clic para ver los cambios de versión",
},
'update_err_outdated': {
	'en': "The latest Source Tools require Blender {0}. Please upgrade.",
	'ru': "Текущая версия Source Tools требует Blender {0}. Пожалуйста, обновитесь.",
	'es': "La ultima version de Source Tools requiere blender {0}. Por favor actualice a esa version",
},
'update_err_unknown': {
	'en': "Could not install update:",
	'ru': "Невозможно обновить Source Tools: ",
	'es': "No se pudo instalar la actualización:",
},
'offerchangelog_title': {
	'en': "Source Tools Update",
	'ru': "Обновление Source Tools",
	'es': "Actualización de Source Tools",
},
'update_err_corruption': {
	'en': "Update was downloaded, but file was not valid",
	'ru': "Не удалось обновиться: файлы обновления повреждены",
	'es': "La actualizacion se ha descargado, pero el archivo no era valido",
},
'update_done': {
	'en': "Installed Source Tools {0}!",
	'ru': "Обновлено до Source Tools {0}!",
	'es': "¡Soutce Tools {0} instalado!",
},
'updater_title_tip': {
	'en': "Connects to http://steamreview.org/BlenderSourceTools/latest.php",
	'ru': "Смотрит обновления на http://steamreview.org/BlenderSourceTools/latest.php",
	'es': "",
},
'update_alreadylatest': {
	'en': "The latest Source Tools ({0}) are already installed.",
	'ru': "Уже установлена самая последняя версия Blender Source Tools ({0}).",
	'es': "",
},
}

def _get_ids():	
	ids = {}
	for id,values in _data.items():
		ids[id] = values['en']
	return ids
ids = _get_ids()

def _get_translations():
	import collections
	translations = collections.defaultdict(dict)
	for lang in _languages:
		for id,values in _data.items():
			value = values.get(lang)
			if value: translations[lang][(None, ids[id])] = value
	return translations
translations = _get_translations()
