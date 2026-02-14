# Vedant CLI

A fast command-line tool that prints the directory tree of the current folder.

## Install (recommended)
```bash
pipx install vedant
```

## Install (not recommended)
```bash
pip install vedant
```

## Install (for local development)

```bash
pip install -e .
```

## 📁 Show only directories
```bash
vedant --dirs-only
```

## 💾 Ask to save output to file
```bash
vedant --save
```

### If enabled, the program will ask:

    Save to `vedant_tree.txt` ? (y/n)

If you type `y`, the tree will be saved in the current folder.