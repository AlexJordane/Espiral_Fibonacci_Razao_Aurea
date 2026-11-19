from manim import *
from manim_slides import Slide

class RazaoAurea(Slide):
    def pausar_com_play(self):
    # Criação de um pequeno ícone de reprodução (triângulo estilizado)
        triangulo = Triangle(fill_opacity=0.6, fill_color=PURE_GREEN, stroke_width=0)
        triangulo.scale(0.2)
        triangulo.rotate(-90 * DEGREES)  # Aponta o triângulo para a direita
        
        circulo = Circle(
            radius=triangulo.width, 
            color=PURE_GREEN,
            stroke_opacity=0.6,
            fill_color=PURE_GREEN,     # Cor do preenchimento interno
            fill_opacity=0.2,
            stroke_width=5
        ).move_to(triangulo.get_center()).shift(LEFT * 0.05)
        
        icone_play = VGroup(circulo, triangulo)
        # Posicionamento no canto inferior direito do ecrã
        icone_play.to_corner(DR, buff=0.6).shift(UP * 0.8)

        # 1. Surge discretamente no ecrã
        self.play(FadeIn(icone_play, scale=0.8), run_time=0.4)
        
        # 2. Ponto de paragem da apresentação
        self.next_slide()
        
        # 3. Assim que o utilizador avança, o ícone desaparece
        self.play(FadeOut(icone_play, scale=0.8), run_time=0.3)

    def construct(self):
        # Configuração de cores e logo
        mycolor = ManimColor('#071E25')
        self.camera.background_color = mycolor
        
        img = ImageMobject('../alexjordane.github.io/ifes.jpeg')
        img.scale(1)  
        img.shift(3.3 * DOWN + 5.6 * RIGHT)  
        self.add(img) 

        # --- SLIDE 1: Abertura e Identificação ---
        titulo = Tex("Razão Áurea", font_size=48).to_edge(UP, buff=0.3)
        turma = Tex("Educimat", font_size=35).next_to(titulo, DOWN, buff=0.15)
        prof = Tex("Prof. Alex Jordane", font_size=30).next_to(turma, DOWN, buff=0.15)
        
        self.play(Write(titulo))
        self.play(Write(turma))
        self.play(Write(prof))

        # --- Bloco de Instruções de Navegação ---
        guia_navegacao = VGroup(
            Tex(r"\textbf{Instruções de navegação:}", font_size=28, color=GREEN_C),
            Tex(r"$\bullet$ Pressione a \textbf{Seta para a Direita} para avançar.", font_size=24),
            Tex(r"$\bullet$ Pressione a \textbf{Seta para a Esquerda} para voltar um slide.", font_size=24),
            Tex(r"$\bullet$ Pressione \textbf{Barra de Espaço} para iniciar o slide atual do começo.", font_size=24),
            Tex(r"$\bullet$ Pressione \textbf{F} para entrar em tela cheia.", font_size=24),
            Tex(r"$\bullet$ Pressione \textbf{ESC} para sair da tela cheia.", font_size=24),
            Tex(r"$\bullet$ Enquanto o símbolo de play estiver invisível, o slide está em movimento.", font_size=24),
            Tex(r"$\bullet$ Quando o símbolo de play aparecer, o slide pode ser avançado.", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(DOWN, buff=1.2)

        self.play(FadeIn(guia_navegacao, shift=UP * 0.3))
        
        self.pausar_com_play()

        # --- SLIDE 2: Criação do segmento e divisão áurea ---
        self.play(FadeOut(guia_navegacao))

        # 1. Definição e construção do segmento AB
        comprimento_total = 7.0
        pt_a = LEFT * (comprimento_total / 2) + UP * 0.2
        pt_b = RIGHT * (comprimento_total / 2) + UP * 0.2
        
        dot_a = Dot(point=pt_a, color=WHITE, radius=0.08)
        dot_b = Dot(point=pt_b, color=WHITE, radius=0.08)
        label_a = Tex("A", font_size=34).next_to(dot_a, DOWN, buff=0.2)
        label_b = Tex("B", font_size=34).next_to(dot_b, DOWN, buff=0.2)
        
        segmento_ab = Line(pt_a, pt_b, stroke_width=4, color=WHITE)

        self.play(
            Create(segmento_ab),
            FadeIn(dot_a, label_a),
            FadeIn(dot_b, label_b),
            run_time=1.2
        )

        # 2. Marcação do ponto C (em extrema e média razão)
        # AC = AB / phi, onde phi = (1 + sqrt(5)) / 2
        phi = (1 + 5**0.5) / 2
        pt_c = pt_a + (pt_b - pt_a) / phi
        
        dot_c = Dot(point=pt_c, color=YELLOW, radius=0.09)
        label_c = Tex("C", font_size=34, color=YELLOW).next_to(dot_c, DOWN, buff=0.2)
        
        # Destaque colorido para o segmento maior AC
        segmento_ac = Line(pt_a, pt_c, stroke_width=5, color=YELLOW)

        self.play(
            Create(segmento_ac),
            FadeIn(dot_c, scale=1.4),
            Write(label_c),
            run_time=1.0
        )

        # 3. Apresentação da expressão matemática
        expressao = MathTex(
            r"\frac{AB}{AC} = \frac{AC}{CB} \implies (AC)^2 = AB \cdot CB",
            font_size=38,
            color=WHITE
        ).shift(DOWN * 1.6)

        self.play(Write(expressao), run_time=1.2)

        # Pausa no final do Slide 2
        self.pausar_com_play()

        # --- SLIDE 3: Construção Geométrica (Prolongamento e Semicírculo) ---
        # Limpeza da expressão e das marcações teóricas do Slide 2
        expressao2 = MathTex(
                    r"(AC)^2 = AB \cdot CB",
                    font_size=20,
                    color=WHITE
                ).shift(DOWN * 1.6)

        self.play(ReplacementTransform(expressao, expressao2), run_time=1.0)
        self.play(
            expressao2.animate.to_corner(UL, buff=0.6).scale(0.85),
            run_time=1.0
        )

        # 2. Animar o deslocamento para cima
        self.play(
            segmento_ab.animate.shift(DOWN * 1.5),
            segmento_ac.animate.shift(DOWN * 1.5),
            dot_a.animate.shift(DOWN * 1.5),
            label_a.animate.shift(DOWN * 1.5),
            dot_b.animate.shift(DOWN * 1.5),
            label_b.animate.shift(DOWN * 1.5),
            dot_c.animate.shift(DOWN * 1.5),
            label_c.animate.shift(DOWN * 1.5),
            run_time=1.5
        )

        expressao4 = MathTex(
            r"(AC)^2 = AB \cdot (AB-AC)",
            font_size=20
        ).next_to(expressao2, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(expressao4), run_time=2.0)

        self.pausar_com_play()

        expressao5 = MathTex(
            r"(AC)^2 = AB \cdot AB -AB \cdot AC",
            font_size=20
        ).next_to(expressao4, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(expressao5), run_time=2.0)

        self.pausar_com_play()

        expressao6 = MathTex(
            r"(AC)^2 + AB \cdot AC - AB \cdot AB =0",
            font_size=20
        ).next_to(expressao5, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(expressao6), run_time=2.0)
        
        self.pausar_com_play()

        expressao7 = MathTex(
            r"(AC)^2 + AB \cdot AC - (AB)^2 =0",
            font_size=20
        ).next_to(expressao6, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(expressao7), run_time=2.0)

        self.pausar_com_play()

        expressao8 = Tex(
            r"Vamos resolver a equação quadrática para encontrar o valor de $AC$ em função de $AB$.",
            font_size=20
        ).next_to(expressao7, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(expressao8), run_time=2.0)

        self.pausar_com_play()

        expressao9 = MathTex(
            r"AC=\frac{-AB \pm \sqrt{(AB)^2 - 4 \cdot [-(AB)^2 ] }}{2}",
            font_size=20
        ).align_to(expressao8, DL)#.next_to(expressao8, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(ReplacementTransform(expressao8, expressao9), run_time=2.0)

        self.pausar_com_play()

        expressao10 = MathTex(
            r"AC=\frac{-AB \pm \sqrt{(AB)^2 + 4 \cdot (AB)^2}}{2}",
            font_size=20
        ).next_to(expressao9, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(expressao10), run_time=2.0)

        self.pausar_com_play()

        expressao11 = MathTex(
            r"AC=\frac{-AB \pm \sqrt{5(AB)^2}}{2}",
            font_size=20
        ).next_to(expressao10, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(expressao11), run_time=2.0)

        self.pausar_com_play()

        expressao12 = MathTex(
            r"AC=\frac{-AB \pm AB \cdot \sqrt{5}}{2}",
            font_size=20
        ).next_to(expressao11, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(expressao12), run_time=2.0)

        self.pausar_com_play()

        expressao12a = Tex(
            r"Podemos descartar a solução negativa.",
            font_size=20
        ).next_to(expressao12, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(Write(expressao12a), run_time=2.0)

        self.pausar_com_play()

        expressao13 = MathTex(
            r"AC=\frac{-AB + AB \cdot \sqrt{5}}{2}",
            font_size=20
        ).align_to(expressao12a, DL)#.next_to(expressao12, DOWN, buff=0.35, aligned_edge=RIGHT)

        self.play(ReplacementTransform(expressao12a, expressao13), run_time=2.0)

        self.pausar_com_play()

        self.play(expressao13.animate.to_corner(UR, buff=0.6).scale(0.85),
                    run_time=2.0
                )

        expressao14 = MathTex(
            r"AC=\frac{AB \cdot \sqrt{5} - AB}{2}",
            font_size=20
        ).next_to(expressao13, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(expressao14), run_time=2.0)

        self.pausar_com_play()

        expressao15 = MathTex(
            r"AC=\frac{AB \cdot (\sqrt{5} - 1)}{2}",
            font_size=20
        ).next_to(expressao14, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(Write(expressao15), run_time=2.0)

        self.pausar_com_play()

        expressao16 = MathTex(
            r"AC=\frac{AB \cdot (\sqrt{5} - 1)}{2}",
            font_size=36
        ).align_to(expressao15, DR)

        self.play(ReplacementTransform(expressao15, expressao16), run_time=2.0)

        self.play(
            FadeOut(expressao2, expressao4, expressao5, expressao6, 
                    expressao7, expressao8, expressao9, expressao10, 
                    expressao11, expressao12, expressao13, expressao14),
            run_time=2.0
        )

        self.play(expressao16.animate.to_corner(UR, buff=0.6),
                    run_time=1.0
                )

        # Reposicionamento suave do segmento AB para acomodar a extensão à esquerda e o semicírculo
        self.play(
            segmento_ab.animate.shift(UP * 1.5),
            segmento_ac.animate.shift(UP * 1.5),
            dot_a.animate.shift(UP * 1.5),
            label_a.animate.shift(UP * 1.5),
            dot_b.animate.shift(UP * 1.5),
            label_b.animate.shift(UP * 1.5),
            dot_c.animate.shift(UP * 1.5),
            label_c.animate.shift(UP * 1.5),
            run_time=1.5
        )

        self.pausar_com_play()

        raio = 2.8
        novo_pt_a = DOWN * 1.2
        novo_pt_b = novo_pt_a + RIGHT * raio
        novo_pt_d = novo_pt_a + LEFT * raio

        novo_segmento_ab = Line(novo_pt_a, novo_pt_b, stroke_width=4, color=WHITE)

        self.play(FadeOut(segmento_ac, dot_c, label_c), run_time=0.5)

        self.play(
            dot_a.animate.move_to(novo_pt_a),
            label_a.animate.next_to(novo_pt_a, DOWN*1.3, buff=0.2),
            dot_b.animate.move_to(novo_pt_b),
            label_b.animate.next_to(novo_pt_b, DOWN*1.3, buff=0.2),
            Transform(segmento_ab, novo_segmento_ab),
            run_time=1.0
        )

        # 1. Ampliação do segmento AB para DB, tal que DA = AB
        dot_d = Dot(point=novo_pt_d, color=WHITE, radius=0.08)
        label_d = Tex("D", font_size=34).next_to(dot_d, DOWN, buff=0.2)
        segmento_da = Line(novo_pt_a, novo_pt_d, stroke_width=4, color=WHITE)

        texto_passo1 = Tex(r"1. Amplia-se $AB$ at\'e $D$, de modo que $DA = AB$", font_size=28, color=YELLOW_C).to_edge(DOWN, buff=1.0)
        
        self.play(
            Create(segmento_da),
            FadeIn(dot_d, label_d),
            Write(texto_passo1),
            run_time=1.2
        )
        self.pausar_com_play()

        # 2. Semicírculo com centro em A passando por D e B
        semicirculo = Arc(
            radius=raio,
            arc_center=novo_pt_a,
            start_angle=-0.08,
            angle=3.3,
            stroke_width=4,
            color=YELLOW
        )
        semicirculo_pontilhado = DashedVMobject(semicirculo, num_dashes=40, color=GRAY_A)

        texto_passo2 = Tex(r"2. Tra\c{c}a-se o semic\'\i rculo com centro em $A$ passando por $D$ e $B$", font_size=28, color=YELLOW_C).to_edge(DOWN, buff=1.0)

        self.play(
            ReplacementTransform(texto_passo1, texto_passo2),
            Create(semicirculo_pontilhado),
            run_time=1.5
        )

        # Pausa no final do Slide 3
        self.pausar_com_play()

        # --- NOVO SLIDE: Pontos E, segmento AE e ponto médio M ---

        # 1. Ponto E no arco com a mesma abscissa de A
        pt_e = novo_pt_a + UP * raio
        dot_e = Dot(point=pt_e, color=WHITE, radius=0.08)
        label_e = Tex("E", font_size=34).next_to(dot_e, UP, buff=0.2)

        # 2. Segmento pontilhado AE
        segmento_ae = DashedLine(novo_pt_a, pt_e, stroke_width=3, color=WHITE)

        texto_passo3 = Tex(
            r"3. Marca-se o ponto $E$ na perpendicular a $AB$ passando por $A$",
            font_size=28,
            color=YELLOW_C
        ).to_edge(DOWN, buff=1.0)

        self.play(
            ReplacementTransform(texto_passo2, texto_passo3),
            Create(segmento_ae),
            FadeIn(dot_e, label_e),
            run_time=1.2
        )
        self.pausar_com_play()
        # 3. Ponto M (ponto médio de DA)
        pt_m = (novo_pt_d + novo_pt_a) / 2
        dot_m = Dot(point=pt_m, color=WHITE, radius=0.08)
        label_m = Tex("M", font_size=34).next_to(dot_m, DOWN, buff=0.2)

        texto_passo4 = Tex(
            r"4. Determina-se $M$, ponto m\'edio de $DA$",
            font_size=28,
            color=YELLOW_C
        ).to_edge(DOWN, buff=1.0)

        self.play(
            ReplacementTransform(texto_passo3, texto_passo4),
            FadeIn(dot_m, label_m),
            run_time=1.0
        )

        # Pausa do slide
        self.pausar_com_play()

        # --- Construção do Triângulo MAE ---

        # Segmentos que completam o triângulo (hipotenusa ME e base MA)
        segmento_me = Line(pt_m, pt_e, stroke_width=3, color=WHITE)
        segmento_ma = Line(pt_m, novo_pt_a, stroke_width=3, color=WHITE)
        segmento_ae2 = Line(novo_pt_a, pt_e, stroke_width=3, color=WHITE)

        # Região interna com preenchimento translúcido suave
        triangulo_mae = Polygon(
            pt_m, novo_pt_a, pt_e,
            stroke_width=0,
            fill_color=BLUE_E,
            fill_opacity=0.3
        )

        # Símbolo do ângulo reto em A (opcional, para clareza geométrica)
        angulo_reto = RightAngle(
            segmento_ae2, segmento_ma,
            length=0.25,
            stroke_width=2,
            color=WHITE
        )

        self.play(
            Create(segmento_me),
            Create(segmento_ae2),
            FadeIn(triangulo_mae),
            Create(angulo_reto),
            run_time=1.2
        )
        texto_passo5 = Tex(
            r"5. Marcamos o triângulo retângulo $MAE$",
            font_size=28,
            color=YELLOW_C
        ).to_edge(DOWN, buff=1.0)

        self.play(
            ReplacementTransform(texto_passo4, texto_passo5),
            FadeIn(dot_m, label_m),
            run_time=1.0
        )

        self.pausar_com_play()

        # --- Rótulos dos lados do triângulo MAE ---
        label_r = MathTex("r", font_size=32, color=YELLOW).next_to(segmento_ae, RIGHT, buff=0.15)
        label_r2 = MathTex(r"\frac{r}{2}", font_size=30, color=YELLOW).next_to(segmento_ma, DOWN, buff=0.15)
        
        # Posicionamento de x ao longo da hipotenusa ME
        label_x = MathTex("x", font_size=32, color=YELLOW).move_to(segmento_me.get_center()).shift(UP * 0.25 + LEFT * 0.25)

        self.play(
            FadeIn(label_r),
            FadeIn(label_r2),
            FadeIn(label_x),
            run_time=0.8
        )
        self.pausar_com_play()

        texto_passo6 = Tex(
            r"6. Aplicamos o Teorema de Pit\'agoras no tri\^angulo $MAE$",
            font_size=28,
            color=YELLOW_C
        ).to_edge(DOWN, buff=1.0)

        self.play(
            ReplacementTransform(texto_passo5, texto_passo6),
            FadeIn(dot_m, label_m),
            run_time=1.0
        )
        
        # Termos elevados ao quadrado
        termo_x2 = MathTex("x^2", font_size=36)
        termo_r2 = MathTex("r^2", font_size=36)
        termo_r2_frac = MathTex(r"\left(\frac{r}{2}\right)^2", font_size=36)

        # Montagem da equação no canto superior esquerdo (abaixo dos títulos)
        # x^2 = r^2 + (r/2)^2
        equacao_pitagoras = VGroup(
            termo_x2,
            MathTex("=", font_size=36),
            termo_r2,
            MathTex("+", font_size=36),
            termo_r2_frac
        ).arrange(RIGHT, buff=0.15).to_corner(UL, buff=0.8)

        # Migração e elevação ao quadrado de cada termo
        self.play(
            TransformMatchingShapes(label_x.copy(), termo_x2),
            run_time=1
        )
        self.play(
            Write(equacao_pitagoras[1]), # sinal de igual
            TransformMatchingShapes(label_r.copy(), termo_r2),
            run_time=1
        )
        self.play(
            Write(equacao_pitagoras[3]), # sinal de mais
            TransformMatchingShapes(label_r2.copy(), termo_r2_frac),
            run_time=1
        )
        self.pausar_com_play()

        # Linha inferior com a simplificação da fração: x^2 = r^2 + r^2/4
        linha_inferior = MathTex(
            r"x^2 = r^2 + \frac{r^2}{4}",
            font_size=36
        ).next_to(equacao_pitagoras, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_inferior), run_time=2.0)

        linha_inferior2 = MathTex(
            r"x^2 = \frac{4r^2}{4} + \frac{r^2}{4}",
            font_size=36
        ).next_to(linha_inferior, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_inferior2), run_time=2.0)

        linha_inferior3 = MathTex(
            r"x^2 = \frac{4r^2 + r^2}{4}",
            font_size=36
        ).next_to(linha_inferior2, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_inferior3), run_time=2.0)

        linha_inferior4 = MathTex(
            r"x^2 = \frac{5r^2}{4}",
            font_size=36
        ).next_to(linha_inferior3, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_inferior4), run_time=2.0)

        linha_inferior5 = MathTex(
            r"x = \frac{r \cdot \sqrt{5}}{2}",
            font_size=36
        ).next_to(linha_inferior4, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_inferior5), run_time=2.0)

        self.pausar_com_play()

        self.play(FadeOut(equacao_pitagoras, linha_inferior, linha_inferior2, linha_inferior3, linha_inferior4), run_time=2.0)

        self.play(linha_inferior5.animate.to_corner(UL, buff=0.6), run_time=1.0)

        linha_inferior6 = MathTex(
            r"x = \frac{AB \cdot \sqrt{5}}{2}",
            font_size=36
        ).next_to(linha_inferior5, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_inferior6), run_time=2.0)

        self.wait(1)

        self.play(
            FadeOut(linha_inferior5),
            linha_inferior6.animate.to_corner(UL, buff=0.6), 
            run_time=2.0
            )

        self.pausar_com_play()

        # --- Arco centrado em M com raio ME passando por E e C ---

        # Vetor de M até E e cálculo do raio (comprimento da hipotenusa ME)
        vetor_me = pt_e - pt_m
        raio_me = np.linalg.norm(vetor_me)
        angulo_e = np.arctan2(vetor_me[1], vetor_me[0]) + 0.2

        # O ponto C localiza-se sobre a reta horizontal à direita de M:
        # C = M + (raio_me, 0, 0), portanto o ângulo no ponto C é 0 radianos
        pt_c = pt_m + RIGHT * raio_me
        dot_c = Dot(point=pt_c, color=YELLOW, radius=0.08)
        label_c = Tex("C", font_size=34, color=YELLOW).next_to(dot_c, DL, buff=0.2)

        # Construção do arco pontilhado que vai de E até C (sentido horário: ângulo negativo)
        arco_base_mc = Arc(
            radius=raio_me,
            arc_center=pt_m,
            start_angle=angulo_e,
            angle=-angulo_e-0.2,
            stroke_width=2.5,
            color=YELLOW_C
        )
        arco_me_c = DashedVMobject(arco_base_mc, num_dashes=30, color=BLUE)

        # Texto explicativo da etapa
        texto_passo7 = Tex(
            r"7. Com centro em $M$ e raio $ME$, tra\c{c}a-se o arco que determina $C$",
            font_size=28,
            color=YELLOW_C
        ).to_edge(DOWN, buff=1.0)

        self.play(
            FadeOut(label_r2, label_r),
            ReplacementTransform(texto_passo6, texto_passo7),
            Create(arco_me_c),
            run_time=1.4
        )
        self.play(
            FadeIn(dot_c, label_c),
            run_time=0.8
        )
        self.pausar_com_play()

        texto_passo8 = Tex(
            r"8. $MC = ME = x$",
            font_size=28,
            color=YELLOW_C
        ).to_edge(DOWN, buff=1.0)

        self.play(
            FadeOut(segmento_ma, segmento_ae2, triangulo_mae, angulo_reto),
            ReplacementTransform(texto_passo7, texto_passo8),
            run_time=2.0
        )

        # 1. Transforma label_x em MC (verde), mantendo rigorosamente a mesma posição
        label_mc = MathTex("MC", font_size=32, color=GREEN).move_to(label_x.get_center())
        self.play(
            ReplacementTransform(label_x, label_mc),
            run_time=1.0
        )

        self.wait(0.5)

        # 2. Torna o segmento_me verde mantendo sua posição geométrica
        self.play(
            segmento_me.animate.set_color(GREEN).set_stroke(width=4),
            run_time=1.0
        )

        self.wait(0.5)

        # 3. Rotaciona segmento_me em torno de M
        # O ângulo para coincidir com a horizontal (ponto C) é exatamente o ângulo polar de ME negativo
        angulo_rotacao = -np.arctan2(pt_e[1] - pt_m[1], pt_e[0] - pt_m[0])
        self.play(
            Rotate(segmento_me, angle=angulo_rotacao, about_point=pt_m),
            run_time=1.5
        )

        self.wait(0.5)

        # 4. Reposiciona o rótulo MC acima do segmento já deitado
 
        self.play(
            label_mc.animate.next_to(segmento_me, UP, buff=0.15).shift(RIGHT * 0.3),
            run_time=1.0
        )

        self.pausar_com_play()

        linha_MC1 = MathTex(
            r"MC = MA + AC",
            font_size=28
        ).next_to(linha_inferior6, DOWN, buff=1, aligned_edge=LEFT)

        self.play(Write(linha_MC1), run_time=2.0)

        self.pausar_com_play()

        linha_MC2 = MathTex(
            r"\frac{AB \cdot \sqrt{5}}{2} = \frac{AB}{2} + AC",
            font_size=28
        ).next_to(linha_MC1, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_MC2), run_time=2.0)

        self.pausar_com_play()

        linha_MC3 = MathTex(
            r"AC = \frac{AB \cdot \sqrt{5}}{2} - \frac{AB}{2}",
            font_size=28
        ).next_to(linha_MC2, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_MC3), run_time=2.0)

        self.pausar_com_play()

        linha_MC4 = MathTex(
            r"AC = \frac{AB \cdot \sqrt{5}-AB}{2}",
            font_size=28
        ).next_to(linha_MC3, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_MC4), run_time=2.0)

        self.pausar_com_play()

        linha_MC5 = MathTex(
            r"AC = \frac{AB \cdot (\sqrt{5}-1)}{2}",
            font_size=36
        ).next_to(linha_MC4, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_MC5), run_time=2.0)

        self.pausar_com_play()

        self.play(
            linha_MC5.animate.to_corner(UR, buff=0.6),
            run_time=2.0
        )

        self.pausar_com_play()

        self.play(
            FadeOut(linha_inferior6, linha_MC1, linha_MC2, linha_MC3, linha_MC4, expressao16, arco_me_c, dot_m, label_m, dot_e, label_e, dot_d, label_d, segmento_da, semicirculo_pontilhado, segmento_me, label_mc, segmento_ae, texto_passo8),
            run_time=2.0
        )

        # Fator de escala desejado e nova posição central do segmento
        fator_escala = 2.5
        novo_centro = ORIGIN + UP * 1.5

        # 1. Cria a linha com a nova escala e posição
        novo_segmento = segmento_ab.copy().scale(fator_escala).move_to(novo_centro)

        # 2. Obtém as novas posições das extremidades A e B
        novo_ponto_a = novo_segmento.get_start()
        novo_ponto_b = novo_segmento.get_end()

        # 3. Calcula a nova posição de C mantendo a mesma razão de divisão
        phi = (1 + 5**0.5) / 2
        novo_ponto_c = novo_ponto_a + (novo_ponto_b - novo_ponto_a) / phi

        # 4. Animação coordenada: o segmento amplia, mas os pontos e rótulos apenas se movem
        self.play(
            Transform(segmento_ab, novo_segmento),
            dot_a.animate.move_to(novo_ponto_a),
            label_a.animate.next_to(novo_ponto_a, DOWN, buff=0.2),
            dot_b.animate.move_to(novo_ponto_b),
            label_b.animate.next_to(novo_ponto_b, DOWN, buff=0.2),
            dot_c.animate.move_to(novo_ponto_c),
            label_c.animate.next_to(novo_ponto_c, DOWN, buff=0.2),
            run_time=2
        )

        segmento_razao = VGroup(
            segmento_ab,
            dot_a, label_a,
            dot_b, label_b,
            dot_c, label_c
        )

        linha_MC6 = Tex(
            r"A razão áurea é dada por: $\frac{AB}{AC}$",
            font_size=28
        ).to_corner(UL, buff=0.8)

        self.play(Write(linha_MC6), run_time=2.0)

        linha_MC61 = MathTex(
            r"AC = \frac{AB \cdot (\sqrt{5}-1)}{2}",
            font_size=28
        ).next_to(linha_MC6, DOWN, buff=0.35, aligned_edge=LEFT)

        self.pausar_com_play()

        linha_MC7 = MathTex(
            r"\frac{AC}{AB} = \frac{\sqrt{5}-1}{2}",
            font_size=28
        ).next_to(linha_MC61, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_MC61), run_time=2.0)

        self.pausar_com_play()

        self.play(Write(linha_MC7), run_time=2.0)

        self.pausar_com_play()

        linha_MC8 = MathTex(
            r"\frac{AB}{AC} = \frac{2}{\sqrt{5}-1}",
            font_size=28
        ).next_to(linha_MC7, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_MC8), run_time=2.0)

        self.pausar_com_play()

        linha_MC9 = MathTex(
            r"\frac{AB}{AC} = \frac{2}{\sqrt{5}-1} \cdot \frac{\sqrt{5}+1}{\sqrt{5}+1}",
            font_size=28
        ).next_to(linha_MC8, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_MC9), run_time=2.0)

        self.pausar_com_play()

        linha_MC10 = MathTex(
            r"\frac{AB}{AC} = \frac{2 \cdot (\sqrt{5}+1)}{(\sqrt{5}-1) \cdot (\sqrt{5}+1)}",
            font_size=28
        ).next_to(linha_MC9, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_MC10), run_time=2.0)

        self.pausar_com_play()

        linha_MC11 = MathTex(
            r"\frac{AB}{AC} = \frac{2 \cdot (\sqrt{5}+1)}{5 - 1}",
            font_size=28
        ).next_to(segmento_razao, DOWN, buff=0.35, aligned_edge=RIGHT)

        linha_MC12 = MathTex(
            r"\frac{AB}{AC} = \frac{2 \cdot (\sqrt{5}+1)}{4}",
            font_size=28
        ).next_to(linha_MC11, DOWN, buff=0.35, aligned_edge=LEFT)

        linha_MC13 = MathTex(
            r"\frac{AB}{AC} = \frac{\sqrt{5}+1}{2} = \phi",
            font_size=28
        ).next_to(linha_MC12, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Write(linha_MC11), run_time=2.0)

        self.pausar_com_play()

        self.play(Write(linha_MC12), run_time=2.0)

        self.pausar_com_play()

        self.play(Write(linha_MC13), run_time=2.0)

        self.pausar_com_play()

        self.play(
            FadeOut(linha_MC5, linha_MC6, linha_MC61, linha_MC7, linha_MC8, linha_MC9, linha_MC10, linha_MC11, linha_MC12, linha_MC13),
            run_time=2.0
        )

        self.play(
            segmento_razao.animate.move_to(ORIGIN),
            run_time=2
        )

        texto_final = Tex(
            r"Portanto, a Razão Áurea é $\phi =\frac{AB}{AC} = \frac{\sqrt{5}+1}{2}$.  $\square$.",
            font_size=45,
            color=YELLOW_C
        ).to_edge(DOWN, buff=1.0)

        self.play(Write(texto_final), run_time=2)

        self.pausar_com_play()
