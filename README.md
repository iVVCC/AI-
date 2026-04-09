# 智扫通机器人智能客服 (ZhiSaoTong Intelligent Customer Service)

这是一个基于 LangChain 和 Streamlit 构建的智能客服机器人系统。该系统利用 RAG（检索增强生成）技术和自定义 Agent 工具，为用户提供精准的知识检索、外部数据查询以及实时信息服务（如天气、IP 定位等）。

## 🚀 核心功能

- **RAG 知识检索**：集成 ChromaDB 向量数据库，能够从海量文档中检索相关内容并结合大模型进行总结回答。
- **自定义 Agent 工具集**：
    - `rag_summarize`: 知识库内容检索与总结。
    - `fetch_external_data`: 获取外部系统中的用户使用记录。
    - `get_ip_info`: 自动获取本机公网 IP 及地理位置。
    - `get_city_adcode`: 通过 Excel 匹配城市编码。
    - `get_weather_by_adcode`: 基于城市编码查询实时天气。
- **Streamlit 交互界面**：简洁直观的聊天式 UI，支持流式输出响应。
- **模块化架构**：清晰的代码组织结构，便于扩展新功能、新工具或更换底层模型。

## 📂 项目结构

```text
Agent/
├── agent/                  # Agent 核心逻辑
│   ├── tools/              # 自定义工具集与中间件
│   └── react_agent.py      # ReAct Agent 实现
├── config/                 # 配置文件 (YAML)
├── model/                  # 模型工厂，支持多种 LLM 接入
├── prompts/                # 提示词模板文件
├── rag/                    # RAG 服务与向量存储实现
├── utils/                  # 各种工具类 (日志、配置、路径等)
├── app.py                  # Streamlit 应用入口
├── requirements.txt        # 项目依赖
└── Dockerfile              # Docker 部署配置
```

## 🛠️ 安装与运行

### 1. 环境准备
确保已安装 Python 3.9+。建议使用虚拟环境：

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置文件
在 `config/` 目录下根据实际情况修改配置文件（如 API 密钥、数据库路径等）。主要配置文件包括：
- `agent.yml`: Agent 相关参数。
- `chroma.yml`: 向量数据库配置。
- `prompts.yml`: 提示词配置。
- `rag.yml`: RAG 服务配置。

### 4. 启动应用
```bash
streamlit run app.py
```

## 🐳 Docker 部署

```bash
docker build -t zhisao-agent .
docker run -p 8501:8501 zhisao-agent
```

## 🛠️ 技术栈

- **框架**: [LangChain](https://github.com/langchain-ai/langchain)
- **前端**: [Streamlit](https://streamlit.io/)
- **向量数据库**: [ChromaDB](https://www.trychroma.com/)
- **大语言模型**: 通义千问 (Dashscope) 等
- **数据处理**: Pandas, Openpyxl
