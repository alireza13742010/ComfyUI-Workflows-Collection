
import streamlit as st
import requests
import tempfile
import json
print(1)
COMFYUI_API_URL = "http://127.0.0.1:8188/api/queue"

st.set_page_config(page_title="Lyrics & Prompt to Audio via ComfyUI", page_icon="🎤")

st.title("🎤 Lyrics & Prompt to Audio via ComfyUI")
st.write("Enter lyrics and a prompt, send them to ComfyUI, and hear the generated audio.")

# Load your saved ComfyUI workflow JSON
with open("Ace_step_music_generation.json", "r") as f:
    workflow_data = json.load(f)

# Two separate inputs
lyrics = st.text_area("Enter lyrics:", height=150)
tags = st.text_input("Enter tags:")

if st.button("Generate Audio"):
    if not lyrics.strip() or not tags.strip():
        st.warning("Please enter both lyrics and tags.")
    else:
        try:
            # Update the workflow JSON with the user's inputs
            # Adjust these keys to match your actual workflow node IDs and input names
            workflow_data["6"]["inputs"]["lyrics"] = lyrics
            workflow_data["6"]["inputs"]["tags"] = tags

            with st.spinner("Generating audio..."):
                # Send the updated workflow to ComfyUI
                response = requests.post(COMFYUI_API_URL, json=workflow_data)
                response.raise_for_status()
                # ComfyUI returns JSON with output file info
                result = response.json()
                print(3)
                # Adjust these keys to match your output node ID
                audio_filename = result["10"]["inputs"]["filename_prefix"][0]["filename"]
                print(4)
                # Download the audio file from ComfyUI's /view endpoint
                audio_url = f"http://localhost:8188/view?filename={audio_filename}"
                audio_response = requests.get(audio_url)
                audio_response.raise_for_status()

                # Save audio to a temporary file
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
                temp_file.write(audio_response.content)
                temp_file.close()

            st.success("Audio generated successfully!")
            st.audio(temp_file.name, format="audio/wav")

        except Exception as e:
            st.error(f"Error: {e}")
