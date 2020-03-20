import traceback


def insert_summary(pool, data, upsert=True):

    connection = pool.connection()

    if upsert:
        sql_statement = "INSERT INTO `curw_corona`.`summary` (`label`,`count`) VALUES " \
                        "(%s,%s) ON DUPLICATE KEY UPDATE `count` = VALUES(`count`);"

    else:
        sql_statement = "INSERT INTO `curw_corona`.`summary` (`label`,`count`) VALUES (%s,%s);"

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


def bulk_insert_hospital_data(pool, data, upsert=True, id=True, hospital_name=False, cumulative_local=False,
                              cumulative_foreign=False, treatment_local=False, treatment_foreign=False,
                              cumulative_total=False, treatment_total=False):

    connection = pool.connection()

    pre_sql_statement = "INSERT INTO `curw_corona`.`hospital_data` "

    variable_list = []
    value_list = []
    update_list = []
    variable_list.append("`id`")
    value_list.append("id")

    if hospital_name:
        variable_list.append("`hospital_name`")
        value_list.append("hospital_name")
        update_list.append("`hospital_name` = VALUES(`hospital_name`)")
    if cumulative_local:
        variable_list.append("`cumulative_local`")
        value_list.append("cumulative_local")
        update_list.append("`cumulative_local` = VALUES(`cumulative_local`)")
    if cumulative_foreign:
        variable_list.append("`cumulative_foreign`")
        value_list.append("cumulative_foreign")
        update_list.append("`cumulative_foreign` = VALUES(`cumulative_foreign`)")
    if treatment_local:
        variable_list.append("`treatment_local`")
        value_list.append("treatment_local")
        update_list.append("`treatment_local` = VALUES(`treatment_local`)")
    if treatment_foreign:
        variable_list.append("`treatment_foreign`")
        value_list.append("treatment_foreign")
        update_list.append("`treatment_foreign` = VALUES(`treatment_foreign`)")
    if cumulative_total:
        variable_list.append("`cumulative_total`")
        value_list.append("cumulative_total")
        update_list.append("`cumulative_total` = VALUES(`cumulative_total`)")
    if treatment_total:
        variable_list.append("`treatment_total`")
        value_list.append("treatment_total")
        update_list.append("`treatment_total` = VALUES(`treatment_total`)")

    variables = ",".join(variable_list)
    values = ",".join(["%s"] * len(value_list))
    updates = ",".join(update_list)

    try:
        with connection.cursor() as cursor:
            if upsert:
                sql_statement = pre_sql_statement + "(" + variables + ") VALUES (" + values + ") ON DUPLICATE KEY UPDATE " \
                                       + updates + ";"
            else:
                sql_statement = pre_sql_statement + "(" + variables + ") VALUES (" + values + ");"

            print(sql_statement)
            row_count = cursor.executemany(sql_statement, data)

        connection.commit()
        return row_count
    except Exception as exception:
        connection.rollback()
        traceback.print_exc()
    finally:
        if connection is not None:
            connection.close()