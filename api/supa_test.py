'''
requirements.txt
28/10/2024

async_pyserial==0.2.3
blinker==1.8.2
click==8.1.7
colorama==0.4.6
Flask==3.0.3
future==1.0.0
iso8601==2.1.0
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
mysql==0.0.3
mysqlclient==2.2.4
psycopg2==2.9.9
pyserial==3.5
PyYAML==6.0.2
serial==0.0.97
Werkzeug==3.0.4


'''



from supabase import create_client, Client # type: ignore

#Supabase data connection:URL, KEY
SUPABASE_URL="https://utjsexhrdgpwggokykfi.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV0anNleGhyZGdwd2dnb2t5a2ZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY2NDgsImV4cCI6MjA0NTc0MjY0OH0.iHOS6sud6Jatfe11FS0e-RolUguQlQk_HANu3efm9y0"

#Connect to Supabase Client
supabase: Client = create_client(SUPABASE_URL,SUPABASE_KEY)

#Get data function
def save_data(e,p):
    #Insert into users model
    response = supabase.table('users').insert({"email":e,"password":p}).execute()
    
    if response.data:
        print(f"User has been save successfully: {response.data}")
    elif response.error:
        print(f"Error saving user: {response.error}")
    
#Main
email = input("E-mail: ")
passwd = input("Password: ")

save_data(email,passwd)

