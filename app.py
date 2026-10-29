import streamlit as st
from pypdf import PdfReader
from urllib.parse import quote_plus

st.set_page_config(
    page_title="مساعد الطلاب",
    page_icon="📚"
)

st.title("مساعد الطلاب")
st.write("ارفع ملف PDF للعثور على شروحات مرتبطة به.")

pdf_file = st.file_uploader(
    "اختر ملف PDF",
    type=["pdf"]
)

if pdf_file is not None:
    reader = PdfReader(pdf_file)
    pages_text = []

    for page in reader.pages:
        pages_text.append(page.extract_text() or "")

    text = "\n".join(pages_text)

    st.success("تم فتح ملف PDF بنجاح!")
    st.write(f"عدد الصفحات: {len(reader.pages)}")

    with st.expander("عرض النص المستخرج من الملف"):
        st.text(text[:10000])

    topic = st.text_input(
        "اكتب اسم الدرس الذي تريد شرحه"
    )

    if topic:
        query = quote_plus(topic)

        st.subheader("ابحث عن شرح الدرس")

        st.link_button(
            "البحث في YouTube",
            "https://www.youtube.com/results?search_query=" + query
        )

        st.link_button(
            "البحث في Google",
            "https://www.google.com/search?q=" + query
        )

        st.info(
            "افتح نتائج البحث واختر الشرح المناسب لدرسك."
        )