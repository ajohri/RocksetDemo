from rockset import Client, Q
from credentials import rockset_api_key

# TODO create config files to store api key
# Use the config method in the Rockset client
rs = Client(api_key=rockset_api_key, api_server='https://api.rs2.usw2.rockset.com')

results = rs.sql(Q('''SELECT c."age" FROM "commons"."Testing2" c'''))

print(results)
