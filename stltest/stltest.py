import subprocess
import streamlit as st
import os

def disp():
	base = os.path.dirname(os.path.abspath(__file__))
	print(base)
	name = os.path.normpath(base)
	# subprocess.run('poetry run streamlit run qiita.py', cwd=base, shell=True)
	subprocess.run('streamlit run fisrt.py', cwd=base, shell=True)
	# subprocess.run('poetry run streamlit run ./stltest/first.py', shell=True)

if __name__ == "__main__":
	disp()