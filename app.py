import os
import re
import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# IBM watsonx.ai
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

load_dotenv()


st.set_page_config(
    page_title="EduSimplify AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .stButton button {
        border-radius: 8px;
        font-weight: 600;
    }

    div[data-baseweb="select"] > div {
        border-radius: 8px;
    }

    textarea {
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)


WATSONX_APIKEY = os.getenv("WATSONX_APIKEY")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")

WATSONX_URL = os.getenv(
    "WATSONX_URL",
    "https://us-south.ml.cloud.ibm.com"
)



st.title("🎓 EduSimplify AI")

st.caption(
    "Transform complex academic content into personalized, "
    "accessible learning material."
)


if not WATSONX_APIKEY or not WATSONX_PROJECT_ID:

    st.warning(
        "⚠️ IBM watsonx.ai credentials are not configured. "
        "Please add WATSONX_APIKEY and WATSONX_PROJECT_ID "
        "to your .env file."
    )


with st.sidebar:

    st.header("Learning Preferences")

    learning_level = st.selectbox(
        "Target Level",
        ["Beginner", "Intermediate", "Advanced"],
        help="Adjusts the technical depth of the generated breakdown."
    )

    language = st.selectbox(
        "Output Language",
        ["English", "Kannada", "Hindi", "Tamil", "Telugu"],
        help=(
            "Translates explanations while preserving "
            "key technical terminology."
        )
    )

    output_style = st.selectbox(
        "Explanation Format",
        [
            "Simple and Clear",
            "Detailed",
            "Exam Preparation"
        ],
        help="Changes the focus and structure of the output material."
    )

    st.divider()

    st.markdown("""
    **How it works**

    1. Provide text or upload a syllabus/notes PDF.
    2. Choose your preferred depth and language.
    3. Generate tailored breakdowns, analogies, and quizzes.
    """)

def extract_pdf_text(uploaded_file):

    try:

        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:

        return f"PDF extraction error: {str(e)}"

def create_prompt(
    content,
    level,
    language,
    style
):

    return f"""
You are EduSimplify AI, an intelligent academic learning assistant.

Transform the following complex academic content into
personalized educational material.

STUDENT LEARNING LEVEL:
{level}

OUTPUT LANGUAGE:
{language}

EXPLANATION STYLE:
{style}

ACADEMIC CONTENT:
{content}

INSTRUCTIONS:

1. Preserve original technical accuracy without inventing facts.
2. Adapt complexity to match the specified learning level.
3. Explain concepts clearly and logically.
4. Use appropriate real-world examples.
5. If the target language is not English, explain concepts
   in that language while retaining critical technical terms.
6. Make the content useful for academic learning and revision.

Produce the output strictly in the following sections
using clear Markdown headers:

## 1. Simple Explanation

## 2. Real-World Analogy

## 3. Key Concepts

## 4. Important Terminology

## 5. Practical Example

## 6. Exam Points

## 7. Quick Revision

## 8. Quiz (5 MCQs with answers)

## 9. One-Line Summary
"""


def generate_content(content):

    if not WATSONX_APIKEY or not WATSONX_PROJECT_ID:

        return None

    try:

        credentials = Credentials(
            url=WATSONX_URL,
            api_key=WATSONX_APIKEY
        )

        model = ModelInference(
            model_id="ibm/granite-4-h-small",
            credentials=credentials,
            project_id=WATSONX_PROJECT_ID,
            params={
                GenParams.MAX_NEW_TOKENS: 1800,
                GenParams.MIN_NEW_TOKENS: 1,
                GenParams.TEMPERATURE: 0.2,
                GenParams.REPETITION_PENALTY: 1.05
            }
        )

        prompt = create_prompt(
            content,
            learning_level,
            language,
            output_style
        )

        response = model.generate_text(
            prompt=prompt
        )

        return response

    except Exception as e:

        st.error(
            f"IBM Granite generation failed: {str(e)}"
        )

        return None


st.subheader("Source Material")

input_method = st.radio(
    "Choose input method",
    ["Paste Text", "Upload PDF"],
    horizontal=True,
    label_visibility="collapsed"
)

content = ""


if input_method == "Paste Text":

    content = st.text_area(
        "Paste your notes or textbook excerpt below:",
        height=220,
        placeholder=(
            "Example: TCP is a connection-oriented protocol "
            "used for reliable communication..."
        )
    )
else:

    uploaded_file = st.file_uploader(
        "Upload an academic PDF document",
        type=["pdf"]
    )

    if uploaded_file:

        with st.spinner(
            "Extracting text from PDF..."
        ):

            content = extract_pdf_text(
                uploaded_file
            )

        if (
            content
            and not content.startswith(
                "PDF extraction error"
            )
        ):

            st.success(
                f"Successfully loaded PDF "
                f"({len(content):,} characters extracted)."
            )

            with st.expander(
                "Preview raw extracted text"
            ):

                st.write(
                    content[:3000]
                    + (
                        "..."
                        if len(content) > 3000
                        else ""
                    )
                )

        elif content.startswith(
            "PDF extraction error"
        ):

            st.error(content)


if content and len(content) > 15000:

    st.warning(
        "Content exceeds 15,000 characters. "
        "Automatically truncating to the first "
        "15,000 characters."
    )

    content = content[:15000]

st.markdown("")

if st.button(
    "🚀 Simplify Course Content",
    type="primary",
    use_container_width=True
):

    if not content.strip():

        st.error(
            "Please provide academic content via text input "
            "or PDF upload before generating."
        )

    elif not WATSONX_APIKEY:

        st.error(
            "Missing IBM watsonx.ai API key. "
            "Configure WATSONX_APIKEY in your .env file."
        )

    elif not WATSONX_PROJECT_ID:

        st.error(
            "Missing IBM watsonx.ai Project ID. "
            "Configure WATSONX_PROJECT_ID in your .env file."
        )

    else:

        progress_bar = st.progress(0)

        status_text = st.empty()

        status_text.write(
            "Analyzing academic content structure..."
        )

        progress_bar.progress(30)

        status_text.write(
            f"Tailoring material for "
            f"{learning_level} level in {language}..."
        )

        progress_bar.progress(60)

        status_text.write(
            "Generating material using IBM Granite..."
        )

        result = generate_content(
            content
        )

        progress_bar.progress(90)

        if result:

            status_text.write(
                "Generation complete."
            )

            progress_bar.progress(100)

            st.divider()

            st.subheader(
                "✨ Personalized Learning Material"
            )

            st.markdown(result)

            st.divider()

            st.download_button(
                label="📥 Download Structured Notes",
                data=result,
                file_name="EduSimplify_Notes.md",
                mime="text/markdown",
                use_container_width=True
            )
st.divider()

st.caption(
    "EduSimplify AI — Built for cleaner, focused learning."
)