from setuptools import setup, find_packages

setup(
    name='mcqgen',
    version='0.1.0',
    description='MCQ Generator using LangChain and OpenAI',
    author='Your Name',
    author_email='veekshith@veekshith.dev',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'openai',
        'langchain',
        'streamlit',
        'python-dotenv',
        'PyPDF2',
    ],
    python_requires='>=3.8',
)
