"""
总结服务类：用户提问，检索知识库，将提问和参考资料提交给模型，大模型总结给出回答
"""
from langchain_classic.chains.summarize.map_reduce_prompt import prompt_template, PROMPT
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from model.factory import chat_model
from rag.vector_store import VectorStoreService
from utils.prompt_loader import load_rag_prompt


class RagSummarizeService(object):
    def __init__(self):
        self.vector_store =VectorStoreService()
        self.retriever = self.vector_store.get_retriever()
        self.prompt_text = load_rag_prompt()
        self.prompt_template = PromptTemplate.from_template(self.prompt_text)
        self.model = chat_model
        self.chain = self._init_chain()

    def print_prompt(self,prompt):
        print("="*20)
        print(prompt.to_string())
        print("="*20)
        return prompt


    def _init_chain(self):
        chain = self.prompt_template | self.print_prompt | self.model | StrOutputParser()
        return chain

    def retriever_docs(self,query:str)->list[Document]:
        return self.retriever.invoke(query)

    def rag_summarize(self,query:str)->str:
        docs = self.retriever_docs(query)
        context = ""
        counter = 0
        for doc in docs:
            counter += 1
            context +=f"【参考资料{counter}】: 参考资料{doc.page_content},【参考元数据{doc.metadata}】\n"
        return self.chain.invoke(
            {
                "input": query,
                "context": context
            }
        )

