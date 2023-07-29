# Personal Assistant V1
Personal Assistant是一个可以帮你处理你本地文件数据的助手。你可以以对话形式向它获取你想要的信息，或者发出你的指令。

## Installation 安装
安装 [LangChain](https://github.com/hwchase17/langchain)和其他依赖的包。
```
pip install -r requirements.txt
```

填入你的[OpenAI API key](https://platform.openai.com/account/api-keys)
```
export OPENAI_API_KEY='sk-...'
```

将`data/data.txt`文件中替换成你的数据，或者在`data`文件夹中添加你的文件。

## Usage 使用
例：总结`data/data.txt`文件信息。
### 方式一：通过命令行输入指令
```
> python personal_assistant.py "总结一下，用列表和中文"

1. Mind Wisdom Money 提到 Excel 技能是任何职业必备的，并列出 5 个可以节省数百小时的 Excel 技巧。
2. Cal 分享了一个 AI 编辑器，可以根据已发布的文章自我训练，比一般工具更有效，可以免费试用。
```

### 方式二：通过UI界面输入指令
```
> streamlit run personal_assistant.py
```
