import streamlit as st
import cv2
import numpy as np
from keras.models import load_model


def app():
    

    # Load the trained CNN model
    def load_cnn_model(model_path):
        try:
            model = load_model(model_path)
            return model
        except Exception as e:
            st.write("Error loading the model:", str(e))
            return None
        

    # Preprocess Function
    def preprocess_image(image):
        try:
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (128, 128))
            img = img / 255.0  # Normalize the image
            img = np.expand_dims(img, axis=0)  # Add a batch dimension
            return img
        except Exception as e:
            st.write("Error processing image:", str(e))
            return None

    def predict(model, image):
        if model is None:
            return None

        try:
            
            prediction = model.predict(image)
        
            
            return prediction
        except Exception as e:
            st.write("Error predicting:", str(e))
            return None

           
    
    st.title("Phát hiện mũ bảo hiểm with CNN")
    st.write("Tải hỉnh ảnh lên để check.")

    uploaded_file = st.file_uploader("Chọn ảnh..", type=["jpg", "png", "jpeg"])

    
    model_path = 'helmet_detection_model.h5'  # model
    if 'model' not in st.session_state:
        st.session_state.model = load_cnn_model(model_path)

    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)

        if image is not None:
            st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Đã tải ảnh lên.", use_column_width=True)

            if st.button("Xỷ lý"):
                preprocessed_image = preprocess_image(image)
                if preprocessed_image is not None:

                    prediction = predict(st.session_state.model, preprocessed_image)
                    if prediction is not None:
                        if prediction < 0.5:
                            st.write("Phát hiện : Có nón bảo hiểm.")
                        else:
                            st.write("Phát hiện : Không có nón bảo hiểm.")
                    else:
                        st.write("Lỗi khi phát hiện phân tích.")
                else:
                    st.write("Lỗi khi tải ảnh.")
        else:
            st.write("Error: Unable to read the image. Please upload a valid image.")
    