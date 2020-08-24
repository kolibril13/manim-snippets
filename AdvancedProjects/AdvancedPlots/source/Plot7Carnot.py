from manim import *


class CarnotProcess(GraphScene):
    CONFIG = {

        "x_min": 0.5,
        "x_max": 4,
        "x_axis_width": 9,
        "x_axis_label": "$V$",
        "x_tick_frequency": 3.5,

        "y_min": 0,
        "y_max": 40,
        "y_tick_frequency": 1,
        "y_axis_label": "$P$",  # note: to make this black as well, change the default color of TextMobject (in the sourcecode)

        "graph_origin": 3 * DOWN + 6.5 * LEFT,
        "function_color": RED,
        "axes_color": GREY,

        "x_label_direction": RIGHT,
        "y_label_direction": LEFT,
    }

    def construct(self):

        R = 8.314
        self.setup_axes(animate=False)
        self.x_axis_label_mob.shift(0.5 * LEFT * abs(self.y_axis[0].points[0] - self.x_axis[0].points[0]))
        self.x_axis.shift(LEFT * abs(self.y_axis[0].points[0] - self.x_axis[0].points[0]))
        import matplotlib.pyplot as plt
        from scipy.constants import zero_Celsius
        plt.rcParams['figure.dpi'] = 150

        Tmax = zero_Celsius + 150
        Tmin = zero_Celsius + 20
        R = 8.314
        kappa = 5 / 3
        V1 = 1
        V2 = 2

        p1 = R * Tmax / V1
        p2 = p1 * V1 / V2

        V3 = (Tmax / Tmin * V2 ** (kappa - 1)) ** (1 / (kappa - 1))
        p3 = p2 * V2 ** kappa / V3 ** kappa

        V4 = (Tmax / Tmin * V1 ** (kappa - 1)) ** (1 / (kappa - 1))
        p4 = p3 * V3 / V4

        def p_isotherm(V, T):
            return (R * T) / V

        def p_adiabatisch(V, p_start, v_start):
            return (p_start * v_start ** kappa) / V ** kappa

        isotherm12_graph = self.get_graph(lambda x: p_isotherm(x, Tmax) * 0.01, x_min=V1, x_max=V2, color=BLACK)
        adiabatisch23_graph = self.get_graph(lambda x: p_adiabatisch(x, p2, V2) * 0.01, x_min=V2, x_max=V3, color=BLACK)
        isotherm34_graph = self.get_graph(lambda x: p_isotherm(x, Tmin) * 0.01, x_min=V3, x_max=V4, color=BLACK)
        adiabatisch41_graph = self.get_graph(lambda x: p_adiabatisch(x, p4, V4) * 0.01, x_min=V4, x_max=V1, color=BLACK)

        isotherm12_graph_over = self.get_graph(lambda x: p_isotherm(x, Tmax) * 0.01, x_min=V1 - 0.1, x_max=V2 + 0.5,
                                               color=RED, stroke_opacity=0.5)
        isotherm12_graph_over_Text = TexMobject(r" \text{T}_{\text{max}}").scale(0.7).next_to(isotherm12_graph_over,
                                                                                              RIGHT, aligned_edge=DOWN,
                                                                                              buff=0).set_color(BLACK)
        self.add(isotherm12_graph_over, isotherm12_graph_over_Text)

        isotherm34_graph_over = self.get_graph(lambda x: p_isotherm(x, Tmin) * 0.01, x_min=V3 + 0.3, x_max=V4 - 0.5,
                                               color=BLUE, stroke_opacity=0.5)
        isotherm34_graph_over_Text = TexMobject(r"\text{T}_{\text{min}}").scale(0.7).next_to(isotherm34_graph_over,
                                                                                             RIGHT, aligned_edge=DOWN,
                                                                                             buff=0).set_color(BLACK)
        self.add(isotherm34_graph_over, isotherm34_graph_over_Text)

        upper_graph = self.get_graph(
            lambda x: p_isotherm(x, Tmax) * 0.01 if x < V2 else p_adiabatisch(x, p2, V2) * 0.01)
        lower_graph = self.get_graph(
            lambda x: p_adiabatisch(x, p4, V4) * 0.01 if x < V4 else p_isotherm(x, Tmin) * 0.01)
        area_in_bewtween = self.get_area(upper_graph, V1, V3, bounded=lower_graph, dx_scaling=0.2)
        self.add(area_in_bewtween)
        upper_graph.get_function()

        def work_out(x):
            return p_isotherm(x, Tmax) if x < V2 else p_adiabatisch(x, p2, V2)

        def work_in(x):
            return p_adiabatisch(x, p4, V4) if x < V4 else p_isotherm(x, Tmin)

        from scipy.integrate import quad

        oben = quad(work_out, V1, V3)[0]
        print(f"Arbeit raus {oben=:.2f}")
        unten = quad(work_in, V3, V1)[0]
        print(f"Arbeit rein {unten=:.2f}")

        self.add(isotherm12_graph, adiabatisch23_graph, isotherm34_graph, adiabatisch41_graph)
        self.wait(0.1)

        def get_y_value(input_tracker, graph):
            return graph.underlying_function(get_x_value(input_tracker))

        def get_graph_point(input_tracker, graph):
            return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker, graph))

        def get_x_value(input_tracker):
            return input_tracker.get_value()

        def get_x_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), 0)

        def get_v_line(input_tracker, graph):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker, graph),
                              stroke_width=2).set_color(BLACK)

        input_tracker_p1 = ValueTracker(V1)
        v_line_p1 = get_v_line(input_tracker_p1, isotherm12_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1, isotherm12_graph))
        x_label_p1 = TexMobject("{ V }_{ 1 }").set_color(BLACK)
        x_label_p1.next_to(v_line_p1, DOWN)
        self.add(v_line_p1, graph_dot_p1, x_label_p1)
        num1 = TexMobject(r"{\large \textcircled{\small 1}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1, RIGHT, buff=0.4 * SMALL_BUFF)
        self.add(v_line_p1, graph_dot_p1, x_label_p1, num1)

        input_tracker_p1 = ValueTracker(V2)
        v_line_p1 = get_v_line(input_tracker_p1, adiabatisch23_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1, adiabatisch23_graph))
        x_label_p1 = TexMobject("{ V }_{ 2 }").set_color(BLACK)
        x_label_p1.next_to(v_line_p1, DOWN)
        num1 = TexMobject(r"{\large \textcircled{\small 2}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1, UP, buff=0.4 * SMALL_BUFF)
        self.add(v_line_p1, graph_dot_p1, x_label_p1, num1)

        input_tracker_p1 = ValueTracker(V3)
        v_line_p1 = get_v_line(input_tracker_p1, isotherm34_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1, isotherm34_graph))
        x_label_p1 = TexMobject("{ V }_{ 3 }").set_color(BLACK)
        x_label_p1.next_to(v_line_p1, DOWN)
        self.add(v_line_p1, graph_dot_p1, x_label_p1)
        num1 = TexMobject(r"{\large \textcircled{\small 3}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1, UP, buff=0.4 * SMALL_BUFF)
        self.add(v_line_p1, graph_dot_p1, x_label_p1, num1)

        input_tracker_p1 = ValueTracker(V4)
        v_line_p1 = get_v_line(input_tracker_p1, adiabatisch41_graph)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1, adiabatisch41_graph))
        x_label_p1 = TexMobject("{ V }_{ 4 }").set_color(BLACK)
        x_label_p1.next_to(v_line_p1, DOWN)
        num1 = TexMobject(r"{\large \textcircled{\small 4}} ").set_color(BLACK).scale(0.7)
        num1.next_to(graph_dot_p1, DOWN + LEFT, buff=-0.3 * SMALL_BUFF)
        self.add(v_line_p1, graph_dot_p1, x_label_p1, num1)

        # annotation:
        ddd = TexMobject(r"\Delta W").next_to(graph_dot_p1, UP).scale(0.7).set_color(BLACK)
        self.add(ddd)
        input_tracker_Q = ValueTracker(V1 + (V2 - V1) / 2)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_Q, isotherm12_graph))
        # self.add(graph_dot_p1)
        aa = Arrow(graph_dot_p1.get_center() + UR * 0.5, graph_dot_p1.get_center(), buff=0).set_color(BLACK)
        self.add(aa)
        ddd = TexMobject(r"\Delta Q_a").scale(0.7).set_color(BLACK)
        self.add(ddd.next_to(graph_dot_p1.get_center() + UR * 0.5, UP, buff=0))

        input_tracker_Q2 = ValueTracker(V3 + (V4 - V3) / 2)
        graph_dot_p1 = Dot(color=BLACK)
        graph_dot_p1.move_to(get_graph_point(input_tracker_Q2, isotherm34_graph))
        # self.add(graph_dot_p1)
        aa = Arrow(graph_dot_p1.get_center(), graph_dot_p1.get_center() + DL * 0.5, buff=0).set_color(BLACK)
        self.add(aa)
        ddd = TexMobject(r"\Delta Q_{ab}").scale(0.7).set_color(BLACK)
        self.add(ddd.next_to(graph_dot_p1.get_center() + DL * 0.5, DOWN, buff=0.05))

        sourunding_dot = Dot().scale(1.3).set_fill(color=BLACK).set_z_index(-1)
        innerdot = Dot().set_color(WHITE).scale(1)
        moving_dot = VGroup(sourunding_dot, innerdot)
        moving_dot.move_to(graph_dot_p1.get_center())
        self.add(moving_dot)


from pathlib import Path

if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l  -s -p -c 'WHITE'  " + script)