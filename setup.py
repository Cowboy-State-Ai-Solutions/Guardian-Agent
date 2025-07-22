"""
Guardian Agent: Open Source Anti-Hallucination Framework
Enterprise-grade hallucination detection for Large Language Models
"""

import os
from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
def read_requirements(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Core requirements
install_requires = [
    "numpy>=1.21.0",
    "torch>=2.0.0",
    "transformers>=4.30.0",
    "sentence-transformers>=2.2.0",
    "scikit-learn>=1.0.0",
    "pyyaml>=6.0",
    "tqdm>=4.65.0",
    "requests>=2.28.0",
    "aiohttp>=3.8.0",
    "pydantic>=2.0.0",
    "rich>=13.0.0",
    "click>=8.1.0",
    "fastapi>=0.100.0",
    "uvicorn>=0.22.0",
]

# Optional dependencies
extras_require = {
    "dev": [
        "pytest>=7.3.0",
        "pytest-cov>=4.0.0",
        "pytest-asyncio>=0.21.0",
        "black>=23.0.0",
        "flake8>=6.0.0",
        "mypy>=1.3.0",
        "pre-commit>=3.3.0",
        "sphinx>=6.0.0",
        "sphinx-rtd-theme>=1.2.0",
        "twine>=4.0.0",
    ],
    "openai": ["openai>=1.0.0"],
    "anthropic": ["anthropic>=0.3.0"],
    "langchain": ["langchain>=0.1.0"],
    "llamaindex": ["llama-index>=0.9.0"],
    "google": ["google-generativeai>=0.3.0"],
    "transformers": ["accelerate>=0.20.0", "bitsandbytes>=0.40.0"],
    "all": [],  # Will be populated below
}

# Add all optional dependencies to 'all'
all_extras = []
for extra, deps in extras_require.items():
    if extra != "all":
        all_extras.extend(deps)
extras_require["all"] = list(set(all_extras))

setup(
    name="guardian-agent",
    version="1.0.0",
    author="Guardian Agent Contributors",
    author_email="team@guardian-agent.ai",
    description="Enterprise-grade hallucination detection and prevention for Large Language Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guardian-agent/guardian-agent",
    project_urls={
        "Bug Tracker": "https://github.com/guardian-agent/guardian-agent/issues",
        "Documentation": "https://guardian-agent.readthedocs.io",
        "Source Code": "https://github.com/guardian-agent/guardian-agent",
        "Discord": "https://discord.gg/guardian-agent",
        "Demo": "https://contextual-refresher-technology-insurancegpts.replit.app/guardian-agent-anti-hallucination",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "guardian=guardian_agent.cli:main",
            "guardian-agent=guardian_agent.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "guardian_agent": [
            "patterns/*.yaml",
            "patterns/**/*.yaml",
            "data/*.json",
            "data/*.yaml",
        ],
    },
    keywords=[
        "ai",
        "llm",
        "hallucination",
        "detection",
        "artificial-intelligence",
        "machine-learning",
        "nlp",
        "safety",
        "reliability",
        "gpt",
        "claude",
        "gemini",
        "llama",
    ],
    zip_safe=False,
)
