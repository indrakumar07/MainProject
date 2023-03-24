import streamlit as st
import display

# st.image('Images/head.gif')
st.markdown("<h1 style='text-align: left; color: green;'>Segmentation of organs",
            unsafe_allow_html=True)
dataset = st.selectbox(' Select Data Class:',
                       ("LUNG", "RETINA", "BRAIN", "LIVER","POLYP"))

if dataset == 'LUNG':
    st.markdown("<h1 style='text-align: left; color: green;'>"+dataset+"</h1>",
                unsafe_allow_html=True)
    img = st.file_uploader("Choose a "+dataset +
                           " image file", type=["jpg", "png"])
    if img is not None:
        display.disp_png_jpg(img, dataset)

elif dataset == 'LIVER':
    st.markdown("<h1 style='text-align: left; color: green;'>"+dataset+"</h1>",
                unsafe_allow_html=True)
    img = st.text_input("Enter location for LIVER file(eg:liver.nii)")
    store = st.text_input("Enter location to save:")
    displaynii = st.text_input("Enter NII File Location:")
    if img and store:
        x = st.button("Start-Segmentation")
        if x:
            display.disp_nii(img, store)
            x = False
    if displaynii:
        dispb = st.button("Visualize")
        if dispb:
            display.visualize(displaynii)
            dispb = False

elif dataset == 'RETINA':
    st.markdown("<h1 style='text-align: left; color: green;'>"+dataset+"</h1>",
                unsafe_allow_html=True)
    img = st.file_uploader("Choose a "+dataset +
                           " image file", type=["jpg", "png"])
    if img is not None:
        display.disp_png_jpg(img, dataset)

elif dataset == 'POLYP':
    st.markdown("<h1 style='text-align: left; color: green;'>"+dataset+"</h1>",
                unsafe_allow_html=True)
    img = st.file_uploader("Choose a "+dataset +
                           " image file", type=["tif"])
    if img is not None:
        display.disp_tif(img)

else:
    st.markdown("<h1 style='text-align: left; color: green;'>"+dataset+"</h1>",
                unsafe_allow_html=True)
    img = st.file_uploader("Choose a "+dataset +
                           " image file", type=["jpg", "png"])
    if img is not None:
        display.disp_png_jpg(img, dataset)

st.markdown(
    "<style> footer {visibility: hidden;}</style>", unsafe_allow_html=True)
