import database as db
import pandas as pd
import config
def test_login():
    assert config.password=='1234'
    
def test_redundancies():
    verify = True
    conn, c = db.connection()
    with conn:
        c.execute(
            """
            SELECT id
            FROM prescription_record;
            """
        )
    presciption_id_list=[id[0] for id in c.fetchall()]
    for presciption_id in presciption_id_list:
        if (presciption_id_list.count(presciption_id))>1:
            verify = False
            break
    conn.close()
    assert verify


def test_foriegn_key_constraits():
    conn, c = db.connection()
    verify=True
    with conn:
        c.execute(
            """
            SELECT department_id
            FROM doctor_record;
            """
        )
    doctor_deprt_id_list =[did[0] for did in c.fetchall()]
    conn.close()

    conn, c = db.connection()
    with conn:
        c.execute(
            """
            SELECT id
            FROM department_record;
            """
        )
    deprt_id_list=[did[0]for did in c.fetchall()]
    conn.close()
    for id in doctor_deprt_id_list:
        if id not in deprt_id_list:
            verify=False
            break
    assert verify







    
