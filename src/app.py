import dearpygui.dearpygui as dpg
import string
import nltk

from helper.functions import categorize_words, pre_process, predict
nltk.download('punkt')
nltk.download('stopwords')

# dearpygui expects these two args for callbacks
def check_spam(sender, data, pred=[]):
    # clear all previous instances of result related widgets
    try:
        dpg.delete_item("result_spacer_1")
        dpg.delete_item("result_separator")
        dpg.delete_item("result_spacer_2")
        dpg.delete_item("result_text")
    except Exception as e:
        # within try catch for first click incase these do not exist
        print(e)

    # get input value from the input text widget
    input_value = dpg.get_value('Input')
    
    # some spacing and separator
    dpg.add_spacing(count=6, parent="Primary Window", tag="result_spacer_1")
    dpg.add_separator(parent="Primary Window", tag="result_separator")
    dpg.add_spacing(count=6, parent="Primary Window", tag="result_spacer_2")
    
    # preprocess input string
    pre_processed_input_value = pre_process(input_value)
    
    # get predictions
    pred_text, pred_color = predict(pre_processed_input_value)
    
    # display predictions
    dpg.add_text(pred_text, color=pred_color, parent="Primary Window", tag="result_text")
    


dpg.create_context()

# loading the logo image
width, height, channels, data = dpg.load_image("logo_spamFilter.png")

# added tag to help identify this is the primary window
with dpg.window(label="Simple SMS Spam Filter", tag="Primary Window"):

    # displaying the image at the top
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width, height, data, tag="texture_tag")

    # adding the image to the tag
    dpg.add_image("texture_tag", indent=30)
    dpg.add_separator(label="separator")
    dpg.add_spacing(count=12)
    
    # instructions
    dpg.add_text("Please enter an SMS message of your choice to check if it's spam or not", color=[232, 163, 33])
    dpg.add_spacing(count=6)

    # add input text
    dpg.add_input_text(tag="Input", label="Input", width=415, default_value="Type Message Here!")
    dpg.add_spacing(count=6)
    dpg.add_button(label="Check", callback=check_spam)

    

dpg.create_viewport(title="Simple SMS Spam Filter", width=540, height=720)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()