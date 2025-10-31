from sqlalchemy.orm import Session
from sqlalchemy import MetaData, Table, select, text

class QueryService:

    def __init__(self, db: Session):
        self.db = db
        self.metadata = MetaData()
        print(self.metadata)

    def select_all(self, table: str) -> list[dict]:
        try:
            # Note o `Table` sendo chamado com a engine para reflexão
            table_obj = Table(table, self.metadata, autoload_with=self.db.get_bind())

        except Exception:
             # Trata erro se a tabela não existir no banco
            raise ValueError(f"A tabela '{table}' não foi encontrada no banco de dados.")
        
        command = select(table_obj)

        result = self.db.execute(command)
        
        return [dict(row) for row in result.mappings().all()]
    
    