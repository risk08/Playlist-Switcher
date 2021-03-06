import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

api_service_name ="youtube"
api_version ="v3"
client_secrets_file ="client_secret.json"

scopes = ["https://www.googleapis.com/auth/youtube"]
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file,scopes)
credentials = flow.run_console()

youtube_client = googleapiclient.discovery.build(api_service_name,api_version,credentials=credentials)