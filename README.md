# private data/llm
1.首先要在环境变量力设定openai_api_key才能运行starter.py文件。
2.在同级文件夹放置名为data的文件夹，里面储存任意形式的文档（如txt/pdf/docx等，目前测试了这三种都可以）。
3.运行后生成storage文档，里面储存json格式的数据库内容；同时生成chromadb文件夹，里面有sqlite3格式的数据库内容。
4.已经跑完embedding后可以直接加载sqlite3格式的数据库内容，不需要重新跑一次。
