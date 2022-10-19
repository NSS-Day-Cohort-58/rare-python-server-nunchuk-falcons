import json
import sqlite3



def get_all_categories(query_params):
    with sqlite3.connect("./loaddata") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""

        if len(query_params) != 0:
            param = query_params[0]
            [qs_key, qs_value] = param.split("=")

            if qs_key == "_sortBy":
                if qs_value == 'location':
                    sort_by = " ORDER BY location_id"

            # Write the SQL query to get the information you want
            sql_to_execute =