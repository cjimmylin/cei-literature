# Codestral

## Overview
Open-weight generative model specifically tailored for code-centric tasks, supporting 80+ programming languages. Features Fill-in-the-Middle (FIM) capability for IDE integration.

## Technical Specifications
- **Release Year:** 2024
- **Parameters:** 22B
- **Languages:** 80+ programming languages (Python, Java, C, C++, JavaScript, Bash, etc.)
- **License:** MNPL-0.1 (Mistral Non-Production License)
- **Format:** Safetensors (BF16)

## Documentation & Links

### Official Resources
| Resource | Link |
|----------|------|
| Blog Announcement | [Codestral](https://mistral.ai/news/codestral/) |
| Documentation | [docs.mistral.ai](https://docs.mistral.ai/) |
| Code Generation Guide | [docs.mistral.ai/capabilities/code_generation](https://docs.mistral.ai/capabilities/code_generation/) |

### HuggingFace Models
| Model | Link |
|-------|------|
| Base Model | [mistralai/Codestral-22B-v0.1](https://huggingface.co/mistralai/Codestral-22B-v0.1) |

### GitHub Repositories
| Repository | Description |
|------------|-------------|
| [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | Official inference library with FIM support |
| [mistralai/mistral-common](https://github.com/mistralai/mistral-common) | Common utilities and tokenizers |

### API & Playground
| Service | Link |
|---------|------|
| La Plateforme API | [console.mistral.ai](https://console.mistral.ai/) |
| Le Chat Playground | [chat.mistral.ai](https://chat.mistral.ai/) |
| API Documentation | [docs.mistral.ai/api](https://docs.mistral.ai/api/) |
| Codestral API Endpoint | [codestral.mistral.ai](https://codestral.mistral.ai/) |

### IDE Integrations
| IDE | Plugin |
|-----|--------|
| VS Code | Continue, Tabnine |
| JetBrains | Mistral Plugin |
| Vim/Neovim | Various LSP clients |

## Capabilities
- **Instruct Mode:** Answer questions about code, write documentation, generate code
- **Fill-in-the-Middle (FIM):** Predict middle tokens between prefix/suffix for IDE autocomplete
