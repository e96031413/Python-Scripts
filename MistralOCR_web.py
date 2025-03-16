import json
import os
from typing import Any, Dict, Optional

import requests
import streamlit as st

# Page configuration - removed "wide" layout to make it narrower
st.set_page_config(page_title="PDF to Markdown Converter", page_icon="📄")

# Custom CSS to make the app narrower
st.markdown(
    """
<style>
    .main .block-container {
        max-width: 700px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        margin: 0 auto;
    }
</style>
""",
    unsafe_allow_html=True,
)

# JavaScript to store API key in browser's local storage
js_code = """
<script>
// Local storage key
const API_KEY_STORAGE_KEY = "mistral_ocr_api_key";

// Load API key from local storage
document.addEventListener("DOMContentLoaded", function() {
    const apiKey = localStorage.getItem(API_KEY_STORAGE_KEY);
    if (apiKey) {
        // Give Streamlit time to initialize
        setTimeout(() => {
            const inputElem = document.querySelector('input[aria-label="API Key"]');
            if (inputElem) {
                inputElem.value = apiKey;
                // Trigger an input event to update Streamlit state
                inputElem.dispatchEvent(new Event('input', { bubbles: true }));
            }
        }, 500);
    }
});

// Function to save API key
window.saveApiKey = function(key) {
    if (key) {
        localStorage.setItem(API_KEY_STORAGE_KEY, key);
        return true;
    }
    return false;
}
</script>
"""


def test_api_availability(api_key: str) -> bool:
    """Test if the Mistral API is available and the API key is valid."""
    url = "https://api.mistral.ai/v1/models"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except Exception:
        return False


def upload_file_to_mistral(file_data: bytes, file_name: str, api_key: str) -> Optional[Dict[str, Any]]:
    """Upload a file to Mistral's servers."""
    url = "https://api.mistral.ai/v1/files"
    headers = {"Authorization": f"Bearer {api_key}"}

    files = {"file": (file_name, file_data, "application/pdf"), "purpose": (None, "ocr")}

    try:
        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"File upload failed: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Error uploading file: {str(e)}")
        return None


def get_file_url(file_id: str, api_key: str) -> Optional[str]:
    """Get a temporary URL for the uploaded file."""
    url = f"https://api.mistral.ai/v1/files/{file_id}/url?expiry=24"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("url")
        else:
            st.error(f"Failed to get file URL: {response.text}")
            return None
    except Exception as e:
        st.error(f"Error getting file URL: {str(e)}")
        return None


def process_ocr(document_url: str, api_key: str) -> Optional[Dict[str, Any]]:
    """Process the document using Mistral OCR API."""
    url = "https://api.mistral.ai/v1/ocr"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    data = {
        "model": "mistral-ocr-latest",
        "document": {"type": "document_url", "document_url": document_url},
        "include_image_base64": True,  # Include images in the output
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"OCR processing failed: {response.text}")
            return None
    except Exception as e:
        st.error(f"Error processing OCR: {str(e)}")
        return None


def main():
    st.title("PDF to Markdown Converter")
    st.caption("Powered by Mistral OCR API")

    # Inject JavaScript for local storage
    st.components.v1.html(js_code, height=0)

    # Initialize session state
    if "markdown_result" not in st.session_state:
        st.session_state["markdown_result"] = None

    if "file_name" not in st.session_state:
        st.session_state["file_name"] = None

    # About this app
    with st.expander("About this app", expanded=False):
        st.markdown(
            """
        This app uses the Mistral OCR API to convert PDF documents to Markdown format.
        
        **Features:**
        - Preserves document structure including headings, lists, tables
        - Maintains images from the original document
        - Supports multiple languages and complex layouts
        - Results are downloadable as Markdown files
        
        **To use:**
        1. Enter your Mistral API key (get one from [Mistral AI](https://console.mistral.ai/))
        2. Upload a PDF file
        3. Convert and download the Markdown
        
        For more information, visit the [Mistral OCR documentation](https://docs.mistral.ai/capabilities/document).
        """
        )

    # API Key section
    st.subheader("1. Enter your API Key")

    api_key = st.text_input(
        "API Key", type="password", help="Your Mistral API key will be stored in your browser's local storage"
    )

    col1, col2 = st.columns([1, 1])  # Changed column ratio for narrower UI

    with col1:
        if st.button("Save API Key", use_container_width=True):
            if not api_key:
                st.error("Please enter an API key")
            else:
                js_save = f"""
                <script>
                    if(window.saveApiKey("{api_key}")) {{
                        window.parent.postMessage({{type: "streamlit:set", key: "apiKeySaved", value: true}}, "*");
                    }}
                </script>
                """
                st.components.v1.html(js_save, height=0)
                st.success("API key saved to browser storage")

    with col2:
        if st.button("Test API Connection", use_container_width=True):
            if not api_key:
                st.error("Please enter an API key first")
            else:
                with st.spinner("Testing API connection..."):
                    if test_api_availability(api_key):
                        st.success("✅ API connection successful!")
                    else:
                        st.error("❌ API connection failed. Please check your API key.")

    st.markdown("---")

    # PDF Upload Section
    st.subheader("2. Upload PDF Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        file_info = f"File: **{uploaded_file.name}** ({uploaded_file.size / 1024:.1f} KB)"
        st.write(file_info)

        if st.button("Convert to Markdown", type="primary", use_container_width=True):
            if not api_key:
                st.error("Please enter your API key first")
            else:
                with st.status("Processing PDF...", expanded=True) as status:
                    # Step 1: Upload file
                    st.write("📤 Uploading PDF to Mistral servers...")
                    pdf_bytes = uploaded_file.getvalue()
                    upload_result = upload_file_to_mistral(pdf_bytes, uploaded_file.name, api_key)

                    if upload_result:
                        file_id = upload_result.get("id")

                        # Step 2: Get file URL
                        st.write("🔗 Retrieving file URL...")
                        file_url = get_file_url(file_id, api_key)

                        if file_url:
                            # Step 3: Process with OCR
                            st.write("🔍 Running OCR analysis...")
                            ocr_result = process_ocr(file_url, api_key)

                            if ocr_result:
                                # Combine all page markdown content
                                st.write("📝 Compiling Markdown content...")
                                full_markdown = ""
                                page_count = len(ocr_result.get("pages", []))

                                for page in ocr_result.get("pages", []):
                                    full_markdown += page.get("markdown", "") + "\n\n"

                                # Store results in session state
                                st.session_state["markdown_result"] = full_markdown
                                st.session_state["file_name"] = os.path.splitext(uploaded_file.name)[0]

                                status.update(
                                    label=f"✅ Conversion successful! Processed {page_count} pages.", state="complete"
                                )

    # Display results and download button (simplified, no preview)
    if st.session_state["markdown_result"]:
        st.markdown("---")
        st.subheader("3. Download Converted Markdown")

        st.success(f"Your PDF has been successfully converted to Markdown! Click below to download.")

        # Download button
        markdown_filename = f"{st.session_state['file_name']}.md"

        st.download_button(
            label="📥 Download Markdown File",
            data=st.session_state["markdown_result"],
            file_name=markdown_filename,
            mime="text/markdown",
            use_container_width=True,
        )

        # Process another file button
        if st.button("Process Another File", use_container_width=True):
            st.session_state["markdown_result"] = None
            st.session_state["file_name"] = None
            st.experimental_rerun()


if __name__ == "__main__":
    main()