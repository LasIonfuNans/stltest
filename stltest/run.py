import subprocess
import streamlit as st
import os

# folder = r'C:\\Users\\prime\\python\\3.10.5\\Streamlit\\src\app'
# subprocess.run('poetry run streamlit run qiita.py', cwd=folder, shell=True)
# subprocess.Popen('poetry run streamlit run qiita.py', cwd=folder, shell=True)

def kidou():
	base = os.path.dirname(os.path.abspath(__file__))
	# name = os.path.normpath(os.path.join(base, '../app'))
	name = os.path.normpath(base)
	subprocess.run('poetry run streamlit run qiita.py', cwd=base, shell=True)
