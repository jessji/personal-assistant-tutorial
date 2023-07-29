import os
from config import OPENAI_API_KEY

import sys
import streamlit as st

from langchain.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader, PyPDFDirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY # 填入你的OpenAI API key，或者在命令行输入"export OPENAI_API_KEY='sk-...'"，将其设置为环境变量

####################
# 加载本地文件的几种方式
####################

# 方式一：加载一份文件
loader = TextLoader('data/memo.txt') # 加载txt文件
# loader = PyPDFLoader("data/*.pdf") # 加载pdf文件

# 方式二：加载一个目录下的多份文件
# loader = DirectoryLoader("data", glob="*.txt") # 加载data目录下的所有.txt文件
# loader = PyPDFDirectoryLoader("data", glob="*.pdf") # 加载data目录下的所有.pdf文件

index = VectorstoreIndexCreator().from_loaders([loader])

####################
# 获取指令的几种方式
####################

# # 方式一：通过命令行输入
# query = sys.argv[1] # 获取命令行的指令
# print(query)
# print(index.query(query))

# 方式二：用streamlit生成UI界面，通过UI界面输入
st.title("你的私人AI助理")
query = st.text_input('请输入你的问题或指令')
if query:
    print(query)
    st.write(index.query(query))
