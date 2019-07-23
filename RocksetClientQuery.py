from rockset import Client, Q

# TODO create config files to store api key
# Use the config method in the Rockset client
rs = Client(api_key='9s2DcuS7Ola8Ykt9ZreZ5lJHTm9gYgmt8kVbN8LobnCzK5eqsMtSPIw8xxTh4cal', api_server='https://api.rs2.usw2.rockset.com')

results = rs.sql(Q('''SELECT c."age" FROM "commons"."Testing2" c'''))

print(results)
