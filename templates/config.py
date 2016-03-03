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

    "WeatherLeftExtraW": 170,  # 0
    "WeatherRightExtraW": 30,  # 0
    "DialogButtonExtraWidth": 170,  # 0

    "LogoScale": 2,  # 1
    "FavoritesBladeWidth": 650,  # 400

    # 1+16 Cols. Shift width = 1+4 Cols
    "VirtualKeyboardWidth": 17*62+50,  # 860
    "VirtualKeyboardKeyWidth": 62,  # 50
    "VirtualNumpadWidth": 450,  # ?

    "OSDBookmarksWidth": 1000,  # 800
    "OSDBookmarksItemHeight": 245,  # 215
    "OSDSettingsWidth": 1000,  # 800
    "OSDSeekSliderWidth": 720,  # 720
    "OSDSubtitleMenuWidth": 356,  # 256
}

substitutions["OSDBookmarksItemWidth"] = int(
    (substitutions["OSDBookmarksWidth"] - 2*40)/3)


# Finally, extend by other dicts here
map(lambda x: substitutions.update(x), [])
