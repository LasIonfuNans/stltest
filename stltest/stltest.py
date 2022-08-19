import subprocess
import streamlit as st
import os

def disp():
	base = os.path.dirname(os.path.abspath(__file__))
	subprocess.run('streamlit run top_page.py', cwd=base, shell=True)

if __name__ == "__main__":
	disp()