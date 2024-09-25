from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr"

def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'company'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[-1]

    assert row1["id"] == 115
    assert row1["name"] == "Шиномонтаж на Ленинском"

def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")

    rows = db.execute(sql_statement, company_id = 112).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == "Кондитерская Профи-тролли"


def test_select_1_row_with_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"isActive\" = :isActive and id >= :id")

    my_params = {
        'id': 113,
        'isActive': True
    }
    rows = db.execute(sql_statement, my_params).fetchall()

    assert len(rows) == 2

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into company(\"name\") values (:new_name)")

    rows = db.execute(sql, new_name = 'SkyPro')
    
def test_update():
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr where id = :id")
    db.execute(sql, descr = 'New descr', id = 163)

def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    db.execute(sql, id = 163)