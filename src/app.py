import dearpygui.dearpygui as dpg



dpg.create_context()

# loading the logo image
width, height, channels, data = dpg.load_image("starter_files/logo_spamFilter.png")

# added tag to help identify this is the primary window
with dpg.window(label="Simple SMS Spam Filter", tag="Primary Window") as win1:
    dpg.add_text("Hello, world")

    with dpg.texture_registry(show=True):
        dpg.add_static_texture(width, height, data, tag="texture_tag")

    with dpg.window(label="Tutorial"):
        dpg.add_image("texture_tag")


# dpg.show_style_editor()
dpg.create_viewport(title="Simple SMS Spam Filter", width=540, height=720)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()