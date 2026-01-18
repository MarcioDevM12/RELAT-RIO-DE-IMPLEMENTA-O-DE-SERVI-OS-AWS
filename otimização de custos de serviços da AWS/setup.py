"""
Setup configuration for AWS Cost Optimization Tool
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Package version
VERSION = '1.0.0'

# Package description
DESCRIPTION = 'AWS Cost Optimization Tool - Complete implementation case study'
AUTHOR = 'Márcio Dias Dos Santos'
AUTHOR_EMAIL = 'marcio.dias@example.com'
URL = 'https://github.com/yourusername/aws-cost-optimization'
LICENSE = 'MIT'

setup(
    name='aws-cost-optimizer',
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    license=LICENSE,
    
    # Package discovery
    packages=find_packages(include=['scripts', 'scripts.*']),
    include_package_data=True,
    
    # Dependencies
    install_requires=requirements,
    
    # Python version requirement
    python_requires='>=3.8',
    
    # Entry points for command line tools
    entry_points={
        'console_scripts': [
            'aws-cost-analyzer=scripts.cost_analyzer:main',
            'aws-ec2-optimizer=scripts.ec2_optimizer:main',
            'aws-report-generator=scripts.report_generator:main',
            'aws-optimization-cli=scripts.cli:main',
        ],
    },
    
    # Package classifiers for PyPI
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Natural Language :: English',
        'Natural Language :: Portuguese (Brazilian)',
    ],
    
    # Keywords for search
    keywords=[
        'aws',
        'cost-optimization',
        'cloud-cost',
        'finops',
        'aws-cost-management',
        'python',
        'devops',
    ],
    
    # Project URLs
    project_urls={
        'Documentation': 'https://github.com/yourusername/aws-cost-optimization/docs',
        'Source': URL,
        'Tracker': f'{URL}/issues',
    },
    
    # Additional package data
    package_data={
        'scripts': ['*.json', '*.yaml', '*.yml'],
    },
    
    # Data files
    data_files=[
        ('config', ['configs-aws/main.tf', 'configs-aws/template.yaml']),
        ('docs', ['docs/setup-guide.md', 'docs/how-to-use.md']),
    ],
    
    # Scripts (alternative to entry_points)
    scripts=[
        'scripts/cost_analyzer.py',
        'scripts/ec2_optimizer.py',
        'scripts/report_generator.py',
    ],
    
    # Testing
    test_suite='tests',
    tests_require=['pytest>=7.0.0'],
    
    # Extras
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
            'mypy>=1.0.0',
            'pre-commit>=3.0.0',
        ],
        'docs': [
            'sphinx>=7.0.0',
            'sphinx-rtd-theme>=1.0.0',
            'myst-parser>=2.0.0',
        ],
        'aws': [
            'boto3>=1.28.0',
            'awscli>=1.29.0',
            'botocore>=1.31.0',
        ],
    },
    
    # Options
    options={
        'bdist_wheel': {
            'universal': True,
        },
    },
    
    # ZIP safe
    zip_safe=False,
)

# Post-install message
print("\n" + "="*60)
print("AWS Cost Optimization Tool Installed Successfully!")
print("="*60)
print("\nAvailable commands:")
print("  aws-cost-analyzer    - Analyze AWS costs")
print("  aws-ec2-optimizer    - Optimize EC2 instances")
print("  aws-report-generator - Generate optimization reports")
print("\nFor documentation, visit:", URL)
print("="*60)