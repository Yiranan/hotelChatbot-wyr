# environment requires
python>=3.8
# requirements install
pip install requirements.txt
# offline parsing
## this part is used for trainset vectordatabase parsing
python offline_main.py
# online QA
streamlit run hotelChatbot_wyr.py