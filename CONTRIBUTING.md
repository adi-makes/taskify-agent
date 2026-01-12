# Contributing to Taskify Agent

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### Reporting Bugs
1. Check if the bug has already been reported in Issues
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version)
   - Relevant logs or screenshots

### Suggesting Features
1. Open an issue with the "enhancement" label
2. Describe the feature and its use case
3. Explain why it would be valuable
4. Provide examples if possible

### Submitting Code

#### Setup Development Environment
```bash
# Clone the repository
git clone https://github.com/yourusername/taskify-agent.git
cd taskify-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

#### Code Style
- Follow PEP 8 guidelines
- Use type hints for function arguments and returns
- Add docstrings to all functions (Google style)
- Keep functions focused and modular
- Maximum line length: 88 characters (Black formatter)

#### Before Submitting
```bash
# Run linting
pip install ruff
ruff check .

# Run type checking
pip install mypy
mypy agent.py tools/ --ignore-missing-imports

# Check for security issues
safety check -r requirements.txt
```

#### Pull Request Process
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m "Add: feature description"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Open a Pull Request with:
   - Clear description of changes
   - Reference to related issues
   - Screenshots/examples if applicable

## 📋 Code Review Checklist

- [ ] Code follows PEP 8 style guidelines
- [ ] All functions have type hints
- [ ] Docstrings added for new functions
- [ ] No hardcoded credentials or API keys
- [ ] Error handling implemented
- [ ] Logging added for important operations
- [ ] No breaking changes (or clearly documented)
- [ ] Updated README if needed

## 🏗️ Project Structure

```
taskify-agent/
├── agent.py           # Main agent definition
├── config.py          # Configuration management
├── tools/             # Utility tools
│   ├── pdf_tools.py   # PDF processing
│   └── datetime_tools.py  # Date/time utilities
├── examples/          # Usage examples
└── tests/             # Unit tests (future)
```

## 🧪 Testing Guidelines

Currently, the project uses manual testing. We welcome contributions for:
- Unit tests for tools
- Integration tests for agent workflows
- Test fixtures and sample PDFs

## 📝 Commit Message Format

Use conventional commits:
- `Add: new feature or file`
- `Fix: bug fix`
- `Update: changes to existing functionality`
- `Docs: documentation changes`
- `Refactor: code restructuring`
- `Test: adding or updating tests`

## 🔒 Security

- Never commit `.env` files or API keys
- Report security vulnerabilities privately via email
- Follow secure coding practices
- Validate all user inputs

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

Feel free to open an issue for any questions about contributing!
