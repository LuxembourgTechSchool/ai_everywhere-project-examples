# Module: AI Everywhere
## Project Examples

Some examples for how to access the lts proxy as well as some project examples. 

## How to run the scripts
1. Create venv have activate it.
2. In order to run any of the scripts, you need to add the file .streamlit/secrets.toml. 
   Add a new line to the file:​ lts_secret = `'coach-will-tell-you ;)'​`
3. Install streamlit: `pip install streamlit`
4. Check streamlit is installed: `streamlit --version`
5. Run a script. For example: `streamlit run example_get_speech.py`

## Notes 
### Spotify Example
One data file is zipped to minimize its size. Unzip `spotify/universal_top_spotify_songs.zip` as such:
```
    cd spotify
    unzip universal_top_spotify_songs.zip
```
### Postcard Example
An example selfie image can be found in the `postcard` directory.
Example prompts:
- "An image of the Niagara falls. No people or objects in the image at all. The image is taken from the distance."
- "An image of a beach with the ocean in the background."

### Other examples
These examples show how to use the different OpenAI API points through the LTS proxy: 
chat, image generation, text-to-speech, vision.
