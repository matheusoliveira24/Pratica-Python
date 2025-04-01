from model.database import Database

class Tarefa:
    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao 
        

    def salvarTarefa(self): 
        """Salva uma nova tarefa no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusao)

        db.executar(sql, params)
        db.desconectar()
    @staticmethod
    def listarTarefa():
        """Retornar uma lista com todas as tarefas cadastradas."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []
    @staticmethod
    def apagarTarefa(idTarefa):
        """Apagar uma tarefa cadastrada no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (idTarefa,) # Precisa passar como tupla (a, b, c, ...)
        db.executar(sql, params)
        db.desconectar()
    
    def atualizarTarefa(self):
        db = Database()
        db.conectar()
        sql = 'UPDATE tarefa SET titulo = %s,  data_conclusao = %s, WHERE id = %s'
        params = (self.id, self.titulo, self.data_conclusao, )
        db.executar(sql, params)
        db.desconectar()

    