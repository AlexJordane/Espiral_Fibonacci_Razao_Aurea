from manim import *
from manim_slides import Slide
import numpy as np

class EspiralFibonacci(Slide, MovingCameraScene):
    def construct(self):
        # 1. Parâmetros de cada etapa baseados no seu TikZ:
        # (lado, canto_inferior_esquerdo, canto_superior_direito, centro_arco, angulo_inicio, angulo_fim, raio)
        etapas = [
            {
                "lado": 1,
                "box": [(0, 0), (1, 1)],
                "centro": (1, 1),
                "ang_ini": PI,
                "ang_fim": 3 * PI / 2,
                "raio": 1,
            },
            {
                "lado": 1,
                "box": [(1, 0), (2, 1)],
                "centro": (1, 1),
                "ang_ini": -PI / 2,
                "ang_fim": 0,
                "raio": 1,
            },
            {
                "lado": 2,
                "box": [(0, 1), (2, 3)],
                "centro": (0, 1),
                "ang_ini": 0,
                "ang_fim": PI / 2,
                "raio": 2,
            },
            {
                "lado": 3,
                "box": [(-3, 0), (0, 3)],
                "centro": (0, 0),
                "ang_ini": PI / 2,
                "ang_fim": PI,
                "raio": 3,
            },
            {
                "lado": 5,
                "box": [(-3, -5), (2, 0)],
                "centro": (2, 0),
                "ang_ini": PI,
                "ang_fim": 3 * PI / 2,
                "raio": 5,
            },
            {
                "lado": 8,
                "box": [(2, -5), (10, 3)],
                "centro": (2, 3),
                "ang_ini": -PI / 2,
                "ang_fim": 0,
                "raio": 8,
            },
            {
                "lado": 13,
                "box": [(-3, 3), (10, 16)],
                "centro": (-3, 3),
                "ang_ini": 0,
                "ang_fim": PI / 2,
                "raio": 13,
            },
            {
                "lado": 21,
                "box": [(-24, -5), (-3, 16)],
                "centro": (-3, -5),
                "ang_ini": PI / 2,
                "ang_fim": PI,
                "raio": 21,
            },
        ]

        # 2. Configuração inicial da câmera focada no primeiro quadrado
        self.camera.frame.set(width=7)
        self.camera.frame.move_to(np.array([0.5, 0.5, 0]))

        # Malha de fundo pontilhada / discreta

        # Limites cobrindo com folga de segurança toda a trajetória até o lado 21
        x_min, x_max = -26, 12
        y_min, y_max = -8, 18
        largura_total = x_max - x_min
        altura_total = y_max - y_min

        malha = NumberPlane(
            x_range=[x_min, x_max, 1],
            y_range=[y_min, y_max, 1],
            x_length=largura_total,
            y_length=altura_total,
            background_line_style={
                "stroke_color": GRAY_C,
                "stroke_width": 1.2,
                "stroke_opacity": 0.35,
            },
            axis_config={"stroke_opacity": 0},
        )
        # Garante que a coordenada matemática (0,0) do plano coincida perfeitamente com o ponto (0,0,0) da cena
        malha.shift(-malha.c2p(0, 0))
        self.add(malha)

        # Marcador do ponto inicial (1, 1)
        ponto_inicial = Dot(np.array([1.0, 1.0, 0]), radius=0.08, color=RED)
        self.play(FadeIn(ponto_inicial), run_time=0.8)

        quadrados_construidos = VGroup()
        arcos_construidos = VGroup()

        # 3. Execução passo a passo
        for i, info in enumerate(etapas):
            x1, y1 = info["box"][0]
            x2, y2 = info["box"][1]
            largura = x2 - x1
            altura = y2 - y1
            centro_box = np.array([(x1 + x2) / 2.0, (y1 + y2) / 2.0, 0])

            # Criação do retângulo/quadrado
            quadrado = Rectangle(
                width=largura,
                height=altura,
                stroke_color=WHITE,
                stroke_width=2.5,
                fill_color=BLUE_E,
                fill_opacity=0.15,
            ).move_to(centro_box)

            # Rótulo com o valor de Fibonacci no centro
            rotulo = MathTex(str(info["lado"]), font_size=28, color=YELLOW).move_to(centro_box)

            # Criação do arco correspondente
            cx, cy = info["centro"]
            arco = Arc(
                radius=info["raio"],
                start_angle=info["ang_ini"],
                angle=info["ang_fim"] - info["ang_ini"],
                arc_center=np.array([cx, cy, 0]),
                stroke_color=RED,
                stroke_width=4.0,
            )

            # Ajuste de enquadramento da câmera considerando altura e largura (16:9)
            if i >= 2:
                grupo_total = VGroup(quadrados_construidos, quadrado, arco)
                
                # Margem de segurança de 30% ao redor da figura acumulada
                fator_margem = 1.30
                largura_necessaria = grupo_total.width * fator_margem
                altura_necessaria = grupo_total.height * fator_margem

                # Converte a altura necessária para a largura correspondente em 16:9
                largura_pela_altura = altura_necessaria * (16.0 / 9.0)

                # Escolhe a maior dimensão para evitar qualquer corte horizontal ou vertical
                alvo_largura = max(largura_necessaria, largura_pela_altura, 7.0)
                alvo_centro = grupo_total.get_center()

                self.play(
                    self.camera.frame.animate.set(width=alvo_largura).move_to(alvo_centro),
                    Create(quadrado),
                    Write(rotulo),
                    run_time=1.2,
                )
            else:
                self.play(Create(quadrado), Write(rotulo), run_time=0.9)

            # Traçado contínuo do arco
            self.play(Create(arco), run_time=1.0)

            quadrados_construidos.add(quadrado, rotulo)
            arcos_construidos.add(arco)

        self.wait(2)