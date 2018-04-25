from django.contrib.auth.models import Group

# filter the Group model for current logged in user instance
query_set = Group.objects.filter(user = request.user)

# print to console for debug/checking
for g in query_set:
    # this should print all group names for the user
    print(g.name)