import traceback


def bulk_insert_prefecture_data(pool, data, upsert=True):

    """'Prefecture', 'Cases', 'Recovered', 'Deaths'"""

    connection = pool.connection()

    if upsert:
        sql_statement = "INSERT INTO `curw_corona`.`prefecture_data` (`Prefecture`,`time`,`Cases`,`Recovered`,`Deaths`) " \
                        "VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE " \
                        "`Cases` = VALUES(`Cases`),`Recovered` = VALUES(`Recovered`),`Deaths` = VALUES(`Deaths`);"

    else:
        sql_statement = "INSERT INTO `curw_corona`.`prefecture_data` (`Prefecture`,`time`,`Cases`,`Recovered`,`Deaths`) " \
                        "VALUES (%s,%s,%s,%s,%s);"

    print(sql_statement)

    try:
        with connection.cursor() as cursor:

            row_count = cursor.executemany(sql_statement, data)

        connection.commit()
        return row_count
    except Exception as exception:
        connection.rollback()
        traceback.print_exc()
    finally:
        if connection is not None:
            connection.close()
