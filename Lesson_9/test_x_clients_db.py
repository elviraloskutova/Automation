from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

api = CompanyApi("https://x-clients-be.onrender.com")
db = CompanyTable(db_connection_string = "postgresql://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")

def test_get_companies():
    api_result = api.get_company_list() # шаг 1 - получить список из api
    db_result = db.get_companies() # шаг 2 - получить список из БД
    assert len(api_result) == len(db_result) # шаг 3 - прверить, что списки равны

def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={'active' : 'true'})
    db_list = db.get_active_companies()
    assert len(filtered_list) == len(db_list)

def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)

    assert len_after - len_before == 1
    for company in body:
        if company["id"] == new_id:
            assert company["name"] == name
            assert company["description"] == descr
            assert company["id"] == new_id

def test_get_one_company():
    # подготовка 
    name = 'SkyPro'
    db.create(name)
    max_id = db.get_max_id()

    # главное действие
    new_company = api.get_company(max_id)

    # пост
    db.delete(max_id)

    assert new_company["id"] == max_id
    assert new_company["name"] == name
    # доработать db.create так, чтобы в базу пробрасывалось описание
    #assert new_company["description"] == descr
    assert new_company["isActive"] == True
