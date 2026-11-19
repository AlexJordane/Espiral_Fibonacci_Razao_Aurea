# Espiral de Fibonacci e Razão Áurea

Conjunto de materiais didáticos, animações matemáticas interativas (**Manim / Manim Slides**) e roteiro de investigação geométrica e algébrica sobre a **Razão Áurea ($\phi$)**, a **Sequência de Fibonacci** e a **Espiral de Fibonacci**, desenvolvido no âmbito do **Doutorado em Educação em Ciências e Matemática (Educimat — Ifes)**.

## Links de Acesso

- **Página do Projeto (GitHub Pages):** https://alexjordane.github.io/Espiral_Fibonacci_Razao_Aurea/
- **Apresentação Interativa — Razão Áurea:** https://alexjordane.github.io/Espiral_Fibonacci_Razao_Aurea/apresentacao_razao_aurea.html
- **Animação Interativa — Espiral de Fibonacci:** https://alexjordane.github.io/Espiral_Fibonacci_Razao_Aurea/Espiral.html
- **Tarefa Investigativa (PDF):** [Tarefa_Fibonacci.pdf](./Tarefa_Fibonacci.pdf)
- **Repositório no GitHub:** https://github.com/AlexJordane/Espiral_Fibonacci_Razao_Aurea

---

## Componentes do Projeto

### 1. Apresentação Interativa: Razão Áurea (`apresentacao_razao_aurea.html` e `razaoaurea_manin_slides.py`)
Apresentação animada passo a passo gerada em Python com **Manim** e exportada via **Manim Slides** para HTML autossuficiente (Reveal.js).
- **Modelagem Algébrica:** Parte da divisão de um segmento $AB$ em extrema e média razão ($\frac{AB}{AC} = \frac{AC}{CB}$) e resolve passo a passo a equação quadrática $(AC)^2 + AB \cdot AC - (AB)^2 = 0$, obtendo $AC = \frac{AB(\sqrt{5}-1)}{2}$.
- **Construção Geométrica com Régua e Compasso:** Anima a construção do ponto $C$ que divide $AB$ na razão áurea por meio do prolongamento do segmento, traçado de semicírculo, construção do triângulo retângulo $MAE$ de catetos $r$ e $\frac{r}{2}$, aplicação do Teorema de Pitágoras ($x = \frac{AB\sqrt{5}}{2}$) e transporte do arco de raio $ME = MC$.
- **Dedução de $\phi$:** Conclui com a racionalização algébrica que demonstra:
  $$\phi = \frac{AB}{AC} = \frac{\sqrt{5}+1}{2} \approx 1{,}6180$$

**Controles da Apresentação HTML:**
- `Seta para a Direita`: Avança para o próximo passo/slide (aguarde o ícone verde de *play* aparecer no canto inferior direito).
- `Seta para a Esquerda`: Retorna ao slide anterior.
- `Barra de Espaço`: Reinicia a animação do slide atual.
- `F` / `ESC`: Ativa ou sai do modo de tela cheia.

---

### 2. Animação da Espiral de Fibonacci (`Espiral.html` e `Espiral.py`)
Cena animada construída com `MovingCameraScene` no **Manim** e exportada para HTML interativo.
- Constrói sequencialmente, sobre uma malha cartesiana, os quadrados cujos lados correspondem aos termos da sequência de Fibonacci ($1, 1, 2, 3, 5, 8, 13, 21$).
- Traça, em cada quadrado, o arco de circunferência de $90^\circ$ com concordância suave nos vértices, formando a **Espiral de Fibonacci**.
- Ajusta dinamicamente o enquadramento e o zoom da câmera (proporção 16:9) à medida que a espiral se expande.

---

### 3. Tarefa Investigativa em LaTeX/PDF (`Tarefa_Fibonacci.pdf` e `Tarefa_Fibonacci.tex`)
Roteiro de atividades elaborado para a disciplina *Debates Conceituais Avançados em Matemática* (Doutorado Educimat — Ifes), estruturado em quatro problemas encadeados:
1. **Construção Geométrica da Secção Áurea:** Demonstração da divisão de um segmento em extrema e média razão a partir de um quadrado de lado $L$ e do arco de raio $MB'$.
2. **Problema Clássico dos Coelhos de Fibonacci:** Preenchimento e modelagem da tabela de crescimento populacional (casais jovens, adultos e total $F_n$) ao longo de 12 meses e generalização para $n$ meses.
3. **Taxa de Crescimento e Convergência:** Cálculo das razões sucessivas $\frac{F_n}{F_{n-1}}$ com quatro casas decimais e análise da convergência para a Razão Áurea $\phi$.
4. **Traçado na Malha Quadriculada:** Construção geométrica guiada dos quadrados de Fibonacci (até o lado $34$) e dos arcos concordantes de $90^\circ$ sobre malha quadriculada gerada em TikZ.

---

## Como Executar ou Compilar os Códigos-Fonte

- **Visualização imediata (Web):** Basta abrir os arquivos `apresentacao_razao_aurea.html` e `Espiral.html` diretamente em qualquer navegador web moderno.
- **Recompilar as animações em Python (Manim + Manim Slides):**
  ```bash
  pip install manim manim-slides
  manim-slides render razaoaurea_manin_slides.py RazaoAurea
  manim-slides convert RazaoAurea apresentacao_razao_aurea.html --one-file

  manim-slides render Espiral.py EspiralFibonacci
  manim-slides convert EspiralFibonacci Espiral.html --one-file
  ```
- **Recompilar o roteiro em LaTeX:**
  ```bash
  pdflatex Tarefa_Fibonacci.tex
  ```

---

## Autoria e Licença

- **Autor:** Professor Alex Jordane (Instituto Federal do Espírito Santo — Licenciatura em Matemática • Educimat), em colaboração com Inteligência Artificial (Gemini).
- **Licença:** O compartilhamento e a reprodução deste material são permitidos para fins didáticos, desde que citadas a fonte e a autoria.

