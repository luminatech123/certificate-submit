import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Title of the app
st.title("Cyber Security Internship Certificate Generator")

# User input for name
name = st.text_input("Enter your name:")

# Load the uploaded certificate image
uploaded_image_path = "luminatechz.png"  # This should be the path of the uploaded image
certificate_image = Image.open(uploaded_image_path)

# Check if the user has entered a name
if name:
    # Create a drawing context
    draw = ImageDraw.Draw(certificate_image)

    # Set the font (ensure you have the font file in your working directory or use a built-in font)
    font_path = "arial.ttf"  # Replace with the path to your font file
    try:
        name_font = ImageFont.truetype(font_path, 90)  # Font size can be adjusted
        intern_font = ImageFont.truetype(font_path, 90)
    except IOError:
        st.error("Font file not found. Please ensure 'arial.ttf' or your desired font is available.")
        name_font = ImageFont.load_default()
        intern_font = ImageFont.load_default()

    # Coordinates for the name and "Cyber Security Intern" text (adjust as needed)
    name_position = (350, 550)  # Adjust the X, Y coordinates for proper placement
    intern_position = (550, 850)  # Adjust the X, Y coordinates for proper placement

    # Draw the name in yellow
    draw.text(name_position, name, fill="yellow", font=name_font)

    # Draw "Cyber Security Intern" in yellow
    draw.text(intern_position, "Cyber Security Intern", fill="yellow", font=intern_font)

    # Display the image in Streamlit
    st.image(certificate_image, caption="Generated Certificate", use_column_width=True)

    # Option to download the modified certificate
    certificate_image.save("certificate_generated.png")
    with open("certificate_generated.png", "rb") as file:
        st.download_button(
            label="Download Certificate",
            data=file,
            file_name="certificate_generated.png",
            mime="image/png"
        )
else:
    st.write("Please enter your name to generate the certificate.")
