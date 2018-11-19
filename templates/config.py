"""
Define substitutions dict here with all defined variables for the templates.
Notes:
    • The value after  # was the standard value.
    • Pixel sizes are related to input resolution.
    • Currently, most <textwidth>-Tags will not be scaled. The factor
      GlobalFontScaling would be a good basis if you want change that.
"""
substitutions = {
    "W": 1280,
    "H": 720,

    # Font scaling is uncoupled from resolution scaling.
    # "GlobalFontScaling": 0.75, # Normal sized font at 720x480
    "GlobalFontScaling": 1.0,  # Big font at 720x480
    # "GlobalFontScaling": 1.1, # Font fits still in most labels.

    # Factor for VT323 font type.
    "VT323FontScaling": 1.2,

    # Horizontal HomeMenu dimensions
    "HomeMenuItemWidth": 400,  # 300

    # HomeSubMenu width
    "HomeSubMenuWidth": 250,  # 180

    # Home controls menu
    "HomeControlPanelExtraWidth": 400,  # 0
    "HomeSearchWidth": 230,  # 145
    "HomeFullscreenWidth": 265,  # 145
    "HomeControlIconWidth": 45,  # 30

    # File meta data at home screen
    "AlbumLabelOffsetY": -0,  # 0
    "BackgroundForInfoHeight": 154,

    # Give desciption text space for two extra lines
    "SettingDescExtraHeight": 80,  # 0
    "SettingPanelExtraWidthL": 45,  # 0
    "SettingPanelExtraWidthR": 145,  # 0
    "SettingProfileExtraWidth": 260,  # 0
    "SideBladeExtraWidth": 300,  # 0

    "WeatherLeftExtraW": 100,  # 0
    "WeatherLeftExtraW2": 60,  # 0
    "WeatherListExtraH": 26,  # 0, increases width between Wind and Sunset
    "WeatherListExtraGap": 2,  # 0
    "WeatherRightExtraW": 30,  # 0
    "WeatherItemExtraHeight": 15,  # 0
    "DialogButtonExtraWidth": 170,  # 0

    "LogoScale": 2,  # 1
    "FavoritesBladeWidth": 650,  # 400

    # 1+16 Cols. Shift width = 1+4 Cols
    "VirtualKeyboardWidth": 17*60+50,  # 860
    "VirtualKeyboardKeyWidth": 60,  # 50
    "VirtualNumpadWidth": 450,  # 380

    "OSDBookmarksWidth": 1000,  # 800
    "OSDBookmarksItemHeight": 238,  # 215
    "OSDSettingsWidth": 1000,  # 800
    "OSDSeekSliderWidth": 670,  # 720
    "OSDSubtitleMenuWidth": 356,  # 256

    # Dimensions of Seek bar region
    "DialogSeekBarWidth": 390,  # 370
    "DialogSeekBarHeight": 90,  # 70
    # The bar length
    "DialogSeekBarWidth2": 340,  # 240

    "DialogBusyWidth": 300,  # 200
    "DialogNotificationExtraWidth": 200,  # 0

    "DialogPVRExtraWidth": 200,  # 0
    "DialogPVRExtraHeight": 34,  # 0
    "DialogPVRItemExtraHeight": 40,  # 0

    "DialogSliderExtraWidth": 300,  # 0 Used in DialogSlider
    "DialogSettingsExtraHeight": 200,  # 0 Used in DialogSettings

    "FullScreenExtraHeight": 44,  # 0
    "FullScreenExtraWidth": 32,  # 0
    "FullScreenExtraIconDim": 10,  # 0

    "MyPVRChannelsLeftExtraWidth": 100,  # 0
    "MyPVRChannelsLeftItemHeight": 80,  # ?
    "MyPVRChannelsPreviewHeight": 300,  # 400
    "MyPVRChannelsRightExtraHeight": 54,  # 0

    # Higher desciption box
    "DialogPVRGuideInfoExtraHeight": 150,  # 0
    "ThumbnailViewItemExtraWidth": 150,
    "ThumbnailViewItemExtraHeight": 0,  # -100,  # Smaller icons
    "ThumbnailViewItemColumns": 3,

    "MusicVisualisationExtraHeight": 75,
    }

substitutions["OSDBookmarksItemWidth"] = int(
    (substitutions["OSDBookmarksWidth"] - 2*40)/3)

substitutions["DialogExtraWidth"] =\
    substitutions.get("SettingPanelExtraWidthL", 0) +\
    substitutions.get("SettingPanelExtraWidthR", 0) +\
    140
substitutions["DialogExtraWidthL"] =\
    substitutions.get("SettingPanelExtraWidthL", 0) +\
    30
substitutions["DialogExtraWidthR"] =\
    substitutions.get("SettingPanelExtraWidthR", 0) +\
    110

# Finally, extend by other dicts here
map(lambda x: substitutions.update(x), [])
