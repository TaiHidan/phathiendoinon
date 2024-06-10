
import streamlit as st 
from main import MultiApp


def app():
  
    
    
  
    st.markdown('# Đồ Án Môn : Phát Hiện Người đội nón bảo hiểm bằng CNN')
    st.markdown("----")

    
    st.subheader("Về chún tôi")
    st.write("Huỳnh Minh Thắng - 2001216159")
    st.write(" Ngụy Hữu Tài - 2001216121")
    st.write(" Phạm Hữu Anh Quân - 2001216082")
    


    st.write("Thực nghiệm chỉ mang tính chất thực nghiệm không áp dụng vào thực tế")

    col1, col2 ,col3 = st.columns([55,1,55]) 
    
    
    
    with col3:
        st.image("1.jpeg", caption='Template Matching using SQDIFF', use_column_width=True)
        

    with col1:
        st.image("3.jpeg", caption='Helmet Feature Matching with SIFT features using FLANN based matcher', use_column_width=True)

        
