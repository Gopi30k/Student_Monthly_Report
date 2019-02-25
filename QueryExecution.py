import DbConnection as D
import logging
def DBQueryExecution( Query):
    try:
        D.crsr.execute(Query)
        D.db.commit()
    except Exception:
        logging.info("Queries not Executed")


def SELECTQueryExe(SelQuery):

    D.crsr.execute(SelQuery)
    res = D.crsr.fetchall()
    return res
def SELECTQueryExe1(SelQuery,dated):
    SelQuery+=dated
    D.crsr.execute(SelQuery)
    header = [i[0] for i in D.crsr.description]
    res = D.crsr.fetchall()
    res.insert(0, header)
    return res