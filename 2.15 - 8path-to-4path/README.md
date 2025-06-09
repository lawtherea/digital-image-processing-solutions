# 8-Path to 4-Path Converter

Este projeto implementa um algoritmo para converter caminhos binários **8-conectados** em caminhos **4-conectados** dentro de uma matriz 2D. A conversão preserva a topologia do caminho original, substituindo passos diagonais por sequências horizontais e verticais.

---

## 📚 Referência

Esta é a **solução da Questão 2.15** do livro:

> **Digital Image Processing, 4th Edition**  
> Autores: Rafael C. Gonzalez, Richard E. Woods

> **2.15**: *Develop an algorithm for converting a one-pixel-thick 8-path to a 4-path.*

---

## 🧠 Conceito

- **8-path**: Caminho que pode seguir em todas as 8 direções (inclusive diagonais).
- **4-path**: Caminho que só pode seguir para cima, baixo, esquerda ou direita (sem diagonais).

O algoritmo substitui cada movimento diagonal por dois movimentos ortogonais (linha + coluna), preservando a conectividade do caminho.

---

## ▶️ Como usar

Execute o script no terminal e insira a matriz linha por linha (formato binário: apenas 0s e 1s):

```bash
python convert_path.py
```

## Exemplo de Entrada

```bash
0 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
```

## Exemplo de Saída

```bash
Matriz com 4-conectividade:
0 0 0 0
0 1 1 0
0 0 1 1
0 0 0 1
\
```

> Projeto acadêmico — Orion Lab • Grupo de Estudo - Visão Computacional