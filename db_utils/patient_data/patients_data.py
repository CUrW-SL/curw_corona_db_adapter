import traceback


def insert_patient_data(pool, Patient_No, upsert=True, Confirmed_Date=None, Confined_Date=None, Symptoms_Start_Date=None,
                        Symptoms_Start_Location=None, Residence_City=None, Detected_City=None, Detected_Prefecture=None,
                        Gender=None, Age=None, Transmission_Type=None, Status=None, Notes=None):

    connection = pool.connection()

    pre_sql_statement = "INSERT INTO `curw_corona`.`patient_data` "

    variable_list = []
    value_list = []
    update_list = []
    variable_list.append("`Patient_No`")
    value_list.append(Patient_No)

    if Confirmed_Date is not None:
        variable_list.append("`Confirmed_Date`")
        value_list.append(Confirmed_Date)
        update_list.append("`Confirmed_Date` = VALUES(`Confirmed_Date`)")
    if Confined_Date is not None:
        variable_list.append("`Confined_Date`")
        value_list.append(Confined_Date)
        update_list.append("`Confined_Date` = VALUES(`Confined_Date`)")
    if Symptoms_Start_Date is not None:
        variable_list.append("`Symptoms_Start_Date`")
        value_list.append(Symptoms_Start_Date)
        update_list.append("`Symptoms_Start_Date` = VALUES(`Symptoms_Start_Date`)")
    if Symptoms_Start_Location is not None:
        variable_list.append("`Symptoms_Start_Location`")
        value_list.append(Symptoms_Start_Location)
        update_list.append("`Symptoms_Start_Location` = VALUES(`Symptoms_Start_Location`)")
    if Residence_City is not None:
        variable_list.append("`Residence_City`")
        value_list.append(Residence_City)
        update_list.append("`Residence_City` = VALUES(`Residence_City`)")
    if Detected_City is not None:
        variable_list.append("`Detected_City`")
        value_list.append(Detected_City)
        update_list.append("`Detected_City` = VALUES(`Detected_City`)")
    if Detected_Prefecture is not None:
        variable_list.append("`Detected_Prefecture`")
        value_list.append(Detected_Prefecture)
        update_list.append("`Detected_Prefecture` = VALUES(`Detected_Prefecture`)")
    if Gender is not None:
        variable_list.append("`Gender`")
        value_list.append(Gender)
        update_list.append("`Gender` = VALUES(`Gender`)")
    if Age is not None:
        variable_list.append("`Age`")
        value_list.append(Age)
        update_list.append("`Age` = VALUES(`Age`)")
    if Transmission_Type is not None:
        variable_list.append("`Transmission_Type`")
        value_list.append(Transmission_Type)
        update_list.append("`Transmission_Type` = VALUES(`Transmission_Type`)")
    if Status is not None:
        variable_list.append("`Status`")
        value_list.append(Status)
        update_list.append("`Status` = VALUES(`Status`)")
    if Notes is not None:
        variable_list.append("`Notes`")
        value_list.append(Notes)
        update_list.append("`Notes` = VALUES(`Notes`)")

    variables = ",".join(variable_list)
    values = ",".join("%s" * len(value_list))
    updates = ",".join(update_list)


    try:
        with connection.cursor() as cursor:
            if upsert:
                sql_statement = pre_sql_statement + "(" + variables + ") VALUES (" + values + ") ON DUPLICATE KEY UPDATE " \
                                       + updates + ";"
            else:
                sql_statement = pre_sql_statement + "(" + variables + ") VALUES (" + values + ");"

            print(sql_statement)
            row_count = cursor.execute(sql_statement, tuple(value_list))

        connection.commit()
        return row_count
    except Exception as exception:
        connection.rollback()
        traceback.print_exc()
    finally:
        if connection is not None:
            connection.close()


def bulk_insert_patient_data(pool, data, upsert=True):

    """Patient_No, Confirmed_Date=None, Confined_Date=None, Symptoms_Start_Date=None,
                        Symptoms_Start_Location=None, Residence_City=None, Detected_City=None, Detected_Prefecture=None,
                        Gender=None, Age=None, Transmission_Type=None, Status=None, Notes=None"""

    connection = pool.connection()

    if upsert:
        sql_statement = "INSERT INTO `curw_corona`.`patient_data` (`Patient_No`,`Confirmed_Date`,`Confined_Date`," \
                        "`Symptoms_Start_Date`,`Symptoms_Start_Location`,`Residence_City`,`Detected_City`," \
                        "`Detected_Prefecture`,`Gender`,`Age`,`Transmission_Type`,`Status`,`Notes`) VALUES " \
                        "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE " \
                        "`Confirmed_Date` = VALUES(`Confirmed_Date`),`Confined_Date` = VALUES(`Confined_Date`)," \
                        "`Symptoms_Start_Date` = VALUES(`Symptoms_Start_Date`)," \
                        "`Symptoms_Start_Location` = VALUES(`Symptoms_Start_Location`)," \
                        "`Residence_City` = VALUES(`Residence_City`),`Detected_City` = VALUES(`Detected_City`)," \
                        "`Detected_Prefecture` = VALUES(`Detected_Prefecture`),`Gender` = VALUES(`Gender`)," \
                        "`Age` = VALUES(`Age`),`Transmission_Type` = VALUES(`Transmission_Type`)," \
                        "`Status` = VALUES(`Status`),`Notes` = VALUES(`Notes`);"

    else:
        sql_statement = "INSERT INTO `curw_corona`.`patient_data` (`Patient_No`,`Confirmed_Date`,`Confined_Date`," \
                        "`Symptoms_Start_Date`,`Symptoms_Start_Location`,`Residence_City`,`Detected_City`," \
                        "`Detected_Prefecture`,`Gender`,`Age`,`Transmission_Type`,`Status`,`Notes`) VALUES " \
                        "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

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


def bulk_insert_patient_data_customized(pool, data, upsert=True, Patient_No=True, Confirmed_Date=False, Confined_Date=False, Symptoms_Start_Date=False,
                        Symptoms_Start_Location=False, Residence_City=False, Detected_City=False, Detected_Prefecture=False,
                        Gender=False, Age=False, Transmission_Type=False, Status=False, Notes=False):

    connection = pool.connection()

    pre_sql_statement = "INSERT INTO `curw_corona`.`patient_data` "

    variable_list = []
    value_list = []
    update_list = []
    variable_list.append("`Patient_No`")
    value_list.append("Patient_No")

    if Confirmed_Date:
        variable_list.append("`Confirmed_Date`")
        value_list.append("Confirmed_Date")
        update_list.append("`Confirmed_Date` = VALUES(`Confirmed_Date`)")
    if Confined_Date:
        variable_list.append("`Confined_Date`")
        value_list.append("Confined_Date")
        update_list.append("`Confined_Date` = VALUES(`Confined_Date`)")
    if Symptoms_Start_Date:
        variable_list.append("`Symptoms_Start_Date`")
        value_list.append("Symptoms_Start_Date")
        update_list.append("`Symptoms_Start_Date` = VALUES(`Symptoms_Start_Date`)")
    if Symptoms_Start_Location:
        variable_list.append("`Symptoms_Start_Location`")
        value_list.append("Symptoms_Start_Location")
        update_list.append("`Symptoms_Start_Location` = VALUES(`Symptoms_Start_Location`)")
    if Residence_City:
        variable_list.append("`Residence_City`")
        value_list.append("Residence_City")
        update_list.append("`Residence_City` = VALUES(`Residence_City`)")
    if Detected_City:
        variable_list.append("`Detected_City`")
        value_list.append("Detected_City")
        update_list.append("`Detected_City` = VALUES(`Detected_City`)")
    if Detected_Prefecture:
        variable_list.append("`Detected_Prefecture`")
        value_list.append("Detected_Prefecture")
        update_list.append("`Detected_Prefecture` = VALUES(`Detected_Prefecture`)")
    if Gender:
        variable_list.append("`Gender`")
        value_list.append("Gender")
        update_list.append("`Gender` = VALUES(`Gender`)")
    if Age:
        variable_list.append("`Age`")
        value_list.append("Age")
        update_list.append("`Age` = VALUES(`Age`)")
    if Transmission_Type:
        variable_list.append("`Transmission_Type`")
        value_list.append("Transmission_Type")
        update_list.append("`Transmission_Type` = VALUES(`Transmission_Type`)")
    if Status:
        variable_list.append("`Status`")
        value_list.append("Status")
        update_list.append("`Status` = VALUES(`Status`)")
    if Notes:
        variable_list.append("`Notes`")
        value_list.append("Notes")
        update_list.append("`Notes` = VALUES(`Notes`)")

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