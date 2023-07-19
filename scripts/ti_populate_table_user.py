import pandas
from django.contrib.auth.models import User
from ti.models import Department, Profile


def run():
    try:
        path_file = "doc/populate/ti_users.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        for index, row in df.iterrows():
            print(index, row)
            print(index, row.login)

            department_id_find = Department.objects.filter(name=row.setor)
            department_id = department_id_find.values("id")[0].get("id")

            print("department_id", row.setor, department_id)

            User.objects.create_user(
                username=row.login,
                email=row.email,
                password="teste@123",
                # department=Profile.objects.get(id=department_id),
            )

            user_id_find = User.objects.filter(username=row.login)
            user_id = user_id_find.values("id")[0].get("id")

            print(user_id_find, user_id)

            Profile.objects.create(
                user=User.objects.get(id=user_id),
                department=Department.objects.get(id=department_id),
            )

    except Exception as error:
        print("Internal error:", error)
        raise
