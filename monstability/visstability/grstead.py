"""
Модуль расчета устойчивости и формирования сигналов отклонений
Допущения:
    Граф устойчивости направленный.
    Обход графа начинается с узлов метрик.
    Ребра имеют веса.
Ограничения:
    Узлы графа содержат атрибуты:
        'type':string - тип узла
            'metric' - узел метрики
            'service' - узел сервиса
            'and' - узел логического И
            'or' - улел логического ИЛИ
        'access':integer - текущая доступность
        'stead':float - текущая устойчивость
    Ребра графа содержат свойство:
        'weight':float - вес ребра (коэффициент передачи сигнала)
"""

import networkx as nx

TYPE_METRIC = 'metric'
TYPE_SERVICE = 'service'
TYPE_AND = 'and'
TYPE_OR = 'or'

class GStead:
    """Класс графа устойчивости и доступности """

    G = None    # граф класса
    nodesid_metric = []   # список нод с метриками

    def __init__(self):
        self.G = nx.DiGraph()

    def read_gexf(self, path):
        """ загрузка графа из файла GEXF """
        self.G = nx.read_gexf(path)

        # self.nodesid_metric.clear()
        # for node in self.G.nodes.data():    # обход по нода
        #     if node[1]['type'] == TYPE_METRIC:    # тип ноды 'metric'
        #         self.nodesid_metric.append(node[0])   # добавляем id ноды в список нод метрик

    def write_gexf(self, path):
        """ выгрузка графа в файла GEXF """
        nx.write_gexf(self.G, path)

    def calc_node_stead(self, node_id):
        """ пересчет устойчивости ноды """
        edge_list = list(nx.edge_bfs(self.G, node_id))  # обход в ширину для узла node
        for u, v in edge_list:  # перебор всех ребер текущей ноды
            nu_stead = self.G.nodes[u]['stead']  # текущая устойчивость ноды u
            nu_access = self.G.nodes[u]['access']  # текущая доступность ноды u
            nv_stead = self.G.nodes[v]['stead']  # текущая устойчивость ноды v
            nv_access = self.G.nodes[v]['access']  # текущая доступность ноды v
            weight = self.G[u][v]['weight']  # вес ребра u,v
            print(f'before: ({u})--{weight}-->({v}) : ({u})stead={nu_stead} ({v})stead={nv_stead} :'
                  f' ({u})access={nu_access} ({v})access={nv_access}')

            self._calc_stead(node_id=v)
            self._calc_access(node_id=v)

            nu_stead = self.G.nodes[u]['stead']  # текущая устойчивость ноды u
            nu_access = self.G.nodes[u]['access']  # текущая доступность ноды u
            nv_stead = self.G.nodes[v]['stead']  # текущая устойчивость ноды v
            nv_access = self.G.nodes[v]['access']  # текущая доступность ноды v
            print(f'after: ({u})--{weight}-->({v}) : ({u})stead={nu_stead} ({v})stead={nv_stead} :'
                  f' ({u})access={nu_access} ({v})access={nv_access}')
            print()

    def calc_metrics_stead(self):
        """ пересчет устойчивости по всем нодам метрик"""
        for node_id in self.nodesid_metric:
            self.calc_node_stead(node_id)

    def _calc_stead(self, node_id):
        """функция расчета устойчивости ноды"""
        lst_in_edges = list(self.G.in_edges(node_id))   # список входящих ребер
        stead = 0;
        for u,v in lst_in_edges:
            stead += self.G.nodes[u]['stead'] * self.G[u][v]['weight']  # сумма устойчивости входящих нод умноженный на вес ребра
        self.G.nodes[node_id]['stead'] = stead  # обновление устойчивости текущей ноды

    def _calc_access(self, node_id):
        """функция расчета доступности ноды"""
        lst_in_edges = list(self.G.in_edges(node_id))   # список входящих ребер
        access = 1;
        for u,v in lst_in_edges:
            if self.G.nodes[v]['type'] == TYPE_OR:
                access = access or self.G.nodes[u]['access']    # ИЛИ доступностей входящих узлов
            else:
                access = access and self.G.nodes[u]['access']     # И доступностей входящих узлов
        self.G.nodes[node_id]['access'] = access  # обновление доступности текущей ноды

if __name__ == '__main__':
    pass
    # gs = GStead()
    # gs.read_gexf("monstability_model_1.xml")
    # gs.calc_metrics_stead()
    # gs.calc_node_stead('2')