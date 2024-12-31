import streamlit as st
from transformers import pipeline
import requests
import pandas as pd
import re

# Agent Classes
class UseCaseAgent:
    def __init__(self):
        """Agent to generate AI/ML use cases."""
        self.generator = pipeline("text-generation", model="gpt2")

    def generate_use_cases(self, industry, trends):
        """Generate 3 use cases with a brief debrief based on industry and trends."""
        prompt = (
            f"Industry: {industry}\n"
            f"Trends: {trends}\n"
            f"Suggest 3 AI/ML/GenAI use cases with a brief debrief for each to improve operations and customer satisfaction:"
            "\n1. "
        )
        result = self.generator(prompt, max_length=300, num_return_sequences=1)
        use_cases = result[0]["generated_text"]

        # Format the output into a list by extracting each line that starts with a number
        use_case_list = re.findall(r'\d+\.\s*(.*?)(?:\n|$)', use_cases)
        
        # Limit the use cases to 3
        return use_case_list[:3]


class ResourceAgent:
    def __init__(self):
        """Agent to search and retrieve datasets."""
        pass

    def search_huggingface(self, query):
        """Search datasets on HuggingFace."""
        hf_url = f"https://huggingface.co/api/models?search={query}"
        response = requests.get(hf_url)
        return response.json()[:5] if response.status_code == 200 else []

    def search_kaggle(self, query):
        """Search datasets on Kaggle."""
        kaggle_url = f"https://www.kaggle.com/api/v1/datasets/list?search={query}"
        response = requests.get(kaggle_url)
        return response.json()[:5] if response.status_code == 200 else []


# Multi-Agent System
class MultiAgentSystem:
    def __init__(self):
        self.use_case_agent = UseCaseAgent()
        self.resource_agent = ResourceAgent()

    def process_query(self, industry_query, trends_query):
        """End-to-end query processing."""
        use_cases = self.use_case_agent.generate_use_cases(industry_query, trends_query)
        return use_cases

    def fetch_datasets(self, use_cases):
        """Fetch relevant datasets based on generated use cases."""
        keywords = self.extract_keywords(use_cases)
        datasets = {}

        for keyword in keywords:
            hf_datasets = self.resource_agent.search_huggingface(keyword)
            kaggle_datasets = self.resource_agent.search_kaggle(keyword)
            datasets[keyword] = {
                "huggingface": hf_datasets,
                "kaggle": kaggle_datasets
            }
        return datasets

    def extract_keywords(self, use_cases):
        """Extract relevant keywords from use cases for dataset search."""
        # Simple keyword extraction: split by spaces and take the first two words as keywords
        keywords = set()
        for use_case in use_cases:
            words = re.findall(r'\w+', use_case)
            if words:
                keywords.add(words[0])  # For simplicity, take the first word as a keyword
        return list(keywords)


# Streamlit UI
def run_streamlit_ui():
    st.title("Market Research & AI Use Case Generator")
    st.write("Generate actionable insights and find relevant datasets.")

    mas = MultiAgentSystem()

    # Trends and Use Case Generation
    st.header("AI/ML Use Case Generation")
    industry_query = st.text_input("Enter industry/company:")
    st.caption("Example: Automotive, Retail, Healthcare, etc.")
    trends_query = st.text_input("Enter industry trends or focus areas:")
    st.caption("Example: Supply chain optimization, Customer experience, etc.")
    
    # Store use cases in session state
    if "use_cases" not in st.session_state:
        st.session_state["use_cases"] = []

    if st.button("Generate Use Cases"):
        with st.spinner("Generating insights..."):
            st.session_state["use_cases"] = mas.process_query(industry_query, trends_query)
            st.subheader("Proposed Use Cases")
            for i, use_case in enumerate(st.session_state["use_cases"], start=1):
                st.write(f"**Use Case {i}:** {use_case}")

    # Add a button to search for relevant datasets
    if st.session_state["use_cases"]:
        st.subheader("Search for Relevant Datasets")
        if st.button("Search Datasets"):
            with st.spinner("Searching datasets..."):
                datasets = mas.fetch_datasets(st.session_state["use_cases"])

                for keyword, dataset_info in datasets.items():
                    st.write(f"### Datasets related to: {keyword}")

                    # HuggingFace Datasets
                    st.subheader("HuggingFace Datasets")
                    if dataset_info["huggingface"]:
                        for dataset in dataset_info["huggingface"]:
                            dataset_id = dataset.get('modelId', 'Unknown ID')
                            dataset_url = f"https://huggingface.co/models/{dataset_id}"
                            st.write(f"- [{dataset_id}]({dataset_url})")
                    else:
                        st.write("No relevant datasets found on HuggingFace.")

                    # Kaggle Datasets
                    st.subheader("Kaggle Datasets")
                    if dataset_info["kaggle"]:
                        for dataset in dataset_info["kaggle"]:
                            dataset_title = dataset.get('title', 'Unknown Title')
                            dataset_url = dataset.get('url', '#')
                            st.write(f"- [{dataset_title}]({dataset_url})")
                    else:
                        st.write("No relevant datasets found on Kaggle.")


if __name__ == "__main__":
    run_streamlit_ui()
